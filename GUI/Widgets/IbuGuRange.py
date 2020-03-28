# ======================================================================================================================
#        File:  GUI/Widgets/IbuGuRange.py
#     Project:  Brewing Recipe Planner
# Description:  Custom widget that extends the RangedSlider widget to provide opinionated background colors for beer
#               IBU/GU range.
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
from PySide2 import QtCore, QtGui

from GUI.Widgets.RangedSlider import RangedSliderWidget



# ======================================================================================================================
# IBU/GU Range Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class IbuGuRangeWidget(RangedSliderWidget):
    """Extends the custom Ranged Slider widget to add opinionated styleing to best provide a base for beer IBU/GU
    sliders in this application."""

    def __init__(self, parent):
        super().__init__(parent)

        self.setRange(0, 1)
        self.setPreferredRange(0, 0)
        self.setPrecision(2)

        grad = QtGui.QLinearGradient(0, 0, 1, 0)
        grad.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        grad.setColorAt((0.28 + 0.36) / 2, QtGui.QColor(252, 144, 48))
        grad.setColorAt((0.36 + 0.44) / 2, QtGui.QColor(252, 204, 4))
        grad.setColorAt((0.44 + 0.53) / 2, QtGui.QColor(243, 252, 4))
        grad.setColorAt((0.53 + 0.64) / 2, QtGui.QColor(185, 240, 120))
        grad.setColorAt((0.64 + 0.85) / 2, QtGui.QColor(121, 201, 121))
        self.setBackgroundBrush(grad)

        self.setMarkerBrush(QtGui.QColor(0, 0, 0))
        self.setTickMarks(0, 0)

        self.repaint()


# ----------------------------------------------------------------------------------------------------------------------
    def setValue(self, value):
        """Override to set the text for this slider based upon the range of the input value."""
        if not value:
            text = 'N/A'
        elif value < 0.28:
            text = 'Cloying'
        elif value < 0.36:
            text = 'Extra Malty'
        elif value < 0.44:
            text = 'Slightly Malty'
        elif value < 0.53:
            text = 'Balanced'
        elif value < 0.64:
            text = 'Slightly Hoppy'
        elif value < 0.85:
            text = 'Extra Hoppy'
        else:
            text = 'Way Hoppy'

        self.setMarkerText(text)
        super().setValue(value)



# End of File
