# ======================================================================================================================
#        File:  Model/MeasureableUnits/SimpleType.py
#     Project:  AlphaBrew
# Description:  Provides a base class for simple types, extended by BeerJSON standards.
#      Author:  Jared Julien <jaredjulien@gmail.com>
#   Copyright:  (c) 2020 Jared Julien
# ----------------------------------------------------------------------------------------------------------------------
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================
# Exceptions
# ----------------------------------------------------------------------------------------------------------------------
class UnitError(Exception):
    """Raised when the specified units don't exist for a given type."""




# ======================================================================================================================
# SimpleType Class
# ----------------------------------------------------------------------------------------------------------------------
class SimpleType:
    """Provides a base class for working with most BeerJSON types, extended by other classes in this directory."""

    # This parameter must be overridden by classes extending SimpleType to include a list of items and scale factors.
    # Keys in the dict represent the available unit types for this class while values are scale values relative to the
    # smallest listed unit.
    Types: dict = {}

    # This parameter may be overridden by child classes to remap alternative names for units.  For example, a typical
    # unit of 'lb' bay be used for pounds, but 'pound' and events 'pounds' may be added to the Synonyms table to
    # allow those units to be used for the exact same conversion.
    Synonyms: dict = {}

    # This dictionary can be overridden by child classes to map the outgoing units (upon conversion to_dict) to a
    # specific value.  This is specifically useful for units where upper case is actually important to meet the BeerJSON
    # standard.
    JsonOutput: dict = {}

    # The following minimum and maximum values can be set by child classes to constrain the range of the type.  If a
    # value is assiged that is outside of this range (when set) a ValueError will be thrown.
    Minimum: float = None
    Maximum: float = None

    def __init__(self, value:float=None, unit:str=None, json:dict=None):
        self._value = None
        self._unit = None

        # Set the units from the inputs when provided.
        if value is not None and unit is not None:
            self.value = value
            self.unit = unit

        # Or use JSON.
        elif json is not None:
            self.from_dict(json)

        # But if all inputs are invalid, throw an exception.
        else:
            raise TypeError('SimpleType must be instantiated with either a value AND unit, or via JSON.')




# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def value(self):
        return self._value


# ----------------------------------------------------------------------------------------------------------------------
    @value.setter
    def value(self, value):
        if self.Minimum is not None and value < self.Minimum:
            raise ValueError(f"Value '{value}' exceeds the minimum '{self.Minimum}' for '{__class__.__name__}'")
        if self.Maximum is not None and value > self.Maximum:
            raise ValueError(f"Value '{value}' exceeds the maximum '{self.Maximum}' for '{__class__.__name__}'")
        self._value = value


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def unit(self):
        return self._unit


# ----------------------------------------------------------------------------------------------------------------------
    @unit.setter
    def unit(self, value: str):
        """Sets the units for this type.  Runs the supplied value through the Synonyms table to possibly map it to a
        standardized unit and then verifies that unit is appropriate for this type.  Raises UnitError if the unit is
        not supported by this type."""
        value = self._coerce_unit(value)

        # Raise a UnitError if the units are not supported.
        if value not in self.Types.keys():
            raise UnitError(f'{self.__class__.__name__} does not support unit of "{value}"')

        self._unit = value


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def base(self):
        """Returns the base units for this type as the zeroth entry in the Types attribute."""
        return list(self.Types.keys())[0]


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def root(self):
        """This helper property is used by the comparison methods below to always fetch the zeroth unit from
        the Types attribute for the class.  The intent is to level the playing field on the value by eliminating units
        before performing mathematical comparisons.  i.e. 1 gallon is larger than 2 quarts."""
        return self.as_(self.base)


# ----------------------------------------------------------------------------------------------------------------------
    def __getattr__(self, key: str):
        """Generate dynamic properties for conversion.  These property names are automatically generated from the unit
        names provided in the Types dictionary for the child class."""
        key = self._coerce_unit(key)

        # If this provided key is a unit of this type, return it's value in those units.
        if key in self.Types:
            return self.as_(key)

        # Raise a standard AttributeError when the key doesn't fit the expected format.
        raise AttributeError(f"'{__class__.__name__}' object has no attribute '{key}'")



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert this instance into a dictionary suitable for entry into a BeerJSON document."""
        # Convert the units to the specified output format, if specified.  If not specified, just fall back on the
        # actual value of unit.
        unit = self.JsonOutput.get(self.unit, self.unit)

        return {
            'value': self.value,
            'unit': unit
        }


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data: dict):
        """Parses data from the BeerJSON format dictionary and loads them into this instance."""
        keys = data.keys()
        if len(keys) == 2 and 'value' in keys and 'unit' in keys:
            self.value = data['value']
            self.unit = data['unit']

        else:
            raise TypeError("JSON input expects exactly two keys: 'value' and 'unit'")


# ----------------------------------------------------------------------------------------------------------------------
    def copy(self):
        """Generate a new instance of this type with the same values as this and return it.  Allows the new instance to
        be modified without impacting this instance."""
        return self.__class__(self.value, self.unit)


# ----------------------------------------------------------------------------------------------------------------------
    def as_(self, desired: str) -> float:
        """Return the current value as the specified unit type."""
        desired = self._coerce_unit(desired)
        if desired not in self.Types.keys():
            raise KeyError(f'The specified unit "{desired}" does not exist on class "{self.__class__.__name__}"')
        numerator = self.Types[self.unit]
        denominator = self.Types[desired]
        return self.value * numerator / denominator


# ----------------------------------------------------------------------------------------------------------------------
    def convert(self, desired: str) -> float:
        """Same functionality as the "as_" method above, except that this will change the value stored into the
        specified units.  Useful when looking to change the displayed value."""
        self.value = self.as_(desired)
        self.unit = desired
        return self.value



# ======================================================================================================================
# Private Methods
# ----------------------------------------------------------------------------------------------------------------------
    def _ensure_same_type(self, other):
        """Used by the comparison methods below to ensure that apples are being compared to apples."""
        if self.__class__ != other.__class__:
            raise TypeError(f'Cannot compare {self.__class__.__name__} to {other.__class__.__name__}')


# ----------------------------------------------------------------------------------------------------------------------
    def _coerce_unit(self, unit: str) -> str:
        """Takes in units as a string and performs standard conversion on those units to get them to a standard for this
        type.  This includes conversion to lower case, removal of plurals, and synonym lookup."""
        # Units are not case sensitive, so switch to lower case before lookups.
        unit = unit.lower()

        # Make singular - this is very crude and may need to be updated at some point.
        if unit not in self.Types and unit not in self.Synonyms:
            # Don't attempt to de-pluralize when there is already a match for this type.
            if unit.endswith('ies'):
                unit = unit[:-3] + 'y'
            elif unit.endswith('s'):
                unit = unit[:-1]

        # Attempt to map this to another unit or just fall back on the provided name without a match.
        unit = self.Synonyms.get(unit, unit)

        return unit



# ======================================================================================================================
# Overridden Methods
# ----------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        """When represented as a string, convert this duration into a value with units.

        Will use as many decimal places as needed to represent the number but will strip off any trailing zeros up to,
        and including, the decimal point.
        """
        return f'{self.value:.10f}'.rstrip('0').rstrip('.') + f' {self.unit}'


# ----------------------------------------------------------------------------------------------------------------------
    def __eq__(self, other):
        """Compares two values using the same units to see if they are equal."""
        self._ensure_same_type(other)
        return self.root == other.root


# ----------------------------------------------------------------------------------------------------------------------
    def __ne__(self, other):
        """Compares two values to ensure that they are not equal."""
        self._ensure_same_type(other)
        return self.root != other.root


# ----------------------------------------------------------------------------------------------------------------------
    def __gt__(self, other):
        """Compares two values to ensure that self is greater than other."""
        # Deliberately don't care about type here because we want to be able to sort mixed data (i.e. Mass and Volume
        # can both be used with fermentables and we want to sort them together).
        return self.root > other.root


# ----------------------------------------------------------------------------------------------------------------------
    def __lt__(self, other):
        """Compares two values to ensure that self is less than other."""
        # Deliberately don't care about type here because we want to be able to sort mixed data (i.e. Mass and Volume
        # can both be used with fermentables and we want to sort them together).
        return self.root < other.root


# ----------------------------------------------------------------------------------------------------------------------
    def __ge__(self, other):
        """Compares two values to ensure that self is greater than or equal to other."""
        # Deliberately don't care about type here because we want to be able to sort mixed data (i.e. Mass and Volume
        # can both be used with fermentables and we want to sort them together).
        return self.root >= other.root


# ----------------------------------------------------------------------------------------------------------------------
    def __le__(self, other):
        """Compares two values to ensure that self is less than or equal to other."""
        # Deliberately don't care about type here because we want to be able to sort mixed data (i.e. Mass and Volume
        # can both be used with fermentables and we want to sort them together).
        return self.root <= other.root


# ----------------------------------------------------------------------------------------------------------------------
    def __add__(self, other):
        """Add the two values together and return the result in a new instance with the units of self."""
        self._ensure_same_type(other)
        return self.__class__(self.value + other.as_(self.unit), self.unit)


# ----------------------------------------------------------------------------------------------------------------------
    def __sub__(self, other):
        """Subtract other from self and return the result in a new instance with the units of self."""
        self._ensure_same_type(other)
        return self.__class__(self.value - other.as_(self.unit), self.unit)


# ----------------------------------------------------------------------------------------------------------------------
    def __mul__(self, other):
        """Multiply other by self and return the result in a new instance with the units of self."""
        if isinstance(other, (int, float)):
            # Scaler multiplication.
            multiplier = other

        else:
            try:
                # Percentage type?
                multiplier = other.as_('%') / 100

            except KeyError:
                # If not scaler or percentage, then the type must be identical - throw an exception when not.
                self._ensure_same_type(other)
                multiplier = other.as_(self.unit)

        return self.__class__(self.value * multiplier, self.unit)


# ----------------------------------------------------------------------------------------------------------------------
    def __truediv__(self, other):
        """Divide other by self and return the result in a new instance with the units of self."""
        if isinstance(other, (int, float)):
            # Scaler division.
            denominator = other

        else:
            try:
                # Percentage type?
                denominator = other.as_('%') / 100

            except KeyError:
                # If not scaler or percentage, then the type must be identical - throw an exception when not.
                self._ensure_same_type(other)

                # Division is backwards from a unit perspective.  The result units will be that of the denominator, but
                # that isn't the behavior we desire.  So, do the division as the rot units and convert to the desired
                # units post math.
                result = self.__class__(self.root / other.root, self.base)
                result.convert(self.unit)
                return result

        return self.__class__(self.value / denominator, self.unit)


# ----------------------------------------------------------------------------------------------------------------------
    def __iadd__(self, other):
        return self + other


# ----------------------------------------------------------------------------------------------------------------------
    def __isub__(self, other):
        return self - other


# ----------------------------------------------------------------------------------------------------------------------
    def __imul__(self, other):
        return self * other


# ----------------------------------------------------------------------------------------------------------------------
    def __itruediv__(self, other):
        return self / other



# End of File
