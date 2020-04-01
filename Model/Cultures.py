# ======================================================================================================================
#        File:  Model/Cultures.py
#     Project:  Brewing Recipe Planner
# Description:  A definition for a beer Cultures in list form.
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
from typing import List

from PySide2 import QtCore, QtWidgets

from Model.ListTableBase import ListTableBase
from GUI.Table.Column import Column
from GUI.Table.Sizing import Stretch
from Model.Culture import Culture
from Model.MeasurableUnits import PercentType, PercentRangeType



# ======================================================================================================================
# Cultures Class
# ----------------------------------------------------------------------------------------------------------------------
class Cultures(ListTableBase):
    """Provides for a list of Culture objects, specifically created to aid in parsing Excel database files and
    display within a QtTableView."""
    Columns = [
        Column('amount', editable=True, hideLimited=True),
        Column('name', size=Stretch, align=QtCore.Qt.AlignLeft),
        Column('ctype', 'Type'),
        Column('form'),
        Column('producer'),
        Column('productId', 'Product'),
    ]



# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def averageAttenuation(self):
        """Returns the maximum attenuation of all of the cultures in the collection."""
        return max([culture.averageAttenuation for culture in self.items])



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def from_excel(self, worksheet):
        """Dump any items currently associated with this instance and reload from the provided Excel worksheet."""
        self.items = []
        for idx, row in enumerate(worksheet):
            # Skip the header row.
            if idx == 0:
                continue

            self.append(Culture(
                name=str(row[0].value),
                ctype=str(row[1].value),
                form=str(row[2].value),
                producer=str(row[3].value),
                productId=str(row[4].value),
                attenuationRange=PercentRangeType(
                    minimum=PercentType(row[5].value * 100, '%'),
                    maximum=PercentType(row[6].value * 100, '%')
                ),
                notes=str(row[11].value)
            ))


# ----------------------------------------------------------------------------------------------------------------------
    def sort(self):
        """A void sort function that consistently sorts the culture in decreasing order of amount in the recipe."""
        self.items.sort(key=lambda culture: culture.name)


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert self into a dictionary for BeerJSON storage."""
        return [culture.to_dict() for culture in self]


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, recipe, data):
        """Parse list of cultures from the provided BeerJSON dict."""
        for item in data:
            culture = Culture(recipe)
            culture.from_dict(item)
            self.append(culture)



# End of File
