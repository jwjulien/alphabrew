# ======================================================================================================================
#        File:  Model/Fermentable.py
#     Project:  AlphaBrew
# Description:  Provides the definition for a single fermentable or steepable item in a recipe.
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
from typing import Union

from Model.MeasurableUnits import ColorType, DiastaticPowerType, MassType, PercentType, VolumeType
from Model import Selections



# ======================================================================================================================
# Fermentable Class
# ----------------------------------------------------------------------------------------------------------------------
class Fermentable():
    def __init__(self,
                 recipe=None,
                 name=None,
                 amount=None,
                 ftype=None,
                 group=None,
                 producer=None,
                 origin=None,
                 fyield=None,
                 color=None,
                 moisture=None,
                 diastaticPower=None,
                 addAfterBoil=None, # TODO: This seems to be an artifact from another source but isn't stored in JSON.
                 mashed=None,
                 notes=None,
                 phi=None,
                 bi=None):
        self.recipe = recipe
        self.name: str = name
        self.amount: Union[MassType, VolumeType] = amount
        self.ftype: str = ftype
        self.group: str = group
        self.producer: str = producer
        self.origin: str = origin
        self.fyield: PercentType = fyield
        self.color: ColorType = color
        self.moisture: PercentType = moisture
        self.diastaticPower: DiastaticPowerType = diastaticPower
        self.addAfterBoil: bool = addAfterBoil
        self.mashed: bool = mashed
        self.notes: str = notes.replace('\\n', '\n') if notes else ''

        # These attributes are NOT part of the BeerJSON format but are in the Excel database of grains to support pH
        # calculations.  They are separate from the other attributes to denote this.  They have been added to the
        # BeerJSON output from this tool and therefore make the output non-standard.  Because of this they are also
        # optional and no error is thrown when they are missing from input times.  pH calculations will not be as
        # accurate without them but reasonable defaults will be assumed.
        self._phi = phi
        self._bi = bi


# ======================================================================================================================
# Properties
# ----------------------------------------------------------------------------------------------------------------------
    @property
    def proportion(self) -> PercentType:
        """Returns a PercentType representing this fermentable's proportion within it's associated recipe."""
        percent = 0
        if self.recipe is not None:
            total = sum([fermentable.amount.lb for fermentable in self.recipe.fermentables])
            if total != 0:
                percent = self.amount.lb / total * 100
        return PercentType(percent, '%')


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def isMashed(self) -> bool:
        """Returns a Boolean indicating if this fermentable is mashed and therefor affected by mash efficiency."""
        return self.ftype.lower() == 'grain'


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def isFermentable(self) -> bool:
        """Returns a Boolean indicating if this fermentable is actually fermentable.  Certain sugars such as lactose or
        Splenda are sweet, but do not ferment.

        Unfortunately there is no field in BeerJSON to handle if an ingredient is fermentable so we are forced to
        maintain a magical list of names here in an attempt to best guess if the provided item is fermentable.  This is
        obviously fragile as it would be as simple as editing the name of an ingredient to put it into or take it off
        of this last.
        """
        nonFermentable = [
            'lactose',
            'xylitol',
            'erythritol',
            'stevia',
            'splenda',
            'maltodextrin'
        ]

        # Walk through the blacklist and compare it to the name of this fermentable.
        for item in nonFermentable:
            # If we find a match, then lets assume that this item is NOT fermentable.
            if item in self.name.lower():
                return False

        # Lets assume that everything else is indeed fermentable.
        return True


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def sucrose(self) -> float:
        """Returns the equivalent amount of sucrose in this fermentable."""
        sucrose = self.amount.lb * (self.fyield.percent / 100) * (1 - (self.moisture.percent / 100))

        # "Mashed" (i.e. grain type) but not mashed, then it must be steeped - reduce the yield by 40%.
        if self.isMashed and not self.mashed:
            sucrose *= 0.6

        return sucrose


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def phi(self) -> float:
        """Calculates the pH component that this fermentable contributes to a distilled water mash."""
        if self._phi is not None:
            # If a pH_i value is explicitly defined in the database then just return that.
            return self._phi

        # If not explicitly specified then try to determine a reasonable default for this grain.
        if not self.isMashed or (self.mashed is not None and not self.mashed):
            # Non-mashed ingredients will have no contribution.
            return 0

        srm = self.color.SRM
        if srm > 300:
            # Roasted malts take priority.
            return 4.64

        if 'wheat' in self.name.lower():
            # Wheat malts can be safely assumed as fixed.
            return 5.97

        if self.group == 'Caramel':
            # Crystal malts vary wildly by color and therefore pH.
            if srm < 5:
                return 5.71
            elif srm < 15:
                return 5.26
            elif srm < 30:
                return 5.15
            elif srm < 50:
                return 4.89
            elif srm < 70:
                return 4.81
            elif srm < 100:
                return 4.74
            elif srm < 130:
                return 4.68
            else:
                return 4.48

        # Assume that everything else is more or less a base malt and use it's color to make an estimate.
        if srm < 2.5:
            # Light Base
            return 5.72
        elif srm < 30:
            # Medium Base
            return 5.69
        else:
            # Toasted
            return 5.39


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def bi(self):
        """Calculates the buffering capacity for this grain.  If not explicitly known, a rough estimate is provided
        based upon the grain type."""
        if self._bi is not None:
            # If the value was explicitly stated in the database then use that.
            return self._bi

        # If not explicitly specified then try to determine a reasonable default for this grain.
        if not self.isMashed:
            # Non-mashed ingredients will have no contribution.
            return 0

        srm = self.color.SRM
        if srm > 300:
            # Roasted malts take priority.
            return 68.7

        if 'wheat' in self.name.lower():
            # Wheat malts can be safely assumed as fixed.
            return 34.8

        if self.group == 'Caramel':
            # Crystal malts vary wildly by color and therefore pH.
            if srm < 5:
                return 34.8
            elif srm < 15:
                return 49.3
            elif srm < 30:
                return 54.5
            elif srm < 50:
                return 65
            elif srm < 70:
                return 68.3
            elif srm < 100:
                return 74
            elif srm < 130:
                return 77
            else:
                return 89.1

        # Assume that everything else is more or less a base malt and use it's color to make an estimate.
        if srm < 2.5:
            # Light Base
            return 45.5
        elif srm < 30:
            # Medium Base
            return 52.3
        else:
            # Toasted
            return 55.1




# ======================================================================================================================
# Methods
# ----------------------------------------------------------------------------------------------------------------------
    def copy(self, recipe):
        return Fermentable(
            recipe=recipe,
            name=self.name,
            amount=self.amount.copy() if self.amount is not None else None,
            ftype=self.ftype,
            group=self.group,
            producer=self.producer,
            origin=self.origin,
            fyield=self.fyield.copy(),
            color=self.color.copy(),
            moisture=self.moisture.copy(),
            diastaticPower=self.diastaticPower.copy(),
            addAfterBoil=self.addAfterBoil,
            mashed=self.mashed,
            notes=self.notes,
            phi=self._phi,
            bi=self._bi,
        )


# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self) -> dict:
        """Convert this fermentable into a Python dictionary that can be used in assembling a BeerJSON format file.

        Returns a BeerJSON FermentableType compatible dictionary."""
        data = {
            'name': self.name,
            'type': self.ftype.lower(),
            'origin': self.origin,
            'producer': self.producer,
            'yield': {
                'fine_grind': self.fyield.to_dict(),
            },
            'color': self.color.to_dict(),
            'amount': self.amount.to_dict(),
            'notes': self.notes.replace('\n', '\\n'),
            'moisture': self.moisture.to_dict(),
            'diastatic_power': self.diastaticPower.to_dict(),
            'recommend_mash': self.mashed,
        }
        if self.group is not None:
            data['grain_group'] = self.group.lower()

        # phi and bi are not part of the BeerJSON standard (yet) so don't include them unless they are set.
        if self._phi is not None:
            data['phi'] = self._phi
        if self._bi is not None:
            data['bi'] = self._bi

        return data


# ----------------------------------------------------------------------------------------------------------------------
    def from_dict(self, data: dict):
        self.name = data['name']
        amount = data['amount']
        self.amount = Selections.one_of(amount['value'], amount['unit'], VolumeType, MassType)
        self.ftype = data['type'].title()
        if 'grain_group' in data:
            self.group = data['grain_group'].title()
        self.producer = data['producer']
        self.origin = data['origin']
        self.color = ColorType(json=data['color'])
        self.moisture = PercentType(json=data['moisture'])
        self.diastaticPower = DiastaticPowerType(json=data['diastatic_power'])
        self.fyield = PercentType(json=data['yield']['fine_grind'])
        self.mashed = data['recommend_mash']
        self.notes = data['notes'].replace('\\n', '\n')

        # phi and bi are not a part of the BeerJSON standard so don't worry if they are missing.
        self._phi = data.get('phi')
        self._bi = data.get('bi')



# ======================================================================================================================
# Overridden Methods
# ----------------------------------------------------------------------------------------------------------------------
    def __repr__(self):
        text = '<Fermentable'
        for key, value in self.__dict__.items():
            text += f' {key}="{value}"'
        text += '>'
        return text



# End of File
