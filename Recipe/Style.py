# ======================================================================================================================
#        File:  Recipe/Style.py
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
class Style:
    def __init__(self,
                 name='N/A',
                 stype='',
                 category='',
                 number=0,
                 letter=' ',
                 guide='',
                 ogMin=0,
                 ogMax=0,
                 fgMin=0,
                 fgMax=0,
                 abvMin=0,
                 abvMax=0,
                 ibuMin=0,
                 ibuMax=0,
                 srmMin=0,
                 srmMax=0,
                 co2Min=0,
                 co2Max=0,
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
        self.ogMin = ogMin
        self.ogMax = ogMax
        self.fgMin = fgMin
        self.fgMax = fgMax
        self.abvMin = abvMin
        self.abvMax = abvMax
        self.ibuMin = ibuMin
        self.ibuMax = ibuMax
        self.srmMin = srmMin
        self.srmMax = srmMax
        self.co2Min = co2Min
        self.co2Max = co2Max
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
            'original_gravity': {
                'minimum': {
                    'value': self.ogMin,
                    'unit': 'sg'
                },
                'maximum': {
                    'value': self.ogMax,
                    'unit': 'sg'
                }
            },
            'final_gravity': {
                'minimum': {
                    'value': self.fgMin,
                    'unit': 'sg'
                },
                'maximum': {
                    'value': self.fgMax,
                    'unit': 'sg'
                }
            },
            'international_bitterness_units': {
                'minimum': {
                    'value': self.ibuMin,
                    'unit': 'IBUs'
                },
                'maximum': {
                    'value': self.ibuMax,
                    'unit': 'IBUs'
                }
            },
            'color': {
                'minimum': {
                    'value': self.srmMin,
                    'unit': 'SRM'
                },
                'maximum': {
                    'value': self.srmMax,
                    'unit': 'SRM'
                }
            },
            'carbonation': {
                'minimum': {
                    'value': self.co2Min,
                    'unit': 'vols'
                },
                'maximum': {
                    'value': self.co2Max,
                    'unit': 'vols'
                }
            },
            'alcohol_by_volume': {
                'minimum': {
                    'value': self.abvMin,
                    'unit': '%'
                },
                'maximum': {
                    'value': self.abvMax,
                    'unit': '%'
                }
            },
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
            self.ogMin = data['original_gravity']['minimum']['value'] # TODO: Handle other units.
            self.ogMax = data['original_gravity']['maximum']['value'] # TODO: Handle other units.
        if 'final_gravity' in data:
            self.fgMin= data['final_gravity']['minimum']['value'] # TODO: Handle other units.
            self.fgMax = data['final_gravity']['maximum']['value'] # TODO: Handle other units.
        if 'alcohol_by_volume' in data:
            self.abvMin = data['alcohol_by_volume']['minimum']['value']
            self.abvMax = data['alcohol_by_volume']['maximum']['value']
        if 'international_bitterness_units' in data:
            self.ibuMin = data['international_bitterness_units']['minimum']['value']
            self.ibuMax = data['international_bitterness_units']['maximum']['value']
        if 'color' in data:
            self.srmMin = data['color']['minimum']['value'] # TODO: Handle other units.
            self.srmMax = data['color']['maximum']['value'] # TODO: Handle other units.
        if 'carbonation' in data:
            self.co2Min = data['carbonation']['minimum']['value']
            self.co2Max = data['carbonation']['maximum']['value']

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
