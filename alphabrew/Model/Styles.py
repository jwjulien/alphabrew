# ======================================================================================================================
#        File:  Model/Styles.py
#     Project:  AlphaBrew
# Description:  A definition for a beer Style in list form.
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
from Model.Style import Style
from Model.MeasurableUnits import BitternessType
from Model.MeasurableUnits import BitternessRangeType
from Model.MeasurableUnits import CarbonationType
from Model.MeasurableUnits import CarbonationRangeType
from Model.MeasurableUnits import ColorType
from Model.MeasurableUnits import ColorRangeType
from Model.MeasurableUnits import GravityType
from Model.MeasurableUnits import GravityRangeType
from Model.MeasurableUnits import PercentType
from Model.MeasurableUnits import PercentRangeType



# ======================================================================================================================
# Styles Class
# ----------------------------------------------------------------------------------------------------------------------
class Styles(list):
    """Provides for a list of Style objects, specifically created to aid in parsing Excel database files."""

    @staticmethod
    def from_excel(worksheet):
        styles = Styles()
        for idx, row in enumerate(worksheet):
            # Skip the header row.
            if idx <= 1:
                continue

            def attemptParagraph(cell):
                value = cell.value
                if value is None:
                    return None
                return value.replace('\\n', '\n')

            style = Style(
                name=row[0].value,
                stype=row[1].value,
                category=row[2].value,
                number=row[3].value,
                letter=row[4].value,
                guide=row[5].value,
                og=GravityRangeType(
                    minimum=GravityType(row[6].value, 'sg'),
                    maximum=GravityType(row[7].value, 'sg')
                ),
                fg=GravityRangeType(
                    minimum=GravityType(row[8].value, 'sg'),
                    maximum=GravityType(row[9].value, 'sg'),
                ),
                bitterness=BitternessRangeType(
                    minimum=BitternessType(row[10].value, 'IBUs'),
                    maximum=BitternessType(row[11].value, 'IBUs')
                ),
                color=ColorRangeType(
                    minimum=ColorType(row[12].value, 'SRM'),
                    maximum=ColorType(row[13].value, 'SRM')
                ),
                abv=PercentRangeType(
                    minimum=PercentType(row[14].value * 100, '%'),
                    maximum=PercentType(row[15].value * 100, '%')
                ),
                carbonation=CarbonationRangeType(
                    minimum=CarbonationType(row[16].value, 'vols'),
                    maximum=CarbonationType(row[17].value, 'vols')
                ),
                notes=attemptParagraph(row[18]),
                overall=attemptParagraph(row[19]),
                ingredients=attemptParagraph(row[20]),
                examples=attemptParagraph(row[21])
            )
            styles.append(style)
        return styles



# End of File
