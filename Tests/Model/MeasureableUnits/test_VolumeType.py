# ======================================================================================================================
#        File:  Tests/Model/Fermentable.py
#     Project:  AlphaBrew
# Description:  Test cases for the Fermentable Model class.
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

from Model.MeasurableUnits import VolumeType



# ======================================================================================================================
# Volume Type Tests
# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'tsp',
    'tbsp',
    'floz',
    'cup',
    'pt',
    'qt',
    'gal',
    'bbl',
    'ifloz',
    'ipt',
    'iqt',
    'igal',
    'ml',
    'l',
])
def test_creation_discrete(unit):
    """Verify that a Volume Type instantiates with the properproperty values from inputs."""
    value = random.randint(0, 1000) / 10
    instance = VolumeType(value, unit)
    assert isinstance(instance, VolumeType)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)



# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'tsp',
    'tbsp',
    'floz',
    'cup',
    'pt',
    'qt',
    'gal',
    'bbl',
    'ifloz',
    'ipt',
    'iqt',
    'igal',
    'ml',
    'l',
])
def test_creation_json(unit):
    """Verify that a Volume Type instantiates with the properproperty values from JSON dict input."""
    value = random.randint(0, 1000) / 10
    json = {
        'value': value,
        'unit': unit
    }
    instance = VolumeType(json=json)
    assert isinstance(instance, VolumeType)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)



# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'lb',
    '%',
    'SRM',
    'Lintner',
    'obscure',
])
def test_creation_invalid_discrete(unit):
    """Verify that an exception is thrown when instantiating with an invalid unit."""
    with pytest.raises(ValueError):
        VolumeType(0, unit)



# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'lb',
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
        VolumeType(json=json)



# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("inVal,inUnit,outVal,outUnit", [
    (1, 'tbsp', 3, 'tsp'),
    (1, 'floz', 2, 'tbsp'),
    (1, 'cup', 16, 'tbsp'),
    (1, 'cup', 8, 'floz'),
    (2, 'cup', 1, 'pt'),
    (2, 'pt', 1, 'qt'),
    (4, 'qt', 1, 'gal'),
    (1, 'bbl', 42, 'gal'),
    (1, 'gal', 133.2279, 'ifloz'),
    (1, 'gal', 6.661406, 'ipt'),
    (1, 'gal', 3.3307, 'iqt'),
    (1, 'gal', 0.832674, 'igal'),
    (1, 'pt', 473.17679, 'ml'),
    (1, 'gal', 3.7854143, 'l'),
])
def test_conversion(inVal, inUnit, outVal, outUnit):
    """Verify appropriate conversions between types."""
    instance = VolumeType(inVal, inUnit)
    result = instance.as_(outUnit)
    assert result == pytest.approx(outVal)




# End of File
