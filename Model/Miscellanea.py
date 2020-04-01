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
from PySide2 import QtCore, QtWidgets
from typing import List

from GUI.Helpers.Column import Column
from GUI.Helpers.Sizing import Stretch
from Model.Miscellaneous import Miscellaneous
from Model import Selections
from Model.MeasurableUnits import MassType, TimeType, UnitType, VolumeType



# ======================================================================================================================
# Miscellanea Class
# ----------------------------------------------------------------------------------------------------------------------
class Miscellanea(QtCore.QAbstractTableModel):
    """Provides for a list of misc objects, specifically created to aid in parsing Excel database files and
    display within a QtTableView."""

    changed = QtCore.Signal()

    Columns = [
        Column('name', size=Stretch, align=QtCore.Qt.AlignLeft),
        Column('mtype', 'Type', align=QtCore.Qt.AlignCenter),
        Column('useFor', 'Use For', align=QtCore.Qt.AlignRight),
        Column('amount', align=QtCore.Qt.AlignRight),
        Column('timing.use', 'Use', align=QtCore.Qt.AlignRight),
        Column('timing.duration', 'Duration', align=QtCore.Qt.AlignRight),
    ]


# ----------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__()
        self.items = []
        self.control = None



# ======================================================================================================================
# List Functions
# ----------------------------------------------------------------------------------------------------------------------
    def append(self, item: Miscellaneous):
        """Add a new misc item to the model."""
        parent = QtCore.QModelIndex()
        row = len(self.items)
        self.beginInsertRows(parent, row, row)
        self.items.append(item)
        self.endInsertRows()
        self.sort()
        self.changed.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def extend(self, items: List[Miscellaneous]):
        """Merge a list of misc items into this model."""
        parent = QtCore.QModelIndex()
        start = len(self.items)
        end = start + len(items) - 1
        self.beginInsertRows(parent, start, end)
        self.items.extend(items)
        self.endInsertRows()
        self.sort()
        self.changed.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def pop(self, index: int=None):
        """Remove and return a misc item from the model at the provided index."""
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
    def __setitem__(self, key: int, value: Miscellaneous):
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
        return len(self.Columns)


# ----------------------------------------------------------------------------------------------------------------------
    def headerData(self, index, orientation, role):
        """Return the column heading text when the display role has been requested."""
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.Columns[index].heading


# ----------------------------------------------------------------------------------------------------------------------
    def flags(self, index):
        """Provide the flags for what a given cell is capable of doing.  Only certain columns are editable."""
        flags = QtCore.Qt.ItemIsEnabled
        flags |= QtCore.Qt.ItemIsSelectable
        flags |= QtCore.Qt.ItemIsEditable
        return flags


# ----------------------------------------------------------------------------------------------------------------------
    def data(self, index, role):
        """Fetch data for a cell, either for display of for editing."""
        # Display role is read-only textual display for data in the table.
        if role == QtCore.Qt.DisplayRole:
            misc = self[index.row()]
            column = self.Columns[index.column()]
            return column.format(misc)

        # Edit role is when the user double clicks a cell to trigger editing, return the non-formatted value.
        elif role == QtCore.Qt.EditRole:
            misc = self[index.row()]

            if self.control is not None:
                self.control.horizontalHeader().setSectionResizeMode(index.column(), QtWidgets.QHeaderView.Stretch)

            if index.column() == 0:
                return misc.name
            elif index.column() == 1:
                return misc.mtype
            elif index.column() == 2:
                return misc.useFor
            elif index.column() == 3:
                return (misc.amount.value, misc.amount.unit)
            elif index.column() == 4:
                return misc.timing.use
            elif index.column() == 5:
                return (misc.timing.duration.value, misc.timing.duration.unit)

        # Text alignment role is for setting the right/center/left text alignment within a given cell.
        elif role == QtCore.Qt.TextAlignmentRole:
            return self.Columns[index.column()].align

        elif role == QtCore.Qt.UserRole:
            return self[index.row()]


# ----------------------------------------------------------------------------------------------------------------------
    def setData(self, index, value, role):
        """Store changed data once editing has completed."""
        if role == QtCore.Qt.EditRole:
            misc = self[index.row()]

            if index.column() == 0:
                misc.name = value
            elif index.column() == 1:
                misc.mtype = value
            elif index.column() == 2:
                misc.useFor = value
            elif index.column() == 3:
                misc.amount = Selections.one_of(value[0], value[1], MassType, VolumeType, UnitType)
            elif index.column() == 4:
                misc.timing.use = value
            elif index.column() == 5:
                if misc.timing.duration is None:
                    misc.timing.duration = TimeType()
                misc.timing.duration.value = value[0]
                misc.timing.duration.unit = value[1]

            if self.control is not None:
                self.control.horizontalHeader().setSectionResizeMode(index.column(), self.Columns[index.column()].size)

            self.sort()

            self.changed.emit()
            return True

        return False



# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------



# ======================================================================================================================
# Other Methods
# ----------------------------------------------------------------------------------------------------------------------
    def setWidths(self, control: QtWidgets.QTableView):
        """Called from the main window and passed the table widget, step through each column and setup the column widths
        per the Column configuration above."""
        self.control = control
        for index, column in enumerate(self.Columns):
            control.horizontalHeader().setSectionResizeMode(index, column.size)


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
