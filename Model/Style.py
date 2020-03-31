# ======================================================================================================================
#        File:  Model/Style.py
#     Project:  Brewing Recipe Planner
# Description:  A definition for a beer Style.
#      Author:  Jared Julien <jaredjulien@gmail.com>
#   Copyright:  (c) 2020 Jared Julien
# ----------------------------------------------------------------------------------------------------------------------
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the folMining conditions:
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
from Model.MeasurableUnits import BitternessRangeType
from Model.MeasurableUnits import CarbonationRangeType
from Model.MeasurableUnits import ColorRangeType
from Model.MeasurableUnits import GravityRangeType
from Model.MeasurableUnits import PercentRangeType



# ======================================================================================================================
# Style Class
# ----------------------------------------------------------------------------------------------------------------------
class Style:
    def __init__(self,
                 name='N/A',
                 stype='',
                 category='',
                 number=0,
                 letter=' ',
                 guide='',
                 og=None,
                 fg=None,
                 abv=None,
                 bitterness=None,
                 color=None,
                 carbonation=None,
                 notes='',
                 aroma='',
                 appearance='',
                 flavor='',
                 mouthfeel='',
                 overall='',
                 ingredients='',
                 examples=''):
        self.name = name
        self.stype = stype
        self.category = category
        self.number = number
        self.letter = letter
        self.guide = guide
        self.og = og
        self.fg = fg
        self.abv = abv
        self.bitterness = bitterness
        self.color = color
        self.carbonation = carbonation
        self.notes = notes
        self.aroma = aroma
        self.appearance = appearance
        self.flavor = flavor
        self.mouthfeel = mouthfeel
        self.overall = overall
        self.ingredients = ingredients
        self.examples = examples



# ======================================================================================================================
# BeerJSON Parsing Functions
# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert self into BeerJSON compatible dictionary."""
        return {
            'name': self.name,
            'type': self.stype.lower(),
            'category': self.category,
            'category_number': self.number,
            'style_letter': self.letter,
            'style_guide': self.guide,
            'original_gravity': self.og.to_dict(),
            'final_gravity': self.fg.to_dict(),
            'international_bitterness_units': self.bitterness.to_dict(),
            'color': self.color.to_dict(),
            'carbonation': self.carbonation.to_dict(),
            'alcohol_by_volume': self.abv.to_dict(),
            'notes': self.notes.replace('\n', '\\n') if self.notes else None,
            'aroma': self.aroma.replace('\n', '\\n') if self.aroma else None,
            'appearance': self.appearance.replace('\n', '\\n') if self.appearance else None,
            'flavor': self.flavor.replace('\n', '\\n') if self.flavor else None,
            'mouthfeel': self.mouthfeel.replace('\n', '\\n') if self.mouthfeel else None,
            'overall_impression': self.overall.replace('\n', '\\n') if self.overall else None,
            'ingredients': self.ingredients.replace('\n', '\\n') if self.ingredients else None,
            'examples': self.examples.replace('\n', '\\n') if self.examples else None
        }


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data):
        """Parse out style data into self from provided BeerJSON compatible dictionary."""
        self.name = data['name']
        self.stype = data['type'].title()
        self.category = data['category']
        self.number = data.get('category_number')
        self.letter = data.get('style_letter')
        self.guide = data['style_guide']
        if 'original_gravity' in data:
            self.og = GravityRangeType()
            self.og.from_dict(data['original_gravity'])
        if 'final_gravity' in data:
            self.fg = GravityRangeType()
            self.fg.from_dict(data['final_gravity'])
        if 'alcohol_by_volume' in data:
            self.abv = PercentRangeType()
            self.abv.from_dict(data['alcohol_by_volume'])
        if 'international_bitterness_units' in data:
            self.bitterness = BitternessRangeType()
            self.bitterness.from_dict(data['international_bitterness_units'])
        if 'color' in data:
            self.color = ColorRangeType()
            self.color.from_dict(data['color'])
        if 'carbonation' in data:
            self.carbonation = CarbonationRangeType()
            self.carbonation.from_dict(data['carbonation'])

        def paragraph(key):
            try:
                return data[key].replace('\\n', '\n')
            except AttributeError:
                return None

        self.notes = paragraph('notes')
        self.aroma = paragraph('aroma')
        self.appearance = paragraph('appearance')
        self.flavor = paragraph('flavor')
        self.mouthfeel = paragraph('mouthfeel')
        self.overall = paragraph('overall_impression')
        self.ingredients = paragraph('ingredients')
        self.examples = paragraph('examples')



# ======================================================================================================================
# Overridden Methods
# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self):
        text = '<style'
        for key, value in self.__dict__.items():
            text += f' {key}="{value}"'
        text += '>'
        return text



# End of File
