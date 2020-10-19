# ======================================================================================================================
#        File:  GUI/TabSalts.py
#     Project:  Brewing Recipe Planner
# Description:  Extensions and functionality for the main GUI window.
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
# Import Statements
# ----------------------------------------------------------------------------------------------------------------------
from PySide2 import QtWidgets

from GUI.Base.TabSalts import Ui_TabSalts
from Model.MeasurableUnits import ConcentrationType, MassType
from Model.Timing import TimingType
from Model.Miscellaneous import Miscellaneous



# ======================================================================================================================
# Salt Tab Class
# ----------------------------------------------------------------------------------------------------------------------
class TabSalts(QtWidgets.QWidget):
    """Extends the MainWindow Salt tab widget containing a subset of controls specific to miscellaneous in the
    recipe."""

    def __init__(self, parent, recipe):
        super().__init__(parent)
        self.ui = Ui_TabSalts()
        self.ui.setupUi(self)

        # Store the recipe with which these misc items are associated.
        self.recipe = recipe
        self.recipe.changed.connect(self.recalculate)
        self.recipe.loaded.connect(self.setup_salt_additions)

        # Connect event handlers for each of the input boxes to trigger recalculation.
        self.ui.cacl2_mash.valueChanged.connect(self.update_recipe_salts)
        self.ui.caso4_mash.valueChanged.connect(self.update_recipe_salts)
        self.ui.mgcl2_mash.valueChanged.connect(self.update_recipe_salts)
        self.ui.mgso4_mash.valueChanged.connect(self.update_recipe_salts)
        self.ui.nacl_mash.valueChanged.connect(self.update_recipe_salts)
        self.ui.nahco3_mash.valueChanged.connect(self.update_recipe_salts)
        self.ui.caoh2_mash.valueChanged.connect(self.update_recipe_salts)
        self.ui.cacl2_kettle.valueChanged.connect(self.update_recipe_salts)
        self.ui.caso4_kettle.valueChanged.connect(self.update_recipe_salts)
        self.ui.mgcl2_kettle.valueChanged.connect(self.update_recipe_salts)
        self.ui.mgso4_kettle.valueChanged.connect(self.update_recipe_salts)
        self.ui.nacl_kettle.valueChanged.connect(self.update_recipe_salts)
        self.ui.nahco3_kettle.valueChanged.connect(self.update_recipe_salts)
        self.ui.caoh2_kettle.valueChanged.connect(self.update_recipe_salts)

        self.ui.phosphoric.valueChanged.connect(self.recalculate)
        self.ui.lactic.valueChanged.connect(self.recalculate)
        self.ui.acidMalt.valueChanged.connect(self.recalculate)

        self.setup_recommendations()
        self.setup_salt_additions()




# ======================================================================================================================
# Setup Methods
# ----------------------------------------------------------------------------------------------------------------------
    def setup_recommendations(self):
        """Sets up the dropdowns and values in the recommendation box."""
        # Setup the available yes/no options for the pale color, hop forward, and hazy prompt drop downs.
        for option in ['No', 'Yes']:
            self.ui.pale.addItem(option)
            self.ui.hopForward.addItem(option)
            self.ui.hazeDesired.addItem(option)

        # Setup the values and selection for the body dropdown.
        for option in ['High', 'Medium', 'Low']:
            self.ui.body.addItem(option)
        self.ui.body.setCurrentText('Medium')

        # Attach event handlers to the inputs to recalculate when the value changes.
        self.ui.pale.currentIndexChanged.connect(self.recommend)
        self.ui.body.currentIndexChanged.connect(self.recommend)
        self.ui.hopForward.currentIndexChanged.connect(self.recommend)
        self.ui.hazeDesired.currentIndexChanged.connect(self.recommend)

        # Run the calculations once based upon the initial values.
        self.recommend()


# ----------------------------------------------------------------------------------------------------------------------
    def setup_salt_additions(self):
        """Populate and run the calculations for the salt addition spin boxes from the recipe."""
        def load_mass(salts, name):
            """Helper to extract the mass amount for a given salt by name and return it's decimal value."""
            if name not in salts:
                return 0
            salt = salts[name]
            return salt.amount.as_('g')

        mash = self._list_to_dict(self.recipe.misc.mashSalts)
        self.ui.cacl2_mash.setValue(load_mass(mash, 'Calcium Chloride'))
        self.ui.caso4_mash.setValue(load_mass(mash, 'Calcium Sulfate'))
        self.ui.mgcl2_mash.setValue(load_mass(mash, 'Magnesium Chloride'))
        self.ui.mgso4_mash.setValue(load_mass(mash, 'Magnesium Sulfate'))
        self.ui.nacl_mash.setValue(load_mass(mash, 'Sodium Chloride'))
        self.ui.nahco3_mash.setValue(load_mass(mash, 'Sodium Bicarbonate'))
        self.ui.caoh2_mash.setValue(load_mass(mash, 'Calcium Hydroxide'))

        kettle = self._list_to_dict(self.recipe.misc.kettleSalts)
        self.ui.cacl2_kettle.setValue(load_mass(kettle, 'Calcium Chloride'))
        self.ui.caso4_kettle.setValue(load_mass(kettle, 'Calcium Sulfate'))
        self.ui.mgcl2_kettle.setValue(load_mass(kettle, 'Magnesium Chloride'))
        self.ui.mgso4_kettle.setValue(load_mass(kettle, 'Magnesium Sulfate'))
        self.ui.nacl_kettle.setValue(load_mass(kettle, 'Sodium Chloride'))
        self.ui.nahco3_kettle.setValue(load_mass(kettle, 'Sodium Bicarbonate'))
        self.ui.caoh2_kettle.setValue(load_mass(kettle, 'Calcium Hydroxide'))

        # TODO: Load acids from recipe.

        # Run the calculations once to generate an initial set of values.
        self.recalculate()



# ======================================================================================================================
# Event Handlers
# ----------------------------------------------------------------------------------------------------------------------
    def recommend(self):
        """Called whenever the user changes any of the recommendation dropdowns allowing the recommended pH value to be
        recalculated.

        The maths for the suggestions here were taken verbatim from BrewCipher.  I don't really know if they are good
        suggestions (up or down a tenth of a point for the differnet questions) but they are certainly better than what
        had to work with previously.
         """
        palest = self.ui.pale.currentText() == 'Yes'
        body = self.ui.body.currentText()
        hopForward = self.ui.hopForward.currentText() == 'Yes'
        hazeDesired = self.ui.hazeDesired.currentText() == 'Yes'

        ph = 5.4
        ph += -0.1 if palest else 0.05
        ph += 0.1 if body == 'High' else -0.1 if body == 'Low' else 0
        ph -= 0.1 if hopForward else 0
        ph += 0.1 if hazeDesired else 0

        self.ui.recommended.setText(f'{ph:.2f}')


# ----------------------------------------------------------------------------------------------------------------------
    def recalculate(self):
        """Connected to the input boxes to recalculate the water chemistry whenever the inputs change."""
        # There is nothing we can calculate here until the strike volume can be calculated.
        if self.recipe.strikeVolume.value == 0:
            return


        # Start with the base water ion concentrations.
        try:
            calciumWater = self.recipe.waters.calcium
            magnesiumWater = self.recipe.waters.magnesium
            sodiumWater = self.recipe.waters.sodium
            chlorideWater = self.recipe.waters.chloride
            sulfateWater = self.recipe.waters.sulfate
            bicarbonateWater = self.recipe.waters.bicarbonate
        except AttributeError:
            # This gets thrown when the recipe information isn't complete enough to calculate ion concentrations.
            return

        # Calculate the ion concentrations for the mash.
        calciumMash = ConcentrationType(0.273 * self.ui.cacl2_mash.value() * 1000, 'ppm')
        calciumMash += ConcentrationType(0.233 * self.ui.caso4_mash.value() * 1000, 'ppm')
        calciumMash += ConcentrationType(0.541 * self.ui.caoh2_mash.value() * 1000, 'ppm')
        calciumMash /= self.recipe.strikeVolume.as_('l')
        calciumMash += calciumWater

        magnesiumMash = ConcentrationType(0.12 * self.ui.mgcl2_mash.value() * 1000, 'ppm')
        magnesiumMash += ConcentrationType(0.099 * self.ui.mgso4_mash.value() * 1000, 'ppm')
        magnesiumMash /= self.recipe.strikeVolume.as_('l')
        magnesiumMash += magnesiumWater

        sodiumMash = ConcentrationType(0.393 * self.ui.nacl_mash.value() * 1000, 'ppm')
        sodiumMash += ConcentrationType(0.274 * self.ui.nahco3_mash.value() * 1000, 'ppm')
        sodiumMash /= self.recipe.strikeVolume.as_('l')
        sodiumMash += sodiumWater

        chlorideMash = ConcentrationType(0.482 * self.ui.cacl2_mash.value() * 1000, 'ppm')
        chlorideMash += ConcentrationType(0.349 * self.ui.mgcl2_mash.value() * 1000, 'ppm')
        chlorideMash += ConcentrationType(0.607 * self.ui.nacl_mash.value() * 1000, 'ppm')
        chlorideMash /= self.recipe.strikeVolume.as_('l')
        chlorideMash += chlorideWater

        sulfateMash = ConcentrationType(0.558 * self.ui.caso4_mash.value() * 1000, 'ppm')
        sulfateMash += ConcentrationType(0.39 * self.ui.mgso4_mash.value() * 1000, 'ppm')
        sulfateMash /= self.recipe.strikeVolume.as_('l')
        sulfateMash += sulfateWater

        bicarbonateMash = ConcentrationType(0.726 * self.ui.nahco3_mash.value() * 1000, 'ppm')
        bicarbonateMash /= self.recipe.strikeVolume.as_('l')
        bicarbonateMash += bicarbonateWater

        # Update the UI totals for the mash contributions.
        self.ui.strikeCalcium.setText(str(calciumMash))
        self.ui.strikeMagnesium.setText(str(magnesiumMash))
        self.ui.strikeSodium.setText(str(sodiumMash))
        self.ui.strikeChloride.setText(str(chlorideMash))
        self.ui.strikeSulfate.setText(str(sulfateMash))
        self.ui.strikeBicarbonate.setText(str(bicarbonateMash))

        # Calculate the ion concentrations for the kettle.
        calciumKettle = ConcentrationType(0.273 * self.ui.cacl2_kettle.value() * 1000, 'ppm')
        calciumKettle += ConcentrationType(0.233 * self.ui.caso4_kettle.value() * 1000, 'ppm')
        calciumKettle += ConcentrationType(0.541 * self.ui.caoh2_kettle.value() * 1000, 'ppm')
        calciumKettle /= self.recipe.spargeVolume.as_('l')
        calciumKettle += calciumWater

        magnesiumKettle = ConcentrationType(0.12 * self.ui.mgcl2_kettle.value() * 1000, 'ppm')
        magnesiumKettle += ConcentrationType(0.099 * self.ui.mgso4_kettle.value() * 1000, 'ppm')
        magnesiumKettle /= self.recipe.spargeVolume.as_('l')
        magnesiumKettle += magnesiumWater

        sodiumKettle = ConcentrationType(0.393 * self.ui.nacl_kettle.value() * 1000, 'ppm')
        sodiumKettle += ConcentrationType(0.274 * self.ui.nahco3_kettle.value() * 1000, 'ppm')
        sodiumKettle /= self.recipe.spargeVolume.as_('l')
        sodiumKettle += sodiumWater

        chlorideKettle = ConcentrationType(0.482 * self.ui.cacl2_kettle.value() * 1000, 'ppm')
        chlorideKettle += ConcentrationType(0.349 * self.ui.mgcl2_kettle.value() * 1000, 'ppm')
        chlorideKettle += ConcentrationType(0.607 * self.ui.nacl_kettle.value() * 1000, 'ppm')
        chlorideKettle /= self.recipe.spargeVolume.as_('l')
        chlorideKettle += chlorideWater

        sulfateKettle = ConcentrationType(0.558 * self.ui.caso4_kettle.value() * 1000, 'ppm')
        sulfateKettle += ConcentrationType(0.39 * self.ui.mgso4_kettle.value() * 1000, 'ppm')
        sulfateKettle /= self.recipe.spargeVolume.as_('l')
        sulfateKettle += sulfateWater

        bicarbonateKettle = ConcentrationType(0.726 * self.ui.nahco3_kettle.value() * 1000, 'ppm')
        bicarbonateKettle /= self.recipe.spargeVolume.as_('l')
        bicarbonateKettle += bicarbonateWater

        # Update the UI totals for the kettle contributions.
        self.ui.spargeCalcium.setText(str(calciumKettle))
        self.ui.spargeMagnesium.setText(str(magnesiumKettle))
        self.ui.spargeSodium.setText(str(sodiumKettle))
        self.ui.spargeChloride.setText(str(chlorideKettle))
        self.ui.spargeSulfate.setText(str(sulfateKettle))
        self.ui.spargeBicarbonate.setText(str(bicarbonateKettle))

        def average(mash, kettle):
            mash *= self.recipe.strikeVolume.as_('gal')
            kettle *= self.recipe.spargeVolume.as_('gal')
            return (mash + kettle) / self.recipe.boilSize.as_('gal')

        # Total up everything
        calcium = average(calciumMash, calciumKettle)
        magnesium = average(magnesiumMash, magnesiumKettle)
        sodium = average(sodiumMash, sodiumKettle)
        chloride = average(chlorideMash, chlorideKettle)
        sulfate = average(sulfateMash, sulfateKettle)
        bicarbonate = average(bicarbonateMash, bicarbonateKettle)

        # Update the output UI boxes and sliders.
        self.ui.calcium.setText(str(calcium))
        self.ui.calciumSlide.setValue(calcium.as_('ppm'))
        self.ui.magnesium.setText(str(magnesium))
        self.ui.magnesiumSlide.setValue(magnesium.as_('ppm'))
        self.ui.sodium.setText(str(sodium))
        self.ui.sodiumSlide.setValue(sodium.as_('ppm'))
        self.ui.chloride.setText(str(chloride))
        self.ui.chlorideSlide.setValue(chloride.as_('ppm'))
        self.ui.sulfate.setText(str(sulfate))
        self.ui.sulfateSlide.setValue(sulfate.as_('ppm'))
        self.ui.bicarbonate.setText(str(bicarbonate))
        self.ui.bicarbonateSlide.setValue(bicarbonate.as_('ppm'))


# ----------------------------------------------------------------------------------------------------------------------
    def update_recipe_salts(self):
        """Update that salts in the actual recipe in response to a change in one of the input boxes."""

        def updateSalt(name, value, use, salts):
            """Local helper function to assist with the sale updates.  Handles both the mash and kettle salts."""
            if value > 0:
                # If there is a value greater than zero, then we want to update this misc ingredient amount.
                mass = MassType(value, 'g')
                if name in salts:
                    # Salt already exists, lets just update the value.
                    salts[name].amount = mass
                else:
                    # Salt does not yet exist, need to add it as a new misc ingredient.
                    timing = TimingType(use=use)
                    misc = Miscellaneous(self.recipe, name, 'water agent', timing=timing, amount=mass)
                    self.recipe.misc.append(misc)
            else:
                # Value has been made zero.
                if name in salts:
                    # If there was previously an entry, remove it from the ingredient list now.
                    self.recipe.misc.pop(self.recipe.misc.indexOf(salts[name]))

        mashSalts = self._list_to_dict(self.recipe.misc.mashSalts)
        updateSalt('Calcium Chloride', self.ui.cacl2_mash.value(), 'Mash', mashSalts)
        updateSalt('Calcium Sulfate', self.ui.caso4_mash.value(), 'Mash', mashSalts)
        updateSalt('Magnesium Chloride', self.ui.mgcl2_mash.value(), 'Mash', mashSalts)
        updateSalt('Magnesium Sulfate', self.ui.mgso4_mash.value(), 'Mash', mashSalts)
        updateSalt('Sodium Chloride', self.ui.nacl_mash.value(), 'Mash', mashSalts)
        updateSalt('Sodium Bicarbonate', self.ui.nahco3_mash.value(), 'Mash', mashSalts)
        updateSalt('Calcium Hydroxide', self.ui.caoh2_mash.value(), 'Mash', mashSalts)

        kettleSalts = self._list_to_dict(self.recipe.misc.kettleSalts)
        updateSalt('Calcium Chloride', self.ui.cacl2_kettle.value(), 'Boil', kettleSalts)
        updateSalt('Calcium Sulfate', self.ui.caso4_kettle.value(), 'Boil', kettleSalts)
        updateSalt('Magnesium Chloride', self.ui.mgcl2_kettle.value(), 'Boil', kettleSalts)
        updateSalt('Magnesium Sulfate', self.ui.mgso4_kettle.value(), 'Boil', kettleSalts)
        updateSalt('Sodium Chloride', self.ui.nacl_kettle.value(), 'Boil', kettleSalts)
        updateSalt('Sodium Bicarbonate', self.ui.nahco3_kettle.value(), 'Boil', kettleSalts)
        updateSalt('Calcium Hydroxide', self.ui.caoh2_kettle.value(), 'Boil', kettleSalts)



# ======================================================================================================================
# Private Functions
# ----------------------------------------------------------------------------------------------------------------------
    def _list_to_dict(self, salts):
        """Convert a list of salts into a dict of salts combinint items by name."""
        output = {}
        for salt in salts:
            if salt.name not in output:
                output[salt.name] = salt
            else:
                output[salt.name].amount += salt.amount
        return output



# End of File
