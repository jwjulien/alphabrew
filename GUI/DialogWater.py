# ======================================================================================================================
#        File:  GUI/DialogWater.py
#     Project:  AlphaBrew
# Description:  Implements a dialog for editing the details of a particular water profile.
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
import qtawesome

from GUI.Base.DialogWater import Ui_DialogWater
from Model.MeasurableUnits import ConcentrationType



# ======================================================================================================================
# Water Dialog GUI Class
# ----------------------------------------------------------------------------------------------------------------------
class DialogWater(QtWidgets.QDialog):
    """Extends the GUI DialogWater class to provide the base functionality of the application."""

    def __init__(self, parent, water):
        super().__init__(parent)
        self.ui = Ui_DialogWater()
        self.ui.setupUi(self)
        self.water = water

        self.accepted.connect(self.on_accept)

        ok = self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        ok.setIcon(qtawesome.icon('fa5s.check'))

        cancel = self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        cancel.setIcon(qtawesome.icon('fa5s.times'))

        self.ui.name.setText(self.water.name)
        self.ui.calcium.setValue(self.water.calcium.as_('ppm'))
        self.ui.magnesium.setValue(self.water.magnesium.as_('ppm'))
        self.ui.sodium.setValue(self.water.sodium.as_('ppm'))
        self.ui.chloride.setValue(self.water.chloride.as_('ppm'))
        self.ui.sulfate.setValue(self.water.sulfate.as_('ppm'))
        self.ui.bicarbonate.setValue(self.water.bicarbonate.as_('ppm'))
        self.ui.ph.setValue(self.water.ph)
        self.ui.notes.setPlainText(self.water.notes)


# ----------------------------------------------------------------------------------------------------------------------
    def on_accept(self):
        """Fires when the user hits to okay button, stores the data from the GUI back into the water passed into init.
        """
        self.water.name = self.ui.name.text()
        self.water.calcium = ConcentrationType(self.ui.calcium.value(), 'ppm')
        self.water.magnesium = ConcentrationType(self.ui.magnesium.value(), 'ppm')
        self.water.sodium = ConcentrationType(self.ui.sodium.value(), 'ppm')
        self.water.chloride = ConcentrationType(self.ui.chloride.value(), 'ppm')
        self.water.sulfate = ConcentrationType(self.ui.sulfate.value(), 'ppm')
        self.water.bicarbonate = ConcentrationType(self.ui.bicarbonate.value(), 'ppm')
        self.water.ph = self.ui.ph.value()
        self.water.notes = self.ui.notes.toPlainText()



# End of File
