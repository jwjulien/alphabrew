# ======================================================================================================================
#        File:  Model/MashStep.py
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
from Model.MeasurableUnits import TemperatureType, SpecificVolumeType, TimeType, VolumeType



# ======================================================================================================================
# Mash Step Class
# ----------------------------------------------------------------------------------------------------------------------
class MashStep():
    def __init__(self, recipe=None, name=None, mtype=None, temperature=None, time=None):
        self.recipe = recipe
        self.name = name
        self.mtype = mtype
        self.temperature = temperature
        self.time = time

        self.infusionTemperature = None
        self.infusionVolume = None
        self.totalVolume = None
        self.ratio = None



# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def postTemperature(self):
        hours = self.time.as_('hr')
        degrees = self.recipe.equipment.mashTunHeatLoss * hours
        tempLoss = TemperatureType(degrees, 'F')
        return self.temperature - tempLoss



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert this fermentation step into BeerJSON."""
        data = {
            'name': self.name,
            'type': 'infusion',
        }
        if self.temperature is not None:
            data['step_temperature'] = self.temperature.to_dict()
        if self.time is not None:
            data['step_time'] = self.time.to_dict()

        # The following properties are written to the JSON output for downstream users but are calculated properties
        # here in this tool so they are not mirrored in the parsing below.
        if self.infusionVolume is not None:
            data['amount'] = self.infusionVolume.to_dict()
        if self.infusionTemperature is not None:
            data['infuse_temperature'] = self.infusionTemperature.to_dict()
        if self.ratio is not None:
            data['water_grain_ratio'] = self.ratio.to_dict()
        return data


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data):
        """Convert a BeerJSON dict into values for this instance."""
        self.name = data['name']
        self.mtype = data['type'].title()
        if 'step_temperature' in data:
            self.temperature = TemperatureType(json=data['step_temperature'])
        if 'step_time' in data:
            self.time = TimeType(json=data['step_time'])
        # Everything else is calculated off of this data.


# ----------------------------------------------------------------------------------------------------------------------
    def calculate(self, previous, final=False):
        """Run the calculations for infusion temperature and volume given the previous step as a stepping stone."""
        mashWeight = self.recipe.fermentables.mashWeight.as_('lb')
        tunEquiv = self.recipe.equipment.mashTunEquivVol

        # If the user has not setup a mash, provided a temperature for this step or the previous step then we can't do
        # any math yet so clear out possible data and bail out.
        if mashWeight == 0 or self.temperature is None or (previous is not None and previous.temperature is None):
            self.infusionTemperature = None
            self.infusionVolume = None
            self.totalVolume = None
            return

        def temperature(initial, target, volume, existing):
            """Calculates the required temperature of a `volume` of infusion water to bring the mash up to the desired
            `target` temperature from the `initial` temperature taking an `existing` volume of water into account.

            initial: The initial temperature of the mash in degrees Fahrenheit.
            target: The final target temperature of the mash in degrees Fahrenheit.
            volume: The amount of watering being added in quarts.
            existing: The amount of water already in the mash tun from previous infusions, in quarts.
            """
            return (((target - initial) * ((0.2 * mashWeight) + (existing + tunEquiv))) / volume) + target

        def volume(initial, target, addition, existing):
            """Calculate the volume of water at the specified `addition` temperature that is required to raise the
            temperature of the mash from the `initial` temperature to the `target` temperature taking into account the
            thermal mass of the `existing` volume of water.

            initial: The initial temperature of the mash in degrees Fahrenheit.
            target: The final target temperature of the mash in degrees Fahrenheit.
            addition: The temperature of the water being added in degrees Fahrenheit.
            existing: The amount of water already in the mash tun from previous infusions, in quarts.
            """
            return ((target - initial) * ((0.2 * mashWeight) + (existing + tunEquiv))) / (addition - target)

        if previous is None:
            # This is the first step, calculate it based upon some of the other factors instead of previous step.
            # Calculate the strike volume from grain bill and specified ratio.
            quarts = mashWeight * self.recipe.mash.ratio.as_('qt/lb')
            self.infusionVolume = VolumeType(quarts, 'qt')
            self.infusionVolume.convert('gal')
            self.totalVolume = self.infusionVolume.copy()

            # Calculate the infusion temperature based upon the themal mass of the grains and mash tun.
            ambient = self.recipe.mash.ambient.as_('F')
            target = self.temperature.as_('F')
            strike = temperature(ambient, target, quarts, existing=0)
            self.infusionTemperature = TemperatureType(strike, 'F')

        elif not final:
            # Intermediate step (only applies when there are three or more steps in the mash).
            # Determine the volume of boiling water (Fixed temp: 212 F) that needs to be added to achieve this step.
            self.infusionTemperature = TemperatureType(212, 'F')

            # Calculate the volume rather than the temperature here.
            target = self.temperature.as_('F')
            initial = previous.temperature.as_('F')
            existing = previous.totalVolume.as_('qt')
            quarts = volume(initial, target, 212, existing)
            self.infusionVolume = VolumeType(quarts, 'qt')
            self.totalVolume = previous.totalVolume + self.infusionVolume

        else:
            # Compute the temperature of the final infusion based upon the remaining quantity of water.

            gallons = self.recipe.boilSize - previous.totalVolume.as_('gal')
            self.infusionVolume = VolumeType(gallons, 'gal')
            self.totalVolume = previous.totalVolume + self.infusionVolume

            target = self.temperature.as_('F')
            initial = previous.postTemperature.as_('F')
            existing = previous.totalVolume.as_('qt')
            mashout = temperature(initial, target, gallons * 4, existing)
            self.infusionTemperature = TemperatureType(mashout, 'F')

        # Calculate the ratio of this step.
        self.ratio = SpecificVolumeType(self.totalVolume.as_('qt') / mashWeight, 'qt/lb')

        return self




# ======================================================================================================================
# Overridden Methods
# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self):
        text = '<MashStep'
        for key, value in self.__dict__.items():
            text += f' {key}="{value}"'
        text += '>'
        return text



# End of File
