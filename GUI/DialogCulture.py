# ======================================================================================================================
#        File:  GUI/DialogCulture.py
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

from GUI.Base.DialogCulture import Ui_DialogCulture



# ======================================================================================================================
# Constants
# ----------------------------------------------------------------------------------------------------------------------
CultureTypes = [
    'Ale',
    'Lager',
    'Bacteria',
    'Brett',
    'Lacto',
    'Wine',
    'Champagne',
    'Kveik',
    'Malolactic',
    'Mixed Culture',
    'Pedio',
    'Spontaneous',
    'Other'
]

CultureForms = [
    "Liquid",
    "Dry",
    "Slant",
    "Culture",
    "Dregs"
]



# ======================================================================================================================
# Culture Dialog GUI Class
# ----------------------------------------------------------------------------------------------------------------------
class DialogCulture(QtWidgets.QDialog):
    """Extends the GUI DialogCulture class to provide the base functionality of the application."""

    def __init__(self, parent, culture):
        super().__init__(parent)
        self.ui = Ui_DialogCulture()
        self.ui.setupUi(self)
        self.culture = culture

        self.accepted.connect(self.on_accept)

        ok = self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        ok.setIcon(qtawesome.icon('fa5s.check'))

        cancel = self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        cancel.setIcon(qtawesome.icon('fa5s.times'))

        for htype in CultureTypes:
            self.ui.type.addItem(htype)

        for form in CultureForms:
            self.ui.form.addItem(form)

        self.ui.name.setText(self.culture.name)
        self.ui.type.setCurrentText(self.culture.ctype)
        self.ui.form.setCurrentText(self.culture.form)
        self.ui.producer.setText(self.culture.producer)
        self.ui.productId.setText(self.culture.productId)
        self.ui.notes.setPlainText(self.culture.notes)


# ----------------------------------------------------------------------------------------------------------------------
    def on_accept(self):
        """Fires when the user hits to okay button, stores the data from the GUI back into the culture passed into init."""
        self.culture.name = self.ui.name.text()
        self.culture.ctype = self.ui.type.currentText()
        self.culture.form = self.ui.form.currentText()
        self.culture.producer = self.ui.producer.text()
        self.culture.productId = self.ui.productId.text()
        self.culture.notes = self.ui.notes.toPlainText()



# End of File
