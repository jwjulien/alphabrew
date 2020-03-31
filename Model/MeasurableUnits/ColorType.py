# ======================================================================================================================
#        File:  Model/MeasureableUnits/ColorType.py
#     Project:  Brewing Recipe Planner
# Description:  Provides a base class for working with acidity in recipes which can have differing units.
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
# ColorType Class
# ----------------------------------------------------------------------------------------------------------------------
class ColorType(SimpleType):
    """Extends the SimpleType class to provide a class for working with ColorType as defined in the BeerJson standard
    2.0 draft."""

    # The scaling between colors is linear but has an offset so the "as_" method is overloaded below.
    Types = {
        'SRM': None,
        'Lovi': None,
        'EBC': None
    }



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def as_(self, desired):
        """Convert this color to a color of another, specified base."""
        if self.unit == 'SRM':
            srm = self.value
        elif self.unit == 'Lovi':
            srm = (1.3546 * self.value) - 0.76
        else: # EBC
            srm = self.value * 0.508

        if desired == 'Lovi':
            return (srm + 0.76) / 1.3546
        if desired == 'EBC':
            return srm * 1.97
        return srm




# End of File
