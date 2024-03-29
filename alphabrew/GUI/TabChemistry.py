# ======================================================================================================================
#        File:  GUI/TabChemistry.py
#     Project:  AlphaBrew
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

from GUI.Base.TabChemistry import Ui_TabChemistry
from Model.MeasurableUnits import ConcentrationType, MassType, VolumeType
from Model.Timing import TimingType
from Model.Miscellaneous import Miscellaneous



# ======================================================================================================================
# Chemistry Tab Class
# ----------------------------------------------------------------------------------------------------------------------
class TabChemistry(QtWidgets.QWidget):
    """Extends the MainWindow Salt tab widget containing a subset of controls specific to miscellaneous in the
    recipe."""

    def __init__(self, parent, recipe):
        super().__init__(parent)
        self.ui = Ui_TabChemistry()
        self.ui.setupUi(self)

        # Store the recipe with which these misc items are associated.
        self.recipe = recipe
        self.recipe.changed.connect(self.recalculate)
        self.recipe.loaded.connect(self.activated)

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

        self.ui.phosphoric.valueChanged.connect(self.update_recipe_acids)
        self.ui.lactic.valueChanged.connect(self.update_recipe_acids)
        self.ui.acidMalt.valueChanged.connect(self.update_recipe_acids)

        self.setup_recommendations()
        self.activated()




# ======================================================================================================================
# Methods
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
    def activated(self):
        """Called by the MainWindow when this tab is selected by the user.  This provides an opportunity for us to
        update the salts from the recipe.  That way, if changes were made on the misc tab, they will be reflected here
        without a circular update.

        Populate and run the calculations for the salt addition spin boxes from the recipe."""
        def load_simple_type(items: dict, name: str, unit: str):
            """Helper to extract the mass amount for a given salt by name and return it's decimal value."""
            if name not in items:
                return 0
            item = items[name]
            return item.amount.as_(unit)

        mash = self._list_to_dict(self.recipe.misc.mashSalts)
        self.ui.cacl2_mash.setValue(load_simple_type(mash, 'Calcium Chloride', 'g'))
        self.ui.caso4_mash.setValue(load_simple_type(mash, 'Calcium Sulfate', 'g'))
        self.ui.mgcl2_mash.setValue(load_simple_type(mash, 'Magnesium Chloride', 'g'))
        self.ui.mgso4_mash.setValue(load_simple_type(mash, 'Magnesium Sulfate', 'g'))
        self.ui.nacl_mash.setValue(load_simple_type(mash, 'Sodium Chloride', 'g'))
        self.ui.nahco3_mash.setValue(load_simple_type(mash, 'Sodium Bicarbonate', 'g'))
        self.ui.caoh2_mash.setValue(load_simple_type(mash, 'Calcium Hydroxide', 'g'))

        kettle = self._list_to_dict(self.recipe.misc.kettleSalts)
        self.ui.cacl2_kettle.setValue(load_simple_type(kettle, 'Calcium Chloride', 'g'))
        self.ui.caso4_kettle.setValue(load_simple_type(kettle, 'Calcium Sulfate', 'g'))
        self.ui.mgcl2_kettle.setValue(load_simple_type(kettle, 'Magnesium Chloride', 'g'))
        self.ui.mgso4_kettle.setValue(load_simple_type(kettle, 'Magnesium Sulfate', 'g'))
        self.ui.nacl_kettle.setValue(load_simple_type(kettle, 'Sodium Chloride', 'g'))
        self.ui.nahco3_kettle.setValue(load_simple_type(kettle, 'Sodium Bicarbonate', 'g'))
        self.ui.caoh2_kettle.setValue(load_simple_type(kettle, 'Calcium Hydroxide', 'g'))

        acids = self._list_to_dict(self.recipe.misc.acids)
        self.ui.lactic.setValue(load_simple_type(acids, 'Lactic Acid', 'ml'))
        self.ui.phosphoric.setValue(load_simple_type(acids, 'Phosphoric Acid', 'ml'))

        # TODO: This is a little bit quirky.  There are actually a few malts that are specifically acidic and this
        # tool is currently attempting to keep track of them.  To make things a little easier, this just tallies them
        # and re-runs calculations.  The acidic grains must be added to the fermentables tab by the user.
        grains = self._list_to_dict(self.recipe.fermentables)
        acidMalts = load_simple_type(grains, 'Acid Malt', 'oz')
        acidMalts += load_simple_type(grains, 'Acidulated Malt', 'oz')
        self.ui.acidMalt.setValue(acidMalts)

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
        """Connected to the input boxes to recalculate the water chemistry whenever the inputs change.

        This method only updates te read-only, calculated properties of the tab - it does not update any of the user
        input boxes.

        It is intended as a response to user input, and does not trigger actions deliberately to prevent circular
        updates."""

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
        calciumMash /= self.recipe.strikeVolume.liters
        calciumMash += calciumWater

        magnesiumMash = ConcentrationType(0.12 * self.ui.mgcl2_mash.value() * 1000, 'ppm')
        magnesiumMash += ConcentrationType(0.099 * self.ui.mgso4_mash.value() * 1000, 'ppm')
        magnesiumMash /= self.recipe.strikeVolume.liters
        magnesiumMash += magnesiumWater

        sodiumMash = ConcentrationType(0.393 * self.ui.nacl_mash.value() * 1000, 'ppm')
        sodiumMash += ConcentrationType(0.274 * self.ui.nahco3_mash.value() * 1000, 'ppm')
        sodiumMash /= self.recipe.strikeVolume.liters
        sodiumMash += sodiumWater

        chlorideMash = ConcentrationType(0.482 * self.ui.cacl2_mash.value() * 1000, 'ppm')
        chlorideMash += ConcentrationType(0.349 * self.ui.mgcl2_mash.value() * 1000, 'ppm')
        chlorideMash += ConcentrationType(0.607 * self.ui.nacl_mash.value() * 1000, 'ppm')
        chlorideMash /= self.recipe.strikeVolume.liters
        chlorideMash += chlorideWater

        sulfateMash = ConcentrationType(0.558 * self.ui.caso4_mash.value() * 1000, 'ppm')
        sulfateMash += ConcentrationType(0.39 * self.ui.mgso4_mash.value() * 1000, 'ppm')
        sulfateMash /= self.recipe.strikeVolume.liters
        sulfateMash += sulfateWater

        bicarbonateMash = ConcentrationType(0.726 * self.ui.nahco3_mash.value() * 1000, 'ppm')
        bicarbonateMash /= self.recipe.strikeVolume.liters
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
        calciumKettle /= self.recipe.spargeVolume.liters
        calciumKettle += calciumWater

        magnesiumKettle = ConcentrationType(0.12 * self.ui.mgcl2_kettle.value() * 1000, 'ppm')
        magnesiumKettle += ConcentrationType(0.099 * self.ui.mgso4_kettle.value() * 1000, 'ppm')
        magnesiumKettle /= self.recipe.spargeVolume.liters
        magnesiumKettle += magnesiumWater

        sodiumKettle = ConcentrationType(0.393 * self.ui.nacl_kettle.value() * 1000, 'ppm')
        sodiumKettle += ConcentrationType(0.274 * self.ui.nahco3_kettle.value() * 1000, 'ppm')
        sodiumKettle /= self.recipe.spargeVolume.liters
        sodiumKettle += sodiumWater

        chlorideKettle = ConcentrationType(0.482 * self.ui.cacl2_kettle.value() * 1000, 'ppm')
        chlorideKettle += ConcentrationType(0.349 * self.ui.mgcl2_kettle.value() * 1000, 'ppm')
        chlorideKettle += ConcentrationType(0.607 * self.ui.nacl_kettle.value() * 1000, 'ppm')
        chlorideKettle /= self.recipe.spargeVolume.liters
        chlorideKettle += chlorideWater

        sulfateKettle = ConcentrationType(0.558 * self.ui.caso4_kettle.value() * 1000, 'ppm')
        sulfateKettle += ConcentrationType(0.39 * self.ui.mgso4_kettle.value() * 1000, 'ppm')
        sulfateKettle /= self.recipe.spargeVolume.liters
        sulfateKettle += sulfateWater

        bicarbonateKettle = ConcentrationType(0.726 * self.ui.nahco3_kettle.value() * 1000, 'ppm')
        bicarbonateKettle /= self.recipe.spargeVolume.liters
        bicarbonateKettle += bicarbonateWater

        # Update the UI totals for the kettle contributions.
        self.ui.spargeCalcium.setText(str(calciumKettle))
        self.ui.spargeMagnesium.setText(str(magnesiumKettle))
        self.ui.spargeSodium.setText(str(sodiumKettle))
        self.ui.spargeChloride.setText(str(chlorideKettle))
        self.ui.spargeSulfate.setText(str(sulfateKettle))
        self.ui.spargeBicarbonate.setText(str(bicarbonateKettle))

        def average(mash, kettle):
            mash *= self.recipe.strikeVolume.gallons
            kettle *= self.recipe.spargeVolume.gallons
            return (mash + kettle) / self.recipe.boilVolume.gallons

        # Total up everything
        calcium = average(calciumMash, calciumKettle)
        magnesium = average(magnesiumMash, magnesiumKettle)
        sodium = average(sodiumMash, sodiumKettle)
        chloride = average(chlorideMash, chlorideKettle)
        sulfate = average(sulfateMash, sulfateKettle)
        bicarbonate = average(bicarbonateMash, bicarbonateKettle)

        # Update the output UI boxes and sliders.
        self.ui.calcium.setText(str(calcium))
        self.ui.calciumSlide.setValue(calcium.ppm)
        self.ui.magnesium.setText(str(magnesium))
        self.ui.magnesiumSlide.setValue(magnesium.ppm)
        self.ui.sodium.setText(str(sodium))
        self.ui.sodiumSlide.setValue(sodium.ppm)
        self.ui.chloride.setText(str(chloride))
        self.ui.chlorideSlide.setValue(chloride.ppm)
        self.ui.sulfate.setText(str(sulfate))
        self.ui.sulfateSlide.setValue(sulfate.ppm)
        self.ui.bicarbonate.setText(str(bicarbonate))
        self.ui.bicarbonateSlide.setValue(bicarbonate.ppm)

        # Change the slider color if any of the values go out of range.
        errorStyle = "QSlider::handle:horizontal {background-color: red;}"
        resetStyle = "QSlider::handle:horizontal {}"

        if calcium.ppm < 50 or calcium.ppm > 150:
            self.ui.calciumSlide.setStyleSheet(errorStyle)
        else:
            self.ui.calciumSlide.setStyleSheet(resetStyle)

        if magnesium.ppm < 10 or magnesium.ppm > 30:
            self.ui.magnesiumSlide.setStyleSheet(errorStyle)
        else:
            self.ui.magnesiumSlide.setStyleSheet(resetStyle)

        if sodium.ppm > 150:
            self.ui.sodiumSlide.setStyleSheet(errorStyle)
        else:
            self.ui.sodiumSlide.setStyleSheet(resetStyle)

        if chloride.ppm > 250:
            self.ui.chlorideSlide.setStyleSheet(errorStyle)
        else:
            self.ui.chlorideSlide.setStyleSheet(resetStyle)

        if sulfate.ppm < 50 or sulfate.ppm > 350:
            self.ui.sulfateSlide.setStyleSheet(errorStyle)
        else:
            self.ui.sulfateSlide.setStyleSheet(resetStyle)

        if bicarbonate.ppm > 250:
            self.ui.bicarbonateSlide.setStyleSheet(errorStyle)
        else:
            self.ui.bicarbonateSlide.setStyleSheet(resetStyle)



        strikeL = self.recipe.strikeVolume.liters

        # Strength is fixed in this tool as 10% phosphoric seems pretty typical.
        phosphoricStrength = 0.1
        phosphoricVolume = self.ui.phosphoric.value()
        phosphoricDensity = 1 + (0.49 * phosphoricStrength) + ((0.375 * phosphoricStrength) ** 2)
        phosphoricAlkalinity = -phosphoricStrength * phosphoricDensity / 98 * 1000 * phosphoricVolume / strikeL

        # Strength is fixed in this tool as 88% lactic seems pretty typical.
        lacticStrength = 0.88
        lacticVolume = self.ui.lactic.value()
        lacticDensity = 1 + (0.237 * lacticStrength)
        lacticAlkalinity = -lacticStrength * lacticDensity / 90.09 * 1000 * lacticVolume / strikeL

        acidMaltStrength = 0.03
        actiMaltMass = self.ui.acidMalt.value() # oz
        acidMaltAlkalinity = -acidMaltStrength * actiMaltMass * 28.35 / 90.09 / strikeL * 1000

        bicarbonateNorm = bicarbonateMash.ppm / 61.016
        carbonateNorm = 2 * self.recipe.waters.carbonate.ppm / 60.008
        cAlkalinity = bicarbonateNorm + carbonateNorm

        mashHardness = self.recipe.waters.hardness + (self.ui.nahco3_mash.value() / 61.016 / strikeL * 1000)
        calciumNorm = 2 * calciumMash.ppm / 40.078
        magnesiumNorm = 2 * magnesiumMash.ppm / 24.305

        hydroxide = 0.459 * self.ui.caoh2_mash.value() * 1000 / strikeL
        hydroxideNorm = hydroxide / 17.007

        phRaSlope = self.recipe.mash.ratio.litersPerKilogram / self.recipe.fermentables.mashBiFi
        phRaSlopeCorrected = phRaSlope / self.recipe.calibrations.maltBufferingCorrectionFactor

        def calculate_ph(ph, salts=True, acids=True):
            """Run a single iteration of the pH calculations.  The optional arguments will run the calculations using
            inputs from salts and acids, respectively, when True."""
            for _ in range(25):
                fph = 1
                fph += 4.435e-7 * (10 ** ph)
                fph += 4.435e-7 * 4.667e-11 * (10 ** (2 * ph))
                fph /= 4.435e-7 * (10 ** ph)

                zra = cAlkalinity
                zra -= mashHardness / fph
                zra -= calciumNorm / 2.8
                zra -= magnesiumNorm / 5.6
                if acids:
                    zra += phosphoricAlkalinity
                    zra += lacticAlkalinity
                    zra += acidMaltAlkalinity
                if salts:
                    zra += hydroxideNorm

                ph = self.recipe.fermentables.mashPh + phRaSlopeCorrected * zra

            return ph

        ph = calculate_ph(self.recipe.fermentables.mashPh)
        self.ui.ph.setText(f'{ph:.2f}')
        self.ui.phSlide.setValue(ph * 100)
        if ph < 5.2 or ph > 5.6:
            self.ui.phSlide.setStyleSheet(errorStyle)
        else:
            self.ui.phSlide.setStyleSheet(resetStyle)

        # Calculate the chloride to sulfate ratio.
        try:
            ratio = chloride.ppm / sulfate.ppm
        except ZeroDivisionError:
            ratio = 0
        self.ui.ratio.setText(f'{ratio:.2f}')
        self.ui.ratioSlide.setValue(ratio * 100)


# ----------------------------------------------------------------------------------------------------------------------
    def update_recipe_salts(self):
        """Update that salts in the actual recipe in response to a change in one of the input boxes."""

        def updateSalt(name, value, use, salts):
            """Local helper function to assist with the salt updates.  Handles both the mash and kettle salts."""
            if value > 0:
                # If there is a value greater than zero, then we want to update this misc ingredient amount.
                mass = MassType(value, 'g')
                if name in salts:
                    # Salt already exists, lets just update the value.
                    salts[name].amount = mass
                else:
                    # Salt does not yet exist, need to add it as a new misc ingredient.
                    timing = TimingType(use=use)
                    misc = Miscellaneous(self.recipe, name, 'Water Agent', timing=timing, amount=mass)
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

        self.recalculate()


# ----------------------------------------------------------------------------------------------------------------------
    def update_recipe_acids(self):
        """Update that acids in the actual recipe in response to a change in one of the input boxes."""

        def updateAcid(name, value, acids):
            """Local helper function to assist with the acid updates."""
            if value > 0:
                # If there is a value greater than zero, then we want to update this misc ingredient amount.
                volume = VolumeType(value, 'ml')
                if name in acids:
                    # Salt already exists, lets just update the value.
                    acids[name].amount = volume
                else:
                    # Salt does not yet exist, need to add it as a new misc ingredient.
                    timing = TimingType(use='Mash')
                    misc = Miscellaneous(self.recipe, name, 'Water Agent', timing=timing, amount=volume)
                    self.recipe.misc.append(misc)
            else:
                # Value has been made zero.
                if name in acids:
                    # If there was previously an entry, remove it from the ingredient list now.
                    self.recipe.misc.pop(self.recipe.misc.indexOf(acids[name]))

        acids = self._list_to_dict(self.recipe.misc.acids)
        updateAcid('Phosphoric Acid', self.ui.phosphoric.value(), acids)
        updateAcid('Lactic Acid', self.ui.lactic.value(), acids)

        self.recalculate()



# ======================================================================================================================
# Private Functions
# ----------------------------------------------------------------------------------------------------------------------
    def _list_to_dict(self, items):
        """Convert a list of items (salts or acids) into a dict of items combining items by name."""
        output = {}
        for item in items:
            if item.name not in output:
                output[item.name] = item
            else:
                output[item.name].amount += item.amount
        return output



# End of File
