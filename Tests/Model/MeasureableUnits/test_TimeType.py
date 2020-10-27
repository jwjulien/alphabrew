# ======================================================================================================================
#        File:  Tests/Model/MeasureableUnits/test_TimeType.py
#     Project:  AlphaBrew
# Description:  Test cases for the TimeType measureable unit
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
import random

import pytest

from Model.MeasurableUnits import UnitError, TimeType



# ======================================================================================================================
# Time Type Tests
# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'sec',
    'min',
    'hr',
    'day',
    'week',
    'month',
    'year',
    'second',
    'minute',
    'hour',
    'date',
])
def test_creation(unit):
    """Verify that a Time Type instantiates with the properproperty values from inputs."""
    value = random.randint(0, 1000) / 10
    instance = TimeType(value, unit)
    assert isinstance(instance, TimeType)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)



# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("inVal,inUnit,outVal,outUnit,tolerance", [
    (60, 'sec', 1, 'min', 1e-6),
    (60, 'min', 1, 'hr', 1e-6),
    (24, 'hr', 1, 'day', 1e-6),
    (7, 'days', 1, 'week', 1e-6),
    (4, 'weeks', 1, 'month', 1e-1),
    (12, 'months', 1, 'year', 1e-1),
    (1, 'minute', 60, 'seconds', 1e-6),
    (1, 'hour', 60, 'minutes', 1e-6),
    (1, 'hour', 3600, 'seconds', 1e-6),
    (1, 'day', 24, 'hours', 1e-6),
    (1, 'week', 7, 'days', 1e-6),
    (1, 'month', 4, 'weeks', 1e-1),
    (1, 'year', 12, 'months', 1e-1),
])
def test_conversion(inVal, inUnit, outVal, outUnit, tolerance):
    """Verify appropriate conversions between types."""
    instance = TimeType(inVal, inUnit)
    result = instance.as_(outUnit)
    assert result == pytest.approx(outVal, tolerance)




# End of File
