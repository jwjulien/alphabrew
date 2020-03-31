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

from GUI.Helpers.Column import Column
from GUI.Helpers.Sizing import Stretch
from Model.Hop import Hop
from Model.MeasurableUnits import PercentType



# ======================================================================================================================
# Hops Class
# ----------------------------------------------------------------------------------------------------------------------
class Hops(QtCore.QAbstractTableModel):
    """Provides for a list of Hop objects, specifically created to aid in parsing Excel database files and
    display within a QtTableView."""

    changed = QtCore.Signal()

    AllColumns = [
        Column('Amount', align=QtCore.Qt.AlignRight),
        Column('Use In', align=QtCore.Qt.AlignLeft),
        Column('Duration', align=QtCore.Qt.AlignHCenter),
        Column('IBUs', align=QtCore.Qt.AlignRight),
        Column('Name', size=Stretch, align=QtCore.Qt.AlignLeft),
        Column('Type', align=QtCore.Qt.AlignLeft),
        Column('Form', align=QtCore.Qt.AlignRight),
        Column('Origin', align=QtCore.Qt.AlignHCenter),
        Column('Alpha', align=QtCore.Qt.AlignRight)
    ]

    # These column indexes should be hidden when the class is instantiated with the limited flag set.
    # Intended to hide columns specific to inclusion in a recipe, such as amount, proportion, time, etc.
    HideWhenLimited = [0, 1, 2, 3]


# ----------------------------------------------------------------------------------------------------------------------
    def __init__(self, limited=False):
        super().__init__()
        self.items = []
        self.limited = limited

        self.control = None

        self.columns = []
        for index, column in enumerate(self.AllColumns):
            if not limited or index not in self.HideWhenLimited:
                self.columns.append(column)


# ----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def from_excel(worksheet):
        """A constructor, of a sort, that will return a new Hops list containing the data parsed from the
        provided openpyxl Worksheet object."""
        hops = Hops(limited=True)
        for idx, row in enumerate(worksheet):
            # Skip the header row.
            if idx == 0:
                continue

            hop = Hop(
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
            )
            hops.append(hop)
        return hops


# ======================================================================================================================
# List Functions
# ----------------------------------------------------------------------------------------------------------------------
    def append(self, item: Hop):
        """Add a new Hop item to the model."""
        parent = QtCore.QModelIndex()
        row = len(self.items)
        self.beginInsertRows(parent, row, row)
        self.items.append(item)
        self.endInsertRows()
        if not self.limited:
            self.sort()
        self.changed.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def extend(self, items: List[Hop]):
        """Merge a list of Hop items into this model."""
        parent = QtCore.QModelIndex()
        start = len(self.items)
        end = start + len(items) - 1
        self.beginInsertRows(parent, start, end)
        self.items.extend(items)
        self.endInsertRows()
        if not self.limited:
            self.sort()
        self.changed.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def pop(self, index: int=None):
        """Remove and return a Hop item from the model at the provided index."""
        if index is None:
            index = len(self.items) - 1
        parent = QtCore.QModelIndex()
        self.beginRemoveRows(parent, index, index)
        item = self.items.pop(index)
        self.endRemoveRows()
        self.changed.emit()
        return item


# ----------------------------------------------------------------------------------------------------------------------
    def __getitem__(self, key: int):
        """A convenience function to allow array like access of items in this model."""
        return self.items[key]


# ----------------------------------------------------------------------------------------------------------------------
    def __setitem__(self, key: int, value: Hop):
        """A convenience function to allow modification of array like access of items in this model."""
        self.items[key] = value
        self.changed.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def __len__(self):
        return len(self.items)



# ======================================================================================================================
# QAbstractTableModel Functions
# ----------------------------------------------------------------------------------------------------------------------
    def rowCount(self, index):
        """Return the total number of rows in the table."""
        return len(self.items)


# ----------------------------------------------------------------------------------------------------------------------
    def columnCount(self, index):
        """Return the total number of columns in the table."""
        return len(self.columns)


# ----------------------------------------------------------------------------------------------------------------------
    def headerData(self, index, orientation, role):
        """Return the column heading text when the display role has been requested."""
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.columns[index].heading


# ----------------------------------------------------------------------------------------------------------------------
    def flags(self, index):
        """Provide the flags for what a given cell is capable of doing.  Only certain columns are editable."""
        flags = QtCore.Qt.ItemIsEnabled
        flags |= QtCore.Qt.ItemIsSelectable
        if index.column() in [0, 1, 2] and not self.limited:
            flags |= QtCore.Qt.ItemIsEditable
        return flags


# ----------------------------------------------------------------------------------------------------------------------
    def data(self, index, role):
        """Fetch data for a cell, either for display of for editing."""
        # Display role is read-only textual display for data in the table.
        if role == QtCore.Qt.DisplayRole:
            hop = self[index.row()]
            column = index.column()

            if self.limited:
                column += len(self.HideWhenLimited)

            if column == 0:
                return str(hop.amount)
            elif column == 1:
                return hop.timing.use
            elif column == 2:
                return str(hop.timing.duration)
            elif column == 3:
                return f'{hop._ibus:.1f} IBU' if hop._ibus else '--'
            elif column == 4:
                return hop.name
            elif column == 5:
                return hop.htype
            elif column == 6:
                return hop.form
            elif column == 7:
                return hop.origin
            elif column == 8:
                return f"{hop.alpha.as_('%'):.1f}%"

        # Edit role is when the user double clicks a cell to trigger editing, return the non-formatted value.
        elif role == QtCore.Qt.EditRole:
            hop = self[index.row()]

            if self.control is not None:
                self.control.horizontalHeader().setSectionResizeMode(index.column(), QtWidgets.QHeaderView.Stretch)

            if index.column() == 0:
                return (hop.amount.value, hop.amount.unit)

            elif index.column() == 1:
                return hop.timing.use

            elif index.column() == 2:
                return (hop.timing.duration.value, hop.timing.duration.unit)

        # Text alignment role is for setting the right/center/left text alignment within a given cell.
        elif role == QtCore.Qt.TextAlignmentRole:
            return self.columns[index.column()].align

        elif role == QtCore.Qt.UserRole:
            return self[index.row()]


# ----------------------------------------------------------------------------------------------------------------------
    def setData(self, index, value, role):
        """Store changed data once editing has completed."""
        if not self.limited and role == QtCore.Qt.EditRole:
            hop = self[index.row()]

            if index.column() == 0:
                hop.amount.value = value[0]
                hop.amount.unit = value[1]

            elif index.column() == 1:
                hop.timing.use = value

            elif index.column() == 2:
                hop.timing.duration.value = value[0]
                hop.timing.duration.unit = value[1]

            if self.control is not None:
                self.control.horizontalHeader().setSectionResizeMode(index.column(), self.columns[index.column()].size)

            self.sort()
            self.changed.emit()
            return True

        return False



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
    def setWidths(self, control: QtWidgets.QTableView):
        """Called from the main window and passed the table widget, step through each column and setup the column widths
        per the Column configuration above."""
        self.control = control
        for index, column in enumerate(self.columns):
            control.horizontalHeader().setSectionResizeMode(index, column.size)


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
