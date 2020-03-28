# ======================================================================================================================
#        File:  Brewhouse/Equipment.py
#     Project:  Brewing Recipe Planner
# Description:  Provides the definition for a system setup and the associated settings and constants.
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
# Equipment Class
# ----------------------------------------------------------------------------------------------------------------------
class Equipment:
    """Provides the definition for a system setup and the associated settings and constants.  Represents one particular
    equipment profile/setup for a brewing system.  A single Brewhouse may contain more than one Equipment profile."""
    def __init__(self,
                 name='N/A',
                 mashTunVolume=5, # Gallons
                 grainAbsorptionLoss=0.12, # Gallons per pound
                 boilOffRate=1.24, # Gallons per hour
                 coolingLoss=0, # Gallons
                 strikeHltDeadspace=0, # Gallons
                 spargeHltDeadspace=0, # Gallons
                 kettleDeadspace=0, # Gallons
                 siphonLoss=0, # Gallons
    ):
        self.name = name
        self.mashTunVolume = mashTunVolume
        self.grainAbsorptionLoss = grainAbsorptionLoss
        self.boilOffRate = boilOffRate
        self.coolingLoss = coolingLoss
        self.strikeHltDeadspace = strikeHltDeadspace
        self.spargeHltDeadspace = spargeHltDeadspace
        self.kettleDeadspace = kettleDeadspace
        self.siphonLoss = siphonLoss



# End of File
