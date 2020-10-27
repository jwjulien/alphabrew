# ======================================================================================================================
#        File:  Tests/Model/MeasureableUnits/test_GravityType.py
#     Project:  AlphaBrew
# Description:  Test cases for the GravityType measureable unit
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

from Model.MeasurableUnits import UnitError, GravityType



# ======================================================================================================================
# Gravity Type Tests
# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit, tolerance", [
    ('sg',    1e-6),
    ('plato', 1e-6),
    ('brix',  5e-2),
])
def test_creation(unit, tolerance):
    """Verify that a Gravity Type instantiates with the properproperty values from inputs."""
    value = random.randint(1, 100) / 10
    instance = GravityType(value, unit)
    assert isinstance(instance, GravityType)
    assert instance.value == value
    # The tolerance has been lowered because the math is a little lossy.  For the current usage of this tool that is
    # totally acceptable.  If the tolerance of +/-0.05 brix is not acceptable the maths in Math/Gravity.py needs to be
    # adjusted to be more accurate.
    assert instance.as_(unit) == pytest.approx(value, tolerance)



# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("inVal,inUnit,outVal,outUnit", [
    (1.014, 'sg',    1.014,  'sg'   ),
    (1.014, 'sg',    3.574,  'plato'),
    (1.014, 'sg',    3.5741, 'brix' ),
    (5,     'plato', 1.0197, 'sg'   ),
    (5,     'plato', 5,      'plato'),
    (5,     'plato', 4.9986, 'brix' ),
    (9,     'brix',  1.0359, 'sg'   ),
    (9,     'brix',  9.0005, 'plato'),
    (9,     'brix',  9,      'brix' ),
])
def test_conversion(inVal, inUnit, outVal, outUnit):
    """Verify appropriate conversions between types."""
    instance = GravityType(inVal, inUnit)
    result = instance.as_(outUnit)
    assert result == pytest.approx(outVal, 1e-3)




# End of File
