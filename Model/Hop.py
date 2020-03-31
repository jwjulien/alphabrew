# ======================================================================================================================
#        File:  Model/Hop.py
#     Project:  Brewing Recipe Planner
# Description:  Provides the definition for a single hop addition or library item.
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
import math
from typing import Union

from PySide2 import QtCore

from Model.Timing import TimingType
from Model import Selections
from Model.MeasurableUnits import MassType, PercentType, VolumeType



# ======================================================================================================================
# Hop Class
# ----------------------------------------------------------------------------------------------------------------------
class Hop(QtCore.QObject):
    def __init__(self,
                 recipe=None,
                 name=None,
                 amount=None,
                 timing=None,
                 htype=None,
                 form=None,
                 alpha=None,
                 beta=None,
                 hsi=None,
                 origin=None,
                 substitutes=None,
                 humulene=None,
                 caryophyllene=None,
                 cohumulone=None,
                 myrcene=None,
                 notes=None):
        super().__init__()

        self.recipe = recipe
        self.name: str = name
        self.amount: Union[MassType, VolumeType] = amount
        self.timing: TimingType = timing
        self.htype: str = htype
        self.form: str = form
        self.alpha: PercentType = alpha
        self.beta: PercentType = beta
        self.hsi: PercentType = hsi
        self.origin: str = origin
        self.substitutes: str = substitutes
        self.humulene: PercentType = humulene
        self.caryophyllene: PercentType = caryophyllene
        self.cohumulone: PercentType = cohumulone
        self.myrcene: PercentType = myrcene
        self.notes: str = notes.replace('\\n', '\n') if notes else ''

        self._ibus = None


# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def copy(self, recipe):
        return Hop(
            recipe=recipe,
            name=self.name,
            amount=self.amount.copy() if self.amount is not None else None,
            timing=self.timing.copy() if self.timing is not None else None,
            htype=self.htype,
            form=self.form,
            alpha=self.alpha.copy(),
            beta=self.beta.copy(),
            hsi=self.hsi.copy(),
            origin=self.origin,
            substitutes=self.substitutes,
            humulene=self.humulene.copy(),
            caryophyllene=self.caryophyllene.copy(),
            cohumulone=self.cohumulone.copy(),
            myrcene=self.myrcene.copy()
        )


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self) -> dict:
        """Convert this hop into a Python dictionary that can be used in assembling a BeerJSON format file.

        Returns a BeerJSON HopType compatible dictionary."""
        return {
            'name': self.name,
            'amount': self.amount.to_dict(),
            'timing': self.timing.to_dict(),
            'origin': self.origin,
            'form': self.form.lower(),
            'alpha_acid': self.alpha.to_dict(),
            'beta_acid': self.beta.to_dict(),
            'type': self.htype.lower(),
            'percent_lost': self.hsi.to_dict(),
            'substitutes': self.substitutes.replace('\n', '\\n'),
            'oil_content': {
                'humulene': self.humulene.to_dict(),
                'caryophyllene': self.caryophyllene.to_dict(),
                'cohumulone': self.cohumulone.to_dict(),
                'myrcene': self.myrcene.to_dict(),
            },
            'notes': self.notes.replace('\n', '\\n')
        }


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data: dict):
        self.name = data['name']
        amount = data['amount']
        self.amount = Selections.one_of(amount['value'], amount['unit'], MassType, VolumeType)
        self.timing = TimingType()
        self.timing.from_dict(data['timing'])
        self.htype = data['type'].title()
        self.form = data['form'].title()
        self.alpha = PercentType(json=data['alpha_acid'])
        self.beta = PercentType(json=data['beta_acid'])
        self.hsi = PercentType(json=data['percent_lost'])
        self.origin = data['origin']
        self.substitutes = data['substitutes'].replace('\\n', '\n')
        self.humulene = PercentType(json=data['oil_content']['humulene'])
        self.caryophyllene = PercentType(json=data['oil_content']['caryophyllene'])
        self.cohumulone = PercentType(json=data['oil_content']['cohumulone'])
        self.myrcene = PercentType(json=data['oil_content']['myrcene'])
        self.notes = data['notes'].replace('\\n', '\n')


# ----------------------------------------------------------------------------------------------------------------------
    def ibus(self, volume: float, gravity: float, minutes: float) -> float:
        """Calculate this hops IBU contribution using the Tinseth method. #opinionated

        Volume is the volume of wort in which the hops are being boiled, in gallons.
        Gravity is the original gravity (expected at tend of boil) in specific gravity.
        Minutes is the amount of time that the hop will be boiled.
        """
        concentration = self.alpha.as_('%') / 100 * self.amount.as_('oz') * 7490 / volume
        utilization = ((1.0 - math.exp(-0.04 * minutes)) / 4.15) * (1.65 * (0.000125 ** (gravity - 1)))

        if 'plug' in self.form.lower():
            utilization *= 1.02
        elif 'pellet' in self.form.lower():
            utilization *= 1.1

        self._ibus = concentration * utilization
        return self._ibus


# ======================================================================================================================
# Overridden Methods
# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self):
        text = '<Hop'
        for key, value in self.__dict__.items():
            text += f' {key}="{value}"'
        text += '>'
        return text



# End of File
