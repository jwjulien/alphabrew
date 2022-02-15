# ======================================================================================================================
#        File:  Brewhouse/Calibrations.py
#     Project:  AlphaBrew
# Description:  Provides the definition for calibrations, configurable items.
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
# Calibrations Class
# ----------------------------------------------------------------------------------------------------------------------
class Calibrations:
    """
    Provides the definition for calibrations, configurable items.

    The intent of this class is to contain parameters, such as boil off rate, which remain pretty much fixed across
    all of the equipment in a Brewhouse but may need to be tweaked and adjusted from Brewhouse to Brewhouse.
    """
    def __init__(
            self,
            brewhouseEfficiency=70, # Percent
            leafHopTrubLoss=0.0625, # Gallons per ounce
            pelletHopTrubLoss=0.025, # Gallons per ounce
            maltBufferingCorrectionFactor=0.60, # Unitless
        ):

        # Overall Conversion Efficiency
        self.brewhouseEfficiency = brewhouseEfficiency

        # System Losses
        self.leafHopTrubLoss = leafHopTrubLoss
        self.pelletHopTrubLoss = pelletHopTrubLoss

        self.maltBufferingCorrectionFactor = maltBufferingCorrectionFactor



# End of File
