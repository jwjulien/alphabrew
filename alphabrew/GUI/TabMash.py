# ======================================================================================================================
#        File:  GUI/TabMash.py
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
from PySide2 import QtWidgets
import qtawesome

from GUI.Base.TabMash import Ui_TabMash
from GUI.Delegates.ComboBoxDelegate import ComboBoxDelegate
from GUI.Delegates.SimpleTypeDelegate import SimpleTypeDelegate
from Model.MashStep import MashStep
from Model.MeasurableUnits import TemperatureType, TimeType



# ======================================================================================================================
# Mash Tab Class
# ----------------------------------------------------------------------------------------------------------------------
class TabMash(QtWidgets.QWidget):
    def __init__(self, parent, recipe):
        super().__init__(parent)
        self.ui = Ui_TabMash()
        self.ui.setupUi(self)

        self.recipe = recipe
        self.recipe.loaded.connect(self.on_load)
        self.on_load()

        self.recipe.mash.set_control(self.ui.steps)

        # Add a delegate for editing the types.
        options = ['Infusion', 'Temperature', 'Decoction', 'Souring Mash', 'Souring Wort', 'Drain Mash Tun', 'Sparge']
        delegate = ComboBoxDelegate(self, options)
        self.ui.steps.setItemDelegateForColumn(1, delegate)

        # Add a delegate for editing the step temperature.
        delegate = SimpleTypeDelegate(self, [TemperatureType], maximum=212, decimals=1)
        self.ui.steps.setItemDelegateForColumn(2, delegate)

        # Add a delegate for editing the step time.
        delegate = SimpleTypeDelegate(self, [TimeType], decimals=1)
        self.ui.steps.setItemDelegateForColumn(3, delegate)

        # Setup add button with icon and connect an event handler.
        icon = qtawesome.icon('fa5s.plus')
        self.ui.add.setIcon(icon)
        self.ui.add.clicked.connect(self.on_add)

        # Setup remove button with icon and connect an event handler.
        icon = qtawesome.icon('fa5s.trash-alt')
        self.ui.remove.setIcon(icon)
        self.ui.remove.clicked.connect(self.on_remove)

        # Connect event handler for discrete inputs.
        self.ui.ambient.valueChanged.connect(self.on_ambient_changed)
        self.ui.ratio.valueChanged.connect(self.on_ratio_changed)


# ----------------------------------------------------------------------------------------------------------------------
    def on_load(self):
        """Fires when the recipe loads to update the discrete controls with values."""
        self.ui.steps.setModel(self.recipe.mash)
        self.ui.steps.selectionModel().selectionChanged.connect(self.on_selection_change)
        self.ui.ambient.setValue(self.recipe.mash.ambient.F)
        self.ui.ratio.setValue(self.recipe.mash.ratio.quartsPerPound)


# ----------------------------------------------------------------------------------------------------------------------
    def on_ambient_changed(self, value):
        """Fires when the user changes the ambient temperature."""
        self.recipe.mash.ambient.value = value
        self.recipe.mash.ambient.unit = 'F'
        self.recipe.mash.changed.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def on_ratio_changed(self, value):
        """Fires when the user changes the value of the water/grain ratio spin box."""
        self.recipe.mash.ratio.value = value
        self.recipe.mash.ratio.unit = 'qt/lb'
        self.recipe.mash.changed.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def on_selection_change(self):
        """Fires when the user makes a selection in the table."""
        selection = self.ui.steps.selectionModel().selectedIndexes()
        selected = len(selection) > 0
        self.ui.remove.setEnabled(selected)


# ----------------------------------------------------------------------------------------------------------------------
    def on_add(self):
        """Fires when the user clicks the add button."""
        step = MashStep(self.recipe)

        count = len(self.recipe.mash)
        step.name = f'Rest {count + 1}'
        step.mtype = 'Infusion'
        step.time = TimeType(0, 'min')

        self.recipe.mash.append(step)


# ----------------------------------------------------------------------------------------------------------------------
    def on_remove(self):
        """Fires when the user clicks the remove button."""
        for index in self.ui.steps.selectedIndexes():
            if index.column() != 0:
                continue
            self.recipe.mash.pop(index.row())
            break



# End of File
