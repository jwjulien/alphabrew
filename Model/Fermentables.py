# ======================================================================================================================
#        File:  Model/Fermentables.py
#     Project:  Brewing Recipe Planner
# Description:  A definition for a beer Fermentables in list form.
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
from typing import List

from PySide2 import QtCore, QtWidgets

from Model.ListTableBase import ListTableBase
from GUI.Table.Column import Column
from GUI.Table.Sizing import Stretch
from Model.Fermentable import Fermentable
from Model.MeasurableUnits import ColorType, DiastaticPowerType, MassType, PercentType



# ======================================================================================================================
# Fermentables Class
# ----------------------------------------------------------------------------------------------------------------------
class Fermentables(ListTableBase):
    """Provides for a list of Fermentable objects, specifically created to aid in parsing Excel database files and
    display within a QtTableView."""
    Columns = [
        Column('amount', editable=True, hideLimited=True),
        Column('proportion', 'Percent', template='%.0f', align=QtCore.Qt.AlignHCenter, hideLimited=True),
        Column('name', 'Grain/Fermentable', size=Stretch, align=QtCore.Qt.AlignLeft),
        Column('color'),
        Column('ftype', 'Type'),
        Column('group'),
        Column('producer'),
        Column('origin'),
    ]



# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def mashedSugar(self):
        """Return the sucrose equivalent of all of the mashed ingredients."""
        return sum([item.sucrose for item in self.items if item.isMashed and not item.addAfterBoil])


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def nonMashedSugar(self):
        """Returns the total sucrose equivalent of all the non-mashed ingredients."""
        return sum([item.sucrose for item in self.items if not item.isMashed])


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def fermentableSugar(self):
        """Returns to equivalent amount of sucrose, in pounds, that is fermentable.  Excludes ingredients like lactose
        and Splenda."""
        return sum([item.sucrose for item in self.items if item.isFermentable])


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def nonFermentableSugar(self):
        """Returns to equivalent amount of sucrose, in pounds, that is NOT fermentable.  This includes ingredients like
        lactose or Splenda."""
        return sum([item.sucrose for item in self.items if not item.isFermentable])


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def steepedSugar(self):
        """Returns the equivalent amount of sucrose that is steeped post boil, but where it is still "mashed" so
        Brewhouse efficiency still plays a factor."""
        return sum([item.sucrose for item in self.items if item.isMashed and item.addAfterBoil])


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def lateAdditionSugar(self):
        """Returns the equivalent amount of sucrose that is added post boil, but where the efficiency isn't a factor."""
        return sum([item.sucrose for item in self.items if not item.isMashed and item.addAfterBoil])


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def mashWeight(self) -> MassType:
        """Returns the combined weight of all of the mashed ingredients."""
        return sum([item.amount for item in self.items if item.isMashed], MassType(0, 'lb'))


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def mashBiFi(self):
        """A step in calculating the mash pH but also required for calculating the overall water chemistry."""
        total = 0
        for fermentable in self.items:
            total += fermentable.bi * fermentable.proportion / 100
        return total


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def mashPh(self):
        """Calculates the distilled water mash pH for each mashed fermentable and returns the result."""
        phiBiFi = 0
        for fermentable in self.items:
            phiBiFi += fermentable.phi * fermentable.bi * fermentable.proportion / 100
        return phiBiFi / self.mashBiFi



# ======================================================================================================================
# Other Methods
# ----------------------------------------------------------------------------------------------------------------------
    def from_excel(self, worksheet):
        """Parses out a list og Fermentable object and appends them to this instance."""
        def float_or(value, fallback=None):
            """Return the provided value as a float or return fallback if the float conversion fails."""
            try:
                return float(value)
            except TypeError:
                return fallback

        self.items = []
        for idx, row in enumerate(worksheet):
            # Skip the header row.
            if idx == 0:
                continue

            self.append(Fermentable(
                name=str(row[0].value),
                ftype=str(row[1].value),
                group=str(row[2].value),
                producer=str(row[3].value),
                origin=str(row[4].value),
                fyield=PercentType(row[5].value, '%'),
                color=ColorType(row[6].value, 'SRM'),
                moisture=PercentType(row[7].value, '%'),
                diastaticPower=DiastaticPowerType(row[8].value, 'Lintner'),
                addAfterBoil=bool(row[9].value),
                mashed=bool(row[10].value),
                phi=float_or(row[11].value),
                bi=float_or(row[12].value),
                notes=str(row[13].value)
            ))


# ----------------------------------------------------------------------------------------------------------------------
    def sort(self):
        """A void sort function that consistently sorts the fermentable in decreasing order of amount in the recipe."""
        self.items.sort(key=lambda fermentable: (-fermentable.amount.as_('lb'), fermentable.name))


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        """Convert self into a dictionary for BeerJSON storage."""
        return [fermentable.to_dict() for fermentable in self]


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, recipe, data):
        """Parse list of fermentables from the provided BeerJSON dict."""
        for item in data:
            fermentable = Fermentable(recipe)
            fermentable.from_dict(item)
            self.append(fermentable)



# End of File
