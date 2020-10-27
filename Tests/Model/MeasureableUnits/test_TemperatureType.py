# ======================================================================================================================
#        File:  Tests/Model/MeasureableUnits/test_TemperatureType.py
#     Project:  AlphaBrew
# Description:  Test cases for the TemperatureType measureable unit
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

from Model.MeasurableUnits import UnitError, TemperatureType



# ======================================================================================================================
# Temperature Type Tests
# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'F',
    'C',
])
def test_creation(unit):
    """Verify that a Temperature Type instantiates with the properproperty values from inputs."""
    value = random.randint(0, 1000) / 10
    instance = TemperatureType(value, unit)
    assert isinstance(instance, TemperatureType)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)



# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("inVal,inUnit,outVal,outUnit", [
    (-40, 'f', -40, 'c'),
    (32, 'f', 0, 'c'),
    (100, 'c', 212, 'f'),
    (23, 'c', 73.4, 'f'),
])
def test_conversion(inVal, inUnit, outVal, outUnit):
    """Verify appropriate conversions between types."""
    instance = TemperatureType(inVal, inUnit)
    result = instance.as_(outUnit)
    assert result == pytest.approx(outVal)




# End of File
