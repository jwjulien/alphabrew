# ======================================================================================================================
#        File:  Tests/Model/MeasureableUnits/test_MassType.py
#     Project:  AlphaBrew
# Description:  Test cases for the MassType measureable unit
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

from Model.MeasurableUnits import MassType



# ======================================================================================================================
# Mass Type Tests
# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'oz',
    'lb',
    'mg',
    'g',
    'kg',
])
def test_creation_discrete(unit):
    """Verify that a Mass Type instantiates with the properproperty values from inputs."""
    value = random.randint(0, 1000) / 10
    instance = MassType(value, unit)
    assert isinstance(instance, MassType)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)



# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'oz',
    'lb',
    'mg',
    'g',
    'kg',
])
def test_creation_json(unit):
    """Verify that a Mass Type instantiates with the properproperty values from JSON dict input."""
    value = random.randint(0, 1000) / 10
    json = {
        'value': value,
        'unit': unit
    }
    instance = MassType(json=json)
    assert isinstance(instance, MassType)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)



# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'gal',
    '%',
    'SRM',
    'Lintner',
    'obscure',
])
def test_creation_invalid_discrete(unit):
    """Verify that an exception is thrown when instantiating with an invalid unit."""
    with pytest.raises(ValueError):
        MassType(0, unit)



# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'gal',
    '%',
    'SRM',
    'Lintner',
    'obscure',
])
def test_creation_invalid_json(unit):
    """Verify that an exception is thrown when instantiating with an invalid unit from JSON inputs."""
    json = {
        'value': 10,
        'unit': unit
    }
    with pytest.raises(ValueError):
        MassType(json=json)



# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("inVal,inUnit,outVal,outUnit", [
    (16, 'oz', 1, 'lb'),
    (453592, 'mg', 1, 'lb'),
    (453.592, 'g', 1, 'lb'),
    (0.453592, 'kg', 1, 'lb'),
    (1, 'kg', 1000, 'g'),
    (1, 'g', 1000, 'mg'),
])
def test_conversion(inVal, inUnit, outVal, outUnit):
    """Verify appropriate conversions between types."""
    instance = MassType(inVal, inUnit)
    result = instance.as_(outUnit)
    assert result == pytest.approx(outVal)




# End of File
