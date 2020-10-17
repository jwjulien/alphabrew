# ======================================================================================================================
#        File:  Model/MeasureableUnits/SimpleType.py
#     Project:  Brewing Recipe Planner
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
# SimpleType Class
# ----------------------------------------------------------------------------------------------------------------------
class SimpleType:
    """Provides a base class for working with most BeerJSON types, extended by other classes in this directory."""

    # This parameter must be overridden by classes extending SimpleType to include a list of items and scale factors.
    # Keys in the dict represent the available unit types for this class while values are scale values relative to the
    # smallest listed unit.
    Types = {}

    def __init__(self, value=None, unit=None, json=None):
        self.value = value
        self._unit = unit

        if json is not None:
            self.from_dict(json)




# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def unit(self):
        return self._unit


# ----------------------------------------------------------------------------------------------------------------------
    @unit.setter
    def unit(self, value):
        if value not in self.Types.keys():
            raise ValueError(f'{self.__class__.__name__} does not support units of "{value}"')

        self._unit = value


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def root(self):
        """This helper property is used by the comparison methods below to always fetch the zeroth unit from
        the Types attribute for the class.  The intent is to level the playing field on the value by eliminating units
        before performing mathematical comparisons.  i.e. 1 gallon is larger than 2 quarts."""
        base = list(self.Types.keys())[0]
        return self.as_(base)



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert this instance into a dictionary suitable for entry into a BeerJSON document."""
        return {
            'value': self.value,
            'unit': self.unit
        }


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data):
        """Parses data from the BeerJSON format dictionary and loads them into this instance."""
        self.value = data['value']
        self.unit = data['unit']


# ----------------------------------------------------------------------------------------------------------------------
    def copy(self):
        """Generate a new instance of this type with the same values as this and return it.  Allows the new instance to
        be modified without impacting this instance."""
        return self.__class__(self.value, self.unit)


# ----------------------------------------------------------------------------------------------------------------------
    def as_(self, desired):
        """Return the current value as the specified unit type."""
        if desired not in self.Types.keys():
            raise KeyError(f'The specified unit "{desired}" does not exist on class "{self.__class__.__name__}"')
        numerator = self.Types[self.unit]
        denominator = self.Types[desired]
        return self.value * numerator / denominator


# ----------------------------------------------------------------------------------------------------------------------
    def convert(self, desired):
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



# ======================================================================================================================
# Overridden Methods
# ----------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        """When represented as a string, convert this duration into a value with units."""
        return f'{self.value:.1f} {self.unit}'


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
    def __div__(self, other):
        """Divide other by self and return the result in a new instance with the units of self."""
        self._ensure_same_type(other)
        return self.__class__(self.value / other.as_(self.unit), self.unit)



# End of File
