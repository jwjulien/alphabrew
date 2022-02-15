# ======================================================================================================================
#        File:  GUI/Widgets/SrmRange.py
#     Project:  AlphaBrew
# Description:  Custom widget that extends the RangedSlider widget to provide opinionated background colors for beer
#               SRM range.
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
# SRM Color Range Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class SrmRangeWidget(RangedSliderWidget):
    """Extends the custom Ranged Slider widget to add opinionated styleing to best provide a base for beer SRM color
    sliders in this application."""

    def __init__(self, parent):
        super().__init__(parent)

        self.setRange(0, 50)
        self.setPrecision(1)
        self.setTickMarks(10, 2)

        grad = QtGui.QLinearGradient(0, 0, 1, 0)
        grad.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        for idx in range(50):
            grad.setColorAt(idx / 50, self.srmToColor(idx))
        self.setBackgroundBrush(grad)

        # The styleRangeWidget_srm should display a "window" to show acceptable colors for the style
        self.setPreferredRangeBrush(QtGui.QColor(0, 0, 0, 0))
        self.setPreferredRangePen(QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))

        # Half-height "tick" for color marker
        grad = QtGui.QLinearGradient(0, 0, 0, 1)
        grad.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        grad.setColorAt(0, QtGui.QColor(255, 255, 255, 255))
        grad.setColorAt(0.49, QtGui.QColor(255, 255, 255, 255))
        grad.setColorAt(0.50, QtGui.QColor(255, 255, 255, 0))
        grad.setColorAt(1, QtGui.QColor(255, 255, 255, 0))
        self.setMarkerBrush(grad)

        self.repaint()


    def srmToColor(self, srm):
        """Converts an SRM value to a close-ish approximation to the color.

        For what it's worth, colors are not represented all that well on computers and color vary from screen to screen
        (unless they have actually been calibrated).  So this is only for a general reference, not an exact science.

        Taken from [BrewTarget](https://github.com/Brewtarget/brewtarget/blob/develop/src/Algorithms.h).
        """
        # Philip Lee's approximation from a color swatch and curve fitting.
        red = min(0.5 + (272.098 - 5.80255 * srm), 253)
        green = 0 if srm > 35 else (0.5 + (241.975 - (13.314 * srm) + (0.1881895 * srm * srm)))
        blue = 0.5 + (179.3 - (28.7 * srm))

        # Limit all of the colors to range [0, 255].
        red = max(0, min(255, red))
        green = max(0, min(255, green))
        blue = max(0, min(255, blue))

        return QtGui.QColor(red, green, blue)



# End of File
