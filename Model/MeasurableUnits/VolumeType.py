# ======================================================================================================================
#        File:  Model/MeasureableUnits/VolumeType.py
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
# VolumeType Class
# ----------------------------------------------------------------------------------------------------------------------
class VolumeType(SimpleType):
    """Extends the SimpleType class to provide a class for working with VolumeType as defined in the BeerJson standard
    2.0 draft."""

    Types = {
        'tsp': 1,
        'tbsp': 3,
        'floz': 6,
        'cup': 48,
        'pt': 96,
        'qt': 192,
        'gal': 768,
        'bbl': 32256,
        'ifloz': 5.76456,
        'ipt': 115.291,
        'iqt': 230.582,
        'igal': 922.33,
        'ml': 0.202884,
        'l': 202.884
    }



# End of File
