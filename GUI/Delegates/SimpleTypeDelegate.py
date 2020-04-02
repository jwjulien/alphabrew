# ======================================================================================================================
#        File:  GUI/Delegates/SimpleTypeDelegate.py
#     Project:  Brewing Recipe Planner
# Description:  A Delegate implementation specifically for working with Model MeasurableUnit types extending a
#               SimpleTypebase.
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

from GUI.Delegates.ComboSpinBoxDelegate import ComboSpinBoxDelegate
from Model import Selections



# ======================================================================================================================
# Simple Type Delegate Class
# ----------------------------------------------------------------------------------------------------------------------
class SimpleTypeDelegate(ComboSpinBoxDelegate):
    """Extends the double spin and combo bod delegate specifically for working with SimpleType model extensions
    containing `value` and `unit` fields and dealing with the possibility of many different extended types."""

    def __init__(self, parent, types, minimum=0, maximum=99, suffix='', decimals=3, singleStep=1):
        self.types = types
        units = Selections.all_units(*self.types)
        super().__init__(parent, units, minimum, maximum, suffix, decimals, singleStep)


# ----------------------------------------------------------------------------------------------------------------------
    def setEditorData(self, widget: QtWidgets.QWidget, index):
        """Called to set the current value in the editor."""
        simpleType = index.model().data(index, QtCore.Qt.EditRole)
        if simpleType is not None:
            self.spinBox.setValue(simpleType.value)
            self.comboBox.setCurrentText(simpleType.unit)


# ----------------------------------------------------------------------------------------------------------------------
    def setModelData(self, widget: QtWidgets.QWidget, model, index):
        """Called to get the final value from the editor."""
        self.spinBox.interpretText()
        spinValue = self.spinBox.value()
        comboText = self.comboBox.currentText()
        simpleType = Selections.one_of(spinValue, comboText, *self.types)
        model.setData(index, simpleType, QtCore.Qt.EditRole)



# End of File
