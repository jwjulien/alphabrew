# ======================================================================================================================
#        File:  GUI/TabFermentation.py
#     Project:  Brewing Recipe Planner
# Description:  Extensions and functionality for the main GUI window.
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
# Import Statements
# ----------------------------------------------------------------------------------------------------------------------
from PySide2 import QtCore, QtGui, QtWidgets
import qtawesome

from GUI.Base.TabFermentation import Ui_TabFermentation

from Model.FermentationStep import FermentationStep



# ======================================================================================================================
# Fermentation Tab Class
# ----------------------------------------------------------------------------------------------------------------------
class TabFermentation(QtWidgets.QWidget):
    def __init__(self, parent, recipe):
        super().__init__(parent)
        self.ui = Ui_TabFermentation()
        self.ui.setupUi(self)

        self.recipe = recipe

        self.ui.steps.setModel(self.recipe.fermentation)
        self.recipe.fermentation.set_control(self.ui.steps)
        self.ui.steps.selectionModel().selectionChanged.connect(self.on_selection_change)

        # Setup add button with icon and connect an event handler.
        icon = qtawesome.icon('fa5s.plus')
        self.ui.add.setIcon(icon)
        self.ui.add.clicked.connect(self.on_add)

        # Setup remove button with icon and connect an event handler.
        icon = qtawesome.icon('fa5s.trash-alt')
        self.ui.remove.setIcon(icon)
        self.ui.remove.clicked.connect(self.on_remove)


# ----------------------------------------------------------------------------------------------------------------------
    def on_selection_change(self):
        """Fires when the user makes a selection in the table."""
        selection = self.ui.steps.selectionModel().selectedIndexes()
        selected = len(selection) > 0
        self.ui.remove.setEnabled(selected)


# ----------------------------------------------------------------------------------------------------------------------
    def on_add(self):
        """Fires when the user clicks the add button."""
        step = FermentationStep(self.recipe)
        # step.amount = MassType(0, 'lb')
        # step.timing = TimingType(duration=TimeType('0', 'min'))
        self.recipe.fermentation.append(step)


# ----------------------------------------------------------------------------------------------------------------------
    def on_remove(self):
        """Fires when the user clicks the remove button."""
        for index in self.ui.steps.selectedIndexes():
            if index.column() != 0:
                continue
            self.recipe.fermentation.pop(index.row())
            break



# End of File
