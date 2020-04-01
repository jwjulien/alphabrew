# ======================================================================================================================
#        File:  GUI/Table/Column.py
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
from PySide2 import QtCore

from GUI.Table.Sizing import Fit



# ======================================================================================================================
# Column Class
# ----------------------------------------------------------------------------------------------------------------------
class Column:
    """Provides mapping between a column in a Qt table and properties such as title and text alignment.  Provides a
    common method of formatting the values for cells withing the table."""

    def __init__(
            self,
            attribute,
            heading=None,
            template=None,
            default='--',
            size=Fit,
            align=QtCore.Qt.AlignCenter,
            editable=False,
            hideLimited=False
        ):

        self.attribute = attribute
        self.heading = heading if heading is not None else attribute.title()
        self.default = default
        self.template = template
        self.size = size
        self.align = align
        self.editable = editable
        self.hideLimited = hideLimited


# ----------------------------------------------------------------------------------------------------------------------
    def get_value(self, item):
        """Fetch the raw value of an attribute from the provided item.  Used to get the item for display and editing."""

        def dive(thing, path):
            """Local recursive function to handle possible recursion in the attribute path."""
            if not path:
                return thing
            return dive(getattr(thing, path[0]), path[1:])

        return dive(item, self.attribute.split('.'))


# ----------------------------------------------------------------------------------------------------------------------
    def set_value(self, item, value):
        """Update the attribute in item with the provided value."""

        def dive(thing, path):
            """Local recursive function to handle possible recursion in the attribute path."""
            if len(path) == 1:
                return setattr(thing, path[0], value)
            dive(getattr(thing, path[0]), path[1:])

        return dive(item, self.attribute.split('.'))


# ----------------------------------------------------------------------------------------------------------------------
    def format(self, item):
        """Use the template string for this Column to format the provided data for display."""
        # Extract the value from the item using the provided attribute path for this column.
        value = self.get_value(item)

        # If that value is None, return the default for this column instead of "None" which is ugly.
        if value is None:
            return self.default

        # If no template was provided for this column then just convert the value into a string.
        if self.template is None:
            return str(value)

        # With a template, pass the value through to get it into the proper str format.
        return self.template % value



# End of File
