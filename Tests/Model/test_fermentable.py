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
import pytest

from Model.Fermentable import Fermentable
from Model.MeasurableUnits import ColorType, DiastaticPowerType, MassType, PercentType



# ======================================================================================================================
# Recipe Stub Class
# ----------------------------------------------------------------------------------------------------------------------
class RecipeStub:
    def __init__(self):
        self.fermentables = []



# ======================================================================================================================
# Fermentable Generators
# ----------------------------------------------------------------------------------------------------------------------
def base_grain(recipe, pounds):
    return Fermentable(
        recipe=recipe,
        name='Base Grain',
        amount=MassType(pounds, 'lb'),
        ftype='Grain',
        group='Base',
        producer='Generic',
        origin='N/A',
        fyield=PercentType(70, '%'),
        color=ColorType(2, 'SRM'),
        moisture=PercentType(6, '%'),
        diastaticPower=DiastaticPowerType(10, 'Lintner'),
        addAfterBoil=False,
        mashed=True,
        notes='Not a real grain type',
        phi=5.5,
        bi=50,
    )


# ----------------------------------------------------------------------------------------------------------------------
def caramel_grain(recipe, pounds):
    return Fermentable(
        recipe=recipe,
        name='Caramel 20',
        amount=MassType(pounds, 'lb'),
        ftype='Grain',
        group='Caramel',
        producer='Generic',
        origin='N/A',
        fyield=PercentType(68, '%'),
        color=ColorType(20, 'SRM'),
        moisture=PercentType(3, '%'),
        diastaticPower=DiastaticPowerType(6, 'Lintner'),
        addAfterBoil=False,
        mashed=True,
        notes='Not a real grain type',
        phi=5.2,
        bi=56,
    )




# ======================================================================================================================
# Test Functions
# ----------------------------------------------------------------------------------------------------------------------
def test_proper_creation():
    recipe = RecipeStub()

    fermentable = Fermentable(
        recipe=recipe,
        name='Test Grain',
        amount=MassType(1, 'lb'),
        ftype='Grain',
        group='Base',
        producer='Generic',
        origin='US',
        fyield=PercentType(70, '%'),
        color=ColorType(2, 'SRM'),
        moisture=PercentType(6, '%'),
        diastaticPower=DiastaticPowerType(10, 'Lintner'),
        addAfterBoil=False,
        mashed=True,
        notes='Not a real grain type',
        phi=5.5,
        bi=50,
    )

    assert fermentable.name == 'Test Grain'
    assert isinstance(fermentable.amount, MassType)
    assert fermentable.amount.as_('lb') == 1
    assert fermentable.ftype == 'Grain'
    assert fermentable.group == 'Base'
    assert fermentable.group == 'Base'
    assert fermentable.origin == 'US'
    assert isinstance(fermentable.fyield, PercentType)
    assert fermentable.fyield.as_('%') == 70
    assert isinstance(fermentable.color, ColorType)
    assert fermentable.color.as_('SRM') == 2
    assert isinstance(fermentable.moisture, PercentType)
    assert fermentable.moisture.as_('%') == 6
    assert isinstance(fermentable.diastaticPower, DiastaticPowerType)
    assert fermentable.diastaticPower.as_('Lintner') == 10
    assert not fermentable.addAfterBoil
    assert fermentable.mashed
    assert fermentable.notes == 'Not a real grain type'
    assert fermentable.phi == 5.5
    assert fermentable.bi == 50


# ----------------------------------------------------------------------------------------------------------------------
def test_proportions():
    """Verify that the proportions of grains in a recipe are properly calculated."""
    recipe = RecipeStub()
    base = base_grain(recipe, 12)
    caramel = caramel_grain(recipe, 4)
    recipe.fermentables = [base, caramel]

    assert isinstance(base.proportion, PercentType)
    assert base.proportion.as_('%') == 75

    assert isinstance(caramel.proportion, PercentType)
    assert caramel.proportion.as_('%') == 25


# ----------------------------------------------------------------------------------------------------------------------
def test_proportions_no_weight():
    """Verify that the proportion calculation returns zero when there is no weight set for the fermentables."""
    recipe = RecipeStub()
    base = base_grain(recipe, 0)
    recipe.fermentables = [base]

    assert isinstance(base.proportion, PercentType)
    assert base.proportion.as_('%') == 0


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("ftype", [
    'Extract',
    'Dry Extract',
    'Fruit',
    'Honey',
    'Juice',
    'Sugar',
    'Other'
])
def test_is_not_mashed(ftype):
    """Verify that all types of fermentables, save for grains, skip the mash."""
    base = Fermentable(ftype=ftype)
    assert not base.isMashed


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("ftype", [
    'Grain',
    'grain',
])
def test_is_mashed(ftype):
    """Verify that grains get flagged as mashed."""
    base = Fermentable(ftype=ftype)
    assert base.isMashed


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("name", [
    'Maris Otter',
    '2 Row',
    'Light DME',
    'Table Sugar',
    'Molasses',
    'Flaked Oats'
])
def test_is_fermentable(name):
    """Verify that a given Fermentable is, indeed fermentable."""
    base = Fermentable(name=name)
    assert base.isFermentable


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("name", [
    'lactose',
    'xylitol',
    'erythritol',
    'Stevia',
    'Splenda',
    'maltodextrin'
])
def test_is_not_fermentable(name):
    """Verify that a non-fermentable Fermentable is, indeed non-fermentable."""
    sugar = Fermentable(name=name)
    assert not sugar.isFermentable


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("amount,ftype,mashed,fyield,moisture,sucrose", [
    (10, 'DME',   True,  100.0, 0.0, 10    ),
    (10, 'Grain', True,  72.0,  3.0, 6.984 ),
    (10, 'Grain', False, 72.0,  3.0, 4.1904),
])
def test_sucrose(amount, ftype, mashed, fyield, moisture, sucrose):
    """Verify the sucrose value for mashed and non-mashed fermentables."""
    fermentable = Fermentable(
        amount=MassType(amount, 'lb'),
        ftype=ftype,
        fyield=PercentType(fyield, '%'),
        moisture=PercentType(moisture, '%'),
        mashed=mashed,
    )

    assert fermentable.sucrose == pytest.approx(sucrose)


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("name,ftype,group,color,phi", [
    ('Table Sugar',  'Sugar',       None,        0,      0   ),
    ('Light DME',    'Dry Extract', None,        5.0,    0   ),
    ('Maris Otter',  'Grain',       'Base',      2.0,    5.72),
    ('6 Row',        'Grain',       'Base',      3.0,    5.69),
    ('Dextrin',      'Grain',       'Specialty', 45.0,   5.39),
    ('Black Patent', 'Grain',       'Roasted',   500.0,  4.64),
    ('Red Wheat',    'Grain',       'Base',      45.0,   5.97),
    ('Carapils',     'Grain',       'Caramel',   1.3,    5.71),
    ('Caramel 10',   'Grain',       'Caramel',   10.0,   5.26),
    ('Caramel 20',   'Grain',       'Caramel',   20.0,   5.15),
    ('Caramel 30',   'Grain',       'Caramel',   30.0,   4.89),
    ('Caramel 40',   'Grain',       'Caramel',   40.0,   4.89),
    ('Caramel 60',   'Grain',       'Caramel',   60.0,   4.81),
    ('Caramel 80',   'Grain',       'Caramel',   80.0,   4.74),
    ('Caramel 90',   'Grain',       'Caramel',   90.0,   4.74),
    ('Caramel 120',  'Grain',       'Caramel',   120.0,  4.68),
    ('Caramel 150',  'Grain',       'Caramel',   150.0,  4.48),
])
def test_phi(name, ftype, group, color, phi):
    """Verify DI pH estimations for fermentables where not explicitly set."""
    fermentable = Fermentable(
        name=name,
        ftype=ftype,
        group=group,
        color=ColorType(color, 'SRM'),
    )

    assert fermentable.phi == phi


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("name,ftype,group,color,bi", [
    ('Table Sugar',  'Sugar',       None,        0,      0.0 ),
    ('Light DME',    'Dry Extract', None,        5.0,    0.0 ),
    ('Maris Otter',  'Grain',       'Base',      2.0,    45.5),
    ('6 Row',        'Grain',       'Base',      3.0,    52.3),
    ('Dextrin',      'Grain',       'Specialty', 45.0,   55.1),
    ('Black Patent', 'Grain',       'Roasted',   500.0,  68.7),
    ('Red Wheat',    'Grain',       'Base',      45.0,   34.8),
    ('Carapils',     'Grain',       'Caramel',   1.3,    34.8),
    ('Caramel 10',   'Grain',       'Caramel',   10.0,   49.3),
    ('Caramel 20',   'Grain',       'Caramel',   20.0,   54.5),
    ('Caramel 30',   'Grain',       'Caramel',   30.0,   65.0),
    ('Caramel 40',   'Grain',       'Caramel',   40.0,   65.0),
    ('Caramel 60',   'Grain',       'Caramel',   60.0,   68.3),
    ('Caramel 80',   'Grain',       'Caramel',   80.0,   74.0),
    ('Caramel 90',   'Grain',       'Caramel',   90.0,   74.0),
    ('Caramel 120',  'Grain',       'Caramel',   120.0,  77.0),
    ('Caramel 150',  'Grain',       'Caramel',   150.0,  89.1),
])
def test_bi(name, ftype, group, color, bi):
    """Verify DI pH buffering capacity estimations for fermentables where not explicitly set."""
    fermentable = Fermentable(
        name=name,
        ftype=ftype,
        group=group,
        color=ColorType(color, 'SRM'),
    )

    assert fermentable.bi == bi




# End of File
