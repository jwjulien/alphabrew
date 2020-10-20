# ======================================================================================================================
#        File:  Model/MeasureableUnits/SimpleRangeType.py
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
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from Model.MeasurableUnits.SimpleType import SimpleType



# ======================================================================================================================
# SimpleRangeType Class
# ----------------------------------------------------------------------------------------------------------------------
class SimpleRangeType:
    """Provides a base class for working with BeerJSON range types, extended by other classes in this directory."""

    # This root class must be overridden by classes extending this base to provide the class to be instantiated when
    # creating new min/max ranges from BeerJSON.
    RootClass = SimpleType

    def __init__(self, minimum=None, maximum=None):
        self.minimum = minimum
        self.maximum = maximum



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert this instance into a dictionary suitable for entry into a BeerJSON document."""
        return {
            'minimum': self.minimum.to_dict(),
            'maximum': self.maximum.to_dict()
        }


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data):
        """Parses data from the BeerJSON format dictionary and loads them into this instance."""
        self.minimum = self.RootClass(data['minimum']['value'], data['minimum']['unit'])
        self.maximum = self.RootClass(data['maximum']['value'], data['maximum']['unit'])


# ----------------------------------------------------------------------------------------------------------------------
    def copy(self):
        """Return a new instance with the same numeric values."""
        new = self.__class__()
        new.minimum = self.minimum.copy()
        new.maximum = self.maximum.copy()
        return new



# ======================================================================================================================
# Overridden Methods
# ----------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        """When represented as a string, convert this range into a values with units."""
        return f'[{self.minimum} - {self.maximum}]'


# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self):
        """Handle better representation of this class when printed."""
        return f'<{self.__class__.__name__} minimum="{self.minimum}" maximum="{self.maximum}">'




# End of File
