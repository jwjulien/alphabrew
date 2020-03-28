# ======================================================================================================================
#        File:  GUI/Helpers/SpinBoxDelegate.py
#     Project:  Brewing Recipe Planner
# Description:  Provides a QDoubleSpinBox
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
# Double Spin Box Delegate Class
# ----------------------------------------------------------------------------------------------------------------------
class DoubleSpinBoxDelegate(QtWidgets.QItemDelegate):
    """Provides an implementation of the QItemDelegate class to provide a QDoubleSpinBox delegate for editing cells
    within QTableView tables inside of a range limited spin box."""

    def __init__(self, parent=None, minimum=0, maximum=99, suffix='', decimals=3, singleStep=1):
        super().__init__(parent)
        self.minimum = minimum
        self.maximum = maximum
        self.suffix = suffix
        self.decimals = decimals
        self.singleStep = singleStep


# ----------------------------------------------------------------------------------------------------------------------
    def createEditor(self, parent, option, index):
        """Overridden method to generate the editor spin box and return it."""
        editor = QtWidgets.QDoubleSpinBox(parent)
        editor.setMinimum(self.minimum)
        editor.setMaximum(self.maximum)
        editor.setSuffix(self.suffix)
        editor.setDecimals(self.decimals)
        editor.setSingleStep(self.singleStep)
        return editor


# ----------------------------------------------------------------------------------------------------------------------
    def setEditorData(self, editor, index):
        """Called to set the current value in the editor."""
        value = index.model().data(index, QtCore.Qt.EditRole)
        editor.setValue(value)


# ----------------------------------------------------------------------------------------------------------------------
    def setModelData(self, editor, model, index):
        """Called to get the final value from the editor."""
        editor.interpretText()
        value = editor.value()
        model.setData(index, value, QtCore.Qt.EditRole)


# ----------------------------------------------------------------------------------------------------------------------
    def updateEditorGeometry(self, editor, option, index):
        """Called when the geometry of the cell changes to update the geometry of the spin box."""
        editor.setGeometry(option.rect)



# End of File
