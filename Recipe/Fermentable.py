# ======================================================================================================================
#        File:  Recipe/Fermentable.py
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
from PySide2 import QtCore, QtWidgets



# ======================================================================================================================
# Fermentable Class
# ----------------------------------------------------------------------------------------------------------------------
class Fermentable(QtCore.QObject):
    def __init__(self,
                 recipe=None,
                 name='',
                 amount=0,
                 ftype='',
                 group='',
                 producer='',
                 origin='',
                 fyield=0,
                 color=0,
                 moisture=0,
                 diastaticPower=0,
                 protein=0,
                 maxPerBatch=0,
                 coarseFineDiff=0,
                 addAfterBoil=False,
                 mashed=False,
                 notes=''):
        super().__init__()

        self.recipe = recipe
        self.name = name
        self.amount = amount
        self.ftype = ftype
        self.group = group
        self.producer = producer
        self.origin = origin
        self.fyield = fyield
        self.color = color
        self.moisture = moisture
        self.diastaticPower = diastaticPower
        self.protein = protein
        self.maxPerBatch = maxPerBatch
        self.coarseFineDiff = coarseFineDiff
        self.addAfterBoil = addAfterBoil
        self.mashed = mashed
        self.notes = notes.replace('\\n', '\n') if notes else ''


# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def proportion(self):
        """Returns a float in the range [0.0, 100.0] representing this fermentables proportion within the associated
        recipe."""
        if self.recipe is None:
            return 0
        total = sum([fermentable.amount for fermentable in self.recipe.fermentables])
        if total == 0:
            return 0
        return self.amount / total * 100


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def isMashed(self):
        """Returns a Boolean indicating if this fermentable is mashed and therefor affected by mash efficiency."""
        return self.ftype.lower() == 'grain'


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def isFermentable(self):
        """Returns a Boolean indicating if this fermentable is actually fermentable.  Certain sugars such as lactose or
        Splenda are sweet, but do not ferment.

        Unfortunately there is no field in BeerJSON to handle if an ingredient is fermentable so we are forced to
        maintain a magical list of names here in an attempt to best guess if the provided item is fermentable.  This is
        obviously fragile as it would be as simple as editing the name of an ingredient to put it into or take it off
        of this last.
        """
        blacklist = [
            'lactose',
            'xylitol',
            'erythritol',
            'stevia',
            'splenda',
            'maltodextrin'
        ]

        # Walk through the blacklist and compare it to the name of this fermentable.
        for item in blacklist:
            # If we find a match, then lets assume that this item is NOT fermentable.
            if item in self.name.lower():
                return False

        # Lets assume that everything else is indeed fermentable.
        return True


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def sucrose(self):
        """Returns the equivalent amount of sucrose in this fermentable."""
        sucrose = self.amount * self.fyield * (1 - self.moisture)

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
            amount=self.amount,
            ftype=self.ftype,
            group=self.group,
            producer=self.producer,
            origin=self.origin,
            fyield=self.fyield,
            color=self.color,
            moisture=self.moisture,
            diastaticPower=self.diastaticPower,
            protein=self.protein,
            maxPerBatch=self.maxPerBatch,
            coarseFineDiff=self.coarseFineDiff,
            addAfterBoil=self.addAfterBoil,
            mashed=self.mashed,
            notes=self.notes
        )


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert this fermentable into a Python dictionary that can be used in assembling a BeerJSON format file.

        Returns a BeerJSON FermentableType compatible dictionary."""
        data = {
            'name': self.name,
            'type': self.ftype.lower(),
            'origin': self.origin,
            'producer': self.producer,
            'yield': {
                'coarse_grind': {
                    'value': self.fyield,
                    'unit': '%'
                },
                'fine_coarse_difference': {
                    'value': self.coarseFineDiff,
                    'unit': '%'
                }
            },
            'color': {
                'value': self.color,
                'unit': 'SRM'
            },
            'amount': {
                'value': self.amount,
                'unit': 'lb'
            },
            'notes': self.notes.replace('\n', '\\n'),
            'moisture': {
                'value': self.moisture,
                'unit': '%'
            },
            'diastatic_power': {
                'value': self.diastaticPower,
                'unit': 'Lintner'
            },
            'protein': {
                'value': self.protein,
                'unit': '%'
            },
            'max_in_batch': {
                'value': self.maxPerBatch,
                'unit': '%'
            },
            'recommend_mash': self.mashed
        }
        if self.group is not None:
            data['grain_group'] = self.group.lower()
        return data


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data):
        self.name = data['name']
        self.amount = data['amount']['value'] # TODO: Deal with other units
        self.ftype = data['type'].title()
        self.group = data['grain_group'].title() if 'grain_group' in data else None
        self.producer = data['producer']
        self.origin = data['origin']
        self.fyield = data['yield']['coarse_grind']['value']
        self.color = data['color']['value'] # TODO: Other units.
        self.moisture = data['moisture']['value']
        self.diastaticPower = data['diastatic_power']['value'] # TODO: Other units.
        self.protein = data['protein']['value']
        self.maxPerBatch = data['max_in_batch']['value']
        self.coarseFineDiff = data['yield']['fine_coarse_difference']['value']
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
