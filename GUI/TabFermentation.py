# ======================================================================================================================
#        File:  GUI/TabFermentation.py
#     Project:  AlphaBrew
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
from GUI.Delegates.SimpleTypeDelegate import SimpleTypeDelegate
from Model.FermentationStep import FermentationStep
from Model.MeasurableUnits import TemperatureType, TimeType



# ======================================================================================================================
# Fermentation Tab Class
# ----------------------------------------------------------------------------------------------------------------------
class TabFermentation(QtWidgets.QWidget):
    def __init__(self, parent, recipe):
        super().__init__(parent)
        self.ui = Ui_TabFermentation()
        self.ui.setupUi(self)

        self.recipe = recipe

        self.recipe.loaded.connect(self.on_load)
        self.on_load()

        self.ui.steps.setModel(self.recipe.fermentation)
        self.recipe.fermentation.set_control(self.ui.steps)
        self.ui.steps.selectionModel().selectionChanged.connect(self.on_selection_change)

        # Setup a delegate for editing of start and end temperatures.
        temperatureDelegate = SimpleTypeDelegate(self, [TemperatureType], maximum=212, decimals=0, singleStep=5)
        self.ui.steps.setItemDelegateForColumn(1, temperatureDelegate)
        self.ui.steps.setItemDelegateForColumn(2, temperatureDelegate)

        # Setup another delegate for editing the step time.
        timeDelegate = SimpleTypeDelegate(self, [TimeType], decimals=0)
        self.ui.steps.setItemDelegateForColumn(3, timeDelegate)

        # Setup add button with icon and connect an event handler.
        icon = qtawesome.icon('fa5s.plus')
        self.ui.add.setIcon(icon)
        self.ui.add.clicked.connect(self.on_add)

        # Setup remove button with icon and connect an event handler.
        icon = qtawesome.icon('fa5s.trash-alt')
        self.ui.remove.setIcon(icon)
        self.ui.remove.clicked.connect(self.on_remove)


# ----------------------------------------------------------------------------------------------------------------------
    def on_load(self):
        """Fires when the recipe gets loaded to re-associate the recipe model with the Qt table in this tab."""
        self.ui.steps.setModel(self.recipe.fermentation)


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

        # Attempt to set a reasonable default name based upon how many fermentation steps currently exist.
        if len(self.recipe.fermentation) == 0:
            step.name = 'Primary'
        elif len(self.recipe.fermentation) == 1:
            step.name = 'Secondary'
        elif len(self.recipe.fermentation) == 2:
            step.name = 'Tertiary'

        step.startTemperature = TemperatureType(65, 'F')
        step.endTemperature = TemperatureType(65, 'F')

        step.time = TimeType(5, 'day')

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
