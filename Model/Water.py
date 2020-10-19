# ======================================================================================================================
#        File:  Model/Water.py
#     Project:  Brewing Recipe Planner
# Description:  Provides the definition for a single water addition.
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
from Model.MeasurableUnits import ConcentrationType, PercentType, VolumeType



# ======================================================================================================================
# Water Class
# ----------------------------------------------------------------------------------------------------------------------
class Water():
    """The Water class represents a single water contribution to a beer recipe.  Multiple Water instances may be
    gathered in a Waters instance as part of a recipe."""
    def __init__(self,
                 recipe=None,
                 name=None,
                 calcium=None,
                 magnesium=None,
                 sodium=None,
                 chloride=None,
                 sulfate=None,
                 bicarbonate=None,
                 ph=None,
                 percentage=None,
                 notes=None):
        self.recipe = recipe
        self.name: str = name
        self.calcium: ConcentrationType = calcium
        self.magnesium: ConcentrationType = magnesium
        self.sodium: ConcentrationType = sodium
        self.chloride: ConcentrationType = chloride
        self.sulfate: ConcentrationType = sulfate
        self.bicarbonate: ConcentrationType = bicarbonate
        self.ph: float = ph
        self.percentage: PercentType = percentage
        self.notes: str = notes

        # This tool works in percentages, however, this is used to hold the amount read in from BeerJSON when parsing a
        # recipe as the total amount is required before the percentage can be determined.
        self._amount: VolumeType = None



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def copy(self, recipe):
        return Water(
            recipe=recipe,
            name=self.name,
            calcium=self.calcium.copy(),
            magnesium=self.magnesium.copy(),
            sodium=self.sodium.copy(),
            chloride=self.chloride.copy(),
            sulfate=self.sulfate.copy(),
            bicarbonate=self.bicarbonate.copy(),
            ph=self.ph,
            notes=self.notes
        )


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self) -> dict:
        """Convert this misc into a Python dictionary that can be used in assembling a BeerJSON format file.

        Returns a BeerJSON Water Type compatible dictionary."""
        amount = VolumeType(0, 'gal')
        if self.recipe is not None and self.percentage is not None:
            amount.value = self.recipe.mash.totalWater.as_('gal') * self.percentage.as_('%') / 100
        return {
            'name': self.name,
            'calcium': self.calcium.to_dict(),
            'magnesium': self.magnesium.to_dict(),
            'sodium': self.sodium.to_dict(),
            'chloride': self.chloride.to_dict(),
            'sulfate': self.sulfate.to_dict(),
            'bicarbonate': self.bicarbonate.to_dict(),
            'pH': self.ph,
            'amount': amount.to_dict(),
            'notes': self.notes.replace('\n', '\\n')
        }


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data: dict):
        """Populate the data in this instance from the provided BeerJSON format dict."""
        self.name = data['name']
        self.calcium = ConcentrationType(json=data['calcium'])
        self.magnesium = ConcentrationType(json=data['magnesium'])
        self.sodium = ConcentrationType(json=data['sodium'])
        self.chloride = ConcentrationType(json=data['chloride'])
        self.sulfate = ConcentrationType(json=data['sulfate'])
        self.bicarbonate = ConcentrationType(json=data['bicarbonate'])
        if 'pH' in data:
            self.ph = data['pH']
        self._amount = VolumeType(json=data['amount'])
        if 'notes' in data:
            self.notes = data['notes'].replace('\\n', '\n')


# ----------------------------------------------------------------------------------------------------------------------
    def calculate_percentage(self):
        """Called after the Waters object loads all of the waters from JSON to have this instance calculate it's
        percentage of the total water in this recipe."""
        try:
            percent = self._amount.as_('gal') / self.recipe.mash.totalWater.as_('gal') * 100
            self.percentage = PercentType(percent, '%')

        except ZeroDivisionError:
            # We get a divide by zero error when the mash has not been calculated yet.
            self.percentage = PercentType(100 / len(self.recipe.waters), '%')



# ======================================================================================================================
# Overridden Methods
# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self):
        text = '<Water'
        for key, value in self.__dict__.items():
            text += f' {key}="{value}"'
        text += '>'
        return text



# End of File
