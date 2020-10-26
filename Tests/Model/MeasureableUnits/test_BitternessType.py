# ======================================================================================================================
#        File:  Tests/Model/MeasureableUnits/test_BitternessType.py
#     Project:  AlphaBrew
# Description:  Test cases for the BitternessType measureable unit
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

from Model.MeasurableUnits import UnitError, BitternessType



# ======================================================================================================================
# Bitterness Type Tests
# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'ibu',
    'IBUs',
    'ibus',
])
def test_creation(unit):
    """Verify that a Bitterness Type instantiates with the properproperty values from inputs."""
    value = random.randint(0, 1000) / 10
    instance = BitternessType(value, unit)
    assert isinstance(instance, BitternessType)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)


# ----------------------------------------------------------------------------------------------------------------------
def test_beerjson_output():
    """Verify the proper formatting for the BeerJSON pH unit."""
    acidity = BitternessType(45, 'IBUs')
    json = acidity.to_dict()
    assert len(json.keys()) == 2
    assert 'value' in json
    assert json['value'] == 45
    assert 'unit' in json
    assert json['unit'] == 'IBUs'



# End of File
