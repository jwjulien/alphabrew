# ======================================================================================================================
#        File:  Tests/Model/MeasureableUnits/test_UnitType.py
#     Project:  AlphaBrew
# Description:  Test cases for the UnitType measureable unit
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

from Model.MeasurableUnits import UnitError, UnitType



# ======================================================================================================================
# Unit Type Tests
# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'each',
    '1',
    'unit',
    'dimensionless',
    'pkg',
])
def test_creation(unit):
    """Verify that a Unit Type instantiates with the properproperty values from inputs."""
    value = random.randint(0, 1000) / 10
    instance = UnitType(value, unit)
    assert isinstance(instance, UnitType)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)




# End of File
