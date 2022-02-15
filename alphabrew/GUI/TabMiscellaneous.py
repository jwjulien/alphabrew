# ======================================================================================================================
#        File:  GUI/TabMiscellaneous.py
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
from PySide2 import QtCore, QtWidgets
import qtawesome

from GUI.Base.TabMiscellaneous import Ui_TabMiscellaneous
from GUI.Delegates.ComboBoxDelegate import ComboBoxDelegate
from GUI.Delegates.SimpleTypeDelegate import SimpleTypeDelegate
from Model.Miscellaneous import Miscellaneous
from Model.MeasurableUnits import MassType, TimeType, UnitType, VolumeType
from Model.Timing import TimingType



# ======================================================================================================================
# Miscellaneous Tab Class
# ----------------------------------------------------------------------------------------------------------------------
class TabMiscellaneous(QtWidgets.QWidget):
    """Extends the MainWindow Miscellaneous tab widget containing a subset of controls specific to miscellaneous in the
    recipe."""

    def __init__(self, parent, recipe):
        super().__init__(parent)
        self.ui = Ui_TabMiscellaneous()
        self.ui.setupUi(self)

        # Store the recipe with which these misc items are associated.
        self.recipe = recipe
        self.recipe.loaded.connect(self.on_load)
        self.on_load()

        # Setup a delegates to allow editing of fields inside of the table.
        delegate = ComboBoxDelegate(self, ['Spice', 'Fining', 'Water Agent', 'Herb', 'Flavor', 'Wood', 'Other'])
        self.ui.ingredients.setItemDelegateForColumn(1, delegate)

        delegate = SimpleTypeDelegate(self, [MassType, VolumeType, UnitType])
        self.ui.ingredients.setItemDelegateForColumn(3, delegate)

        delegate = ComboBoxDelegate(self, ['Mash', 'Boil', 'Fermentation', 'Package'])
        self.ui.ingredients.setItemDelegateForColumn(4, delegate)

        delegate = SimpleTypeDelegate(self, [TimeType], minimum=0, maximum=240, singleStep=5)
        self.ui.ingredients.setItemDelegateForColumn(5, delegate)

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
        self.ui.ingredients.setModel(self.recipe.misc)
        self.ui.ingredients.selectionModel().selectionChanged.connect(self.on_selection_change)
        self.recipe.misc.set_control(self.ui.ingredients)


# ----------------------------------------------------------------------------------------------------------------------
    def on_selection_change(self):
        """Fires when the user makes a selection in the top table."""
        selection = self.ui.ingredients.selectionModel().selectedIndexes()
        selected = len(selection) > 0
        self.ui.remove.setEnabled(selected)


# ----------------------------------------------------------------------------------------------------------------------
    def on_add(self):
        """Fires when the user clicks the add button."""
        misc = Miscellaneous(self.recipe)
        misc.amount = UnitType(1, 'each')
        misc.timing = TimingType(duration=TimeType(0, 'min'))
        self.recipe.misc.append(misc)


# ----------------------------------------------------------------------------------------------------------------------
    def on_remove(self):
        """Fires when the user clicks the remove button."""
        for index in self.ui.ingredients.selectedIndexes():
            if index.column() != 0:
                continue
            self.recipe.misc.pop(index.row())
            break



# End of File
