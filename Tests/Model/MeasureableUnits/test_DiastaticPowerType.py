# ======================================================================================================================
#        File:  Tests/Model/MeasureableUnits/test_DiastaticPowerType.py
#     Project:  AlphaBrew
# Description:  Test cases for the DiastaticPowerType measureable unit
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

from Model.MeasurableUnits import UnitError, DiastaticPowerType



# ======================================================================================================================
# Diastatic Power Type Tests
# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'lintner',
    'Lintner',
    'wk',
    'WK',
])
def test_creation(unit):
    """Verify that a DiastaticPower Type instantiates with the properproperty values from inputs."""
    value = random.randint(0, 1000) / 10
    instance = DiastaticPowerType(value, unit)
    assert isinstance(instance, DiastaticPowerType)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)



# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("inVal,inUnit,outVal,outUnit", [
    (10, 'Lintner', 19, 'WK'),
    (10, 'Lintner', 10, 'Lintner'),
    (10, 'WK', 7.4285714285714285714285714285714, 'Lintner'),
    (10, 'WK', 10, 'WK'),
])
def test_conversion(inVal, inUnit, outVal, outUnit):
    """Verify appropriate conversions between types."""
    instance = DiastaticPowerType(inVal, inUnit)
    result = instance.as_(outUnit)
    assert result == pytest.approx(outVal)


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize('unit', [
   'Lintner',
   'WK',
])
def test_beerjson_output(unit):
    """Verify the proper formatting for the BeerJSON color units."""
    power = DiastaticPowerType(10, unit)
    json = power.to_dict()
    assert len(json.keys()) == 2
    assert 'value' in json
    assert json['value'] == 10
    assert 'unit' in json
    assert json['unit'] == unit




# End of File
