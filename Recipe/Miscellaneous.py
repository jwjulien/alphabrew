# ======================================================================================================================
#        File:  Recipe/Miscellaneous.py
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



# ======================================================================================================================
# Miscellaneous Class
# ----------------------------------------------------------------------------------------------------------------------
class Miscellaneous(QtCore.QObject):
    def __init__(self,
                 recipe=None,
                 name='',
                 mtype='',
                 useFor='',
                 use='',
                 duration=0,
                 amount=0,
                 unit=''):
        super().__init__()

        self.recipe = recipe
        self.name = name
        self.mtype = mtype
        self.useFor = useFor
        self.use = use
        self.duration = duration
        self.amount = amount
        self.unit = unit



# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert this misc into a Python dictionary that can be used in assembling a BeerJSON format file.

        Returns a BeerJSON MiscellaneousType compatible dictionary."""
        return {
            'name': self.name,
            'type': self.mtype.lower(),
            'use_for': self.useFor,
            'amount': {
                'value': self.amount,
                'unit': self.unit
            },
            'timing': {
                'use': 'add_to_' + self.use.lower(),
                'duration': {
                    'value': self.duration,
                    'unit': 'min'
                }
            }
        }


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data):
        self.name = data['name']
        self.mtype = data['type'].title()
        self.useFor = data['use_for']
        self.amount = data['amount']['value']
        self.unit = data['amount']['unit']
        self.use = data['timing']['use'].replace('add_to_', '').title()
        self.duration = data['timing']['duration']['value'] # TODO: Deal with other timing requirements.



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
