# ======================================================================================================================
#        File:  GUI/TabRecipe.py
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

from GUI.Base.TabRecipe import Ui_TabRecipe
from Model.Styles import Styles



# ======================================================================================================================
# Recipe Tab Class
# ----------------------------------------------------------------------------------------------------------------------
class TabRecipe(QtWidgets.QWidget):
    def __init__(self, parent, recipe, brewhouse, workbook):
        super().__init__(parent)
        self.ui = Ui_TabRecipe()
        self.ui.setupUi(self)

        self.recipe = recipe
        self.brewhouse = brewhouse

        self.styles = Styles.from_excel(workbook['Styles'])

        # Load the styles dropdown.
        for style in self.styles:
            self.ui.style.addItem(style.name)

        # Load the list of types into dropdown.
        self.Types = ['All Grain', 'Partial Mash', 'Extract', 'Cider', 'Wine', 'Kombucha', 'Mead', 'Soda', 'Other']
        for rtype in self.Types:
            self.ui.rtype.addItem(rtype)

        # Populate the equipment dropdown.
        for equipment in self.brewhouse.equipment:
            self.ui.equipment.addItem(equipment.name)

        # Load recipe data.
        self.recipe.loaded.connect(self.on_load)
        self.on_load()

        # Connect events.
        self.ui.name.textChanged.connect(self.on_name_change)
        self.ui.author.textChanged.connect(self.on_author_change)
        self.ui.style.currentIndexChanged.connect(self.on_style_changed)
        self.ui.rtype.currentIndexChanged.connect(self.on_type_changed)
        self.ui.equipment.currentIndexChanged.connect(self.on_equipment_changed)
        self.ui.size.valueChanged.connect(self.on_size_changed)
        self.ui.time_boil.valueChanged.connect(self.on_boilTime_changed)
        self.ui.notes.textChanged.connect(self.on_notes_changed)


# ----------------------------------------------------------------------------------------------------------------------
    def on_load(self):
        """Fires when a new recipe is loaded.  Populates the form fields with the data."""
        self.ui.name.setText(self.recipe.name)
        self.ui.author.setText(self.recipe.author)
        if self.recipe.style:
            self.ui.style.setCurrentText(self.recipe.style.name)
        self.ui.rtype.setCurrentText(self.recipe.rtype)
        self.ui.equipment.setCurrentText(self.recipe.equipment.name)
        self.ui.size.setValue(self.recipe.size.as_('gal'))
        self.ui.time_boil.setValue(self.recipe.boilTime.as_('min'))
        self.ui.notes.setPlainText(self.recipe.notes)


# ----------------------------------------------------------------------------------------------------------------------
    def on_name_change(self, value):
        """Fires when the user changes the name of the recipe in the text box."""
        self.recipe.name = value


# ----------------------------------------------------------------------------------------------------------------------
    def on_author_change(self, value):
        """Fires when the user changes the name of the author in the text box."""
        self.recipe.author = value


# ----------------------------------------------------------------------------------------------------------------------
    def on_style_changed(self, index):
        """Fires when the user changes the selected style."""
        self.recipe.style = self.styles[index]


# ----------------------------------------------------------------------------------------------------------------------
    def on_type_changed(self, index):
        """Fires when the user changes the selected type."""
        self.recipe.type = self.Types[index]


# ----------------------------------------------------------------------------------------------------------------------
    def on_equipment_changed(self, index):
        """Fires when the user changes their selected equipment."""
        self.recipe.equipment = self.brewhouse.equipment[index]


# ----------------------------------------------------------------------------------------------------------------------
    def on_size_changed(self, value):
        """Fires when the user changes the batch size."""
        self.recipe.size.value = value
        self.recipe.size.unit = 'gal'  # The GUI only works with gallons. #opinionated


# ----------------------------------------------------------------------------------------------------------------------
    def on_boilTime_changed(self, value):
        """Fires when the user changes the boil time."""
        self.recipe.time_boil.value = value
        self.recipe.time_boil.unit = 'min'  # The GUI only works with minutes. #opinionated


# ----------------------------------------------------------------------------------------------------------------------
    def on_notes_changed(self):
        """Fires when the user changes the notes."""
        self.recipe.notes = self.ui.notes.toPlainText()



# End of File
