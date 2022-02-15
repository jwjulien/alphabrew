# ======================================================================================================================
#        File:  Tests/Model/test_Hop.py
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

from Model.Hop import Hop
from Model.Timing import TimingType
from Model.MeasurableUnits import MassType, PercentType, TimeType, VolumeType



# ======================================================================================================================
# Recipe Stub Class
# ----------------------------------------------------------------------------------------------------------------------
class RecipeStub:
    def __init__(self):
        self.hops = []




# ======================================================================================================================
# Test Functions
# ----------------------------------------------------------------------------------------------------------------------
def test_creation_mass():
    recipe = RecipeStub()

    hop = Hop(
        recipe=recipe,
        name='Centennial',
        amount=MassType(3, 'oz'),
        timing=TimingType(duration=TimeType(60, 'min')),
        htype='Bittering',
        form='Pellet',
        alpha=PercentType(7, '%'),
        beta=PercentType(12, '%'),
        hsi=PercentType(20, '%'),
        origin='US',
        substitutes='Cascade',
        humulene=PercentType(2, '%'),
        caryophyllene=PercentType(3, '%'),
        cohumulone=PercentType(4, '%'),
        myrcene=PercentType(5, '%'),
        notes='Just a test hop.',
    )

    assert hop.name == 'Centennial'
    assert isinstance(hop.amount, MassType)
    assert hop.amount.oz == 3
    assert isinstance(hop.timing, TimingType)
    assert isinstance(hop.timing.duration, TimeType)
    assert hop.timing.duration.minutes == 60
    assert hop.htype == 'Bittering'
    assert hop.form == 'Pellet'
    assert isinstance(hop.alpha, PercentType)
    assert hop.alpha.percent == 7
    assert isinstance(hop.beta, PercentType)
    assert hop.beta.percent == 12
    assert isinstance(hop.hsi, PercentType)
    assert hop.hsi.percent == 20
    assert hop.origin == 'US'
    assert hop.substitutes == 'Cascade'
    assert isinstance(hop.humulene, PercentType)
    assert hop.humulene.percent == 2
    assert isinstance(hop.caryophyllene, PercentType)
    assert hop.caryophyllene.percent == 3
    assert isinstance(hop.cohumulone, PercentType)
    assert hop.cohumulone.percent == 4
    assert isinstance(hop.myrcene, PercentType)
    assert hop.myrcene.percent == 5
    assert hop.notes == 'Just a test hop.'



# ----------------------------------------------------------------------------------------------------------------------
def test_creation_value():
    """Test that a hop can be created with a VolumeAmount."""
    recipe = RecipeStub()

    hop = Hop(
        recipe=recipe,
        name='Centennial',
        amount=VolumeType(1, 'qt'),
        timing=TimingType(duration=TimeType(60, 'min')),
        htype='Bittering',
        form='Pellet',
        alpha=PercentType(7, '%'),
        beta=PercentType(12, '%'),
        hsi=PercentType(20, '%'),
        origin='US',
        substitutes='Cascade',
        humulene=PercentType(2, '%'),
        caryophyllene=PercentType(3, '%'),
        cohumulone=PercentType(4, '%'),
        myrcene=PercentType(5, '%'),
        notes='Just a test hop.',
    )

    assert hop.name == 'Centennial'
    assert isinstance(hop.amount, VolumeType)
    assert hop.amount.qt == 1
    assert isinstance(hop.timing, TimingType)
    assert isinstance(hop.timing.duration, TimeType)
    assert hop.timing.duration.minutes == 60
    assert hop.htype == 'Bittering'
    assert hop.form == 'Pellet'
    assert isinstance(hop.alpha, PercentType)
    assert hop.alpha.percent == 7
    assert isinstance(hop.beta, PercentType)
    assert hop.beta.percent == 12
    assert isinstance(hop.hsi, PercentType)
    assert hop.hsi.percent == 20
    assert hop.origin == 'US'
    assert hop.substitutes == 'Cascade'
    assert isinstance(hop.humulene, PercentType)
    assert hop.humulene.percent == 2
    assert isinstance(hop.caryophyllene, PercentType)
    assert hop.caryophyllene.percent == 3
    assert isinstance(hop.cohumulone, PercentType)
    assert hop.cohumulone.percent == 4
    assert isinstance(hop.myrcene, PercentType)
    assert hop.myrcene.percent == 5
    assert hop.notes == 'Just a test hop.'



# ----------------------------------------------------------------------------------------------------------------------
def test_copy():
    """Ensure that the copy method makes a proper copy of the hop."""
    recipe = RecipeStub()

    original = Hop(
        recipe=recipe,
        name='Centennial',
        amount=MassType(3, 'oz'),
        timing=TimingType(duration=TimeType(60, 'min')),
        htype='Bittering',
        form='Pellet',
        alpha=PercentType(7, '%'),
        beta=PercentType(12, '%'),
        hsi=PercentType(20, '%'),
        origin='US',
        substitutes='Cascade',
        humulene=PercentType(2, '%'),
        caryophyllene=PercentType(3, '%'),
        cohumulone=PercentType(4, '%'),
        myrcene=PercentType(5, '%'),
        notes='Just a test hop.',
    )

    newRecipe = RecipeStub()
    copy = original.copy(newRecipe)

    assert isinstance(copy, Hop)
    assert copy.recipe == newRecipe
    assert copy.name == 'Centennial'
    assert isinstance(copy.amount, MassType)
    assert copy.amount is not original.amount # Should be a new instance of MassType.
    assert copy.amount.oz == 3
    assert copy.timing is not original.timing
    assert copy.timing.duration is not original.timing.duration
    assert copy.timing.duration == original.timing.duration
    assert copy.htype == 'Bittering'
    assert copy.form == 'Pellet'
    assert copy.alpha is not original.alpha
    assert copy.alpha == original.alpha
    assert copy.beta is not original.beta
    assert copy.beta == original.beta
    assert copy.hsi is not original.hsi
    assert copy.hsi == original.hsi
    assert copy.origin == 'US'
    assert copy.substitutes == 'Cascade'
    assert copy.humulene is not original.humulene
    assert copy.humulene == original.humulene
    assert copy.caryophyllene is not original.caryophyllene
    assert copy.caryophyllene == original.caryophyllene
    assert copy.cohumulone is not original.cohumulone
    assert copy.cohumulone == original.cohumulone
    assert copy.myrcene is not original.myrcene
    assert copy.myrcene == original.myrcene
    assert copy.notes == 'Just a test hop.'



# ----------------------------------------------------------------------------------------------------------------------
def test_to_dict():
    """Verify that the conversion to dict is as expected and follows the BeerJSON format."""





# End of File
