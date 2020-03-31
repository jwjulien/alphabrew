# ======================================================================================================================
#        File:  Model/Culture.py
#     Project:  Brewing Recipe Planner
# Description:  Provides the definition for a single culture or steepable item in a recipe.
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
from typing import Union

from PySide2 import QtCore

from Model.MeasurableUnits import MassType, UnitType, VolumeType
from Model import Selections



# ======================================================================================================================
# Culture Class
# ----------------------------------------------------------------------------------------------------------------------
class Culture(QtCore.QObject):
    def __init__(self,
                 recipe=None,
                 name=None,
                 amount=None,
                 ctype=None,
                 form=None,
                 producer=None,
                 productId=None,
                 notes=None):
        super().__init__()

        self.recipe = recipe
        self.name: str = name
        self.amount: Union[VolumeType, MassType, UnitType] = amount
        self.ctype: str = ctype
        self.form: str = form
        self.producer: str = producer
        self.productId: str = productId
        self.notes: str = notes.replace('\\n', '\n') if notes else None


# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def copy(self, recipe):
        return Culture(
            recipe=recipe,
            name=self.name,
            amount=self.amount.copy() if self.amount is not None else None,
            ctype=self.ctype,
            form=self.form,
            producer=self.producer,
            productId=self.productId,
            notes=self.notes
        )


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self) -> dict:
        """Convert this culture into a Python dictionary that can be used in assembling a BeerJSON format file.

        Returns a BeerJSON CultureType compatible dictionary."""
        return {
            'name': self.name,
            'amount': self.amount.to_dict(),
            'type': self.ctype.lower(),
            'form': self.form,
            'producer': self.producer,
            'productId': self.productId,
            'notes': self.notes.replace('\n', '\\n'),
        }


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data: dict):
        self.name = data['name']
        amount = data['amount']
        self.amount = Selections.one_of(amount['value'], amount['unit'], VolumeType, MassType)
        self.ctype = data['type'].title()
        self.form = data['form']
        self.producer = data['producer']
        self.productId = data['productId']
        self.notes = data['notes'].replace('\\n', '\n')



# ======================================================================================================================
# Overridden Methods
# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self):
        text = '<Culture'
        for key, value in self.__dict__.items():
            text += f' {key}="{value}"'
        text += '>'
        return text



# End of File
