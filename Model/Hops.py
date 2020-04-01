# ======================================================================================================================
#        File:  Model/Hops.py
#     Project:  Brewing Recipe Planner
# Description:  A definition for a beer hops in list form.
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
from typing import List

from Model.ListTableBase import ListTableBase
from GUI.Table.Column import Column
from GUI.Table.Sizing import Stretch
from Model.Hop import Hop
from Model.MeasurableUnits import PercentType



# ======================================================================================================================
# Hops Class
# ----------------------------------------------------------------------------------------------------------------------
class Hops(ListTableBase):
    """Provides for a list of Hop objects, specifically created to aid in parsing Excel database files and
    display within a QtTableView."""
    Columns = [
        Column('amount', align=QtCore.Qt.AlignRight, editable=True, hideLimited=True),
        Column('timing.use', 'Use In', align=QtCore.Qt.AlignLeft, editable=True, hideLimited=True),
        Column('timing.duration', 'Duration', align=QtCore.Qt.AlignHCenter, editable=True, hideLimited=True),
        Column('_ibus', 'IBUs', template='%.1f IBUs', align=QtCore.Qt.AlignRight, hideLimited=True),
        Column('name', size=Stretch, align=QtCore.Qt.AlignLeft),
        Column('htype', 'Type', align=QtCore.Qt.AlignLeft),
        Column('form', align=QtCore.Qt.AlignRight),
        Column('origin', align=QtCore.Qt.AlignHCenter),
        Column('alpha', align=QtCore.Qt.AlignRight)
    ]



# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def trubLoss(self):
        loss = 0
        for hop in self.items:
            if 'Boil' not in hop.timing.use:
                continue

            if 'Leaf' in hop.form:
                loss += hop.amount.as_('oz') * 0.0625

            elif 'Pellet' in hop.form:
                loss += hop.amount.as_('oz') * 0.025

        return loss



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

            self.append(Hop(
                name=str(row[0].value),
                htype=str(row[1].value),
                form=str(row[2].value),
                alpha=PercentType(row[3].value, '%'),
                beta=PercentType(row[4].value, '%'),
                hsi=PercentType(row[5].value, '%'),
                origin=str(row[6].value),
                substitutes=str(row[7].value),
                humulene=PercentType(row[8].value, '%'),
                caryophyllene=PercentType(row[9].value, '%'),
                cohumulone=PercentType(row[10].value, '%'),
                myrcene=PercentType(row[11].value, '%'),
                notes=str(row[12].value)
            ))


# ----------------------------------------------------------------------------------------------------------------------
    def sort(self):
        """A void sort function that consistently sorts the hop in decreasing order of amount in the recipe."""
        uses = ['Mash', 'Boil', 'Fermentation']
        self.items.sort(key=lambda hop: (uses.index(hop.timing.use), -hop.timing.duration.as_('sec'), hop.name))


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert self into a dictionary for BeerJSON storage."""
        return [hop.to_dict() for hop in self]


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, recipe, data):
        """Parse list of hops from the provided BeerJSON dict."""
        for item in data:
            hop = Hop(recipe)
            hop.from_dict(item)
            self.append(hop)



# End of File
