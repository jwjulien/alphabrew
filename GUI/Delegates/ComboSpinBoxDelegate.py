# ======================================================================================================================
#        File:  GUI/Delegates/ComboSpinBoxDelegate.py
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
# Combo Spin Box Delegate Class
# ----------------------------------------------------------------------------------------------------------------------
class ComboSpinBoxDelegate(QtWidgets.QItemDelegate):
    """Provides an implementation of the QItemDelegate class to provide a QComboBox delegate for editing cells
    within QTableView tables using a dropdown."""

    def __init__(self, parent, choices, minimum=0, maximum=99, suffix='', decimals=3, singleStep=1):
        super().__init__(parent)
        self.choices = choices
        self.minimum = minimum
        self.maximum = maximum
        self.suffix = suffix
        self.decimals = decimals
        self.singleStep = singleStep

        self.spinBox = None
        self.comboBox = None


# ----------------------------------------------------------------------------------------------------------------------
    def createEditor(self, parent, option, index):
        """Overridden method to generate the editor combo box and return it."""
        widget = QtWidgets.QWidget(parent)
        container = QtWidgets.QHBoxLayout(widget)
        container.setContentsMargins(0, 0, 0, 0)
        container.setSpacing(0)

        self.spinBox = QtWidgets.QDoubleSpinBox(widget)
        self.spinBox.setMinimum(self.minimum)
        self.spinBox.setMaximum(self.maximum)
        self.spinBox.setSuffix(self.suffix)
        self.spinBox.setDecimals(self.decimals)
        self.spinBox.setSingleStep(self.singleStep)
        container.addWidget(self.spinBox, 1)

        self.comboBox = QtWidgets.QComboBox(widget)
        for choice in self.choices:
            self.comboBox.addItem(choice)
        container.addWidget(self.comboBox)

        return widget


# ----------------------------------------------------------------------------------------------------------------------
    def setEditorData(self, widget: QtWidgets.QWidget, index):
        """Called to set the current value in the editor."""
        spinValue, comboText = index.model().data(index, QtCore.Qt.EditRole)
        self.spinBox.setValue(spinValue)
        self.comboBox.setCurrentText(comboText)


# ----------------------------------------------------------------------------------------------------------------------
    def setModelData(self, widget: QtWidgets.QWidget, model, index):
        """Called to get the final value from the editor."""
        self.spinBox.interpretText()
        spinValue = self.spinBox.value()
        comboText = self.comboBox.currentText()
        model.setData(index, (spinValue, comboText), QtCore.Qt.EditRole)


# ----------------------------------------------------------------------------------------------------------------------
    def updateEditorGeometry(self, widget: QtWidgets.QWidget, option, index):
        """Called when the geometry of the cell changes to update the geometry of the combo box."""
        widget.setGeometry(option.rect)
        self.spinBox.setFixedHeight(option.rect.height())
        self.comboBox.setFixedHeight(option.rect.height())



# End of File
