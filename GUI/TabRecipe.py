# ======================================================================================================================
#        File:  GUI/TabRecipe.py
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

from GUI.Base.TabRecipe import Ui_TabRecipe
from Recipe.Styles import Styles



# ======================================================================================================================
# Mash Tab
# ----------------------------------------------------------------------------------------------------------------------
class TabRecipe(QtWidgets.QWidget):
    def __init__(self, parent, recipe, brewhouse, workbook):
        super().__init__(parent)
        self.ui = Ui_TabRecipe()
        self.ui.setupUi(self)

        self.recipe = recipe
        self.brewhouse =brewhouse

        self.styles = Styles.from_excel(workbook['Styles'])

        # Load the styles dropdown.
        for style in self.styles:
            self.ui.style.addItem(style.name)

        # Populate the equipment dropdown.
        for equipment in self.brewhouse.equipment:
            self.ui.equipment.addItem(equipment.name)

        # Load recipe data.
        self.ui.name.setText(self.recipe.name)
        self.ui.style.setCurrentText(self.recipe.style.name)
        self.ui.equipment.setCurrentText(self.recipe.equipment.name)
        self.ui.size.setValue(self.recipe.size)
        self.ui.ambient.setValue(self.recipe.ambient)

        # Connect events.
        self.ui.name.textChanged.connect(self.on_name_change)
        self.ui.style.currentIndexChanged.connect(self.on_style_changed)
        self.ui.equipment.currentIndexChanged.connect(self.on_equipment_changed)
        self.ui.size.valueChanged.connect(self.on_size_changed)
        self.ui.ambient.valueChanged.connect(self.on_ambient_changed)



# ----------------------------------------------------------------------------------------------------------------------
    def on_name_change(self, name):
        """Fires when the user changes the name of the recipe in the text box."""
        self.recipe.name = name


# ----------------------------------------------------------------------------------------------------------------------
    def on_style_changed(self, index):
        """Fires when the user changes the selected style."""
        self.recipe.style = self.styles[index]


# ----------------------------------------------------------------------------------------------------------------------
    def on_equipment_changed(self, index):
        """Fires when the user changes their selected equipment."""
        self.recipe.equipment = self.brewhouse.equipment[index]


# ----------------------------------------------------------------------------------------------------------------------
    def on_size_changed(self, value):
        """Fires when the user changes the batch size."""
        self.recipe.size = value


# ----------------------------------------------------------------------------------------------------------------------
    def on_ambient_changed(self, value):
        """Fires when the user changes the ambient temperature."""
        self.recipe.ambient = value



# End of File
