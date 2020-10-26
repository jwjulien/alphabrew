# ======================================================================================================================
#        File:  Model/MeasureableUnits/TimeType.py
#     Project:  AlphaBrew
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
# TimeType Class
# ----------------------------------------------------------------------------------------------------------------------
class TimeType(SimpleType):
    """Extends the SimpleType class to provide a class for working with TimeTypes as defined in the BeerJson standard
    2.0 draft."""

    Types = {
        'sec': 1,
        'min': 60,
        'hr': (60 * 60),
        'day': (60 * 60 * 24),
        'week': (60 * 60 * 24 * 7),
        'month': (60 * 60 * 24 * 30), # Approximate
        'year': (60 * 60 * 24 * 365)  # Approximate
    }

    Synonyms = {
        'second': 'sec',
        'minute': 'min',
        'hour': 'hr',
        'date': 'day',
    }



# End of File
