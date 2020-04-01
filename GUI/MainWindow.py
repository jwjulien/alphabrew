# ======================================================================================================================
#        File:  GUI/MainWindow.py
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
import traceback

import openpyxl
from PySide2 import QtCore, QtGui, QtWidgets

import _version

from GUI.Base.MainWindow import Ui_MainWindow

from GUI.TabRecipe import TabRecipe
from GUI.TabFermentables import TabFermentables
from GUI.TabMiscellaneous import TabMiscellaneous
from GUI.TabWater import TabWater
from GUI.TabMash import TabMash
from GUI.TabHops import TabHops
from GUI.TabCultures import TabCultures
from GUI.TabFermentation import TabFermentation

from Brewhouse import Brewhouse
from Model.Recipe import Recipe



# ======================================================================================================================
# Main Window GUI Class
# ----------------------------------------------------------------------------------------------------------------------
class MainWindow(QtWidgets.QMainWindow):
    """Extends the GUI MainWindow class to provide the base functionality of the application."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.version = _version.__version__

        # Setup the range displays for OG, FG, ABV, and IBU.
        self.ui.og.setRange(1, 1.12)
        self.ui.og.setPrecision(3)
        self.ui.og.setTickMarks(0.01, 2)

        self.ui.fg.setRange(1, 1.03)
        self.ui.fg.setPrecision(3)
        self.ui.fg.setTickMarks(0.01, 2)

        self.ui.abv.setRange(0, 15)
        self.ui.abv.setPrecision(2)
        self.ui.abv.setTickMarks(1, 2)

        self.ui.ibu.setRange(0, 120)
        self.ui.ibu.setPrecision(1)
        self.ui.ibu.setTickMarks(10, 2)

        # Connect events to the controls.
        self.ui.actionNew.triggered.connect(self.on_file_new)
        self.ui.actionOpen.triggered.connect(self.on_file_open)
        self.ui.actionSave.triggered.connect(self.on_file_save)
        self.ui.actionSaveAs.triggered.connect(self.on_file_save_as)
        self.ui.actionAbout.triggered.connect(self.on_help_about)
        self.ui.actionContents.triggered.connect(self.on_help_contents)

        self.brewhouse = Brewhouse()
        self.recipe = Recipe(self.brewhouse.calibrations)
        self.recipe.changed.connect(self.update)

        # try:
        with open('recipe.json') as handle:
            self.recipe.from_beerxml(handle.read())
        # except:
        #     print('Failed to load recipe')
        #     traceback.print_exc()

        # Load database items into memory.
        # Load read-only just because we never need to change the database from within this tool.
        workbook = openpyxl.load_workbook('Database.xlsx', read_only=True, data_only=True)

        # Add the tab instances into the tab container.
        self.ui.tab_recipe = TabRecipe(self, self.recipe, self.brewhouse, workbook)
        self.ui.tabs.addTab(self.ui.tab_recipe, "Recipe")

        self.ui.tab_water = TabWater(self, self.recipe, workbook)
        self.ui.tabs.addTab(self.ui.tab_water, "Water")

        self.ui.tab_fermentables = TabFermentables(self, self.recipe, workbook)
        self.ui.tabs.addTab(self.ui.tab_fermentables, "Fermentables")

        self.ui.tab_mash = TabMash(self, self.recipe, workbook)
        self.ui.tabs.addTab(self.ui.tab_mash, "Mash")

        self.ui.tab_hops = TabHops(self, self.recipe, workbook)
        self.ui.tabs.addTab(self.ui.tab_hops, "Hops")

        self.ui.tab_miscellaneous = TabMiscellaneous(self, self.recipe)
        self.ui.tabs.addTab(self.ui.tab_miscellaneous, "Miscellaneous")

        self.ui.tab_cultures = TabCultures(self, self.recipe, workbook)
        self.ui.tabs.addTab(self.ui.tab_cultures, "Cultures")

        self.ui.tab_fermentation = TabFermentation(self, self.recipe)
        self.ui.tabs.addTab(self.ui.tab_fermentation, "Fermentation")

        workbook.close()

        self.update()



# ======================================================================================================================
# Shutdown Hook
# ----------------------------------------------------------------------------------------------------------------------
    def closeEvent(self, event):
        """Ensure that the user has saved all changes and allow them to cancel if they didn't mean to close."""
        # TODO: Check for unsaved changes and warn the user before exiting.



# ======================================================================================================================
# Event Handlers
# ----------------------------------------------------------------------------------------------------------------------
    def on_file_new(self):
        """Fires when the user requests to start a new recipe."""


# ----------------------------------------------------------------------------------------------------------------------
    def on_file_open(self):
        """Fires when the user requests to open a recipe from local file."""


# ----------------------------------------------------------------------------------------------------------------------
    def on_file_save(self):
        """Fires when the user requests to save the current recipe to local file."""
        with open('recipe.json', 'w') as handle:
            handle.write(self.recipe.to_beerjson())
        # TODO: Handle merging BeerJSON with existing files.  The goal would be to update applicable values when saving
        # but not nuke the existing values that may already be in the file.


# ----------------------------------------------------------------------------------------------------------------------
    def on_file_save_as(self):
        """Fires when the user specifically requests to save as a different file."""


# ----------------------------------------------------------------------------------------------------------------------
    def on_help_about(self):
        """Fires whent the user selects about from the help menu."""
        description = 'A highly opinionated beer recipe editor.  It\'s not fancy or elaborate.  It strives to do one '
        description += 'thing, one thing only, and one thing well - edit beer recipes.'
        description += '\n\n'
        description += 'It is not a calculator or an adjuster or a compensator, etc. - download BeerSmith for that.'
        description += '\n\n'
        description += f'Version: {self.version}\n'
        description += 'Author: Jared Julien <jaredjulien@gmail.com>'
        QtWidgets.QMessageBox.about(self, 'Beer Recipe Planner', description)


# ----------------------------------------------------------------------------------------------------------------------
    def on_help_contents(self):
        """Fires when the user asks for help."""
        # TODO: Implement a nice help guide of some kind to walk users through the features and settings.


# ----------------------------------------------------------------------------------------------------------------------
    def update(self):
        """Handles copying of recipe information over to the GUI when the recipe gets changed."""
        # Update the bubble indicating the ideal range based upon the selected beer style.
        if self.recipe.style:
            if self.recipe.style.og is not None:
                self.ui.og.setPreferredRange(
                    self.recipe.style.og.minimum.as_('sg'),
                    self.recipe.style.og.maximum.as_('sg')
                )
            if self.recipe.style.fg is not None:
                self.ui.fg.setPreferredRange(
                    self.recipe.style.fg.minimum.as_('sg'),
                    self.recipe.style.fg.maximum.as_('sg')
                )
            if self.recipe.style.abv is not None:
                self.ui.abv.setPreferredRange(
                    self.recipe.style.abv.minimum.as_('%'),
                    self.recipe.style.abv.maximum.as_('%')
                )
            if self.recipe.style.bitterness is not None:
                self.ui.ibu.setPreferredRange(
                    self.recipe.style.bitterness.minimum.as_('IBUs'),
                    self.recipe.style.bitterness.maximum.as_('IBUs')
                )
            if self.recipe.style.color is not None:
                self.ui.srm.setPreferredRange(
                    self.recipe.style.color.minimum.as_('SRM'),
                    self.recipe.style.color.maximum.as_('SRM')
                )

        # Set the bar for the actual, calclulated value from the recipe.
        self.ui.og.setValue(self.recipe.originalGravity)
        self.ui.fg.setValue(self.recipe.finalGravity)
        self.ui.abv.setValue(self.recipe.abv)
        self.ui.ibu.setValue(self.recipe.bitterness)
        self.ui.srm.setValue(self.recipe.color)
        self.ui.ibu_gu.setValue(self.recipe.ibuGu)

        # Output numbers for the calculated values.
        self.ui.calcBoilSize.setText(f'{self.recipe.boilSize:.1f} gal')
        self.ui.calcBoilSg.setText(f'{self.recipe.boilGravity:.3f}')
        self.ui.calcCalories.setText(f'{self.recipe.calories:.0f} / 16oz')



# End of File
