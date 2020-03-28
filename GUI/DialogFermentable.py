# ======================================================================================================================
#        File:  GUI/DialogFermentable.py
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

from GUI.Base.DialogFermentable import Ui_DialogFermentable


# ======================================================================================================================
# Constants
# ----------------------------------------------------------------------------------------------------------------------
FermentableTypes = [
    "Grain",
    "Extract",
    "Dry Extract",
    "Fruit",
    "Honey",
    "Juice",
    "Sugar",
    "Other"
]

GrainGroups = [
    "Base",
    "Caramel",
    "Flaked",
    "Roasted",
    "Specialty",
    "Smoked",
    "Adjunct"
]



# ======================================================================================================================
# Fermentable Dialog GUI Class
# ----------------------------------------------------------------------------------------------------------------------
class DialogFermentable(QtWidgets.QDialog):
    """Extends the GUI DialogFermentable class to provide the base functionality of the application."""

    def __init__(self, parent, fermentable):
        super().__init__(parent)
        self.ui = Ui_DialogFermentable()
        self.ui.setupUi(self)
        self.fermentable = fermentable

        self.accepted.connect(self.on_accept)

        ok = self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        ok.setIcon(qtawesome.icon('fa5s.check'))

        cancel = self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        cancel.setIcon(qtawesome.icon('fa5s.times'))

        for ftype in FermentableTypes:
            self.ui.type.addItem(ftype)

        for group in GrainGroups:
            self.ui.group.addItem(group)

        self.ui.name.setText(self.fermentable.name)
        self.ui.type.setCurrentText(self.fermentable.ftype)
        self.ui.group.setCurrentText(self.fermentable.group)
        self.ui.producer.setText(self.fermentable.producer)
        self.ui.origin.setText(self.fermentable.origin)
        self.ui.fyield.setValue(self.fermentable.fyield)
        self.ui.color.setValue(self.fermentable.color)
        self.ui.moisture.setValue(self.fermentable.moisture)
        self.ui.diastaticPower.setValue(self.fermentable.diastaticPower)
        self.ui.protein.setValue(self.fermentable.protein)
        self.ui.maxInBatch.setValue(self.fermentable.maxPerBatch)
        self.ui.coarseFineDiff.setValue(self.fermentable.coarseFineDiff)
        self.ui.addAfterBoil.setChecked(self.fermentable.addAfterBoil)
        self.ui.mashed.setChecked(self.fermentable.mashed)
        self.ui.notes.setPlainText(self.fermentable.notes)


    def on_accept(self):
        self.fermentable.name = self.ui.name.text()
        self.fermentable.ftype = self.ui.type.currentText()
        self.fermentable.group = self.ui.group.currentText()
        self.fermentable.producer = self.ui.producer.text()
        self.fermentable.origin = self.ui.origin.text()
        self.fermentable.fyield = self.ui.fyield.value()
        self.fermentable.color = self.ui.color.value()
        self.fermentable.moisture = self.ui.moisture.value()
        self.fermentable.diastaticPower = self.ui.diastaticPower.value()
        self.fermentable.protein = self.ui.protein.value()
        self.fermentable.maxPerBatch = self.ui.maxInBatch.value()
        self.fermentable.coarseFineDiff = self.ui.coarseFineDiff.value()
        self.fermentable.addAfterBoil = self.ui.addAfterBoil.isChecked()
        self.fermentable.mashed = self.ui.mashed.isChecked()
        self.fermentable.notes = self.ui.notes.toPlainText()



# End of File
