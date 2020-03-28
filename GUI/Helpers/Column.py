# ======================================================================================================================
#        File:  GUI/Helpers/Column.py
#     Project:  Brewing Recipe Planner
# Description:  Provides a base class for working with
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
from PySide2 import QtWidgets, QtCore

from GUI.Helpers.Alignment import CenterCenter
from GUI.Helpers.Sizing import Fit



# ======================================================================================================================
# Column Class
# ----------------------------------------------------------------------------------------------------------------------
class Column(object):
    """Provides mapping between a column in a Qt table and properties such as title and text alignment."""
    def __init__(self, attribute, heading=None, template=None, size=Fit, align=QtCore.Qt.AlignCenter):
        self.attribute = attribute
        self.heading = heading if heading is not None else attribute.title()
        self.template = template
        self.size = size
        self.align = align

    def format(self, value, **kwargs):
        if value is None:
            return '--'
        if self.template is None:
            return str(value)
        return self.template.format(value, **kwargs)



# End of File
