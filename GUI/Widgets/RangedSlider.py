# ======================================================================================================================
#        File:  GUI/Widgets/RangedSlider.py
#     Project:  Brewing Recipe Planner
# Description:
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
from PySide2 import QtCore, QtGui, QtWidgets



# ======================================================================================================================
# Ranged Slider Class
# ----------------------------------------------------------------------------------------------------------------------
class RangedSliderWidget(QtWidgets.QWidget):
    """A ranged slider is a generic widget for displaying a bar with tick marks and a bubble showing a highlighted
    range as well as a line showing a current value."""

    def __init__(self,
                 parent,
                 minimum=0,
                 maximum=1,
                 preferredMin=0.25,
                 preferredMax=0.75,
                 value=0.5,
                 valueText="0.500",
                 precision=3,
                 tickInterval=0,
                 secondaryTicks=1,
                 tooltipText="",
                 bgBrush=QtGui.QColor(255, 255, 255),
                 prefRangeBrush=QtGui.QColor(0, 0, 0),
                 prefRangePen=QtCore.Qt.NoPen,
                 markerBrush=QtGui.QColor(255, 255, 255),
                 markerTextIsValue=False):

        super().__init__(parent)
        self.minimum = minimum
        self.maximum = maximum
        self.preferredMin = preferredMin
        self.preferredMax = preferredMax
        self.value = value
        self.valueText = valueText
        self.precision = precision
        self.tickInterval = tickInterval
        self.secondaryTicks = secondaryTicks
        self.tooltipText = tooltipText
        self.bgBrush = bgBrush
        self.prefRangeBrush = prefRangeBrush
        self.prefRangePen = prefRangePen
        self.markerBrush = markerBrush
        self.markerTextIsValue = markerTextIsValue
        self.markerText = ""

        self.setMinimumSize(32, 32)
        self.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)

        # Generate mouse move events whenever mouse movers over widget.
        self.setMouseTracking(True)

        self.repaint()


    def setPreferredRange(self, minimum, maximum):
        self.preferredMin = minimum
        self.preferredMax = maximum

        # Only show tooltips if the range has nonzero size.
        self.setMouseTracking(minimum < maximum)

        template = f'%0.{self.precision}f - %0.{self.precision}f'
        self.tooltipText = template % (self.minimum, self.maximum)

        self.update()


    def setRange(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        self.update()


    def setValue(self, value):
        self.value = value
        template = f'%0.{self.precision}f'
        self.valueText = template % self.value
        self.update()


    def setPrecision(self, precision):
        self.precision = precision
        self.update()


    def setBackgroundBrush(self, brush):
        self.bgBrush = brush
        self.update()


    def setPreferredRangeBrush(self, brush):
        self.prefRangeBrush = brush
        self.update()


    def setPreferredRangePen(self, pen):
        self.prefRangePen = pen
        self.update()


    def setMarkerBrush(self, brush):
        self.markerBrush = brush
        self.update()


    def setMarkerText(self, text):
        self.markerText = text
        self.update()


    def setMarkerTextIsValue(self, value):
        self.markerTextIsValue = value
        self.update()


    def setTickMarks(self, primaryInterval, secondaryTicks=1):
        self.secondaryTicks = max(secondaryTicks, 1)
        self.tickInterval = primaryInterval / self.secondaryTicks
        self.update()


    def sizeHint(self):
        return QtCore.QSize(64, 32)


    def mouseMoveEvent(self, event):
        event.accept()
        tipPoint = self.mapToGlobal(QtCore.QPoint(0, 0))
        QtWidgets.QToolTip.showText(tipPoint, self.tooltipText, self)


    def paintEvent(self, _):
        textFont = QtGui.QFont("Arial", 14)
        textFontMetrics = QtGui.QFontMetrics(textFont)
        indTextHeight = 16
        rectHeight = 16
        indWidth = 4
        textColor = QtGui.QColor(0, 127, 0)

        # Want all the sliders to have exact same width.
        textWidth = textFontMetrics.width("1.000")

        glassGrad = QtGui.QLinearGradient(0, 0, 0, rectHeight)
        glassGrad.setColorAt(0, QtGui.QColor(255, 255, 255, 127))
        glassGrad.setColorAt(1, QtGui.QColor(255, 255, 255, 0))
        glassBrush = QtGui.QBrush(glassGrad)

        painter = QtGui.QPainter(self)
        rectWidth   = 512
        fgRectLeft  = rectWidth / (self.maximum - self.minimum) * (self.preferredMin - self.minimum)
        fgRectWidth = rectWidth / (self.maximum - self.minimum) * (self.preferredMax - self.preferredMin)
        indX        = rectWidth / (self.maximum - self.minimum) * (self.value - self.minimum)

        # Make sure all coordinates are valid.
        fgRectLeft  = max(0, min(rectWidth, fgRectLeft))
        fgRectWidth = max(0, min(rectWidth - fgRectLeft, fgRectWidth))
        indX        = max(0, min(rectWidth - indWidth / 2, indX))
        indLeft     = max(0, min(rectWidth, indX - indWidth / 2))

        painter.save()

        # Indicator text.
        markerTextRect = painter.boundingRect(QtCore.QRectF(), QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom, self.valueText if self.markerTextIsValue else self.markerText)
        markerTextLeft = max(0, min(self.width() - textWidth - 2 - markerTextRect.width(), indLeft * (self.width() - textWidth - 2) / rectWidth - markerTextRect.width() / 2))
        painter.drawText(
            markerTextLeft, 0,
            markerTextRect.width(), 16,
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom,
            self.valueText if self.markerTextIsValue else self.markerText
        )

        # Scale coordinates so that 'rectWidth' units == width()-textWidth-2 pixels.
        painter.scale((self.width() - textWidth - 2) / rectWidth, 1)
        painter.translate(0, indTextHeight)

        painter.setPen(QtCore.Qt.NoPen)

        # Make sure anything we draw "inside" the "glass rectangle" stays inside.
        clipRect = QtGui.QPainterPath()
        clipRect.addRoundedRect(QtCore.QRect(0, 0, rectWidth, rectHeight), 8, 8)
        painter.setClipPath(clipRect)

        # Draw the background rectangle.
        painter.setBrush(self.bgBrush)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.drawRoundedRect(QtCore.QRectF(0, 0, rectWidth, rectHeight), 8, 8)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, False)

        # Draw the style "foreground" rectangle.
        painter.save()
        painter.setBrush(self.prefRangeBrush)
        painter.setPen(self.prefRangePen)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.drawRoundedRect(QtCore.QRectF(fgRectLeft, 0, fgRectWidth, rectHeight), 8, 8)
        painter.restore()

        # Draw the indicator.
        painter.setBrush(self.markerBrush)
        painter.drawRect(QtCore.QRectF(indLeft, 0, indWidth, rectHeight))

        # Draw a white to clear gradient to suggest "glassy."
        painter.setBrush(glassBrush)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.drawRoundedRect(QtCore.QRectF(0, 0, rectWidth, rectHeight), 8, 8)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, False)

        # Draw the ticks.
        painter.setPen(QtCore.Qt.black)
        if self.tickInterval > 0:
            secTick = 1
            totalRange = self.maximum - self.minimum
            for _ in range(int(totalRange / self.tickInterval)):
                painter.translate(rectWidth / totalRange * self.tickInterval, 0)
                if secTick == self.secondaryTicks:
                    painter.drawLine(QtCore.QPointF(0, 0.25 * rectHeight), QtCore.QPointF(0, 0.75 * rectHeight))
                    secTick = 1

                else:
                    painter.drawLine(QtCore.QPointF(0, 0.333 * rectHeight), QtCore.QPointF(0, 0.666 * rectHeight))
                    secTick += 1
        painter.restore()

        painter.translate(self.width() - textWidth, indTextHeight)
        # Draw the text.
        painter.setPen(textColor)
        painter.setFont(textFont)
        painter.drawText(0, 0, textWidth, 16, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter, self.valueText)

        painter.end()


# End of File
