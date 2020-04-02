# ======================================================================================================================
#        File:  GUI/TabHops.py
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
from PySide2 import QtCore, QtWidgets
import qtawesome

from GUI.DialogHop import DialogHop
from GUI.Base.TabIngredients import Ui_TabIngredients
from GUI.Delegates.SimpleTypeDelegate import SimpleTypeDelegate
from GUI.Delegates.ComboBoxDelegate import ComboBoxDelegate
from Model.Hops import Hops
from Model.MeasurableUnits import MassType, TimeType, VolumeType
from Model.Timing import TimingType



# ======================================================================================================================
# Hops Tab Class
# ----------------------------------------------------------------------------------------------------------------------
class TabHops(QtWidgets.QWidget):
    """Extends the MainWindow Hops tab widget containing a subset of controls specific to hops in the
    recipe."""

    def __init__(self, parent, recipe, workbook):
        super().__init__(parent)
        self.ui = Ui_TabIngredients()
        self.ui.setupUi(self)

        # Store the recipe with which these hops are associated.
        self.recipe = recipe

        self.recipe.loaded.connect(self.on_load)
        self.on_load()

        # Load a list of available hops from the Excel database.
        self.database = Hops(limited=True)
        self.database.from_excel(workbook['Hops'])

        # Setup the hop ingredient table at the top of the tab.
        self.ui.ingredients.setModel(self.recipe.hops)
        self.recipe.hops.set_control(self.ui.ingredients)
        self.ui.ingredients.selectionModel().selectionChanged.connect(self.on_ingredient_selection_change)

        # Setup a "delegate" to allow editing of the amount in a spinbox right inside of the table.
        delegate = SimpleTypeDelegate(self, [MassType], minimum=0, maximum=32, decimals=1, singleStep=0.5)
        self.ui.ingredients.setItemDelegateForColumn(0, delegate)

        # Setup a "delegate" to allow editing of the use in a combo box right inside of the table.
        delegate = ComboBoxDelegate(self, ['Mash', 'Boil', 'Fermentation'])
        self.ui.ingredients.setItemDelegateForColumn(1, delegate)

        # Setup a "delegate" to allow editing of the duration in a spinbox right inside of the table.
        delegate = SimpleTypeDelegate(self, [TimeType], maximum=240, decimals=0, singleStep=5)
        self.ui.ingredients.setItemDelegateForColumn(2, delegate)

        # Setup a sorting/filter proxy to make it easier to find library ingredients.
        self.proxy = QtCore.QSortFilterProxyModel(self.ui.library)
        self.proxy.setSourceModel(self.database)
        self.proxy.setFilterKeyColumn(0)
        self.proxy.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.filter.textChanged.connect(lambda: self.proxy.setFilterWildcard(self.ui.filter.text()))
        self.ui.library.setModel(self.proxy)

        # Setup the library table at the bottom of the tab listing available hop ingredients.
        self.database.set_control(self.ui.library)
        self.ui.library.selectionModel().selectionChanged.connect(self.on_available_selection_changed)

        # Setup add button with icon and connect an event handler.
        icon = qtawesome.icon('fa5s.arrow-up')
        self.ui.add.setIcon(icon)
        self.ui.add.clicked.connect(self.on_add)

        # Setup edit button with icon and connect an event handler.
        icon = qtawesome.icon('fa5.edit')
        self.ui.edit.setIcon(icon)
        self.ui.edit.clicked.connect(self.on_edit)

        # Setup remove button with icon and connect an event handler.
        icon = qtawesome.icon('fa5s.trash-alt')
        self.ui.remove.setIcon(icon)
        self.ui.remove.clicked.connect(self.on_remove)


# ----------------------------------------------------------------------------------------------------------------------
    def on_load(self):
        """Fires when the recipe gets loaded to re-associate the recipe model with the Qt table in this tab."""
        self.ui.ingredients.setModel(self.recipe.hops)


# ----------------------------------------------------------------------------------------------------------------------
    def on_ingredient_selection_change(self):
        """Fires when the user makes a selection in the top table."""
        selection = self.ui.ingredients.selectionModel().selectedIndexes()
        selected = len(selection) > 0
        self.ui.remove.setEnabled(selected)
        self.ui.edit.setEnabled(selected)


# ----------------------------------------------------------------------------------------------------------------------
    def on_available_selection_changed(self):
        """Fires when the user makes a selection in the bottom table."""
        selection = self.ui.library.selectionModel().selectedIndexes()
        selected = len(selection) > 0
        self.ui.add.setEnabled(selected)


# ----------------------------------------------------------------------------------------------------------------------
    def on_add(self):
        """Fires when the user clicks the add button."""
        # Iterate though the selection(s) the user has made.
        for index in self.ui.library.selectedIndexes():
            # We get an index for each cell, lets filter down to a single column so that we can focus on row indexes.
            if index.column() != 0:
                continue

            # Get the data through the proxy as the indexes don't align with the library when filtering.
            available = self.proxy.data(index, QtCore.Qt.UserRole)

            # Make a copy of the hop so as to not modify the version in the library when working with recipe.
            hop = available.copy(self.recipe)

            hop.timing = TimingType(use='Boil', duration=TimeType(0, 'min'))
            hop.amount = MassType(0, 'oz')

            # Add the new hop into the recipe.
            self.recipe.hops.append(hop)


# ----------------------------------------------------------------------------------------------------------------------
    def on_edit(self):
        """Fires when the user clicks the edit button."""
        selections = self.ui.ingredients.selectedIndexes()
        selections = [selection for selection in selections if selection.column() == 0]
        if len(selections) != 1:
            return
        hop = self.recipe.hops[selections[0].row()]
        dialog = DialogHop(self, hop)
        dialog.exec_()


# ----------------------------------------------------------------------------------------------------------------------
    def on_remove(self):
        """Fires when the user clicks the remove button."""
        for index in self.ui.ingredients.selectedIndexes():
            if index.column() != 0:
                continue
            self.recipe.hops.pop(index.row())
            break



# End of File
