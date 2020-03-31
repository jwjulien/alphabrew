# ======================================================================================================================
#        File:  GUI/DialogHop.py
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

from GUI.Base.DialogHop import Ui_DialogHop



# ======================================================================================================================
# Constants
# ----------------------------------------------------------------------------------------------------------------------
HopTypes = [
    "Aroma",
    "Bittering",
    "Flavor",
    "Aroma/Bittering",
    "Bittering/Flavor",
    "Aroma/Flavor",
    "Aroma/Bittering/Flavor"
]

HopForms = [
    "Pellet",
    "Leaf",
    "Leaf (Wet)",
    "Plug",
    "Powder",
    "Extract"
]



# ======================================================================================================================
# Hop Dialog GUI Class
# ----------------------------------------------------------------------------------------------------------------------
class DialogHop(QtWidgets.QDialog):
    """Extends the GUI DialogHop class to provide the base functionality of the application."""

    def __init__(self, parent, hop):
        super().__init__(parent)
        self.ui = Ui_DialogHop()
        self.ui.setupUi(self)
        self.hop = hop

        self.accepted.connect(self.on_accept)

        ok = self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        ok.setIcon(qtawesome.icon('fa5s.check'))

        cancel = self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        cancel.setIcon(qtawesome.icon('fa5s.times'))

        for htype in HopTypes:
            self.ui.type.addItem(htype)

        for form in HopForms:
            self.ui.form.addItem(form)

        self.ui.name.setText(self.hop.name)
        self.ui.type.setCurrentText(self.hop.htype)
        self.ui.form.setCurrentText(self.hop.form)
        self.ui.alpha.setValue(self.hop.alpha.as_('%'))
        self.ui.beta.setValue(self.hop.beta.as_('%'))
        self.ui.hsi.setValue(self.hop.hsi.as_('%'))
        self.ui.origin.setText(self.hop.origin)
        self.ui.substitutes.setText(self.hop.substitutes)
        self.ui.humulene.setValue(self.hop.humulene.as_('%'))
        self.ui.caryophyllene.setValue(self.hop.caryophyllene.as_('%'))
        self.ui.cohumulone.setValue(self.hop.cohumulone.as_('%'))
        self.ui.myrcene.setValue(self.hop.myrcene.as_('%'))
        self.ui.notes.setPlainText(self.hop.notes)


# ----------------------------------------------------------------------------------------------------------------------
    def on_accept(self):
        """Fires when the user hits to okay button, stores the data from the GUI back into the hop passed into init."""
        self.hop.name = self.ui.name.text()
        self.hop.htype = self.ui.type.currentText()
        self.hop.form = self.ui.form.currentText()
        self.hop.alpha.value = self.ui.alpha.value()
        self.hop.beta.value = self.ui.beta.value()
        self.hop.hsi.value = self.ui.hsi.value()
        self.hop.origin = self.ui.origin.text()
        self.hop.substitutes = self.ui.substitutes.text()
        self.hop.humulene.value = self.ui.humulene.value()
        self.hop.caryophyllene.value = self.ui.caryophyllene.value()
        self.hop.cohumulone.value = self.ui.cohumulone.value()
        self.hop.myrcene.value = self.ui.myrcene.value()
        self.hop.notes = self.ui.notes.toPlainText()



# End of File
