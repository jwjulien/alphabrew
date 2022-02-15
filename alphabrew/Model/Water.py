# ======================================================================================================================
#        File:  Model/Water.py
#     Project:  AlphaBrew
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
                 amount=None,
                 calcium=None,
                 magnesium=None,
                 sodium=None,
                 chloride=None,
                 sulfate=None,
                 bicarbonate=None,
                 ph=7.0,
                 notes=None):
        self.recipe = recipe
        self.name: str = name
        self.amount: VolumeType = amount
        self.calcium: ConcentrationType = calcium if calcium is not None else ConcentrationType(0, 'ppm')
        self.magnesium: ConcentrationType = magnesium if magnesium is not None else ConcentrationType(0, 'ppm')
        self.sodium: ConcentrationType = sodium if sodium is not None else ConcentrationType(0, 'ppm')
        self.chloride: ConcentrationType = chloride if chloride is not None else ConcentrationType(0, 'ppm')
        self.sulfate: ConcentrationType = sulfate if sulfate is not None else ConcentrationType(0, 'ppm')
        self.bicarbonate: ConcentrationType = bicarbonate if bicarbonate is not None else ConcentrationType(0, 'ppm')
        self.ph: float = ph
        self.notes: str = notes




# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def percentage(self):
        """Calculates the percentage of this water based upon the total amount of water needed."""
        try:
            percent = self.amount.gal / self.recipe.mash.totalWater.gal

        except ZeroDivisionError:
            # We get a divide by zero error when the mash has not been calculated yet.  Default to zero percent
            # so that it remains obvious theres an issue.
            percent = 0

        return PercentType(percent * 100, '%')


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def carbonate(self):
        """Calculates and returns the carbonate level for this water source.  Carbonate is a representation of the
        water hardness and is a factor of the water's pH and alkalinity."""
        alkalinityAsCaCO3 = self.bicarbonate.ppm / 1.22
        k2 = 10.3309621991148
        carbonate = alkalinityAsCaCO3 * (10 ** (self.ph - k2)) / (1 + (2 * (10 ** (self.ph - k2)))) * 60.008 / 50.043
        return ConcentrationType(carbonate, 'ppm')


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def alkalinity(self):
        """Computes the waters alkalinity based upon the bicarbonate and carbonate contributions."""
        return (self.bicarbonate.ppm / 61.016) + (2 * self.carbonate.ppm / 60.008)


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def hardness(self):
        """Compute the total hardness of this water source."""
        totalC = 1
        totalC += 4.435e-7 * (10 ** self.ph)
        totalC += 4.435e-7 * 4.667e-11 * (10 ** (2 * self.ph))
        totalC *= (self.bicarbonate.ppm / 61.016)
        totalC /= 4.435e-7 * (10 ** self.ph)
        return totalC



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
        water = {
            'name': self.name,
            'calcium': self.calcium.to_dict(),
            'magnesium': self.magnesium.to_dict(),
            'sodium': self.sodium.to_dict(),
            'chloride': self.chloride.to_dict(),
            'sulfate': self.sulfate.to_dict(),
            'bicarbonate': self.bicarbonate.to_dict(),
            'pH': self.ph,
            'amount': self.amount.to_dict(),
        }
        if self.notes is not None:
            water['notes'] = self.notes.replace('\n', '\\n')
        return water


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
        self.amount = VolumeType(json=data['amount'])
        if 'notes' in data:
            self.notes = data['notes'].replace('\\n', '\n')




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
