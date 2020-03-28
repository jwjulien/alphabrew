# ======================================================================================================================
#        File:  Recipe/Recipe.py
#     Project:  Brewing Recipe Planner
# Description:  Provides the definition for constants, configurable items.
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
import json

from PySide2 import QtCore

from Recipe.Style import Style
from Recipe.Fermentables import Fermentables
from Recipe.Miscellanea import Miscellanea
from Recipe.Hops import Hops
from Brewhouse import Equipment, Constants
from Math import Gravity, Color



# ======================================================================================================================
# Constants
# ----------------------------------------------------------------------------------------------------------------------
# TODO: Move these constants to a more global location.
WaterDensity_LbPerGal = 8.345
SucroseDensity_LbPerGal = 13.19092344776



# ======================================================================================================================
# Recipe Class
# ----------------------------------------------------------------------------------------------------------------------
class Recipe(QtCore.QObject):

    changed = QtCore.Signal()

    def __init__(self, constants):
        super().__init__()

        self.constants: Constants = constants

        self._name: str = ''
        self._author: str = 'Jared Julien'
        self._style: Style = Style()
        self._rtype: str = 'all grain'
        self._equipment: Equipment = Equipment()
        self._size: float = 5 # Gallons
        self._boilTime: int = 60 # Minutes
        self._ambient: float = 70 # Degrees Fahrenheit

        self.fermentables = Fermentables()
        self.misc = Miscellanea()
        self.hops = Hops()

        # Connect events in children to top level change event.
        self.fermentables.changed.connect(self.changed.emit)
        self.hops.changed.connect(self.changed.emit)
        self.misc.changed.connect(self.changed.emit)



# ======================================================================================================================
# Simple Properties (getters and setters)
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self._name != value:
            self._name = value
            self.changed.emit()

# ----------------------------------------------------------------------------------------------------------------------
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if self._author != value:
            self._author = value
            self.changed.emit()

# ----------------------------------------------------------------------------------------------------------------------
    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        if self._style != value:
            self._style = value
            self.changed.emit()

# ----------------------------------------------------------------------------------------------------------------------
    @property
    def rtype(self):
        return self._rtype

    @rtype.setter
    def rtype(self, value):
        if self._rtype != value:
            self._rtype = value
            self.changed.emit()

# ----------------------------------------------------------------------------------------------------------------------
    @property
    def equipment(self):
        return self._equipment

    @equipment.setter
    def equipment(self, value):
        if self._equipment != value:
            self._equipment = value
            self.changed.emit()

# ----------------------------------------------------------------------------------------------------------------------
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if self._size != value:
            self._size = value
            self.changed.emit()

# ----------------------------------------------------------------------------------------------------------------------
    @property
    def ambient(self):
        return self._ambient

    @ambient.setter
    def ambient(self, value):
        if self._ambient != value:
            self._ambient = value
            self.changed.emit()

# ----------------------------------------------------------------------------------------------------------------------
    @property
    def boilTime(self):
        return self._boilTime

    @boilTime.setter
    def boilTime(self, value):
        if self._boilTime != value:
            self._boilTime = value
            self.changed.emit()



# ======================================================================================================================
# Calculated Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def boilSize(self):
        """Calculates and returns to total wort volume to be collected in the boil kettle during the lautering process.
        """
        # Determine how much water is needed to account for loss to the hops.
        # TODO: Once hops are implemented put some maths here using scale factors from Brewhouse.
        hopWaterLoss = 0

        # Determine how many gallons we expect to boil off over the time of the boil.
        boilOff = self.equipment.boilOffRate * (self.boilTime / 60)

        # TODO: Review and add in other water losses between the start and end of the boil.

        return self.totalWort + boilOff + hopWaterLoss


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def totalWort(self):
        """Calculates and returns to total wort volume to be placed into the fermentor, taking into account the various
        losses to the boil kettle, MLT, and siphoning processes - as defined in the Brewhouse configuration."""
        # TODO: Review the losses to cover for places in the system where sugar could get lost.
        return self.size + self.equipment.spargeHltDeadspace + self.equipment.siphonLoss


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def originalGravity(self):
        """Recalculate the original gravity for this recipe."""
        # Count sugar contributions from mashed ingredients, taking brewhouse efficiency into account.
        sugar = (self.fermentables.mashedSugar + self.fermentables.steepedSugar) * self.constants.brewhouseEfficiency

        # Add the sugar contributions from non-mashed ingredients.  Efficiency doesn't count because these are sugar,
        # juice, fruit, etc. that is just plain added to the batch.
        sugar += self.fermentables.nonMashedSugar

        # TODO: Take in losses from Trub/Chiller/deadspace.

        # Convert this total sugar amount into a Specific Gravity value and store it.
        return self.get_gravity(sugar, self.totalWort)


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def finalGravity(self):
        """Recalculate the final gravity for this recipe."""
        # TODO: No yeasts at the time this was created, put this in later to determine actual attenuation.
        # attenuation = self.yeasts.max_attenuation
        attenuation = 0.75

        # Determine the number of points that come from non-fermentable sugars.
        nonFermentablePoints = self.get_gravity(self.fermentables.nonFermentableSugar, self.totalWort) - 1

        # Convert the OG into points.
        points = self.originalGravity - 1

        # Subtract the non-fermentable points from the total points.
        points -= nonFermentablePoints

        # Determine how much fermentable sugar we expect to remain after fermentation completes.
        points *= (1 - attenuation)

        # Add the non-fermentable points back in again.
        points += nonFermentablePoints

        # Convert the total remaining points back into a specific gravity and store that as the final gravity.
        return points + 1


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def boilGravity(self):
        """Calculates the specific gravity value to be expected pre-boil."""
        sugar = self.constants.brewhouseEfficiency * self.fermentables.mashedSugar

        sugar += self.fermentables.nonMashedSugar

        sugar -= self.fermentables.lateAdditionSugar

        return self.get_gravity(sugar, self.boilSize)


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def abv(self):
        """Calculates the ABV or alcohol by volume for this beer based upon the OG and FG values."""
        return (self.originalGravity - self.finalGravity) * 1.3125


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def ibu(self):
        """Calculate the IBUs or international bittering units for this recipe."""
        ibus = 0

        volume = self.size + self.hops.trubLoss

        gravity = self.originalGravity

        for hop in self.hops:
            if hop.use not in ['Mash', 'Boil']:
                # Dry hopping doesn't contribute to bitterness so ignore those hop additions.
                continue

            minutes = 60 if hop.use == 'Mash' else hop.duration
            ibus += hop.ibus(volume, gravity, minutes)

        return ibus



# ----------------------------------------------------------------------------------------------------------------------
    @property
    def srm(self):
        """Estimate the color of this beer based upon the color contributions of each of the fermentable ingredients."""
        total = sum([fermentable.color * fermentable.amount for fermentable in self.fermentables])
        mcu = total / self.totalWort
        return Color.mcu_to_srm(mcu)


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def ibuGu(self):
        """Calculate the IBU vs. Gravity for an idea of the overall sweetness of the product."""
        points = (self.originalGravity - 1) * 1000
        return self.ibu / points


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def calories(self):
        """Compute the number of calories per 12 oz serving."""
        startPlato = Gravity.sg_to_plato(self.originalGravity)
        finishPlato = Gravity.sg_to_plato(self.finalGravity)

        realExtract = (0.1808 * startPlato) + (0.8192 * finishPlato)

        abw = (startPlato - realExtract) / (2.0665 - (0.010665 * startPlato))

        return((6.9 * abw) + 4 * (realExtract - 0.1)) * self.finalGravity * 3.55



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def to_beerjson(self):
        """Convert this instance into BeerJSON format."""
        recipeJson = {
            'name': self.name,
            'type': self.rtype,
            'style': self.style.to_dict(),
            'batch_size': {
                'value': self.size,
                'unit': 'gal'
            },
            'author': self.author,
            'efficiency': {
                'brewhouse': {
                    'value': self.constants.brewhouseEfficiency * 100,
                    'unit': '%'
                }
            },
            'ingredients': {
                'fermentable_additions': self.fermentables.to_dict(),
                'hop_additions': self.hops.to_dict(),
                'miscellaneous_additions': self.misc.to_dict()
            }
        }
        return json.dumps({
            'beerjson': {
                'version': 2,
                'recipes': [
                    recipeJson
                ]
            }
        })


# ----------------------------------------------------------------------------------------------------------------------
    def from_beerxml(self, beerxml):
        beerJson = json.loads(beerxml)
        root = beerJson['beerjson']
        version = root['version']
        if version != 2:
            raise ValueError(f'BeerJSON version {version} is not supported by this tool')
        recipes = root['recipes']
        if len(recipes) != 1:
            raise ValueError(f'This tool only supports one recipe per file, file contains {len(recipes)}')
        recipe = recipes[0]
        self.name = recipe['name']
        self.style.from_dict(recipe['style'])
        self.rtype = recipe['type']
        self.size = recipe['batch_size']['value']
        self.author = recipe['author']
        ingredients = recipe['ingredients']
        self.fermentables.from_dict(self, ingredients['fermentable_additions'])
        self.hops.from_dict(self, ingredients['hop_additions'])
        self.misc.from_dict(self, ingredients['miscellaneous_additions'])


# ----------------------------------------------------------------------------------------------------------------------
    def get_gravity(self, sugarWeight, wortVolume):
        """Given a weight value relative to the amount of sucrose in the wort, convert that into a specific gravity
        measurement."""
        # Using the density of sucrose, determine the volume that the sugar will take up.
        sugarVolume = sugarWeight / SucroseDensity_LbPerGal

        # Subtract the sugar volume from the total wort volume to get the volume of just the water.
        waterVolume = wortVolume - sugarVolume

        # Convert the volume of water into the water's weight.
        waterWeight = waterVolume * WaterDensity_LbPerGal

        # Calculate Plato gravity as the weight of the sugar over the weight of the solution.
        plato = sugarWeight / (sugarWeight + waterWeight) * 100

        # Finally, convert the Plato value into Specific Gravity and return that.
        return Gravity.plato_to_sg(plato)




# End of File
