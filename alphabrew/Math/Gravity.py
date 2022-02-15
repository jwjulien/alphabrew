# ======================================================================================================================
#        File:  Math/Gravity.py
#     Project:  AlphaBrew
# Description:  Maths for working with specific gravity, Plato, Brix, etc. conversions.
#      Author:  Jared Julien <jaredjulien@exsystems.net>
#   Copyright:  (c) 2020 Jared Julien, eX Systems
# ---------------------------------------------------------------------------------------------------------------------
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
from Math.Polynomial import Polynomial



# ======================================================================================================================
# Constants
# ----------------------------------------------------------------------------------------------------------------------
PlatoFromSg = Polynomial(-616.868, 1111.14, -630.272, 135.997)



# ======================================================================================================================
# Plato to SG
# ----------------------------------------------------------------------------------------------------------------------
def sg_to_plato(sg):
    """Covert the provided specific gravity value into Plato using polynomial regression."""
    return PlatoFromSg.eval(sg)


# ----------------------------------------------------------------------------------------------------------------------
def plato_to_sg(plato):
    """Convert the provided gravity value in Plato to Specific Gravity units using polynomial regression."""
    poly = PlatoFromSg.copy()
    poly[0] -= plato
    return poly.root(1.000, 1.050)


# ----------------------------------------------------------------------------------------------------------------------
def sg_to_brix(sg):
    """Convert the provided specific gravity value into Brix and return it.

    Help pulled from https://straighttothepint.com/specific-gravity-brix-plato-conversion-calculators"""
    return ((((((182.4601 * sg) - 775.6821) * sg) + 1262.7794) * sg) - 669.5622)


# ----------------------------------------------------------------------------------------------------------------------
def brix_to_sg(brix):
    """Convert the provided value from brix to specific gravity and return the result.

    Help pulled from https://straighttothepint.com/specific-gravity-brix-plato-conversion-calculators/"""
    return (brix / (258.6 - ((brix / 258.2) * 227.1))) + 1




# End of File
