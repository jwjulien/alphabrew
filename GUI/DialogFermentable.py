# ======================================================================================================================
#        File:  GUI/DialogFermentable.py
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
        self.ui.fyield.setValue(self.fermentable.fyield.percent)
        self.ui.color.setValue(self.fermentable.color.srm)
        self.ui.moisture.setValue(self.fermentable.moisture.percent)
        self.ui.diastaticPower.setValue(self.fermentable.diastaticPower.lintner)
        self.ui.addAfterBoil.setChecked(self.fermentable.addAfterBoil or False)
        self.ui.mashed.setChecked(self.fermentable.mashed or False)
        self.ui.phi.setValue(self.fermentable._phi if self.fermentable._phi is not None else 0.0)
        self.ui.bi.setValue(self.fermentable._bi if self.fermentable._bi is not None else 0.0)
        self.ui.notes.setPlainText(self.fermentable.notes)


# ----------------------------------------------------------------------------------------------------------------------
    def on_accept(self):
        """Fires when the user hits to okay button, stores the data from the GUI back into the fermentable passed into
        init."""
        def zero_to_none(value):
            """Convert a zero value to a None type."""
            if value == 0.0:
                return None
            return value

        self.fermentable.name = self.ui.name.text()
        self.fermentable.ftype = self.ui.type.currentText()
        self.fermentable.group = self.ui.group.currentText()
        self.fermentable.producer = self.ui.producer.text()
        self.fermentable.origin = self.ui.origin.text()
        self.fermentable.fyield.value = self.ui.fyield.value()
        self.fermentable.color.value = self.ui.color.value()
        self.fermentable.color.unit = 'SRM'
        self.fermentable.moisture.value = self.ui.moisture.value()
        self.fermentable.diastaticPower.value = self.ui.diastaticPower.value()
        self.fermentable.diastaticPower.unit = 'Lintner'
        self.fermentable.addAfterBoil = self.ui.addAfterBoil.isChecked()
        self.fermentable.mashed = self.ui.mashed.isChecked()
        self.fermentable._phi = zero_to_none(self.ui.phi.value())
        self.fermentable._bi = zero_to_none(self.ui.bi.value())
        self.fermentable.notes = self.ui.notes.toPlainText()



# End of File
