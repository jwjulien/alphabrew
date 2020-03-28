# ======================================================================================================================
#        File:  GUI/Helpers/ComboBoxDelegate.py
#     Project:  Brewing Recipe Planner
# Description:  Provides a QComboBox for use with editing directly in QTableViews.
#      Author:  Jared Julien <jaredjulien@exsystems.net>
#   Copyright:  (c) 2020 Jared Julien, eX Systems
# ---------------------------------------------------------------------------------------------------------------------
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



# ======================================================================================================================
# Combo Box Delegate Class
# ----------------------------------------------------------------------------------------------------------------------
class ComboBoxDelegate(QtWidgets.QItemDelegate):
    """Provides an implementation of the QItemDelegate class to provide a QComboBox delegate for editing cells
    within QTableView tables using a dropdown."""

    def __init__(self, parent, choices):
        super().__init__(parent)
        self.choices = choices


# ----------------------------------------------------------------------------------------------------------------------
    def createEditor(self, parent, option, index):
        """Overridden method to generate the editor combo box and return it."""
        editor = QtWidgets.QComboBox(parent)
        for choice in self.choices:
            editor.addItem(choice)
        return editor


# ----------------------------------------------------------------------------------------------------------------------
    def setEditorData(self, editor: QtWidgets.QComboBox, index):
        """Called to set the current value in the editor."""
        value = index.model().data(index, QtCore.Qt.EditRole)
        editor.setCurrentText(value)


# ----------------------------------------------------------------------------------------------------------------------
    def setModelData(self, editor: QtWidgets.QComboBox, model, index):
        """Called to get the final value from the editor."""
        value = editor.currentText()
        model.setData(index, value, QtCore.Qt.EditRole)


# ----------------------------------------------------------------------------------------------------------------------
    def updateEditorGeometry(self, editor, option, index):
        """Called when the geometry of the cell changes to update the geometry of the combo box."""
        editor.setGeometry(option.rect)



# End of File
