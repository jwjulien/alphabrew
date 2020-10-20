# ======================================================================================================================
#        File:  GUI/Widgets/StyleRange.py
#     Project:  AlphaBrew
# Description:  Custom widget that extends the RangedSlider widget to provide opinionated background colors for beer
#               style ranges.
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
from PySide2 import QtGui

from GUI.Widgets.RangedSlider import RangedSliderWidget



# ======================================================================================================================
# Style Range Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class StyleRangeWidget(RangedSliderWidget):
    """Extends the custom Ranged Slider widget to add opinionated styleing to best provide a base for beer style
    sliders in this application."""

    def __init__(self, parent):
        super().__init__(parent)

        self.setBackgroundBrush(QtGui.QColor(121, 201, 121))
        self.setPreferredRangeBrush(QtGui.QColor(0, 127, 0))
        self.setMarkerTextIsValue(True)

        self.repaint()



# End of File
