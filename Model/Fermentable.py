# ======================================================================================================================
#        File:  Model/Fermentable.py
#     Project:  Brewing Recipe Planner
# Description:  Provides the definition for a single fermentable or steepable item in a recipe.
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
from typing import Union

from PySide2 import QtCore, QtWidgets

from Model.MeasurableUnits import ColorType, DiastaticPowerType, MassType, PercentType, VolumeType
from Model import Selections



# ======================================================================================================================
# Fermentable Class
# ----------------------------------------------------------------------------------------------------------------------
class Fermentable(QtCore.QObject):
    def __init__(self,
                 recipe=None,
                 name=None,
                 amount=None,
                 ftype=None,
                 group=None,
                 producer=None,
                 origin=None,
                 fyield=None,
                 color=None,
                 moisture=None,
                 diastaticPower=None,
                 protein=None,
                 maxPerBatch=None,
                 coarseFineDiff=None,
                 addAfterBoil=None,
                 mashed=None,
                 notes=None):
        super().__init__()

        self.recipe = recipe
        self.name: str = name
        self.amount: Union[MassType, VolumeType] = amount
        self.ftype: str = ftype
        self.group: str = group
        self.producer: str = producer
        self.origin: str = origin
        self.fyield: PercentType = fyield
        self.color: ColorType = color
        self.moisture: PercentType = moisture
        self.diastaticPower: DiastaticPowerType = diastaticPower
        self.protein: PercentType = protein
        self.maxPerBatch: PercentType = maxPerBatch
        self.coarseFineDiff: PercentType = coarseFineDiff
        self.addAfterBoil: bool = addAfterBoil
        self.mashed: bool = mashed
        self.notes: str = notes.replace('\\n', '\n') if notes else ''


# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def proportion(self) -> float:
        """Returns a float in the range [0.0, 100.0] representing this fermentables proportion within the associated
        recipe."""
        if self.recipe is None:
            return 0
        total = sum([fermentable.amount.as_('lb') for fermentable in self.recipe.fermentables])
        if total == 0:
            return 0
        return self.amount.as_('lb') / total * 100


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def isMashed(self) -> bool:
        """Returns a Boolean indicating if this fermentable is mashed and therefor affected by mash efficiency."""
        return self.ftype == 'Grain'


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def isFermentable(self) -> bool:
        """Returns a Boolean indicating if this fermentable is actually fermentable.  Certain sugars such as lactose or
        Splenda are sweet, but do not ferment.

        Unfortunately there is no field in BeerJSON to handle if an ingredient is fermentable so we are forced to
        maintain a magical list of names here in an attempt to best guess if the provided item is fermentable.  This is
        obviously fragile as it would be as simple as editing the name of an ingredient to put it into or take it off
        of this last.
        """
        nonFermentable = [
            'lactose',
            'xylitol',
            'erythritol',
            'stevia',
            'splenda',
            'maltodextrin'
        ]

        # Walk through the blacklist and compare it to the name of this fermentable.
        for item in nonFermentable:
            # If we find a match, then lets assume that this item is NOT fermentable.
            if item in self.name.lower():
                return False

        # Lets assume that everything else is indeed fermentable.
        return True


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def sucrose(self) -> float:
        """Returns the equivalent amount of sucrose in this fermentable."""
        sucrose = self.amount.as_('lb') * (self.fyield.as_('%') / 100) * (1 - (self.moisture.as_('%') / 100))

        # If not mashed, then it must be steeped - reduce the yield by 40%.
        if not self.mashed:
            sucrose *= 0.6

        return sucrose




# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def copy(self, recipe):
        return Fermentable(
            recipe=recipe,
            name=self.name,
            amount=self.amount.copy() if self.amount is not None else None,
            ftype=self.ftype,
            group=self.group,
            producer=self.producer,
            origin=self.origin,
            fyield=self.fyield.copy(),
            color=self.color.copy(),
            moisture=self.moisture.copy(),
            diastaticPower=self.diastaticPower.copy(),
            protein=self.protein.copy(),
            maxPerBatch=self.maxPerBatch.copy(),
            coarseFineDiff=self.coarseFineDiff.copy(),
            addAfterBoil=self.addAfterBoil,
            mashed=self.mashed,
            notes=self.notes
        )


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self) -> dict:
        """Convert this fermentable into a Python dictionary that can be used in assembling a BeerJSON format file.

        Returns a BeerJSON FermentableType compatible dictionary."""
        data = {
            'name': self.name,
            'type': self.ftype.lower(),
            'origin': self.origin,
            'producer': self.producer,
            'yield': {
                'fine_grind': self.fyield.to_dict(),
                'fine_coarse_difference': self.coarseFineDiff.to_dict(),
            },
            'color': self.color.to_dict(),
            'amount': self.amount.to_dict(),
            'notes': self.notes.replace('\n', '\\n'),
            'moisture': self.moisture.to_dict(),
            'diastatic_power': self.diastaticPower.to_dict(),
            'protein': self.protein.to_dict(),
            'max_in_batch': self.maxPerBatch.to_dict(),
            'recommend_mash': self.mashed
        }
        if self.group is not None:
            data['grain_group'] = self.group.lower()
        return data


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data: dict):
        self.name = data['name']
        amount = data['amount']
        self.amount = Selections.one_of(amount['value'], amount['unit'], VolumeType, MassType)
        self.ftype = data['type'].title()
        if 'grain_group' in data:
            self.group = data['grain_group'].title()
        self.producer = data['producer']
        self.origin = data['origin']
        self.color = ColorType(json=data['color'])
        self.moisture = PercentType(json=data['moisture'])
        self.diastaticPower = DiastaticPowerType(json=data['diastatic_power'])
        self.protein = PercentType(json=data['protein'])
        self.maxPerBatch = PercentType(json=data['max_in_batch'])
        self.fyield = PercentType(json=data['yield']['fine_grind'])
        self.coarseFineDiff = PercentType(json=data['yield']['fine_coarse_difference'])
        self.mashed = data['recommend_mash']
        self.notes = data['notes'].replace('\\n', '\n')



# ======================================================================================================================
# Overridden Methods
# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self):
        text = '<Fermentable'
        for key, value in self.__dict__.items():
            text += f' {key}="{value}"'
        text += '>'
        return text



# End of File
