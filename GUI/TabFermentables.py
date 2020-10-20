# ======================================================================================================================
#        File:  GUI/TabFermentables.py
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

from GUI.Base.TabIngredients import Ui_TabIngredients
from GUI.DialogFermentable import DialogFermentable
from GUI.Delegates.SimpleTypeDelegate import SimpleTypeDelegate
from Model.Fermentables import Fermentables
from Model.MeasurableUnits import MassType



# ======================================================================================================================
# Fermentables Tab Class
# ----------------------------------------------------------------------------------------------------------------------
class TabFermentables(QtWidgets.QWidget):
    """Extends the MainWindow Fermentables tab widget containing a subset of controls specific to fermentables in the
    recipe."""

    def __init__(self, parent, recipe, workbook):
        super().__init__(parent)
        self.ui = Ui_TabIngredients()
        self.ui.setupUi(self)

        # Store the recipe with which these fermentables are associated.
        self.recipe = recipe

        self.recipe.loaded.connect(self.on_load)
        self.on_load()

        # Load a list of available fermentables from the Excel database.
        self.database = Fermentables(limited=True)
        self.database.from_excel(workbook['Fermentables'])

        # Setup the fermentable ingredient table at the top of the tab.
        self.recipe.fermentables.set_control(self.ui.ingredients)

        # Setup a "delegate" to allow editing of the amount in a spinbox right inside of the table.
        delegate = SimpleTypeDelegate(self, [MassType], maximum=1000, decimals=2, singleStep=1)
        self.ui.ingredients.setItemDelegateForColumn(0, delegate)

        # Setup a sorting/filter proxy to make it easier to find library ingredients.
        self.proxy = QtCore.QSortFilterProxyModel(self.ui.library)
        self.proxy.setSourceModel(self.database)
        self.proxy.setFilterKeyColumn(0)
        self.proxy.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.filter.textChanged.connect(lambda: self.proxy.setFilterWildcard(self.ui.filter.text()))
        self.ui.library.setModel(self.proxy)

        # Setup the library table at the bottom of the tab listing available fermentable ingredients.
        self.database.set_control(self.ui.library)
        self.ui.library.selectionModel().selectionChanged.connect(self.on_library_selection_changed)

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
        self.ui.ingredients.setModel(self.recipe.fermentables)
        self.ui.ingredients.selectionModel().selectionChanged.connect(self.on_ingredient_selection_change)


# ----------------------------------------------------------------------------------------------------------------------
    def on_ingredient_selection_change(self):
        """Fires when the user makes a selection in the top table."""
        selection = self.ui.ingredients.selectionModel().selectedIndexes()
        selected = len(selection) > 0
        self.ui.remove.setEnabled(selected)
        self.ui.edit.setEnabled(selected)


# ----------------------------------------------------------------------------------------------------------------------
    def on_library_selection_changed(self):
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

            # Make a copy of the fermentable so as to not modify the version in the library when working with recipe.
            fermentable = available.copy(self.recipe)

            # Initialize the properties that are required in ingredients but missing in the library of items.
            fermentable.amount = MassType(0, 'lb')

            # Add the new fermentable into the recipe.
            self.recipe.fermentables.append(fermentable)


# ----------------------------------------------------------------------------------------------------------------------
    def on_edit(self):
        """Fires when the user clicks the edit button."""
        selections = self.ui.ingredients.selectedIndexes()
        selections = [selection for selection in selections if selection.column() == 0]
        if len(selections) != 1:
            return
        fermentable = self.recipe.fermentables[selections[0].row()]
        dialog = DialogFermentable(self, fermentable)
        dialog.exec_()


# ----------------------------------------------------------------------------------------------------------------------
    def on_remove(self):
        """Fires when the user clicks the remove button."""
        for index in self.ui.ingredients.selectedIndexes():
            if index.column() != 0:
                continue
            self.recipe.fermentables.pop(index.row())
            break



# End of File
