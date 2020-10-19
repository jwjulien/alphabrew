# ======================================================================================================================
#        File:  GUI/TabWaters.py
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

from GUI.Base.TabWater import Ui_TabWater
from Model.Waters import Waters
from Model.Water import Water
from Model.MeasurableUnits import ConcentrationType, PercentType



# ======================================================================================================================
# Waters Tab Class
# ----------------------------------------------------------------------------------------------------------------------
class TabWaters(QtWidgets.QWidget):
    """Extends the MainWindow Waters tab widget containing a subset of controls specific to waters in the
    recipe.

    Please note: this is one area where this tool becomes opinionated.  To simplify the calculations and inputs, the
    tool assumes that you will only use water from a single source and allows you to combine it with some ratio of
    distilled water.  This is done to prevent the user from needing to balance water percentages and to make the mash
    pH calculations much simpler.  This should suit nearly every beer brewed.

    This does present a quirk that a water source be specified even if using 100% distilled water.  I'm living with that
    for the time being and will adjust later if it bothers me enough.
    """

    def __init__(self, parent, recipe, workbook):
        super().__init__(parent)
        self.ui = Ui_TabWater()
        self.ui.setupUi(self)

        # Store the recipe with which these waters are associated.
        self.recipe = recipe
        self.recipe.loaded.connect(self.on_load)
        self.recipe.changed.connect(self.on_change)

        # Load a list of available waters from the Excel database.
        self.database = Waters(limited=True)
        self.database.from_excel(workbook['Waters'])

        # Setup a sorting/filter proxy to make it easier to find library ingredients.
        self.proxy = QtCore.QSortFilterProxyModel(self.ui.library)
        self.proxy.setSourceModel(self.database)
        self.proxy.setFilterKeyColumn(0)
        self.proxy.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.filter.textChanged.connect(lambda: self.proxy.setFilterWildcard(self.ui.filter.text()))
        self.ui.library.setModel(self.proxy)

        # Setup the library table at the bottom of the tab listing available water ingredients.
        self.database.set_control(self.ui.library)
        self.ui.library.selectionModel().selectionChanged.connect(self.on_library_selection_changed)

        # Setup add button with icon and connect an event handler.
        icon = qtawesome.icon('fa5s.arrow-up')
        self.ui.load.setIcon(icon)
        self.ui.load.clicked.connect(self.on_load_source)

        self.ui.sourceName.textChanged.connect(lambda value: self.on_source_changed('name', value))
        self.ui.sourceCalcium.valueChanged.connect(lambda value: self.on_source_changed('calcium', value))
        self.ui.sourceMagnesium.valueChanged.connect(lambda value: self.on_source_changed('magnesium', value))
        self.ui.sourceSodium.valueChanged.connect(lambda value: self.on_source_changed('sodium', value))
        self.ui.sourceChloride.valueChanged.connect(lambda value: self.on_source_changed('chloride', value))
        self.ui.sourceSulfate.valueChanged.connect(lambda value: self.on_source_changed('sulfate', value))
        self.ui.sourceBicarbonate.valueChanged.connect(lambda value: self.on_source_changed('bicarbonate', value))
        self.ui.sourcePh.valueChanged.connect(lambda value: self.on_source_changed('ph', value))

        self.ui.ratio.valueChanged.connect(self.on_ratio_change)

        self.on_load()



# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def sourcePercentage(self):
        """Returns the PercentType value for the currently selected "source" percentage, based upon the slider."""
        return PercentType(self.ui.ratio.value(), '%')


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def distilledPercentage(self):
        """Returns the PercentType of distilled water set by the slider."""
        return PercentType(100 - self.ui.ratio.value(), '%')


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def sourceAmount(self):
        """Return the source amount in gallons calculated from the mash size.  This isn't necessarily the same amount
        as that which is contained in the actual recipe.  This is intended primarily as a helper to calculate and
        populate the new water when a source gets added to the recipe."""
        return self.recipe.mash.totalWater * self.sourcePercentage


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def distilledAmount(self):
        """Same story as with the source amount, just for the distilled portion."""
        return self.recipe.mash.totalWater * self.distilledPercentage



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def on_load(self):
        """Fires when the recipe gets loaded to re-associate the recipe model with the Qt table in this tab."""
        if len(self.recipe.waters) == 0:
            # If there is nothing to be loaded then bail out now.
            return

        source: Water = self.recipe.waters[0]
        self.ui.sourceName.setText(source.name)
        self.ui.sourceCalcium.setValue(source.calcium.as_('ppm'))
        self.ui.sourceMagnesium.setValue(source.magnesium.as_('ppm'))
        self.ui.sourceSodium.setValue(source.sodium.as_('ppm'))
        self.ui.sourceChloride.setValue(source.chloride.as_('ppm'))
        self.ui.sourceSulfate.setValue(source.sulfate.as_('ppm'))
        self.ui.sourceBicarbonate.setValue(source.bicarbonate.as_('ppm'))
        self.ui.sourcePh.setValue(source.ph)

        self.ui.ratio.setValue(source.percentage.as_('%'))

        self.on_change()


# ----------------------------------------------------------------------------------------------------------------------
    def on_change(self):
        """Fires whenever the recipe is changed.  Recalculates the brewing water chemistry for display."""
        self.ui.mixedCalcium.setText(str(self.recipe.waters.calcium))
        self.ui.mixedMagnesium.setText(str(self.recipe.waters.magnesium))
        self.ui.mixedSodium.setText(str(self.recipe.waters.sodium))
        self.ui.mixedChloride.setText(str(self.recipe.waters.chloride))
        self.ui.mixedSulfate.setText(str(self.recipe.waters.sulfate))
        self.ui.mixedBicarbonate.setText(str(self.recipe.waters.bicarbonate))
        self.ui.mixedPh.setText(f'{self.recipe.waters.ph:.1f}')

        if len(self.recipe.waters) > 0:
            self.ui.sourceVolume.setText(str(self.recipe.waters[0].amount))
        else:
            self.ui.sourceVolume.setText(str(self.recipe.boilVolume))

        if len(self.recipe.waters) > 1:
            self.ui.distilledVolume.setText(str(self.recipe.waters[1].amount))
        else:
            self.ui.distilledVolume.setText('0.0 gal')


# ----------------------------------------------------------------------------------------------------------------------
    def on_library_selection_changed(self):
        """Fires when the user makes a selection in the bottom table."""
        selection = self.ui.library.selectionModel().selectedIndexes()
        selected = len(selection) > 0
        self.ui.load.setEnabled(selected)


# ----------------------------------------------------------------------------------------------------------------------
    def on_load_source(self):
        """Fires when the user clicks the load button to load in a selected water profile."""
        # Iterate though the selection(s) the user has made.
        for index in self.ui.library.selectedIndexes():
            # # We get an index for each cell, lets filter down to a single column so that we can focus on row indexes.
            if index.column() != 0:
                continue

            # Get the data through the proxy as the indexes don't align with the library when filtering.
            selected = self.proxy.data(index, QtCore.Qt.UserRole)

            # Make a copy of the water so as to not modify the version in the library when working with recipe.
            water = selected.copy(self.recipe)
            water.amount = self.sourceAmount

            if len(self.recipe.waters) == 0:
                # Add the new water into the recipe.
                self.recipe.waters.append(water)
            else:
                # Update the zeroth entry, which is forced to be the source water.
                self.recipe.waters[0] = water

            # Force a reload of the source water inputs now that we just updated the recipe.
            self.on_load()
            self.recipe.changed.emit()

            break


# ----------------------------------------------------------------------------------------------------------------------
    def on_source_changed(self, attribute, value):
        """Fires when the user changes one of the controls for the source water and posts the updates back to the
        recipe.  `attribute` is injected above in a lambda function to allow this single handler function to handle
        updates from all of the source water inputs."""
        if len(self.recipe.waters) == 0:
            # If there are no waters yet then lets get one added to the recipe.
            water = Water(self.recipe)
            water.amount = self.sourceAmount
            self.recipe.waters.append(water)
        else:
            # When there is a water pull it for updates.
            water = self.recipe.waters[0]

        if attribute not in ['name', 'ph']:
            value = ConcentrationType(value, 'ppm')

        setattr(water, attribute, value)

        self.recipe.changed.emit()


# ----------------------------------------------------------------------------------------------------------------------
    def on_ratio_change(self):
        """Fires when the ratio for distilled vs source water is changed.  Calculates new values for the amounts of
        source and distilled water and recalculates the brewing percentages."""

        self.ui.sourcePercent.setText(str(self.sourcePercentage))
        self.ui.distilledPercent.setText(str(self.distilledPercentage))

        if len(self.recipe.waters) == 0:
            # We cannot update the ratio when there is no water profile yet.
            return

        self.recipe.waters[0].amount = self.sourceAmount

        if self.distilledPercentage.as_('%') > 0:
            # There is some portion of distilled water in this recipe.
            if len(self.recipe.waters) == 1:
                # Distiled water has not yet been added to the recipe - do that now.
                distilled = Water(
                    self.recipe,
                    name='Distilled Water',
                    amount=self.distilledAmount,
                )
                self.recipe.waters.append(distilled)

            else:
                # Distilled water is already here, lets just update it.
                self.recipe.waters[1].amount = self.distilledAmount

            self.recipe.changed.emit()

        elif len(self.recipe.waters) > 1:
            # The user no longer calls for distilled water but it's still in the recipe - remove it.
            self.recipe.waters.pop(1)




# End of File
