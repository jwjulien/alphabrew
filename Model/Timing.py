# ======================================================================================================================
#        File:  Model/Timing.py
#     Project:  Brewing Recipe Planner
# Description:  Provides implementation for a timing class.
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
from Model.MeasurableUnits import AcidityType, GravityType, TimeType



# ======================================================================================================================
# TimingType Class
# ----------------------------------------------------------------------------------------------------------------------
class TimingType:
    """Represents a BeerJSON TimingType instance providing for timing on ingredients such as fermentables and hops."""

    def __init__(self, time=None, duration=None, continuous=None, specificGravity=None, pH=None, step=None, use=None):
        self._use = None

        self.time: TimeType = time
        self.duration: TimeType = duration
        self.continuous: bool = continuous
        self.specificGravity = specificGravity
        self.pH = pH
        self.step: int = step
        self.use: str = use



# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def use(self):
        """Get the current use value."""
        return self._use

# ----------------------------------------------------------------------------------------------------------------------
    @use.setter
    def use(self, value):
        """Set the use value - but ensure that it is valid."""
        if value is not None and value not in ['Mash', 'Boil', 'Fermentation', 'Package']:
            raise ValueError(f'Timing.use does not support value "{value}"')
        self._use = value



# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert this instance into a BeerJSON compatible dictionary of values."""
        data = {}

        if self.time is not None:
            data['time'] = self.time.to_dict()

        if self.duration is not None:
            data['duration'] = self.duration.to_dict()

        if self.continuous is not None:
            data['continuous'] = self.continuous

        if self.specificGravity is not None:
            data['specific_gravity'] = self.specificGravity.to_dict()

        if self.pH is not None:
            data['pH'] = self.pH.to_dict()

        if self.step is not None:
            data['step'] = self.step.to_dict()

        if self.use is not None:
            data['use'] = 'add_to_' + self.use.lower()

        return data


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data):
        """Load the provided data from a BeerJSON dictionary into this instance."""
        if 'time' in data:
            self.time = TimeType()
            self.time.from_dict(data['time'])

        if 'duration' in data:
            self.duration = TimeType()
            self.duration.from_dict(data['duration'])

        if 'continuous' in data:
            self.continuous = bool(data['continuous'])

        if 'specific_gravity' in data:
            self.continuous = GravityType()
            self.continuous.from_dict(data['specific_gravity'])

        if 'pH' in data:
            self.pH = AcidityType()
            self.pH.from_dict(data['pH'])

        if 'step' in data:
            self.step = int(data['step'])

        if 'use' in data:
            self.use = data['use'].replace('add_to_', '').title()


# ----------------------------------------------------------------------------------------------------------------------
    def copy(self):
        """Return a new instance with the same numerical values."""
        new = TimingType()

        if self.time is not None:
            new.time = self.time.copy()

        if self.duration is not None:
            new.duration = self.duration.copy()

        if self.continuous is not None:
            new.continuous = self.continuous

        if self.specificGravity is not None:
            new.specific_gravity = self.specificGravity.copy()

        if self.pH is not None:
            new.pH = self.pH.copy()

        if self.step is not None:
            new.step = self.step.copy()

        if self.use is not None:
            new.use = self.use

        return new



# End of File
