# ======================================================================================================================
#        File:  GUI/TabWater.py
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

from GUI.Base.TabWater import Ui_TabWater



# ======================================================================================================================
# Water Tab Class
# ----------------------------------------------------------------------------------------------------------------------
class TabWater(QtWidgets.QWidget):
    """Extends the MainWindow Water tab widget containing a subset of controls specific to miscellaneous in the
    recipe."""

    def __init__(self, parent, recipe, workbook):
        super().__init__(parent)
        self.ui = Ui_TabWater()
        self.ui.setupUi(self)

        # Store the recipe with which these misc items are associated.
        self.recipe = recipe

        self.setup_recommendations()




# ======================================================================================================================
# Setup Methods
# ----------------------------------------------------------------------------------------------------------------------
    def setup_recommendations(self):
        """Sets up the dropdowns and values in the recommendation box."""
        for option in ['No', 'Yes']:
            self.ui.pale.addItem(option)
            self.ui.hopForward.addItem(option)
            self.ui.hazeDesired.addItem(option)

        for option in ['High', 'Medium', 'Low']:
            self.ui.body.addItem(option)

        self.ui.body.setCurrentText('Medium')

        self.ui.pale.currentIndexChanged.connect(self.recommend)
        self.ui.body.currentIndexChanged.connect(self.recommend)
        self.ui.hopForward.currentIndexChanged.connect(self.recommend)
        self.ui.hazeDesired.currentIndexChanged.connect(self.recommend)

        self.recommend()




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



# End of File
