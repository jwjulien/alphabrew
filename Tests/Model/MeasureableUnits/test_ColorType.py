# ======================================================================================================================
#        File:  Tests/Model/MeasureableUnits/test_ColorType.py
#     Project:  AlphaBrew
# Description:  Test cases for the ColorType measureable unit
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

from Model.MeasurableUnits import UnitError, ColorType



# ======================================================================================================================
# Color Type Tests
# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'srm',
    'SRM',
    'Lovi',
    'lovi',
    'Lovibond',
    'lovibond',
    'EBC',
    'ebc',
])
def test_creation(unit):
    """Verify that a Color Type instantiates with the properproperty values from inputs."""
    value = random.randint(0, 1000) / 10
    instance = ColorType(value, unit)
    assert isinstance(instance, ColorType)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)



# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("inVal,inUnit,outVal,outUnit", [
    (20, 'SRM', 20, 'SRM'),
    (20, 'SRM', 15.33, 'Lovibond'),
    (20, 'SRM', 39.4, 'EBC'),
    (25, 'Lovibond', 33.11, 'SRM'),
    (25, 'Lovibond', 25, 'Lovibond'),
    (25, 'Lovibond', 65.22, 'EBC'),
    (60, 'EBC', 30.48, 'SRM'),
    (60, 'EBC', 23.06, 'Lovibond'),
    (60, 'EBC', 60, 'EBC'),
])
def test_conversion(inVal, inUnit, outVal, outUnit):
    """Verify appropriate conversions between types."""
    instance = ColorType(inVal, inUnit)
    result = instance.as_(outUnit)
    # These maths are kinda rough, but color is just an approximation anyways - so we an safely open up these
    # tolerances.
    assert result == pytest.approx(outVal, 1e-3)


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize('unit', [
   'SRM',
   'Lovi',
   'EBC',
])
def test_beerjson_output(unit):
    """Verify the proper formatting for the BeerJSON color units."""
    color = ColorType(30, unit)
    json = color.to_dict()
    assert len(json.keys()) == 2
    assert 'value' in json
    assert json['value'] == 30
    assert 'unit' in json
    assert json['unit'] == unit




# End of File
