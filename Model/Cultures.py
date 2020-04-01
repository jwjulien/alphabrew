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

from GUI.Helpers.Column import Column
from GUI.Helpers.Sizing import Stretch
from Model.Culture import Culture
from Model.MeasurableUnits import PercentType, PercentRangeType



# ======================================================================================================================
# Cultures Class
# ----------------------------------------------------------------------------------------------------------------------
class Cultures(QtCore.QAbstractTableModel):
    """Provides for a list of Culture objects, specifically created to aid in parsing Excel database files and
    display within a QtTableView."""

    changed = QtCore.Signal()

    AllColumns = [
        Column('Amount', align=QtCore.Qt.AlignRight),
        Column('Name', size=Stretch, align=QtCore.Qt.AlignLeft),
        Column('Type', align=QtCore.Qt.AlignRight),
        Column('Form', align=QtCore.Qt.AlignRight),
        Column('Producer', align=QtCore.Qt.AlignRight),
        Column('Product', align=QtCore.Qt.AlignRight),
    ]

    # These column indexes should be hidden when the class is instantiated with the limited flag set.
    # Intended to hide columns specific to inclusion in a recipe, such as amount, proportion, time, etc.
    HideWhenLimited = [0]


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
        """A constructor, of a sort, that will return a new Cultures list containing the data parsed from the
        provided openpyxl Worksheet object."""
        cultures = Cultures(limited=True)
        for idx, row in enumerate(worksheet):
            # Skip the header row.
            if idx == 0:
                continue

            culture = Culture(
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
            )
            cultures.append(culture)
        return cultures


# ======================================================================================================================
# List Functions
# ----------------------------------------------------------------------------------------------------------------------
    def append(self, item: Culture):
        """Add a new Culture item to the model."""
        parent = QtCore.QModelIndex()
        row = len(self.items)
        self.beginInsertRows(parent, row, row)
        self.items.append(item)
        self.endInsertRows()
        if not self.limited:
            self.sort()
        self.changed.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def extend(self, items: List[Culture]):
        """Merge a list of Culture items into this model."""
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
        """Remove and return a Culture item from the model at the provided index."""
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
    def __setitem__(self, key: int, value: Culture):
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
        if index.column() == 0 and not self.limited:
            flags |= QtCore.Qt.ItemIsEditable
        return flags


# ----------------------------------------------------------------------------------------------------------------------
    def data(self, index, role):
        """Fetch data for a cell, either for display of for editing."""
        # Display role is read-only textual display for data in the table.
        if role == QtCore.Qt.DisplayRole:
            culture = self[index.row()]
            column = index.column()

            if self.limited:
                column += len(self.HideWhenLimited)

            if column == 0:
                return str(culture.amount)
            elif column == 1:
                return culture.name
            elif column == 2:
                return culture.ctype
            elif column == 3:
                return culture.form
            elif column == 4:
                return culture.producer
            elif column == 5:
                return culture.productId

        # Edit role is when the user double clicks a cell to trigger editing, return the non-formatted value.
        elif role == QtCore.Qt.EditRole:
            culture = self[index.row()]

            if self.control is not None:
                self.control.horizontalHeader().setSectionResizeMode(index.column(), QtWidgets.QHeaderView.Stretch)

            if index.column() == 0:
                return (culture.amount.value, culture.amount.unit)

        # Text alignment role is for setting the right/center/left text alignment within a given cell.
        elif role == QtCore.Qt.TextAlignmentRole:
            return self.columns[index.column()].align

        elif role == QtCore.Qt.UserRole:
            return self[index.row()]


# ----------------------------------------------------------------------------------------------------------------------
    def setData(self, index, value, role):
        """Store changed data once editing has completed."""
        if not self.limited and role == QtCore.Qt.EditRole:
            culture = self[index.row()]

            if index.column() == 0:
                culture.amount.value = value[0]
                culture.amount.unit = value[1]

            if self.control is not None:
                size = self.columns[index.column()].size
                self.control.horizontalHeader().setSectionResizeMode(index.column(), size)

            # Re-sort when the user changes the weightin the recipe.
            self.sort()

            self.changed.emit()
            return True

        return False



# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def averageAttenuation(self):
        """Returns the maximum attenuation of all of the cultures in the collection."""
        return max([culture.averageAttenuation for culture in self.items])



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
