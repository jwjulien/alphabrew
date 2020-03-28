# ======================================================================================================================
#        File:  Recipe/Styles.py
#     Project:  Brewing Recipe Planner
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
from Recipe.Style import Style



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
                ogMin=row[6].value,
                ogMax=row[7].value,
                fgMin=row[8].value,
                fgMax=row[9].value,
                ibuMin=row[10].value,
                ibuMax=row[11].value,
                srmMin=row[12].value,
                srmMax=row[13].value,
                abvMin=row[14].value,
                abvMax=row[15].value,
                co2Min=row[16].value,
                co2Max=row[17].value,
                notes=attemptParagraph(row[18]),
                overall=attemptParagraph(row[19]),
                ingredients=attemptParagraph(row[20]),
                examples=attemptParagraph(row[21])
            )
            styles.append(style)
        return styles



# End of File
