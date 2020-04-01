# ======================================================================================================================
#        File:  Model/Fermentation.py
#     Project:  Brewing Recipe Planner
# Description:  A base for fermenting a beer.
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
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide2 import QtCore

from Model.ListTableBase import ListTableBase
from Model.FermentationStep import FermentationStep
from GUI.Table.Column import Column



# ======================================================================================================================
# Fermentation Class
# ----------------------------------------------------------------------------------------------------------------------
class Fermentation(ListTableBase):
    """Tablular definition for fermentation steps outlining the fermentation process."""
    AllColumns = [
        Column('name', align=QtCore.Qt.AlignRight, editable=True),
        Column('startTemperature', 'Start Temp', align=QtCore.Qt.AlignRight, editable=True),
        Column('endTemperature', 'End Temp', align=QtCore.Qt.AlignRight, editable=True),
        Column('stepTime', 'Time', align=QtCore.Qt.AlignRight, editable=True),
    ]


# ======================================================================================================================
# Static Methods
# ----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def from_excel(worksheet):
        raise NotImplementedError('Fermentation does not support loading library items from Excel worksheets.')



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def sort(self):
        """Steps are sorted manually. Deliberately left blank - will be called but nothing will happen."""


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert this fermentation into BeerJSON."""
        return {
            'name': 'A kick ass fermentation! (Why is the name required?)',
            'steps': [step.to_dict() for step in self.items]
        }


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data):
        """Convert a BeerJSON dict into values for this instance."""
        self.items = []
        for child in data['steps']:
            step = FermentationStep()
            step.from_dict(child)
            self.append(step)



# End of File
