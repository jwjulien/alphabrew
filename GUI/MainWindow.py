# ======================================================================================================================
#        File:  GUI/MainWindow.py
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
import traceback
import os

import openpyxl
from PySide2 import QtCore, QtGui, QtWidgets

import _version

from GUI.Base.MainWindow import Ui_MainWindow

from GUI.TabRecipe import TabRecipe
from GUI.TabFermentables import TabFermentables
from GUI.TabMiscellaneous import TabMiscellaneous
from GUI.TabWaters import TabWaters
from GUI.TabChemistry import TabChemistry
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

        self._touched = None

        self.version = _version.__version__
        self.filename = None

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

        # Load database items into memory.
        # Load read-only just because we never need to change the database from within this tool.
        workbook = openpyxl.load_workbook('Database.xlsx', read_only=True, data_only=True)

        # Add the tab instances into the tab container.
        self.ui.tab_recipe = TabRecipe(self, self.recipe, self.brewhouse, workbook)
        self.ui.tabs.addTab(self.ui.tab_recipe, "Recipe")

        self.ui.tab_waters = TabWaters(self, self.recipe, workbook)
        self.ui.tabs.addTab(self.ui.tab_waters, "Waters")

        self.ui.tab_fermentables = TabFermentables(self, self.recipe, workbook)
        self.ui.tabs.addTab(self.ui.tab_fermentables, "Fermentables")

        self.ui.tab_mash = TabMash(self, self.recipe)
        self.ui.tabs.addTab(self.ui.tab_mash, "Mash")

        self.ui.tab_chemistry = TabChemistry(self, self.recipe)
        self.ui.tabs.addTab(self.ui.tab_chemistry, "Chemistry")

        self.ui.tab_hops = TabHops(self, self.recipe, workbook)
        self.ui.tabs.addTab(self.ui.tab_hops, "Hops")

        self.ui.tab_miscellaneous = TabMiscellaneous(self, self.recipe)
        self.ui.tabs.addTab(self.ui.tab_miscellaneous, "Miscellaneous")

        self.ui.tab_cultures = TabCultures(self, self.recipe, workbook)
        self.ui.tabs.addTab(self.ui.tab_cultures, "Cultures")

        self.ui.tab_fermentation = TabFermentation(self, self.recipe)
        self.ui.tabs.addTab(self.ui.tab_fermentation, "Fermentation")

        self.ui.tabs.currentChanged.connect(self.on_tab_change)

        workbook.close()

        self.update()

        # Once loaded it's safe to assume that nothing has been touched yet.
        self.touched = False



# ======================================================================================================================
# Shutdown Hook
# ----------------------------------------------------------------------------------------------------------------------
    def closeEvent(self, event):
        """Ensure that the user has saved all changes and allow them to cancel if they didn't mean to close."""
        self._warn_unsaved(event)



# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def isDirty(self):
        """Returns True when the currently open file has never been saved or has changed since the last save."""
        # If the recipe has not been changed then it's safe to assume that it's not dirty.
        if not self.touched:
            return False

        # Touched, but possibly no filename yet - no file, nothing to compare - definitely dirty.
        if self.filename is None:
            return True

        # Otherwise, compare the existing contents of the file to the current state.
        current = self.recipe.to_beerjson()
        with open(self.filename) as handle:
            existing = handle.read()

        # Return True, indicating "dirty" when they aren't identical.
        # There's probably a more robust way to compare JSON.
        return current != existing


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def touched(self):
        """Fetches the "dirty" flag that comes from recipe changes.  This is used to better capture when a recipe has
        been modified before it has been saved."""
        return self._touched


# ----------------------------------------------------------------------------------------------------------------------
    @touched.setter
    def touched(self, state):
        """Sets the "touched" flag and updates the GUI window to show an asterisk when it is dirty."""
        self._touched = state
        title = 'AlphaBrew - '
        if self.filename is not None:
            title += os.path.basename(self.filename)
        else:
            title += 'untitled'
        if self.isDirty:
            title += '*'
        self.setWindowTitle(title)



# ======================================================================================================================
# Event Handlers
# ----------------------------------------------------------------------------------------------------------------------
    def on_file_new(self):
        """Fires when the user requests to start a new recipe."""
        if self._warn_unsaved():
            self.filename = None
            self.recipe.clear()
            self.touched = False


# ----------------------------------------------------------------------------------------------------------------------
    def on_file_open(self):
        """Fires when the user requests to open a recipe from local file."""
        if self._warn_unsaved():
            self.recipe.clear()
            filename, filters = QtWidgets.QFileDialog.getOpenFileName(self, "Open Recipe", filter="BeerJSON (*.json)")
            if filename:
                self.filename = filename
                self.recipe.changed.disconnect(self.update)
                with open(filename) as handle:
                    self.recipe.from_beerxml(handle.read())
                # Newly loaded recipe was not touched.  Clear that up despite all of the "change" events reported during
                # the loading.
                self.touched = False
                self.recipe.changed.connect(self.update)


# ----------------------------------------------------------------------------------------------------------------------
    def on_file_save(self):
        """Fires when the user requests to save the current recipe to local file."""
        if self.filename:
            # TODO: Handle merging BeerJSON with existing files.  The goal would be to update applicable values when
            # saving but not nuke the existing values that may already be in the file.
            with open(self.filename, 'w') as handle:
                handle.write(self.recipe.to_beerjson())
            self.touched = False
        else:
            self.on_file_save_as()


# ----------------------------------------------------------------------------------------------------------------------
    def on_file_save_as(self):
        """Fires when the user specifically requests to save as a different file."""
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Recipe As...", filter="BeerJSON (*.json)")
        if filename:
            self.filename = filename
            self.on_file_save()


# ----------------------------------------------------------------------------------------------------------------------
    def on_help_about(self):
        """Fires when the user selects about from the help menu."""
        description = 'A highly opinionated beer recipe editor.  It\'s not fancy or elaborate.  It strives to do one '
        description += 'thing, one thing only, and one thing well - edit beer recipes.'
        description += '\n\n'
        description += 'It is not a calculator or an adjuster or a compensator, etc.'
        description += ' - download something else for that.'
        description += '\n\n'
        description += f'Version: {self.version}\n'
        description += 'Author: Jared Julien <jaredjulien@gmail.com>'
        QtWidgets.QMessageBox.about(self, 'AlphaBrew', description)


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
        self.ui.calcBoilSize.setText(f'{self.recipe.boilVolume.as_("gal"):.1f} gal')
        self.ui.calcBoilSg.setText(f'{self.recipe.boilGravity:.3f}')
        self.ui.calcCalories.setText(f'{self.recipe.calories:.0f} / 16oz')

        self.touched = True


# ----------------------------------------------------------------------------------------------------------------------
    def on_tab_change(self, index):
        """Fires when the active tab changes and calls tries to call the activated method of newly activated tab widget.
        """
        tab = self.ui.tabs.widget(index)

        try:
            tab.activated()

        except AttributeError:
            # Swallow errors when the refresh method does not exist.  It's implementation is optional.
            pass



# ======================================================================================================================
# Private Methods
# ----------------------------------------------------------------------------------------------------------------------
    def _warn_unsaved(self, event=None):
        """Check to see if the current file is dirty and prompt the user to save changes."""
        if self.isDirty:
            text = 'You have unsaved changes, would you like to save them before exiting?'

            buttons = QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel
            stdButtons = QtWidgets.QMessageBox.StandardButtons(buttons)

            default = QtWidgets.QMessageBox.Save

            result = QtWidgets.QMessageBox.warning(self, "Unsaved changes", text, stdButtons, defaultButton=default)

            if result == QtWidgets.QMessageBox.Cancel:
                if event is not None:
                    event.ignore()
                return False

            if result == QtWidgets.QMessageBox.Save:
                self.on_file_save()

        return True


# End of File
