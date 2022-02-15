# ======================================================================================================================
#        File:  Model/ListTableBase.py
#     Project:  AlphaBrew
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
from typing import List
from PySide2 import QtCore, QtWidgets
from alphabrew.GUI.Table.Column import Column



# ======================================================================================================================
# List/Table Base Class
# ----------------------------------------------------------------------------------------------------------------------
class ListTableBase(QtCore.QAbstractTableModel):
    """This is a parent class for any list of objects to be displayed in a Qt QTableView.  It provides functions for
    working with the data like it were a list as well as supporting the function set for a QAbstractTableModel that can
    be associated with a QTableView for display."""

    changed = QtCore.Signal()

    # This property must be populated by child class definitions to provide a set of Column object instances that
    # correspond to the columns in the table and tell this class how to display the data.
    Columns: List[Column] = []


# ----------------------------------------------------------------------------------------------------------------------
    def __init__(self, limited=False):
        super().__init__()
        self.limited = limited

        self.control = None
        self.columns = []
        self.clear()

        # Walk through the list of all columns and produce a list of columns that apply based upon the state of the
        # limited flag.
        for column in self.Columns:
            if not limited or not column.hideLimited:
                self.columns.append(column)


# ----------------------------------------------------------------------------------------------------------------------
    def clear(self):
        """Clear the saved contents of this list of fermentable ingredients.

        Clears data while retaining properties such at the associated controls.
        """
        self.items = []


# ======================================================================================================================
# List Functions
# ----------------------------------------------------------------------------------------------------------------------
    def append(self, item):
        """Add a new item to the model."""
        parent = QtCore.QModelIndex()
        row = len(self.items)
        self.beginInsertRows(parent, row, row)
        self.items.append(item)
        self.endInsertRows()
        if not self.limited:
            self.sort()
        self.changed.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def extend(self, items):
        """Merge a list of items into this model."""
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
        """Remove and return an item from the model at the provided index."""
        if index is None:
            index = len(self.items) - 1
        parent = QtCore.QModelIndex()
        self.beginRemoveRows(parent, index, index)
        item = self.items.pop(index)
        self.endRemoveRows()
        self.changed.emit()
        return item


# ----------------------------------------------------------------------------------------------------------------------
    def indexOf(self, item):
        """Scans the list and returns the index of the provided item or None if the item is not in the list."""
        for idx, test in enumerate(self.items):
            if test == item:
                return idx
        return None



# ----------------------------------------------------------------------------------------------------------------------
    def __getitem__(self, key: int):
        """A convenience function to allow array like access of items in this model."""
        return self.items[key]


# ----------------------------------------------------------------------------------------------------------------------
    def __setitem__(self, key: int, value):
        """A convenience function to allow modification of array like access of items in this model."""
        self.items[key] = value
        self.changed.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def __len__(self):
        return len(self.items)



# ======================================================================================================================
# QAbstractTableModel Functions
# ----------------------------------------------------------------------------------------------------------------------
    def set_control(self, control: QtWidgets.QTableView):
        """Called by the GUI to associate a TableView control with this instance.  Sets up column widths and stores a
        reference for adjusting the widths later."""
        self.control = control

        header = self.control.horizontalHeader()
        header.setStretchLastSection(True)
        for index in range(len(self.columns)):
            header.setSectionResizeMode(index, QtWidgets.QHeaderView.Interactive)
        self.resize()


# ----------------------------------------------------------------------------------------------------------------------
    def resize(self):
        """Automatically resize the columns to remain interactive but best match the current contents."""
        self.control.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)


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
        column = self.columns[index.column()]
        flags = QtCore.Qt.ItemIsEnabled
        flags |= QtCore.Qt.ItemIsSelectable
        if column.editable:
            flags |= QtCore.Qt.ItemIsEditable
        return flags


# ----------------------------------------------------------------------------------------------------------------------
    def data(self, index, role):
        """Fetch data for a cell, either for display of for editing."""
        item = self[index.row()]
        column: Column = self.columns[index.column()]

        # Display role is read-only textual display for data in the table.
        if role == QtCore.Qt.DisplayRole:
            return column.format(item)

        # Edit role is when the user double clicks a cell to trigger editing, return the non-formatted value.
        elif role == QtCore.Qt.EditRole and column.editable:
            if self.control is not None:
                self.control.horizontalHeader().setSectionResizeMode(index.column(), QtWidgets.QHeaderView.Stretch)

            return column.get_value(item)

        # Text alignment role is for setting the right/center/left text alignment within a given cell.
        elif role == QtCore.Qt.TextAlignmentRole:
            return self.columns[index.column()].align

        elif role == QtCore.Qt.UserRole:
            return self[index.row()]


# ----------------------------------------------------------------------------------------------------------------------
    def setData(self, index, value, role):
        """Store changed data once editing has completed."""
        item = self[index.row()]
        column = self.columns[index.column()]

        if role == QtCore.Qt.EditRole:
            # Resize the column back to the configured width.
            if self.control is not None:
                self.control.horizontalHeader().setSectionResizeMode(index.column(), QtWidgets.QHeaderView.Interactive)

            column.set_value(item, value)
            self.sort()
            self.changed.emit()

            # Always report back to Qt that the data was handled in this path.
            return True

        # We couldn't do anything with the data.
        return False



# ======================================================================================================================
# Other Methods
# ----------------------------------------------------------------------------------------------------------------------
    def from_excel(self, worksheet):
        """Overridden by child class to parse out data and populate this list from an Excel workbook."""
        raise NotImplementedError(f'{self.__class__.__name__} has not implemented a from_excel method')


# ----------------------------------------------------------------------------------------------------------------------
    def sort(self):
        """Must be overridden by child classes to implement sorting of the items in this list."""
        raise NotImplementedError(f'{self.__class__.__name__} has not implamented a sort method')


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert self into a dictionary for BeerJSON storage.  Specific to each class, must be overridden."""
        raise NotImplementedError(f'{self.__class__.__name__} has not implamented a to_dict method')


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, recipe, data):
        """Parse list of items from the provided BeerJSON dict into this list.  Specific to each child, must be
        overridden."""
        raise NotImplementedError(f'{self.__class__.__name__} has not implamented a from_dict method')



# End of File
