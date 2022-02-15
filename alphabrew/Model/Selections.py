# ======================================================================================================================
#        File:  Model/Selections.py
#     Project:  AlphaBrew
# Description:  Aids in helping select the proper measureable unit type class to use.
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
# Fermentable Class
# ----------------------------------------------------------------------------------------------------------------------
def one_of(value, unit, *options):
    """Given a dictionary containing a `value` and `unit`, use the unit to determine an appropriate type from the
    provided set of `options`.  If no matching type can be found a TypeError is thrown."""
    for option in options:
        if unit in option.Types.keys():
            return option(value, unit)

    raise TypeError(f'Could not find a suitable match for {unit} in {options}')


# ----------------------------------------------------------------------------------------------------------------------
def all_units(*options):
    """Combine all of the available unit types from the provided SimpleType types and return the list."""
    types = []
    for option in options:
        types.extend(option.Types.keys())
    return types



# End of File
