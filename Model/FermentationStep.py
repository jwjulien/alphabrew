# ======================================================================================================================
#        File:  Model/FermentationStep.py
#     Project:  AlphaBrew
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
from Model.MeasurableUnits import TemperatureType, TimeType



# ======================================================================================================================
# Fermentation Step Class
# ----------------------------------------------------------------------------------------------------------------------
class FermentationStep():
    def __init__(self, recipe=None, name=None, startTemperature=None, endTemperature=None, time=None):
        self.recipe = recipe
        self.name = name
        self.startTemperature = startTemperature
        self.endTemperature = endTemperature
        self.time = time



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert this fermentation step into BeerJSON."""
        return {
            'name': self.name,
            'start_temperature': self.startTemperature.to_dict(),
            'end_temperature': self.endTemperature.to_dict(),
            'step_time': self.time.to_dict(),
        }


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data):
        """Convert a BeerJSON dict into values for this instance."""
        self.name = data['name']
        if 'start_temperature' in data:
            self.startTemperature = TemperatureType(json=data['start_temperature'])
        if 'end_temperature' in data:
            self.endTemperature = TemperatureType(json=data['end_temperature'])
        if 'step_time' in data:
            self.time = TimeType(json=data['step_time'])



# ======================================================================================================================
# Overridden Methods
# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self):
        text = '<FermentationStep'
        for key, value in self.__dict__.items():
            text += f' {key}="{value}"'
        text += '>'
        return text



# End of File
