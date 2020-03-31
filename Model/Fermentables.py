# ======================================================================================================================
#        File:  Model/Fermentables.py
#     Project:  Brewing Recipe Planner
# Description:  A definition for a beer Fermentables in list form.
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
from Model.Fermentable import Fermentable
from Model.MeasurableUnits import ColorType, DiastaticPowerType, PercentType



# ======================================================================================================================
# Fermentables Class
# ----------------------------------------------------------------------------------------------------------------------
class Fermentables(QtCore.QAbstractTableModel):
    """Provides for a list of Fermentable objects, specifically created to aid in parsing Excel database files and
    display within a QtTableView."""

    changed = QtCore.Signal()

    AllColumns = [
        Column('Amount', align=QtCore.Qt.AlignRight),
        Column('Percent', align=QtCore.Qt.AlignHCenter),
        Column('Grain/Fermentable', size=Stretch, align=QtCore.Qt.AlignLeft),
        Column('Type', align=QtCore.Qt.AlignRight),
        Column('Group', align=QtCore.Qt.AlignRight),
        Column('Yield', align=QtCore.Qt.AlignRight),
        Column('Color', align=QtCore.Qt.AlignRight),
    ]

    # These column indexes should be hidden when the class is instantiated with the limited flag set.
    # Intended to hide columns specific to inclusion in a recipe, such as amount, proportion, time, etc.
    HideWhenLimited = [0, 1]


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
        """A constructor, of a sort, that will return a new Fermentables list containing the data parsed from the
        provided openpyxl Worksheet object."""
        fermentables = Fermentables(limited=True)
        for idx, row in enumerate(worksheet):
            # Skip the header row.
            if idx == 0:
                continue

            fermentable = Fermentable(
                name=str(row[0].value),
                ftype=str(row[1].value),
                group=str(row[2].value),
                producer=str(row[3].value),
                origin=str(row[4].value),
                fyield=PercentType(row[5].value, '%'),
                color=ColorType(row[6].value, 'SRM'),
                moisture=PercentType(row[7].value, '%'),
                diastaticPower=DiastaticPowerType(row[8].value, 'Lintner'),
                protein=PercentType(row[9].value, '%'),
                maxPerBatch=PercentType(row[10].value, '%'),
                coarseFineDiff=PercentType(row[11].value, '%'),
                addAfterBoil=bool(row[12].value),
                mashed=bool(row[13].value),
                notes=str(row[14].value)
            )
            fermentables.append(fermentable)
        return fermentables


# ======================================================================================================================
# List Functions
# ----------------------------------------------------------------------------------------------------------------------
    def append(self, item: Fermentable):
        """Add a new Fermentable item to the model."""
        parent = QtCore.QModelIndex()
        row = len(self.items)
        self.beginInsertRows(parent, row, row)
        self.items.append(item)
        self.endInsertRows()
        if not self.limited:
            self.sort()
        self.changed.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def extend(self, items: List[Fermentable]):
        """Merge a list of Fermentable items into this model."""
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
        """Remove and return a Fermentable item from the model at the provided index."""
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
    def __setitem__(self, key: int, value: Fermentable):
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
            fermentable = self[index.row()]
            column = index.column()

            if self.limited:
                column += len(self.HideWhenLimited)

            if column == 0:
                return str(fermentable.amount)
            elif column == 1:
                return f'{fermentable.proportion:.0f}%'
            elif column == 2:
                return fermentable.name
            elif column == 3:
                return fermentable.ftype
            elif column == 4:
                return fermentable.group if fermentable.group is not None else ''
            elif column == 5:
                return f"{fermentable.fyield.as_('%'):.1f}%"
            elif column == 6:
                return f"{fermentable.color.as_('SRM'):.1f} srm"

        # Edit role is when the user double clicks a cell to trigger editing, return the non-formatted value.
        elif role == QtCore.Qt.EditRole:
            fermentable = self[index.row()]

            if self.control is not None:
                self.control.horizontalHeader().setSectionResizeMode(index.column(), QtWidgets.QHeaderView.Stretch)

            if index.column() == 0:
                return (fermentable.amount.value, fermentable.amount.unit)

        # Text alignment role is for setting the right/center/left text alignment within a given cell.
        elif role == QtCore.Qt.TextAlignmentRole:
            return self.columns[index.column()].align

        elif role == QtCore.Qt.UserRole:
            return self[index.row()]


# ----------------------------------------------------------------------------------------------------------------------
    def setData(self, index, value, role):
        """Store changed data once editing has completed."""
        if not self.limited and role == QtCore.Qt.EditRole:
            fermentable = self[index.row()]

            if index.column() == 0:
                fermentable.amount.value = value[0]
                fermentable.amount.unit = value[1]

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
    def mashedSugar(self):
        """Return the sucrose equivalent of all of the mashed ingredients."""
        return sum([item.sucrose for item in self.items if item.isMashed and not item.addAfterBoil])


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def nonMashedSugar(self):
        """Returns the total sucrose equivalent of all the non-mashed ingredients."""
        return sum([item.sucrose for item in self.items if not item.isMashed])


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def fermentableSugar(self):
        """Returns to equivalent amount of sucrose, in pounds, that is fermentable.  Excludes ingredients like lactose
        and Splenda."""
        return sum([item.sucrose for item in self.items if item.isFermentable])


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def nonFermentableSugar(self):
        """Returns to equivalent amount of sucrose, in pounds, that is NOT fermentable.  This includes ingredients like
        lactose or Splenda."""
        return sum([item.sucrose for item in self.items if not item.isFermentable])


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def steepedSugar(self):
        """Returns the equivalent amount of sucrose that is steeped post boil, but where it is still "mashed" so
        Brewhouse efficiency still plays a factor."""
        return sum([item.sucrose for item in self.items if item.isMashed and item.addAfterBoil])


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def lateAdditionSugar(self):
        """Returns the equivalent amount of sucrose that is added post boil, but where the efficiency isn't a factor."""
        return sum([item.sucrose for item in self.items if not item.isMashed and item.addAfterBoil])



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
        """A void sort function that consistently sorts the fermentable in decreasing order of amount in the recipe."""
        self.items.sort(key=lambda fermentable: (-fermentable.amount.as_('lb'), fermentable.name))


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert self into a dictionary for BeerJSON storage."""
        return [fermentable.to_dict() for fermentable in self]


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, recipe, data):
        """Parse list of fermentables from the provided BeerJSON dict."""
        for item in data:
            fermentable = Fermentable(recipe)
            fermentable.from_dict(item)
            self.append(fermentable)

# End of File
