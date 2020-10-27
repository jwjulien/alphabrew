# ======================================================================================================================
#        File:  Tests/Model/MeasureableUnits/test_SpecificVolumeType.py
#     Project:  AlphaBrew
# Description:  Test cases for the SpecificVolumeType measureable unit
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

from Model.MeasurableUnits import UnitError, SpecificVolumeType



# ======================================================================================================================
# Specific Volume Type Tests
# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'qt/lb',
    'gal/lb',
    'gal/oz',
    'l/g',
    'l/kg',
    'floz/oz',
    'm^3/kg',
    'ft^3/lb',
    'quartperpound',
    'quartsperpound',
    'qtperlb',
    'gallonperpound',
    'gallonsperpound',
    'galperlb',
    'litersperkilogram',
])
def test_creation(unit):
    """Verify that a SpecificVolume Type instantiates with the properproperty values from inputs."""
    value = random.randint(0, 1000) / 10
    instance = SpecificVolumeType(value, unit)
    assert isinstance(instance, SpecificVolumeType)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)



# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("inVal,inUnit,outVal,outUnit", [
    (2, 'qt/lb', 1, 'floz/oz'),
    (1, 'qt/lb', 4, 'gal/lb'),
    (1, 'gal/lb', 16, 'gal/oz'),
    (1, 'gal/lb', 7.48053, 'ft^3/lb'),
    (2, 'gal/lb', 1.043175, 'l/kg'),
    (1, 'l/g', 1, 'm^3/kg'),
    (1, 'l/kg', 229.734, 'l/g'),
    (1, 'l/kg', 229.734, 'm^3/kg'),
])
def test_conversion(inVal, inUnit, outVal, outUnit):
    """Verify appropriate conversions between types."""
    instance = SpecificVolumeType(inVal, inUnit)
    result = instance.as_(outUnit)
    assert result == pytest.approx(outVal)




# End of File
