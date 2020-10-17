# ======================================================================================================================
#        File:  Model/Mash.py
#     Project:  Brewing Recipe Planner
# Description:  A base for fermenting a beer.
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
from PySide2 import QtCore

from Model.ListTableBase import ListTableBase
from Model.MashStep import MashStep
from Model.MeasurableUnits import SpecificVolumeType, TemperatureType, VolumeType
from GUI.Table.Column import Column
from GUI.Table.Sizing import Stretch



# ======================================================================================================================
# Mash Class
# ----------------------------------------------------------------------------------------------------------------------
class Mash(ListTableBase):
    """Tabular definition for fermentation steps outlining the fermentation process."""
    Columns = [
        Column('name', size=Stretch, align=QtCore.Qt.AlignLeft, editable=True),
        Column('mtype', 'Type', align=QtCore.Qt.AlignLeft, editable=True),
        Column('temperature', editable=True),
        Column('time', editable=True),
        Column('infusionTemperature'),
        Column('infusionVolume'),
    ]


# ----------------------------------------------------------------------------------------------------------------------
    def __init__(self, recipe):
        super().__init__()
        self.recipe = recipe
        self.changed.connect(self.recalculate)

        self._ambient = TemperatureType(70, 'F')
        self._ratio = SpecificVolumeType(1.25, 'qt/lb')



# ======================================================================================================================
# Properties
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
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, value):
        if self._ratio != value:
            self._ratio = value
            self.changed.emit()


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def totalWater(self):
        """Calculates the total water required for all of the mashing steps."""
        return sum([step.infusionVolume for step in self if step.infusionVolume is not None], VolumeType(0, 'gal'))



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def from_excel(self, worksheet):
        """Not supported for fermentable types - they don't get defined in the Excel database."""
        raise NotImplementedError('Mash does not support loading library items from Excel worksheets.')


# ----------------------------------------------------------------------------------------------------------------------
    def sort(self):
        """Steps are sorted manually. Deliberately left blank - will be called but nothing will happen."""


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert this fermentation into BeerJSON."""
        return {
            'name': 'Why is the name required at this level?',
            'grain_temperature': self.recipe.mash.ambient.to_dict(),
            'mash_steps': [step.to_dict() for step in self.items]
        }


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data):
        """Convert a BeerJSON dict into values for this instance."""
        self.ambient = TemperatureType(json=data['grain_temperature'])
        if 'mash_steps' in data and data['mash_steps'] and 'water_grain_ratio' in data['mash_steps'][0]:
            self.ratio = SpecificVolumeType(json=data['mash_steps'][0]['water_grain_ratio'])

        self.items = []
        for child in data['mash_steps']:
            step = MashStep(self.recipe)
            step.from_dict(child)
            self.append(step)


# ----------------------------------------------------------------------------------------------------------------------
    def recalculate(self):
        """Recalculate the temperatures and volumes for the mash steps."""
        # Can't do anything if there aren't any steps yet.
        if not self.items:
            return
        # Calculate the initial step without any previous step.
        previous = self.items[0].calculate(None)

        # Run through the middle steps (stop one short of the end).
        for step in self.items[1:-1]:
            # NOTE: This loop will not run if there are two or less steps in the mash.
            previous = step.calculate(previous)

        if len(self) > 1:
            # Run the final calculation as a special case because we need to get up to our target volume.
            self.items[-1].calculate(previous, final=True)



# End of File
