# ======================================================================================================================
#        File:  Model/MeasureableUnits/TemperatureType.py
#     Project:  Brewing Recipe Planner
# Description:  Provides a base class for working with time types in recipes which can have differing units.
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
# TemperatureType Class
# ----------------------------------------------------------------------------------------------------------------------
class TemperatureType(SimpleType):
    """Extends the SimpleType class to provide a class for working with TemperatureType as defined in the BeerJson
    standard 2.0 draft."""

    Types = {
        'F': None,
        'C': None
    }



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def as_(self, desired):
        """Override the simple conversion to provide a conversion with offset."""
        if desired not in self.Types.keys():
            return KeyError(f'The specified unit "{desired}" does not exist on class "TemperatureType"')

        if self.unit == desired:
            return self.value

        if self.unit == 'F' and desired == 'C':
            return (self.value - 32) / 1.8

        # With only two options for units, this means that we are in C but want F.
        return (1.8 * self.value) + 32




# End of File
