# ======================================================================================================================
#        File:  Model/Miscellaneous.py
#     Project:  Brewing Recipe Planner
# Description:  Provides the definition for a single misc addition.
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
from typing import Union

from Model.Timing import TimingType
from Model import Selections
from Model.MeasurableUnits import MassType, UnitType, VolumeType



# ======================================================================================================================
# Miscellaneous Class
# ----------------------------------------------------------------------------------------------------------------------
class Miscellaneous(QtCore.QObject):
    def __init__(self,
                 recipe=None,
                 name=None,
                 mtype=None,
                 useFor=None,
                 timing=None,
                 amount=None):
        super().__init__()

        self.recipe = recipe
        self.name: str = name
        self.mtype: str = mtype
        self.useFor: str = useFor
        self.timing: TimingType = timing
        self.amount: Union[MassType, VolumeType, UnitType] = amount



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self) -> dict:
        """Convert this misc into a Python dictionary that can be used in assembling a BeerJSON format file.

        Returns a BeerJSON MiscellaneousType compatible dictionary."""
        return {
            'name': self.name,
            'type': self.mtype.lower(),
            'use_for': self.useFor,
            'amount': self.amount.to_dict(),
            'timing': self.timing.to_dict()
        }


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data: dict):
        """Populate the data in this instance from the provided BeerJSON format dict."""
        self.name = data['name']
        self.mtype = data['type'].title()
        self.useFor = data['use_for']
        amount = data['amount']
        self.amount = Selections.one_of(amount['value'], amount['unit'], MassType, VolumeType, UnitType)

        if 'timing' in data:
            self.timing = TimingType()
            self.timing.from_dict(data['timing'])



# ======================================================================================================================
# Overridden Methods
# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self):
        text = '<Misc'
        for key, value in self.__dict__.items():
            text += f' {key}="{value}"'
        text += '>'
        return text



# End of File
