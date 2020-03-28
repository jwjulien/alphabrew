# ======================================================================================================================
#        File:  Recipe/Hop.py
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

from PySide2 import QtCore, QtWidgets



# ======================================================================================================================
# Hop Class
# ----------------------------------------------------------------------------------------------------------------------
class Hop(QtCore.QObject):
    def __init__(self,
                 recipe=None,
                 name='',
                 amount=0,
                 use='Boil',
                 duration=0,
                 htype='',
                 form='',
                 alpha=0,
                 beta=0,
                 hsi=0,
                 origin='',
                 substitutes='',
                 humulene=0,
                 caryophyllene=0,
                 cohumulone=0,
                 myrcene=0,
                 notes=''):
        super().__init__()

        self.recipe = recipe
        self.name = name
        self.amount = amount
        self.use = use
        self.duration = duration
        self.htype = htype
        self.form = form
        self.alpha = alpha
        self.beta = beta
        self.hsi = hsi
        self.origin = origin
        self.substitutes = substitutes
        self.humulene = humulene
        self.caryophyllene = caryophyllene
        self.cohumulone = cohumulone
        self.myrcene = myrcene
        self.notes = notes.replace('\\n', '\n') if notes else ''

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
            amount=self.amount,
            use=self.use,
            duration=self.duration,
            htype=self.htype,
            form=self.form,
            alpha=self.alpha,
            beta=self.beta,
            hsi=self.hsi,
            origin=self.origin,
            substitutes=self.substitutes,
            humulene=self.humulene,
            caryophyllene=self.caryophyllene,
            cohumulone=self.cohumulone,
            myrcene=self.myrcene
        )


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert this hop into a Python dictionary that can be used in assembling a BeerJSON format file.

        Returns a BeerJSON HopType compatible dictionary."""
        return {
            'name': self.name,
            'amount': {
                'value': self.amount,
                'unit': 'oz'
            },
            'timing': {
                'use': 'add_to_' + self.use.lower(),
                'duration': {
                    'value': self.duration,
                    'unit': 'min'
                }
            },
            'origin': self.origin,
            'form': self.form.lower(),
            'alpha_acid': {
                'value': self.alpha,
                'unit': '%'
            },
            'beta_acid': {
                'value': self.beta,
                'unit': '%'
            },
            'type': self.htype.lower(),
            'percent_lost': {
                'value': self.hsi,
                'unit': '%'
            },
            'substitutes': self.substitutes.replace('\n', '\\n'),
            'oil_content': {
                'humulene': {
                    'value': self.humulene,
                    'unit': '%'
                },
                'caryophyllene': {
                    'value': self.caryophyllene,
                    'unit': '%'
                },
                'cohumulone': {
                    'value': self.cohumulone,
                    'unit': '%'
                },
                'myrcene': {
                    'value': self.myrcene,
                    'unit': '%'
                }
            },
            'notes': self.notes.replace('\n', '\\n')
        }


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data):
        self.name = data['name']
        self.amount = data['amount']['value'] # TODO: Deal with other units
        self.use = data['timing']['use'].replace('add_to_', '').title()
        self.duration = data['timing']['duration']['value'] # TODO: Deal with other timing requirements.
        self.htype = data['type'].title()
        self.form = data['form'].title()
        self.alpha = data['alpha_acid']['value']
        self.beta = data['beta_acid']['value']
        self.hsi = data['percent_lost']['value']
        self.origin = data['origin']
        self.substitutes = data['substitutes'].replace('\\n', '\n')
        self.humulene = data['oil_content']['humulene']['value']
        self.caryophyllene = data['oil_content']['caryophyllene']['value']
        self.cohumulone = data['oil_content']['cohumulone']['value']
        self.myrcene = data['oil_content']['myrcene']['value']
        self.notes = data['notes'].replace('\\n', '\n')


# ----------------------------------------------------------------------------------------------------------------------
    def ibus(self, volume, gravity, minutes):
        """Calculate this hops IBU contribution using the Tinseth method (opinionated).

        Volume is the volume of wort in which the hops are being boiled, in gallons.
        Gravity is the original gravity (expected at tend of boil) in specific gravity.
        Minutes is the amount of time that the hop will be boiled.
        """
        concentration = self.alpha / 100 * self.amount * 7490 / volume
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
