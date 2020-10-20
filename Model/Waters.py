# ======================================================================================================================
#        File:  Model/Waters.py
#     Project:  Brewing Recipe Planner
# Description:  A definition for a beer waters in list form.
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
from GUI.Table.Column import Column
from GUI.Table.Sizing import Stretch
from Model.Water import Water
from Model.MeasurableUnits import ConcentrationType



# ======================================================================================================================
# Waters Class
# ----------------------------------------------------------------------------------------------------------------------
class Waters(ListTableBase):
    """Provides for a list of Water objects, specifically created to aid in parsing Excel database files and
    display within a QtTableView."""
    Columns = [
        Column('name', size=Stretch, align=QtCore.Qt.AlignLeft),
        Column('calcium'),
        Column('magnesium'),
        Column('sodium'),
        Column('chloride'),
        Column('sulfate'),
        Column('bicarbonate'),
        Column('ph', 'pH'),
    ]



# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def calcium(self):
        """Calculate and return the total calcium in the water based upon the percentage of each water component."""
        return sum([water.calcium * water.percentage for water in self], ConcentrationType(0, 'ppm'))


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def magnesium(self):
        """Calculate and return the total magnesium in the water based upon the percentage of each water component."""
        return sum([water.magnesium * water.percentage for water in self], ConcentrationType(0, 'ppm'))


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def sodium(self):
        """Calculate and return the total sodium in the water based upon the percentage of each water component."""
        return sum([water.sodium * water.percentage for water in self], ConcentrationType(0, 'ppm'))


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def chloride(self):
        """Calculate and return the total chloride in the water based upon the percentage of each water component."""
        return sum([water.chloride * water.percentage for water in self], ConcentrationType(0, 'ppm'))


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def sulfate(self):
        """Calculate and return the total sulfate in the water based upon the percentage of each water component."""
        return sum([water.sulfate * water.percentage for water in self], ConcentrationType(0, 'ppm'))


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def bicarbonate(self):
        """Calculate and return the total bicarbonate in the water based upon the percentage of each water component."""
        return sum([water.bicarbonate * water.percentage for water in self], ConcentrationType(0, 'ppm'))


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def carbonate(self):
        """Calculate and return the total carbonate in the water based upon the percentage of each water component."""
        return sum([water.carbonate * water.percentage for water in self], ConcentrationType(0, 'ppm'))


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def alkalinity(self):
        """Calculate and return the total alkalinity in the water based upon the percentage of each water component."""
        return sum([water.alkalinity * water.percentage for water in self], ConcentrationType(0, 'ppm'))


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def hardness(self):
        """Calculate and return the total harness in the water based upon the percentage of each water component."""
        return sum([water.hardness * water.percentage.as_('%') / 100 for water in self])


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def ph(self):
        """Calculate and return the total bicarbonate in the water based upon the percentage of each water component."""
        return sum([water.ph * water.percentage.as_('%') / 100 for water in self])




# ======================================================================================================================
# Other Methods
# ----------------------------------------------------------------------------------------------------------------------
    def from_excel(self, worksheet):
        """Parses out a list of hop objects from the provided Excel worksheet and appends them to this instance."""
        self.items = []
        for idx, row in enumerate(worksheet):
            # Skip the header row.
            if idx == 0:
                continue

            self.append(Water(
                name=str(row[0].value),
                calcium=ConcentrationType(row[1].value, 'ppm'),
                magnesium=ConcentrationType(row[2].value, 'ppm'),
                sodium=ConcentrationType(row[3].value, 'ppm'),
                chloride=ConcentrationType(row[4].value, 'ppm'),
                sulfate=ConcentrationType(row[5].value, 'ppm'),
                bicarbonate=ConcentrationType(row[6].value, 'ppm'),
                ph=float(row[7].value),
                notes=str(row[8].value)
            ))


# ----------------------------------------------------------------------------------------------------------------------
    def sort(self):
        """A void sort function that consistently sorts the water in decreasing order of amount in the recipe."""
        def sorter(water: Water):
            """Give distilled water a higher priority in sorting than any other name."""
            if 'distilled' in water.name.lower():
                return 'A'
            return 'B' + water.name

        self.items.sort(key=sorter, reverse=True)


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert self into a dictionary for BeerJSON storage."""
        return [water.to_dict() for water in self]


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, recipe, data):
        """Parse list of waters from the provided BeerJSON dict."""
        for item in data:
            water = Water(recipe)
            water.from_dict(item)
            self.append(water)



# End of File
