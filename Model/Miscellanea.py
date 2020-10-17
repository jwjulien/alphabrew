# ======================================================================================================================
#        File:  Model/Miscellanea.py
#     Project:  Brewing Recipe Planner
# Description:  A definition for a beer Miscellanea in list form.
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
from Model.Miscellaneous import Miscellaneous



# ======================================================================================================================
# Miscellanea Class
# ----------------------------------------------------------------------------------------------------------------------
class Miscellanea(ListTableBase):
    """Provides for a list of misc objects, specifically created to aid in parsing Excel database files and
    display within a QtTableView."""
    Columns = [
        Column('name', size=Stretch, align=QtCore.Qt.AlignLeft, editable=True),
        Column('mtype', 'Type', align=QtCore.Qt.AlignCenter, editable=True),
        Column('useFor', editable=True),
        Column('amount', editable=True),
        Column('timing.use', editable=True),
        Column('timing.duration', editable=True),
    ]



# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def salts(self):
        """Run through the items in this list a return a list of items that are marked as "water agents" without "acid"
        in there names."""
        return [item for item in self.items if item.mtype == 'Water Agent' and 'acid' not in item.name.lower()]


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def acids(self):
        """Run through the items in this list a return a list of items that are marked as "water agents" with "acid"
        in there names."""
        return [item for item in self.items if item.mtype == 'Water Agent' and 'acid' in item.name.lower()]



# ======================================================================================================================
# Other Methods
# ----------------------------------------------------------------------------------------------------------------------
    def from_excel(self, worksheet):
        """Misc item are not defined in Excel libraries."""
        raise NotImplementedError('Miscellaneous items are not defined in Excel libraries.')


# ----------------------------------------------------------------------------------------------------------------------
    def sort(self):
        """A void sort function that consistently sorts the misc in decreasing order of amount in the recipe."""
        self.items.sort(key=lambda misc: (-misc.amount.root, misc.name))


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert self into a dictionary for BeerJSON storage."""
        return [item.to_dict() for item in self]


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, recipe, data):
        """Parse list of miscellaneous items from the provided BeerJSON dict."""
        for item in data:
            misc = Miscellaneous(recipe)
            misc.from_dict(item)
            self.append(misc)



# End of File
