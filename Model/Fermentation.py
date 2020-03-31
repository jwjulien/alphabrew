# ======================================================================================================================
#        File:  Model/Fermentation.py
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
from Model.FermentationStep import FermentationStep



# ======================================================================================================================
# Fermentation Class
# ----------------------------------------------------------------------------------------------------------------------
class Fermentation:
    def __init__(self):
        self.steps = []



    def to_dict(self):
        """Convert this fermentation into BeerJSON."""
        return {
            'name': 'A kick ass fermentation! (Why is the name required?)',
            'steps': [step.to_dict() for step in self.steps]
        }

    def from_dict(self, data):
        """Convert a BeerJSON dict into values for this instance."""
        self.steps = []
        for child in data['steps']:
            step = FermentationStep()
            step.from_dict(child)
            self.steps.append(step)



# End of File
