# ======================================================================================================================
#        File:  Brewhouse/Brewhouse.py
#     Project:  Brewing Recipe Planner
# Description:  Provides the definition for a Brewhouse which holds the settings pertaining to the house and equipment.
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
# Import Statements
# ----------------------------------------------------------------------------------------------------------------------
import toml

from Brewhouse.Equipment import Equipment
from Brewhouse.Constants import Constants


# ======================================================================================================================
# Brewhouse Class
# ----------------------------------------------------------------------------------------------------------------------
class Brewhouse:
    """
    Provides the definition for a Brewhouse which holds the settings pertaining to the house and equipment.

    When instantiated, the classloads settings from "Brewhouse.toml" and sets appropriate defaults for anything that is
    missing.
    """
    def __init__(self):
        config = toml.load('Brewhouse.toml')

        self.equipment = [Equipment(**data) for data in config.get('equipment', [])]
        # TODO: Load some kind of default equipment setup for when the input file doesn't exist or contain equipment.

        self.constants = Constants(**config.get('constants', {}))


# End of Fil
