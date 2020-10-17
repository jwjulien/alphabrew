# ======================================================================================================================
#        File:  GUI/TabSalts.py
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
from PySide2 import QtWidgets

from GUI.Base.TabSalts import Ui_TabSalts



# ======================================================================================================================
# Salt Tab Class
# ----------------------------------------------------------------------------------------------------------------------
class TabSalts(QtWidgets.QWidget):
    """Extends the MainWindow Salt tab widget containing a subset of controls specific to miscellaneous in the
    recipe."""

    def __init__(self, parent, recipe):
        super().__init__(parent)
        self.ui = Ui_TabSalts()
        self.ui.setupUi(self)

        # Store the recipe with which these misc items are associated.
        self.recipe = recipe
        self.recipe.changed.connect(self.recalculate)

        self.setup_recommendations()
        self.setup_salt_additions()




# ======================================================================================================================
# Setup Methods
# ----------------------------------------------------------------------------------------------------------------------
    def setup_recommendations(self):
        """Sets up the dropdowns and values in the recommendation box."""
        # Setup the available yes/no options for the pale color, hop forward, and hazy prompt drop downs.
        for option in ['No', 'Yes']:
            self.ui.pale.addItem(option)
            self.ui.hopForward.addItem(option)
            self.ui.hazeDesired.addItem(option)

        # Setup the values and selection for the body dropdown.
        for option in ['High', 'Medium', 'Low']:
            self.ui.body.addItem(option)
        self.ui.body.setCurrentText('Medium')

        # Attach event handlers to the inputs to recalculate when the value changes.
        self.ui.pale.currentIndexChanged.connect(self.recommend)
        self.ui.body.currentIndexChanged.connect(self.recommend)
        self.ui.hopForward.currentIndexChanged.connect(self.recommend)
        self.ui.hazeDesired.currentIndexChanged.connect(self.recommend)

        # Run the calculations once based upon the initial values.
        self.recommend()


# ----------------------------------------------------------------------------------------------------------------------
    def setup_salt_additions(self):
        """Populate and run the calculations for the salt addition spin boxes."""
        # TODO: Load salts from recipe.
        # TODO: Load acids from recipe.

        # Connect event handlers for each of the input boxes to trigger recalculation.
        self.ui.cacl2_mash.valueChanged.connect(self.recalculate)
        self.ui.caso4_mash.valueChanged.connect(self.recalculate)
        self.ui.mgcl2_mash.valueChanged.connect(self.recalculate)
        self.ui.mgso4_mash.valueChanged.connect(self.recalculate)
        self.ui.nacl_mash.valueChanged.connect(self.recalculate)
        self.ui.nahco3_mash.valueChanged.connect(self.recalculate)
        self.ui.caoh2_mash.valueChanged.connect(self.recalculate)
        self.ui.cacl2_kettle.valueChanged.connect(self.recalculate)
        self.ui.caso4_kettle.valueChanged.connect(self.recalculate)
        self.ui.mgcl2_kettle.valueChanged.connect(self.recalculate)
        self.ui.mgso4_kettle.valueChanged.connect(self.recalculate)
        self.ui.nacl_kettle.valueChanged.connect(self.recalculate)
        self.ui.nahco3_kettle.valueChanged.connect(self.recalculate)
        self.ui.caoh2_kettle.valueChanged.connect(self.recalculate)

        self.ui.phosphoric.valueChanged.connect(self.recalculate)
        self.ui.lactic.valueChanged.connect(self.recalculate)
        self.ui.acidMalt.valueChanged.connect(self.recalculate)

        # Run the calculations once to generate an initial set of values.
        self.recalculate()



# ======================================================================================================================
# Event Handlers
# ----------------------------------------------------------------------------------------------------------------------
    def recommend(self):
        """Called whenever the user changes any of the recommendation dropdowns allowing the recommended pH value to be
        recalculated.

        The maths for the suggestions here were taken verbatim from BrewCipher.  I don't really know if they are good
        suggestions (up or down a tenth of a point for the differnet questions) but they are certainly better than what
        had to work with previously.
         """
        palest = self.ui.pale.currentText() == 'Yes'
        body = self.ui.body.currentText()
        hopForward = self.ui.hopForward.currentText() == 'Yes'
        hazeDesired = self.ui.hazeDesired.currentText() == 'Yes'

        ph = 5.4
        ph += -0.1 if palest else 0.05
        ph += 0.1 if body == 'High' else -0.1 if body == 'Low' else 0
        ph -= 0.1 if hopForward else 0
        ph += 0.1 if hazeDesired else 0

        self.ui.recommended.setText(f'{ph:.2f}')


# ----------------------------------------------------------------------------------------------------------------------
    def recalculate(self):
        """Connected to the input boxes to recalculate the water chemistry whenever the inputs change."""

        # calcium = self.recipe.waters.calcium
        # self.ui.calcium.setText(str(calcium))
        # self.ui.calciumSlide.setValue(calcium.as_('ppm'))

        # magnesium = self.recipe.waters.magnesium
        # self.ui.magnesium.setText(str(magnesium))
        # self.ui.magnesiumSlide.setValue(magnesium.as_('ppm'))

        # sodium = self.recipe.waters.sodium
        # self.ui.sodium.setText(str(sodium))
        # self.ui.sodiumSlide.setValue(sodium.as_('ppm'))

        # chloride = self.recipe.waters.chloride
        # self.ui.chloride.setText(str(chloride))
        # self.ui.chlorideSlide.setValue(chloride.as_('ppm'))

        # sulfate = self.recipe.waters.sulfate
        # self.ui.sulfate.setText(str(sulfate))
        # self.ui.sulfateSlide.setValue(sulfate.as_('ppm'))

        # bicarbonate = self.recipe.waters.bicarbonate
        # self.ui.bicarbonate.setText(str(bicarbonate))
        # self.ui.bicarbonateSlide.setValue(bicarbonate.as_('ppm'))




# End of File
