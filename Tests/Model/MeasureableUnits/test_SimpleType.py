# ======================================================================================================================
#        File:  Tests/Model/MeasureableUnits/test_SimpleType.py
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

from Model.MeasurableUnits import UnitError, PercentType
from Model.MeasurableUnits.SimpleType import SimpleType



# ======================================================================================================================
# Generic Complex Type Implementation
# ----------------------------------------------------------------------------------------------------------------------
class ComplesTypeStub(SimpleType):
    """A stubbed type used to specifically test the underlying SimpleType parent class."""
    Types = {
        'one': 1,
        'two': 2,
        'three': 3,
        'ten': 10,
        'sixty': 60,
        'hundred': 100,
        'thousand': 1000,
    }

    Synonyms = {
        'onehundred': 'hundred',
        'onethousand': 'thousand',
    }

    JsonOutput = {
        'three': 'Thrice',
    }


# ----------------------------------------------------------------------------------------------------------------------
class AnotherComplexTypeStub(SimpleType):
    """Used to verify math errors when working with two different extensions of the simple type class."""
    Types = {
        'pound': 1
    }



# ======================================================================================================================
# Initialization Tests
# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'one',
    'two',
    'three',
    'hundred',
    'thousand',
])
def test_creation_discrete(unit):
    """Verify initialization with proper values when created from discrete inputs."""
    value = random.randint(0, 1000) / 10
    instance = ComplesTypeStub(value, unit)

    assert isinstance(instance, ComplesTypeStub)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'onehundred',
    'oneHundred',
    'onethousand',
    'oneThousand',
])
def test_creation_discrete_synonyms(unit):
    """Verify initialization with proper values when created from discrete synonym inputs."""
    value = random.randint(0, 1000) / 10
    instance = ComplesTypeStub(value, unit)

    assert isinstance(instance, ComplesTypeStub)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'ones',
    'twos',
    'threes',
    'sixties',
    'hundreds',
    'thousands',
])
def test_creation_discrete_plural(unit):
    """Verify initialization with proper values when created from discrete inputs with pluralized names."""
    value = random.randint(0, 1000) / 10
    instance = ComplesTypeStub(value, unit)

    assert isinstance(instance, ComplesTypeStub)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("unit", [
    'one',
    'two',
    'three',
    'hundred',
    'thousand',
])
def test_creation_json(unit):
    """Verify initialization with proper values when created from JSON dictionary inputs."""
    value = random.randint(0, 1000) / 10
    json = {
        'value': value,
        'unit': unit,
    }
    instance = ComplesTypeStub(json=json)

    assert isinstance(instance, ComplesTypeStub)
    assert instance.value == value
    assert instance.as_(unit) == pytest.approx(value)


# ----------------------------------------------------------------------------------------------------------------------
def test_creation_exception_empty():
    """Verify that an exception is thrown when the inputs are missing."""
    with pytest.raises(TypeError):
        ComplesTypeStub()


# ----------------------------------------------------------------------------------------------------------------------
def test_creation_exception_missing_unit():
    """Verify that an exception is thrown when the units are missing in the constructor."""
    with pytest.raises(TypeError):
        ComplesTypeStub(value=1)


# ----------------------------------------------------------------------------------------------------------------------
def test_creation_exception_missing_value():
    """Verify that an exception is thrown when the value is missing in the constructor."""
    with pytest.raises(TypeError):
        ComplesTypeStub(unit='one')


# ----------------------------------------------------------------------------------------------------------------------
def test_creation_exception_missing_unit_json():
    """Verify that an exception is thrown when the units are missing in the JSON constructor."""
    json = {
        'value': 1
    }
    with pytest.raises(TypeError):
        ComplesTypeStub(json=json)


# ----------------------------------------------------------------------------------------------------------------------
def test_creation_exception_missing_value_json():
    """Verify that an exception is thrown when the units are missing in the JSON constructor."""
    json = {
        'unit': 'one'
    }
    with pytest.raises(TypeError):
        ComplesTypeStub(json=json)


# ----------------------------------------------------------------------------------------------------------------------
def test_invalid_units():
    """Verify that a UnitError is thrown when trying to instantiate with unsupported units."""
    with pytest.raises(UnitError):
        ComplesTypeStub(1, 'five')




# ======================================================================================================================
# Property Validation
# ----------------------------------------------------------------------------------------------------------------------
def test_root():
    """Verify the root property returns the value in the units of "ones"."""
    instance = ComplesTypeStub(10, 'tens')
    assert instance.root == 100


# ----------------------------------------------------------------------------------------------------------------------
def test_dynamic_properties():
    """Verify that the overridden __getattr__ method serves to allow fetching the value in the appropriate units."""
    instance = ComplesTypeStub(10, 'tens')

    assert instance.ones == 100
    assert instance.two == 50
    assert instance.three == pytest.approx(33.333333)
    assert instance.tens == 10
    assert instance.hundreds == 1
    assert instance.HUNDRED == 1
    assert instance.Sixties == pytest.approx(1.666667)
    assert instance.thousands == 0.1
    assert instance.ThOuSandS == 0.1


# ----------------------------------------------------------------------------------------------------------------------
def test_invalid_dynamic_properties():
    """Because __getattr__ has been overridden to provide nifty properties in the units specific to the type, ensure
    that __getattr__ throws AttributeErrors when invalid attributes are requested."""
    instance = ComplesTypeStub(10, 'tens')
    with pytest.raises(AttributeError):
        instance.five




# ======================================================================================================================
# Method Validation
# ----------------------------------------------------------------------------------------------------------------------
def test_to_dict():
    """Verify that the conversion to JSON dict follows the BeerJSON format and the JsonOutput conversion is followed."""
    instance = ComplesTypeStub(1, 'three')
    assert instance.one == 3

    json = instance.to_dict()
    assert len(json.keys()) == 2
    assert 'value' in json.keys()
    assert json['value'] == 1
    assert 'unit' in json.keys()
    assert json['unit'] == 'Thrice'


# ----------------------------------------------------------------------------------------------------------------------
def test_from_dict_error():
    """The from_dict method is pretty well covered in the JSON constructor tests, but specifically this test checks to
    ensure that a TypeError is thrown when bad data is included in the JSON."""
    instance = ComplesTypeStub(1, 'one')
    with pytest.raises(TypeError):
        instance.from_dict({
            'value': 1,
            'unit': 'one',
            'extra': True,
        })


# ----------------------------------------------------------------------------------------------------------------------
def test_copy():
    """Ensure that the copy method creates a new instance of this class and that the values are the same."""
    original = ComplesTypeStub(3, 'one')
    assert original.one == 3

    duplicate = original.copy()
    assert isinstance(duplicate, ComplesTypeStub)
    assert duplicate is not original
    assert duplicate.one == 3
    assert duplicate.unit == original.unit


# ----------------------------------------------------------------------------------------------------------------------
def test_convert():
    """Verify that convert actually changes the stored units/value of the instance."""
    instance = ComplesTypeStub(3, 'one')
    assert instance.value == 3
    assert instance.unit == 'one'

    result = instance.convert('three')
    assert result == 1
    assert instance.value == 1
    assert instance.unit == 'three'



# ======================================================================================================================
# Override Verifications
# ----------------------------------------------------------------------------------------------------------------------
def test_string():
    """Verify that the conversion to string produces the expected human readable string representation."""
    instance = ComplesTypeStub(3, 'tens')
    assert instance.tens == 3
    string = str(instance)
    assert string == '3.0 ten'


# ----------------------------------------------------------------------------------------------------------------------
def test_equal():
    """Verify that the equality operator properly compares the VALUE of two instances."""
    first = ComplesTypeStub(1, 'ten')
    second = ComplesTypeStub(10, 'one')
    assert first is not second
    assert first == second


# ----------------------------------------------------------------------------------------------------------------------
def test_not_equal():
    """Verify that the not-equal operator properly compares the VALUE of two instances."""
    first = ComplesTypeStub(2, 'ten')
    second = ComplesTypeStub(10, 'one')
    assert first is not second
    assert first != second


# ----------------------------------------------------------------------------------------------------------------------
def test_greater_than():
    """Verify that the greater than operator properly compares the VALUE of two instances."""
    first = ComplesTypeStub(2, 'ten')
    second = ComplesTypeStub(10, 'one')
    assert first is not second
    assert first > second


# ----------------------------------------------------------------------------------------------------------------------
def test_less_than():
    """Verify that the less than operator properly compares the VALUE of two instances."""
    first = ComplesTypeStub(1, 'ten')
    second = ComplesTypeStub(20, 'one')
    assert first is not second
    assert first < second


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize('valOne, unitOne, valTwo, unitTwo', [
    (1, 'ten', 10, 'one'),
    (10, 'one', 1, 'ten'),
    (2, 'ten', 10, 'one'),
    (1, 'hundred', 10, 'one'),
])
def test_greater_than_or_equal(valOne, unitOne, valTwo, unitTwo):
    """Verify that the greater than or equal to operator properly compares the VALUE of two instances."""
    first = ComplesTypeStub(valOne, unitOne)
    second = ComplesTypeStub(valTwo, unitTwo)
    assert first is not second
    assert first >= second


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize('valOne, unitOne, valTwo, unitTwo', [
    (1, 'ten', 10, 'one'),
    (10, 'one', 1, 'ten'),
    (1, 'ten', 11, 'one'),
    (1, 'ten', 1, 'hundred'),
])
def test_less_than_or_equal(valOne, unitOne, valTwo, unitTwo):
    """Verify that the less than or equal to operator properly compares the VALUE of two instances."""
    first = ComplesTypeStub(valOne, unitOne)
    second = ComplesTypeStub(valTwo, unitTwo)
    assert first is not second
    assert first <= second


# ----------------------------------------------------------------------------------------------------------------------
def test_addition():
    """Verify that adding two of the same together sums the values."""
    first = ComplesTypeStub(1, 'one')
    second = ComplesTypeStub(1, 'ten')
    assert first is not second
    assert first.one == 1
    assert second.one == 10

    result = second + first

    # Ensure that a new instance is created with the result.
    assert isinstance(result, ComplesTypeStub)
    assert result is not first
    assert result is not second

    # Ensure that the original inputs were not changed.
    assert first.one == 1
    assert first.unit == 'one'
    assert second.one == 10
    assert second.unit == 'ten'

    # Ensure that the results are correct and in the units of the left side of the addition.
    assert result.one == 11
    assert result.unit == 'ten'


# ----------------------------------------------------------------------------------------------------------------------
def test_addition_bad_types():
    """Verify that addition on two different class types fails."""
    first = ComplesTypeStub(1, 'one')
    second = AnotherComplexTypeStub(1, 'pound')
    with pytest.raises(TypeError):
        first + second


# ----------------------------------------------------------------------------------------------------------------------
def test_subtraction():
    """Verify that subtraction works, similar to addition."""
    first = ComplesTypeStub(1, 'one')
    second = ComplesTypeStub(1, 'ten')
    assert first is not second
    assert first.one == 1
    assert second.one == 10

    result = second - first

    # Ensure that a new instance is created with the result.
    assert isinstance(result, ComplesTypeStub)
    assert result is not first
    assert result is not second

    # Ensure that the original inputs were not changed.
    assert first.one == 1
    assert first.unit == 'one'
    assert second.ten == 1
    assert second.unit == 'ten'

    # Ensure that the results are correct and in the units of the left side of the subtraction.
    assert result.one == 9
    assert result.unit == 'ten'


# ----------------------------------------------------------------------------------------------------------------------
def test_subtraction_bad_types():
    """Verify that subtracting two different class types fails."""
    first = ComplesTypeStub(1, 'one')
    second = AnotherComplexTypeStub(1, 'pound')
    with pytest.raises(TypeError):
        first - second


# ----------------------------------------------------------------------------------------------------------------------
def test_multiplication_same():
    """Verify that multiplication works using two instances of the same class."""
    first = ComplesTypeStub(2, 'one')
    second = ComplesTypeStub(1, 'ten')
    assert first is not second
    assert first.one == 2
    assert second.one == 10

    result = first * second

    # Ensure that a new instance is created with the result.
    assert isinstance(result, ComplesTypeStub)
    assert result is not first
    assert result is not second

    # Ensure that the original inputs were not changed.
    assert first.one == 2
    assert first.unit == 'one'
    assert second.ten == 1
    assert second.unit == 'ten'

    # Ensure that the results are correct and in the units of the left side of the multiplication.
    assert result.one == 20
    assert result.unit == 'one'


# ----------------------------------------------------------------------------------------------------------------------
def test_multiplication_percent():
    """Verify that multiplication works using one instance of ComplexTypeSub and one instance of percent."""
    instance = ComplesTypeStub(1, 'hundred')
    percent = PercentType(50, 'percent')
    assert instance is not percent
    assert instance.one == 100
    assert percent.percent == 50

    result = instance * percent

    # Ensure that a new instance is created with the result.
    assert isinstance(result, ComplesTypeStub)
    assert result is not instance
    assert result is not percent

    # Ensure that the original inputs were not changed.
    assert instance.one == 100
    assert instance.unit == 'hundred'
    assert percent.percent == 50
    assert percent.unit == '%'

    # Ensure that the results are correct and in the units original instance.
    assert result.one == 50
    assert result.unit == 'hundred'

    # Verify that the reverse order throws a TypeError
    with pytest.raises(TypeError):
        percent * instance


# ----------------------------------------------------------------------------------------------------------------------
def test_multiplication_scalar_float():
    """Verify that multiplication works using one instance of ComplexTypeSub and one float."""
    instance = ComplesTypeStub(1, 'hundred')
    assert instance.one == 100

    result = instance * 0.5

    # Ensure that a new instance is created with the result.
    assert isinstance(result, ComplesTypeStub)
    assert result is not instance

    # Ensure that the original inputs were not changed.
    assert instance.one == 100
    assert instance.unit == 'hundred'

    # Ensure that the results are correct and in the units original instance.
    assert result.one == 50
    assert result.unit == 'hundred'


# ----------------------------------------------------------------------------------------------------------------------
def test_multiplication_scalar_int():
    """Verify that multiplication works using one instance of ComplexTypeSub and one int."""
    instance = ComplesTypeStub(1, 'hundred')
    assert instance.one == 100

    result = instance * 2

    # Ensure that a new instance is created with the result.
    assert isinstance(result, ComplesTypeStub)
    assert result is not instance

    # Ensure that the original inputs were not changed.
    assert instance.one == 100
    assert instance.unit == 'hundred'

    # Ensure that the results are correct and in the units original instance.
    assert result.one == 200
    assert result.unit == 'hundred'


# ----------------------------------------------------------------------------------------------------------------------
def test_division_same():
    """Verify that division works using two instances of the same class."""
    first = ComplesTypeStub(2, 'one')
    second = ComplesTypeStub(1, 'ten')
    assert first is not second
    assert first.ten == 0.2
    assert second.one == 10

    result = second / first

    # Ensure that a new instance is created with the result.
    assert isinstance(result, ComplesTypeStub)
    assert result is not first
    assert result is not second

    # Ensure that the original inputs were not changed.
    assert first.one == 2
    assert first.unit == 'one'
    assert second.ten == 1
    assert second.unit == 'ten'

    # Ensure that the results are correct and in the units of the left side of the division.
    assert result.one == 5
    assert result.unit == 'ten'


# ----------------------------------------------------------------------------------------------------------------------
def test_division_percent():
    """Verify that division works using one instance of ComplexTypeSub and one instance of percent."""
    instance = ComplesTypeStub(1, 'hundred')
    percent = PercentType(25, 'percent')
    assert instance is not percent
    assert instance.one == 100
    assert percent.percent == 25

    result = instance / percent

    # Ensure that a new instance is created with the result.
    assert isinstance(result, ComplesTypeStub)
    assert result is not instance
    assert result is not percent

    # Ensure that the original inputs were not changed.
    assert instance.one == 100
    assert instance.unit == 'hundred'
    assert percent.percent == 25
    assert percent.unit == '%'

    # Ensure that the results are correct and in the units original instance.
    assert result.one == 400
    assert result.unit == 'hundred'

    # Verify that the reverse order throws a TypeError
    with pytest.raises(TypeError):
        percent / instance


# ----------------------------------------------------------------------------------------------------------------------
def test_division_scalar_float():
    """Verify that division works using one instance of ComplexTypeSub and one float."""
    instance = ComplesTypeStub(1, 'hundred')
    assert instance.one == 100

    result = instance / 0.5

    # Ensure that a new instance is created with the result.
    assert isinstance(result, ComplesTypeStub)
    assert result is not instance

    # Ensure that the original inputs were not changed.
    assert instance.one == 100
    assert instance.unit == 'hundred'

    # Ensure that the results are correct and in the units original instance.
    assert result.one == 200
    assert result.unit == 'hundred'


# ----------------------------------------------------------------------------------------------------------------------
def test_division_scalar_int():
    """Verify that division works using one instance of ComplexTypeSub and one int."""
    instance = ComplesTypeStub(1, 'hundred')
    assert instance.one == 100

    result = instance / 2

    # Ensure that a new instance is created with the result.
    assert isinstance(result, ComplesTypeStub)
    assert result is not instance

    # Ensure that the original inputs were not changed.
    assert instance.one == 100
    assert instance.unit == 'hundred'

    # Ensure that the results are correct and in the units original instance.
    assert result.one == 50
    assert result.unit == 'hundred'


# ----------------------------------------------------------------------------------------------------------------------
def test_in_place_addition():
    """Verify that in-place addition is supported."""
    first = ComplesTypeStub(1, 'one')
    second = ComplesTypeStub(1, 'ten')
    assert first is not second
    assert first.one == 1
    assert second.one == 10

    first += second

    # Ensure that the second inputs was not changed.
    assert second.one == 10
    assert second.unit == 'ten'

    # Ensure that the left side saw assignment of the proper result.
    assert first.one == 11
    assert first.unit == 'one'


# ----------------------------------------------------------------------------------------------------------------------
def test_in_place_subtraction():
    """Verify that in-place subtraction is supported."""
    first = ComplesTypeStub(1, 'ten')
    second = ComplesTypeStub(1, 'one')
    assert first is not second
    assert first.ten == 1
    assert second.one == 1

    first -= second

    # Ensure that the second inputs was not changed.
    assert second.one == 1
    assert second.unit == 'one'

    # Ensure that the left side saw assignment of the proper result.
    assert first.one == 9
    assert first.unit == 'ten'


# ----------------------------------------------------------------------------------------------------------------------
def test_in_place_multiplication():
    """Verify that in-place multiplication is supported."""
    instance = ComplesTypeStub(1, 'ten')
    assert instance.one == 10

    instance *= 3

    assert instance.one == 30
    assert instance.unit == 'ten'


# ----------------------------------------------------------------------------------------------------------------------
def test_in_place_division():
    """Verify that in-place division is supported."""
    instance = ComplesTypeStub(1, 'hundred')
    assert instance.one == 100

    instance /= 2

    assert instance.one == 50
    assert instance.unit == 'hundred'




# End of File
