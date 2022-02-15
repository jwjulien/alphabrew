# ======================================================================================================================
#        File:  Model/MeasureableUnits/GravityType.py
#     Project:  AlphaBrew
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

from Math import Gravity



# ======================================================================================================================
# GravityType Class
# ----------------------------------------------------------------------------------------------------------------------
class GravityType(SimpleType):
    """Extends the SimpleType class to provide a class for working with GravityType as defined in the BeerJson standard
    2.0 draft."""

    # In this special case the scale factors are not linear so they aren't used.  The keys, however, are when writing to
    # "unit" so they are all set to None but the "as_" method is overwritten below and does not use them.
    Types = {
        'sg': None,
        'plato': None,
        'brix': None
    }



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def as_(self, desired):
        """Specifically override the as_ class to make use of the conversions in the Math module for these types."""
        desired = self._coerce_unit(desired)

        if desired not in self.Types.keys():
            return KeyError(f'The specified unit "{desired}" does not exist on class "GravityType"')

        # Get value into specific gravity as a common base.
        if self.unit == 'sg':
            sg = self.value
        elif self.unit == 'plato':
            sg = Gravity.plato_to_sg(self.value)
        else: # Brix
            sg = Gravity.brix_to_sg(self.value)

        # Convert and/or return the value in the desired units.
        if desired == 'sg':
            return sg
        elif desired == 'plato':
            return Gravity.sg_to_plato(sg)
        else: # Brix
            return Gravity.sg_to_brix(sg)



# End of File
