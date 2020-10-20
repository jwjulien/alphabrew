# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TabChemistry.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_TabChemistry(object):
    def setupUi(self, TabChemistry):
        if TabChemistry.objectName():
            TabChemistry.setObjectName(u"TabChemistry")
        TabChemistry.resize(898, 546)
        self.verticalLayout = QVBoxLayout(TabChemistry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.group_salts = QGroupBox(TabChemistry)
        self.group_salts.setObjectName(u"group_salts")
        self.gridLayout = QGridLayout(self.group_salts)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.lbl_neutral = QLabel(self.group_salts)
        self.lbl_neutral.setObjectName(u"lbl_neutral")
        self.lbl_neutral.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_neutral, 0, 5, 1, 1)

        self.line_2 = QFrame(self.group_salts)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 1, 1, 4)

        self.line_7 = QFrame(self.group_salts)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_7, 1, 5, 1, 1)

        self.line_8 = QFrame(self.group_salts)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_8, 1, 6, 1, 2)

        self.lbl_cacl2 = QLabel(self.group_salts)
        self.lbl_cacl2.setObjectName(u"lbl_cacl2")
        self.lbl_cacl2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_cacl2, 2, 1, 1, 1)

        self.lbl_caso4 = QLabel(self.group_salts)
        self.lbl_caso4.setObjectName(u"lbl_caso4")
        self.lbl_caso4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_caso4, 2, 2, 1, 1)

        self.lbl_mgcl2 = QLabel(self.group_salts)
        self.lbl_mgcl2.setObjectName(u"lbl_mgcl2")
        self.lbl_mgcl2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_mgcl2, 2, 3, 1, 1)

        self.lbl_mgso4 = QLabel(self.group_salts)
        self.lbl_mgso4.setObjectName(u"lbl_mgso4")
        self.lbl_mgso4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_mgso4, 2, 4, 1, 1)

        self.lbl_nacl = QLabel(self.group_salts)
        self.lbl_nacl.setObjectName(u"lbl_nacl")
        self.lbl_nacl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_nacl, 2, 5, 1, 1)

        self.lbl_nahco3 = QLabel(self.group_salts)
        self.lbl_nahco3.setObjectName(u"lbl_nahco3")
        self.lbl_nahco3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_nahco3, 2, 6, 1, 1)

        self.lbl_caoh2 = QLabel(self.group_salts)
        self.lbl_caoh2.setObjectName(u"lbl_caoh2")
        self.lbl_caoh2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_caoh2, 2, 7, 1, 1)

        self.lbl_mashSalts = QLabel(self.group_salts)
        self.lbl_mashSalts.setObjectName(u"lbl_mashSalts")
        self.lbl_mashSalts.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_mashSalts, 3, 0, 1, 1)

        self.cacl2_mash = QDoubleSpinBox(self.group_salts)
        self.cacl2_mash.setObjectName(u"cacl2_mash")
        self.cacl2_mash.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.cacl2_mash.setDecimals(1)

        self.gridLayout.addWidget(self.cacl2_mash, 3, 1, 1, 1)

        self.caso4_mash = QDoubleSpinBox(self.group_salts)
        self.caso4_mash.setObjectName(u"caso4_mash")
        self.caso4_mash.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.caso4_mash.setDecimals(1)

        self.gridLayout.addWidget(self.caso4_mash, 3, 2, 1, 1)

        self.mgcl2_mash = QDoubleSpinBox(self.group_salts)
        self.mgcl2_mash.setObjectName(u"mgcl2_mash")
        self.mgcl2_mash.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.mgcl2_mash.setDecimals(1)

        self.gridLayout.addWidget(self.mgcl2_mash, 3, 3, 1, 1)

        self.mgso4_mash = QDoubleSpinBox(self.group_salts)
        self.mgso4_mash.setObjectName(u"mgso4_mash")
        self.mgso4_mash.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.mgso4_mash.setDecimals(1)

        self.gridLayout.addWidget(self.mgso4_mash, 3, 4, 1, 1)

        self.nacl_mash = QDoubleSpinBox(self.group_salts)
        self.nacl_mash.setObjectName(u"nacl_mash")
        self.nacl_mash.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.nacl_mash.setDecimals(1)

        self.gridLayout.addWidget(self.nacl_mash, 3, 5, 1, 1)

        self.nahco3_mash = QDoubleSpinBox(self.group_salts)
        self.nahco3_mash.setObjectName(u"nahco3_mash")
        self.nahco3_mash.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.nahco3_mash.setDecimals(1)

        self.gridLayout.addWidget(self.nahco3_mash, 3, 6, 1, 1)

        self.caoh2_mash = QDoubleSpinBox(self.group_salts)
        self.caoh2_mash.setObjectName(u"caoh2_mash")
        self.caoh2_mash.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.caoh2_mash.setDecimals(1)

        self.gridLayout.addWidget(self.caoh2_mash, 3, 7, 1, 1)

        self.lbl_kettleSalts = QLabel(self.group_salts)
        self.lbl_kettleSalts.setObjectName(u"lbl_kettleSalts")
        self.lbl_kettleSalts.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_kettleSalts, 4, 0, 1, 1)

        self.cacl2_kettle = QDoubleSpinBox(self.group_salts)
        self.cacl2_kettle.setObjectName(u"cacl2_kettle")
        self.cacl2_kettle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.cacl2_kettle.setDecimals(1)

        self.gridLayout.addWidget(self.cacl2_kettle, 4, 1, 1, 1)

        self.caso4_kettle = QDoubleSpinBox(self.group_salts)
        self.caso4_kettle.setObjectName(u"caso4_kettle")
        self.caso4_kettle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.caso4_kettle.setDecimals(1)

        self.gridLayout.addWidget(self.caso4_kettle, 4, 2, 1, 1)

        self.mgcl2_kettle = QDoubleSpinBox(self.group_salts)
        self.mgcl2_kettle.setObjectName(u"mgcl2_kettle")
        self.mgcl2_kettle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.mgcl2_kettle.setDecimals(1)

        self.gridLayout.addWidget(self.mgcl2_kettle, 4, 3, 1, 1)

        self.mgso4_kettle = QDoubleSpinBox(self.group_salts)
        self.mgso4_kettle.setObjectName(u"mgso4_kettle")
        self.mgso4_kettle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.mgso4_kettle.setDecimals(1)

        self.gridLayout.addWidget(self.mgso4_kettle, 4, 4, 1, 1)

        self.nacl_kettle = QDoubleSpinBox(self.group_salts)
        self.nacl_kettle.setObjectName(u"nacl_kettle")
        self.nacl_kettle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.nacl_kettle.setDecimals(1)

        self.gridLayout.addWidget(self.nacl_kettle, 4, 5, 1, 1)

        self.nahco3_kettle = QDoubleSpinBox(self.group_salts)
        self.nahco3_kettle.setObjectName(u"nahco3_kettle")
        self.nahco3_kettle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.nahco3_kettle.setDecimals(1)

        self.gridLayout.addWidget(self.nahco3_kettle, 4, 6, 1, 1)

        self.caoh2_kettle = QDoubleSpinBox(self.group_salts)
        self.caoh2_kettle.setObjectName(u"caoh2_kettle")
        self.caoh2_kettle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.caoh2_kettle.setDecimals(1)

        self.gridLayout.addWidget(self.caoh2_kettle, 4, 7, 1, 1)

        self.lbl_decrease = QLabel(self.group_salts)
        self.lbl_decrease.setObjectName(u"lbl_decrease")
        self.lbl_decrease.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_decrease, 0, 1, 1, 4)

        self.lbl_increase = QLabel(self.group_salts)
        self.lbl_increase.setObjectName(u"lbl_increase")
        self.lbl_increase.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_increase, 0, 6, 1, 2)


        self.verticalLayout.addWidget(self.group_salts)

        self.group_results = QGroupBox(TabChemistry)
        self.group_results.setObjectName(u"group_results")
        self.gridLayout_2 = QGridLayout(self.group_results)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_ca = QLabel(self.group_results)
        self.lbl_ca.setObjectName(u"lbl_ca")
        self.lbl_ca.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_ca, 0, 1, 1, 1)

        self.lbl_mashResults = QLabel(self.group_results)
        self.lbl_mashResults.setObjectName(u"lbl_mashResults")
        self.lbl_mashResults.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_mashResults, 1, 0, 1, 1)

        self.sulfateSlide = QSlider(self.group_results)
        self.sulfateSlide.setObjectName(u"sulfateSlide")
        self.sulfateSlide.setEnabled(False)
        self.sulfateSlide.setMinimum(50)
        self.sulfateSlide.setMaximum(350)
        self.sulfateSlide.setOrientation(Qt.Horizontal)
        self.sulfateSlide.setTickPosition(QSlider.TicksBelow)
        self.sulfateSlide.setTickInterval(50)

        self.gridLayout_2.addWidget(self.sulfateSlide, 5, 5, 1, 1)

        self.bicarbonate = QLineEdit(self.group_results)
        self.bicarbonate.setObjectName(u"bicarbonate")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bicarbonate.setFont(font)
        self.bicarbonate.setAlignment(Qt.AlignCenter)
        self.bicarbonate.setReadOnly(True)

        self.gridLayout_2.addWidget(self.bicarbonate, 4, 6, 1, 1)

        self.strikeCalcium = QLineEdit(self.group_results)
        self.strikeCalcium.setObjectName(u"strikeCalcium")
        self.strikeCalcium.setAlignment(Qt.AlignCenter)
        self.strikeCalcium.setReadOnly(True)

        self.gridLayout_2.addWidget(self.strikeCalcium, 1, 1, 1, 1)

        self.magnesium = QLineEdit(self.group_results)
        self.magnesium.setObjectName(u"magnesium")
        self.magnesium.setFont(font)
        self.magnesium.setAlignment(Qt.AlignCenter)
        self.magnesium.setReadOnly(True)

        self.gridLayout_2.addWidget(self.magnesium, 4, 2, 1, 1)

        self.spargeSodium = QLineEdit(self.group_results)
        self.spargeSodium.setObjectName(u"spargeSodium")
        self.spargeSodium.setAlignment(Qt.AlignCenter)
        self.spargeSodium.setReadOnly(True)

        self.gridLayout_2.addWidget(self.spargeSodium, 2, 3, 1, 1)

        self.lbl_na = QLabel(self.group_results)
        self.lbl_na.setObjectName(u"lbl_na")
        self.lbl_na.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_na, 0, 3, 1, 1)

        self.magnesiumSlide = QSlider(self.group_results)
        self.magnesiumSlide.setObjectName(u"magnesiumSlide")
        self.magnesiumSlide.setEnabled(False)
        self.magnesiumSlide.setMinimum(10)
        self.magnesiumSlide.setMaximum(30)
        self.magnesiumSlide.setOrientation(Qt.Horizontal)
        self.magnesiumSlide.setTickPosition(QSlider.TicksBelow)
        self.magnesiumSlide.setTickInterval(5)

        self.gridLayout_2.addWidget(self.magnesiumSlide, 5, 2, 1, 1)

        self.sulfate = QLineEdit(self.group_results)
        self.sulfate.setObjectName(u"sulfate")
        self.sulfate.setFont(font)
        self.sulfate.setAlignment(Qt.AlignCenter)
        self.sulfate.setReadOnly(True)

        self.gridLayout_2.addWidget(self.sulfate, 4, 5, 1, 1)

        self.lbl_spargeResults = QLabel(self.group_results)
        self.lbl_spargeResults.setObjectName(u"lbl_spargeResults")
        self.lbl_spargeResults.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_spargeResults, 2, 0, 1, 1)

        self.spargeSulfate = QLineEdit(self.group_results)
        self.spargeSulfate.setObjectName(u"spargeSulfate")
        self.spargeSulfate.setAlignment(Qt.AlignCenter)
        self.spargeSulfate.setReadOnly(True)

        self.gridLayout_2.addWidget(self.spargeSulfate, 2, 5, 1, 1)

        self.strikeSulfate = QLineEdit(self.group_results)
        self.strikeSulfate.setObjectName(u"strikeSulfate")
        self.strikeSulfate.setAlignment(Qt.AlignCenter)
        self.strikeSulfate.setReadOnly(True)

        self.gridLayout_2.addWidget(self.strikeSulfate, 1, 5, 1, 1)

        self.lbl_overallResults = QLabel(self.group_results)
        self.lbl_overallResults.setObjectName(u"lbl_overallResults")
        self.lbl_overallResults.setFont(font)
        self.lbl_overallResults.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_overallResults, 4, 0, 1, 1)

        self.bicarbonateSlide = QSlider(self.group_results)
        self.bicarbonateSlide.setObjectName(u"bicarbonateSlide")
        self.bicarbonateSlide.setEnabled(False)
        self.bicarbonateSlide.setMinimum(0)
        self.bicarbonateSlide.setMaximum(250)
        self.bicarbonateSlide.setValue(0)
        self.bicarbonateSlide.setOrientation(Qt.Horizontal)
        self.bicarbonateSlide.setTickPosition(QSlider.TicksBelow)
        self.bicarbonateSlide.setTickInterval(50)

        self.gridLayout_2.addWidget(self.bicarbonateSlide, 5, 6, 1, 1)

        self.lbl_cl = QLabel(self.group_results)
        self.lbl_cl.setObjectName(u"lbl_cl")
        self.lbl_cl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_cl, 0, 4, 1, 1)

        self.line_5 = QFrame(self.group_results)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 3, 0, 1, 7)

        self.strikeSodium = QLineEdit(self.group_results)
        self.strikeSodium.setObjectName(u"strikeSodium")
        self.strikeSodium.setAlignment(Qt.AlignCenter)
        self.strikeSodium.setReadOnly(True)

        self.gridLayout_2.addWidget(self.strikeSodium, 1, 3, 1, 1)

        self.lbl_hco3 = QLabel(self.group_results)
        self.lbl_hco3.setObjectName(u"lbl_hco3")
        self.lbl_hco3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_hco3, 0, 6, 1, 1)

        self.spargeCalcium = QLineEdit(self.group_results)
        self.spargeCalcium.setObjectName(u"spargeCalcium")
        self.spargeCalcium.setAlignment(Qt.AlignCenter)
        self.spargeCalcium.setReadOnly(True)

        self.gridLayout_2.addWidget(self.spargeCalcium, 2, 1, 1, 1)

        self.chlorideSlide = QSlider(self.group_results)
        self.chlorideSlide.setObjectName(u"chlorideSlide")
        self.chlorideSlide.setEnabled(False)
        self.chlorideSlide.setMinimum(0)
        self.chlorideSlide.setMaximum(250)
        self.chlorideSlide.setValue(0)
        self.chlorideSlide.setOrientation(Qt.Horizontal)
        self.chlorideSlide.setTickPosition(QSlider.TicksBelow)
        self.chlorideSlide.setTickInterval(50)

        self.gridLayout_2.addWidget(self.chlorideSlide, 5, 4, 1, 1)

        self.strikeChloride = QLineEdit(self.group_results)
        self.strikeChloride.setObjectName(u"strikeChloride")
        self.strikeChloride.setAlignment(Qt.AlignCenter)
        self.strikeChloride.setReadOnly(True)

        self.gridLayout_2.addWidget(self.strikeChloride, 1, 4, 1, 1)

        self.spargeBicarbonate = QLineEdit(self.group_results)
        self.spargeBicarbonate.setObjectName(u"spargeBicarbonate")
        self.spargeBicarbonate.setAlignment(Qt.AlignCenter)
        self.spargeBicarbonate.setReadOnly(True)

        self.gridLayout_2.addWidget(self.spargeBicarbonate, 2, 6, 1, 1)

        self.sodiumSlide = QSlider(self.group_results)
        self.sodiumSlide.setObjectName(u"sodiumSlide")
        self.sodiumSlide.setEnabled(False)
        self.sodiumSlide.setMinimum(0)
        self.sodiumSlide.setMaximum(150)
        self.sodiumSlide.setValue(0)
        self.sodiumSlide.setOrientation(Qt.Horizontal)
        self.sodiumSlide.setTickPosition(QSlider.TicksBelow)
        self.sodiumSlide.setTickInterval(25)

        self.gridLayout_2.addWidget(self.sodiumSlide, 5, 3, 1, 1)

        self.spargeMagnesium = QLineEdit(self.group_results)
        self.spargeMagnesium.setObjectName(u"spargeMagnesium")
        self.spargeMagnesium.setAlignment(Qt.AlignCenter)
        self.spargeMagnesium.setReadOnly(True)

        self.gridLayout_2.addWidget(self.spargeMagnesium, 2, 2, 1, 1)

        self.calciumSlide = QSlider(self.group_results)
        self.calciumSlide.setObjectName(u"calciumSlide")
        self.calciumSlide.setEnabled(False)
        self.calciumSlide.setMinimum(50)
        self.calciumSlide.setMaximum(150)
        self.calciumSlide.setOrientation(Qt.Horizontal)
        self.calciumSlide.setTickPosition(QSlider.TicksBelow)
        self.calciumSlide.setTickInterval(10)

        self.gridLayout_2.addWidget(self.calciumSlide, 5, 1, 1, 1)

        self.chloride = QLineEdit(self.group_results)
        self.chloride.setObjectName(u"chloride")
        self.chloride.setFont(font)
        self.chloride.setAlignment(Qt.AlignCenter)
        self.chloride.setReadOnly(True)

        self.gridLayout_2.addWidget(self.chloride, 4, 4, 1, 1)

        self.lbl_mg = QLabel(self.group_results)
        self.lbl_mg.setObjectName(u"lbl_mg")
        self.lbl_mg.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_mg, 0, 2, 1, 1)

        self.strikeMagnesium = QLineEdit(self.group_results)
        self.strikeMagnesium.setObjectName(u"strikeMagnesium")
        self.strikeMagnesium.setAlignment(Qt.AlignCenter)
        self.strikeMagnesium.setReadOnly(True)

        self.gridLayout_2.addWidget(self.strikeMagnesium, 1, 2, 1, 1)

        self.calcium = QLineEdit(self.group_results)
        self.calcium.setObjectName(u"calcium")
        self.calcium.setFont(font)
        self.calcium.setAlignment(Qt.AlignCenter)
        self.calcium.setReadOnly(True)

        self.gridLayout_2.addWidget(self.calcium, 4, 1, 1, 1)

        self.sodium = QLineEdit(self.group_results)
        self.sodium.setObjectName(u"sodium")
        self.sodium.setFont(font)
        self.sodium.setAlignment(Qt.AlignCenter)
        self.sodium.setReadOnly(True)

        self.gridLayout_2.addWidget(self.sodium, 4, 3, 1, 1)

        self.strikeBicarbonate = QLineEdit(self.group_results)
        self.strikeBicarbonate.setObjectName(u"strikeBicarbonate")
        self.strikeBicarbonate.setAlignment(Qt.AlignCenter)
        self.strikeBicarbonate.setReadOnly(True)

        self.gridLayout_2.addWidget(self.strikeBicarbonate, 1, 6, 1, 1)

        self.spargeChloride = QLineEdit(self.group_results)
        self.spargeChloride.setObjectName(u"spargeChloride")
        self.spargeChloride.setAlignment(Qt.AlignCenter)
        self.spargeChloride.setReadOnly(True)

        self.gridLayout_2.addWidget(self.spargeChloride, 2, 4, 1, 1)

        self.lbl_so4 = QLabel(self.group_results)
        self.lbl_so4.setObjectName(u"lbl_so4")
        self.lbl_so4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_so4, 0, 5, 1, 1)


        self.verticalLayout.addWidget(self.group_results)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.group_targets = QGroupBox(TabChemistry)
        self.group_targets.setObjectName(u"group_targets")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_targets.sizePolicy().hasHeightForWidth())
        self.group_targets.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.group_targets)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_pale = QLabel(self.group_targets)
        self.lbl_pale.setObjectName(u"lbl_pale")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_pale)

        self.pale = QComboBox(self.group_targets)
        self.pale.setObjectName(u"pale")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.pale)

        self.lbl_body = QLabel(self.group_targets)
        self.lbl_body.setObjectName(u"lbl_body")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_body)

        self.body = QComboBox(self.group_targets)
        self.body.setObjectName(u"body")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.body)

        self.lbl_hopForward = QLabel(self.group_targets)
        self.lbl_hopForward.setObjectName(u"lbl_hopForward")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_hopForward)

        self.hopForward = QComboBox(self.group_targets)
        self.hopForward.setObjectName(u"hopForward")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.hopForward)

        self.lbl_hazeDesired = QLabel(self.group_targets)
        self.lbl_hazeDesired.setObjectName(u"lbl_hazeDesired")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_hazeDesired)

        self.hazeDesired = QComboBox(self.group_targets)
        self.hazeDesired.setObjectName(u"hazeDesired")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.hazeDesired)

        self.line = QFrame(self.group_targets)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.line)

        self.lbl_recommended = QLabel(self.group_targets)
        self.lbl_recommended.setObjectName(u"lbl_recommended")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_recommended)

        self.recommended = QLineEdit(self.group_targets)
        self.recommended.setObjectName(u"recommended")
        self.recommended.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.recommended)


        self.horizontalLayout.addWidget(self.group_targets)

        self.group_acids = QGroupBox(TabChemistry)
        self.group_acids.setObjectName(u"group_acids")
        sizePolicy.setHeightForWidth(self.group_acids.sizePolicy().hasHeightForWidth())
        self.group_acids.setSizePolicy(sizePolicy)
        self.formLayout_2 = QFormLayout(self.group_acids)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_phosphoric = QLabel(self.group_acids)
        self.lbl_phosphoric.setObjectName(u"lbl_phosphoric")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_phosphoric)

        self.phosphoric = QDoubleSpinBox(self.group_acids)
        self.phosphoric.setObjectName(u"phosphoric")
        self.phosphoric.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.phosphoric.setDecimals(1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.phosphoric)

        self.lbl_lactic = QLabel(self.group_acids)
        self.lbl_lactic.setObjectName(u"lbl_lactic")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbl_lactic)

        self.lactic = QDoubleSpinBox(self.group_acids)
        self.lactic.setObjectName(u"lactic")
        self.lactic.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lactic.setDecimals(1)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lactic)

        self.lbl_acidMalt = QLabel(self.group_acids)
        self.lbl_acidMalt.setObjectName(u"lbl_acidMalt")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lbl_acidMalt)

        self.acidMalt = QDoubleSpinBox(self.group_acids)
        self.acidMalt.setObjectName(u"acidMalt")
        self.acidMalt.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.acidMalt.setReadOnly(True)
        self.acidMalt.setDecimals(1)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.acidMalt)


        self.horizontalLayout.addWidget(self.group_acids)

        self.group_ph = QGroupBox(TabChemistry)
        self.group_ph.setObjectName(u"group_ph")
        sizePolicy.setHeightForWidth(self.group_ph.sizePolicy().hasHeightForWidth())
        self.group_ph.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.group_ph)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.ph = QLineEdit(self.group_ph)
        self.ph.setObjectName(u"ph")
        self.ph.setAlignment(Qt.AlignCenter)
        self.ph.setReadOnly(True)

        self.gridLayout_4.addWidget(self.ph, 0, 0, 1, 3)

        self.phSlide = QSlider(self.group_ph)
        self.phSlide.setObjectName(u"phSlide")
        self.phSlide.setEnabled(False)
        self.phSlide.setMinimum(520)
        self.phSlide.setMaximum(560)
        self.phSlide.setValue(560)
        self.phSlide.setOrientation(Qt.Horizontal)
        self.phSlide.setTickPosition(QSlider.TicksBelow)
        self.phSlide.setTickInterval(10)

        self.gridLayout_4.addWidget(self.phSlide, 1, 0, 1, 3)

        self.lbl_ph52 = QLabel(self.group_ph)
        self.lbl_ph52.setObjectName(u"lbl_ph52")

        self.gridLayout_4.addWidget(self.lbl_ph52, 2, 0, 1, 1)

        self.lbl_ph56 = QLabel(self.group_ph)
        self.lbl_ph56.setObjectName(u"lbl_ph56")
        self.lbl_ph56.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.lbl_ph56, 2, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 52, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 1, 1, 1)


        self.horizontalLayout.addWidget(self.group_ph)

        self.group_ratio = QGroupBox(TabChemistry)
        self.group_ratio.setObjectName(u"group_ratio")
        sizePolicy.setHeightForWidth(self.group_ratio.sizePolicy().hasHeightForWidth())
        self.group_ratio.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.group_ratio)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ratio = QLineEdit(self.group_ratio)
        self.ratio.setObjectName(u"ratio")
        self.ratio.setAlignment(Qt.AlignCenter)
        self.ratio.setReadOnly(True)

        self.gridLayout_3.addWidget(self.ratio, 0, 0, 1, 2)

        self.ratioSlide = QSlider(self.group_ratio)
        self.ratioSlide.setObjectName(u"ratioSlide")
        self.ratioSlide.setEnabled(False)
        self.ratioSlide.setMinimum(0)
        self.ratioSlide.setMaximum(200)
        self.ratioSlide.setValue(100)
        self.ratioSlide.setOrientation(Qt.Horizontal)
        self.ratioSlide.setTickPosition(QSlider.TicksBelow)
        self.ratioSlide.setTickInterval(50)

        self.gridLayout_3.addWidget(self.ratioSlide, 1, 0, 1, 2)

        self.lbl_ratioCrisp = QLabel(self.group_ratio)
        self.lbl_ratioCrisp.setObjectName(u"lbl_ratioCrisp")

        self.gridLayout_3.addWidget(self.lbl_ratioCrisp, 2, 0, 1, 1)

        self.lbl_ratioMalty = QLabel(self.group_ratio)
        self.lbl_ratioMalty.setObjectName(u"lbl_ratioMalty")
        self.lbl_ratioMalty.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lbl_ratioMalty, 2, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 3, 0, 1, 1)


        self.horizontalLayout.addWidget(self.group_ratio)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TabChemistry)

        QMetaObject.connectSlotsByName(TabChemistry)
    # setupUi

    def retranslateUi(self, TabChemistry):
        TabChemistry.setWindowTitle(QCoreApplication.translate("TabChemistry", u"Form", None))
#if QT_CONFIG(tooltip)
        self.group_salts.setToolTip(QCoreApplication.translate("TabChemistry", u"Enter amounts of salts (in grams) that you'll add to the Mash and to the Kettle.  There is no reason that they need to be the same or proportional.\n"
"\n"
"Salts added to the mash will affect both pH and flavor (except NaCl, which only affects flavor).\n"
"\n"
"Salts added to the kettle will affect flavor. ", None))
#endif // QT_CONFIG(tooltip)
        self.group_salts.setTitle(QCoreApplication.translate("TabChemistry", u"Salt Additions:", None))
        self.lbl_neutral.setText(QCoreApplication.translate("TabChemistry", u"Neutral", None))
#if QT_CONFIG(tooltip)
        self.lbl_cacl2.setToolTip(QCoreApplication.translate("TabChemistry", u"Calcium chloride", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_cacl2.setText(QCoreApplication.translate("TabChemistry", u"<html><head/><body><p>CaCl<span style=\" vertical-align:sub;\">2</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lbl_caso4.setToolTip(QCoreApplication.translate("TabChemistry", u"Calcium sulfate (Gypsum)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_caso4.setText(QCoreApplication.translate("TabChemistry", u"<html><head/><body><p>CaSO<span style=\" vertical-align:sub;\">4</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lbl_mgcl2.setToolTip(QCoreApplication.translate("TabChemistry", u"Magnesium chloride", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_mgcl2.setText(QCoreApplication.translate("TabChemistry", u"<html><head/><body><p>MgCl<span style=\" vertical-align:sub;\">2</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lbl_mgso4.setToolTip(QCoreApplication.translate("TabChemistry", u"Magnesium sulfate (Epsom Salts)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_mgso4.setText(QCoreApplication.translate("TabChemistry", u"<html><head/><body><p>MgSO<span style=\" vertical-align:sub;\">4</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lbl_nacl.setToolTip(QCoreApplication.translate("TabChemistry", u"Sodium chloride (Table Salt)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_nacl.setText(QCoreApplication.translate("TabChemistry", u"NaCl", None))
#if QT_CONFIG(tooltip)
        self.lbl_nahco3.setToolTip(QCoreApplication.translate("TabChemistry", u"Sodum Bicarbonate (Baking Soda)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_nahco3.setText(QCoreApplication.translate("TabChemistry", u"<html><head/><body><p>NaHCO<span style=\" vertical-align:sub;\">3</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lbl_caoh2.setToolTip(QCoreApplication.translate("TabChemistry", u"Calcium hydroxide (Slaked Lime)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_caoh2.setText(QCoreApplication.translate("TabChemistry", u"<html><head/><body><p>Ca(OH)<span style=\" vertical-align:sub;\">2</span></p></body></html>", None))
        self.lbl_mashSalts.setText(QCoreApplication.translate("TabChemistry", u"Mash Amount:", None))
#if QT_CONFIG(tooltip)
        self.cacl2_mash.setToolTip(QCoreApplication.translate("TabChemistry", u"When adding to the mash to lower pH, consider the Chloride to Sulfate Ratio and its impact on flavor.  pH can also be lowered with CaSO4 (Gypsum), with a different flavor result, or with Acid additions, with little flavor impact.", None))
#endif // QT_CONFIG(tooltip)
        self.cacl2_mash.setSuffix(QCoreApplication.translate("TabChemistry", u" g", None))
#if QT_CONFIG(tooltip)
        self.caso4_mash.setToolTip(QCoreApplication.translate("TabChemistry", u"When adding to the mash to lower pH, consider the Chloride to Sulfate Ratio and its impact on flavor.  pH can also be lowered with CaCl2, with a different flavor result, or with Acid additions, with little flavor impact.", None))
#endif // QT_CONFIG(tooltip)
        self.caso4_mash.setSuffix(QCoreApplication.translate("TabChemistry", u" g", None))
#if QT_CONFIG(tooltip)
        self.mgcl2_mash.setToolTip(QCoreApplication.translate("TabChemistry", u"Beer wort naturally contains more Magnesium than the yeast need. Consider using CaCl2, CaSO4, or Acids to lower mash pH instead.", None))
#endif // QT_CONFIG(tooltip)
        self.mgcl2_mash.setSuffix(QCoreApplication.translate("TabChemistry", u" g", None))
#if QT_CONFIG(tooltip)
        self.mgso4_mash.setToolTip(QCoreApplication.translate("TabChemistry", u"Beer wort naturally contains more Magnesium than the yeast need. Consider using CaCl2, CaSO4, or Acids to lower mash pH instead.", None))
#endif // QT_CONFIG(tooltip)
        self.mgso4_mash.setSuffix(QCoreApplication.translate("TabChemistry", u" g", None))
        self.nacl_mash.setSuffix(QCoreApplication.translate("TabChemistry", u" g", None))
        self.nahco3_mash.setSuffix(QCoreApplication.translate("TabChemistry", u" g", None))
        self.caoh2_mash.setSuffix(QCoreApplication.translate("TabChemistry", u" g", None))
#if QT_CONFIG(tooltip)
        self.lbl_kettleSalts.setToolTip(QCoreApplication.translate("TabChemistry", u"The words 'Sparge' and 'Kettle' are used interchangeably.  Sparge/Kettle salts should normally be added to the Kettle rather than to the sparge/mashout water.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_kettleSalts.setText(QCoreApplication.translate("TabChemistry", u"Kettle Amount:", None))
        self.cacl2_kettle.setSuffix(QCoreApplication.translate("TabChemistry", u" g", None))
        self.caso4_kettle.setSuffix(QCoreApplication.translate("TabChemistry", u" g", None))
        self.mgcl2_kettle.setSuffix(QCoreApplication.translate("TabChemistry", u" g", None))
        self.mgso4_kettle.setSuffix(QCoreApplication.translate("TabChemistry", u" g", None))
        self.nacl_kettle.setSuffix(QCoreApplication.translate("TabChemistry", u" g", None))
        self.nahco3_kettle.setSuffix(QCoreApplication.translate("TabChemistry", u" g", None))
        self.caoh2_kettle.setSuffix(QCoreApplication.translate("TabChemistry", u" g", None))
        self.lbl_decrease.setText(QCoreApplication.translate("TabChemistry", u"Decrease pH", None))
        self.lbl_increase.setText(QCoreApplication.translate("TabChemistry", u"Increase pH", None))
        self.group_results.setTitle(QCoreApplication.translate("TabChemistry", u"Water Results:", None))
#if QT_CONFIG(tooltip)
        self.lbl_ca.setToolTip(QCoreApplication.translate("TabChemistry", u"In general, at least 50 ppm of Calcium in the fermenter is recommended for yeast flocculation.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_ca.setText(QCoreApplication.translate("TabChemistry", u"Ca", None))
        self.lbl_mashResults.setText(QCoreApplication.translate("TabChemistry", u"<html><head/><body><p>Mash H<span style=\" vertical-align:sub;\">2</span>O Concentrations:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.sulfateSlide.setToolTip(QCoreApplication.translate("TabChemistry", u"50-150 ppm for normally bitter beers\n"
"150-350 ppm for very bitter beers", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.bicarbonate.setToolTip(QCoreApplication.translate("TabChemistry", u"Equivalent bicarbonate concentration.", None))
#endif // QT_CONFIG(tooltip)
        self.bicarbonate.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.strikeCalcium.setToolTip(QCoreApplication.translate("TabChemistry", u"In general, at least 50 ppm of Calcium in the fermenter is recommended for yeast flocculation.", None))
#endif // QT_CONFIG(tooltip)
        self.strikeCalcium.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.magnesium.setToolTip(QCoreApplication.translate("TabChemistry", u"Beer wort naturally contains more Magnesium than the yeast need. ", None))
#endif // QT_CONFIG(tooltip)
        self.magnesium.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.spargeSodium.setToolTip(QCoreApplication.translate("TabChemistry", u"Sodium enhances flavors, but too much can cause a salty taste.", None))
#endif // QT_CONFIG(tooltip)
        self.spargeSodium.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.lbl_na.setToolTip(QCoreApplication.translate("TabChemistry", u"Sodium enhances flavors, but too much can cause a salty taste.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_na.setText(QCoreApplication.translate("TabChemistry", u"Na", None))
#if QT_CONFIG(tooltip)
        self.magnesiumSlide.setToolTip(QCoreApplication.translate("TabChemistry", u"10-30 ppm", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sulfate.setToolTip(QCoreApplication.translate("TabChemistry", u"Sulfate enhances the perception of crisp bitterness.", None))
#endif // QT_CONFIG(tooltip)
        self.sulfate.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.lbl_spargeResults.setToolTip(QCoreApplication.translate("TabChemistry", u"The words 'Sparge' and 'Kettle' are used somewhat interchangeably.  Sparge/Kettle salts should normally be added to the Kettle rather than to the sparge/mashout water.  The separate Sparge Water acidification calculation assumes these salts are added to the kettle (and so do not affect the sparge water acidification calculation).", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_spargeResults.setText(QCoreApplication.translate("TabChemistry", u"<html><head/><body><p>Sparge H<span style=\" vertical-align:sub;\">2</span>O Concentrations:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.spargeSulfate.setToolTip(QCoreApplication.translate("TabChemistry", u"Sulfate enhances the perception of crisp bitterness.", None))
#endif // QT_CONFIG(tooltip)
        self.spargeSulfate.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.strikeSulfate.setToolTip(QCoreApplication.translate("TabChemistry", u"Sulfate enhances the perception of crisp bitterness.", None))
#endif // QT_CONFIG(tooltip)
        self.strikeSulfate.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
        self.lbl_overallResults.setText(QCoreApplication.translate("TabChemistry", u"<html><head/><body><p>Overall H<span style=\" vertical-align:sub;\">2</span>O Concentrations:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.bicarbonateSlide.setToolTip(QCoreApplication.translate("TabChemistry", u"0-50 ppm for pale, base malt-only beers\n"
"50-150 ppm for amber-colored, toasted malt beers\n"
"150-250 ppm for dark, roasted malt beers", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lbl_cl.setToolTip(QCoreApplication.translate("TabChemistry", u"Chloride enhances malty flavors.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_cl.setText(QCoreApplication.translate("TabChemistry", u"Cl", None))
#if QT_CONFIG(tooltip)
        self.strikeSodium.setToolTip(QCoreApplication.translate("TabChemistry", u"Sodium enhances flavors, but too much can cause a salty taste.", None))
#endif // QT_CONFIG(tooltip)
        self.strikeSodium.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.lbl_hco3.setToolTip(QCoreApplication.translate("TabChemistry", u"Equivalent bicarbonate concentration.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_hco3.setText(QCoreApplication.translate("TabChemistry", u"<html><head/><body><p>HCO<span style=\" vertical-align:sub;\">3</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.spargeCalcium.setToolTip(QCoreApplication.translate("TabChemistry", u"In general, at least 50 ppm of Calcium in the fermenter is recommended for yeast flocculation.", None))
#endif // QT_CONFIG(tooltip)
        self.spargeCalcium.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.chlorideSlide.setToolTip(QCoreApplication.translate("TabChemistry", u"0-250 ppm", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.strikeChloride.setToolTip(QCoreApplication.translate("TabChemistry", u"Chloride enhances malty flavors.", None))
#endif // QT_CONFIG(tooltip)
        self.strikeChloride.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.spargeBicarbonate.setToolTip(QCoreApplication.translate("TabChemistry", u"Equivalent bicarbonate concentration.", None))
#endif // QT_CONFIG(tooltip)
        self.spargeBicarbonate.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.sodiumSlide.setToolTip(QCoreApplication.translate("TabChemistry", u"0-150 ppm", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.spargeMagnesium.setToolTip(QCoreApplication.translate("TabChemistry", u"Beer wort naturally contains more Magnesium than the yeast need. ", None))
#endif // QT_CONFIG(tooltip)
        self.spargeMagnesium.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.calciumSlide.setToolTip(QCoreApplication.translate("TabChemistry", u"50-150 ppm", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.chloride.setToolTip(QCoreApplication.translate("TabChemistry", u"Chloride enhances malty flavors.", None))
#endif // QT_CONFIG(tooltip)
        self.chloride.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.lbl_mg.setToolTip(QCoreApplication.translate("TabChemistry", u"Beer wort naturally contains more Magnesium than the yeast need. ", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_mg.setText(QCoreApplication.translate("TabChemistry", u"Mg", None))
#if QT_CONFIG(tooltip)
        self.strikeMagnesium.setToolTip(QCoreApplication.translate("TabChemistry", u"Beer wort naturally contains more Magnesium than the yeast need. ", None))
#endif // QT_CONFIG(tooltip)
        self.strikeMagnesium.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.calcium.setToolTip(QCoreApplication.translate("TabChemistry", u"In general, at least 50 ppm of Calcium in the fermenter is recommended for yeast flocculation.", None))
#endif // QT_CONFIG(tooltip)
        self.calcium.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.sodium.setToolTip(QCoreApplication.translate("TabChemistry", u"Sodium enhances flavors, but too much can cause a salty taste.", None))
#endif // QT_CONFIG(tooltip)
        self.sodium.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.strikeBicarbonate.setToolTip(QCoreApplication.translate("TabChemistry", u"Equivalent bicarbonate concentration.", None))
#endif // QT_CONFIG(tooltip)
        self.strikeBicarbonate.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.spargeChloride.setToolTip(QCoreApplication.translate("TabChemistry", u"Chloride enhances malty flavors.", None))
#endif // QT_CONFIG(tooltip)
        self.spargeChloride.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.lbl_so4.setToolTip(QCoreApplication.translate("TabChemistry", u"Sulfate enhances the perception of crisp bitterness.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_so4.setText(QCoreApplication.translate("TabChemistry", u"<html><head/><body><p>SO<span style=\" vertical-align:sub;\">4</span></p></body></html>", None))
        self.group_targets.setTitle(QCoreApplication.translate("TabChemistry", u"Target Characteristics:", None))
        self.lbl_pale.setText(QCoreApplication.translate("TabChemistry", u"Maintain Palest Color:", None))
        self.lbl_body.setText(QCoreApplication.translate("TabChemistry", u"Desired Body:", None))
        self.body.setCurrentText("")
        self.lbl_hopForward.setText(QCoreApplication.translate("TabChemistry", u"Hop Forward:", None))
        self.lbl_hazeDesired.setText(QCoreApplication.translate("TabChemistry", u"Haze Desired:", None))
        self.lbl_recommended.setText(QCoreApplication.translate("TabChemistry", u"Recommended pH:", None))
#if QT_CONFIG(tooltip)
        self.recommended.setToolTip(QCoreApplication.translate("TabChemistry", u"Credit for this goes to VikeMan's BrewCipher.", None))
#endif // QT_CONFIG(tooltip)
        self.group_acids.setTitle(QCoreApplication.translate("TabChemistry", u"Mash Acid Additions:", None))
        self.lbl_phosphoric.setText(QCoreApplication.translate("TabChemistry", u"Phosphoric Acid (10%):", None))
        self.phosphoric.setSuffix(QCoreApplication.translate("TabChemistry", u" ml", None))
        self.lbl_lactic.setText(QCoreApplication.translate("TabChemistry", u"Lactic Acid (88%):", None))
        self.lactic.setSuffix(QCoreApplication.translate("TabChemistry", u" ml", None))
        self.lbl_acidMalt.setText(QCoreApplication.translate("TabChemistry", u"Acid Malt (3%):", None))
        self.acidMalt.setSuffix(QCoreApplication.translate("TabChemistry", u" oz", None))
#if QT_CONFIG(tooltip)
        self.group_ph.setToolTip(QCoreApplication.translate("TabChemistry", u"Ideally, mash pH should be in the range of 5.2 to 5.6, measured at room temperature.\n"
"\n"
"Note: For Step Mashes, this pH will not necessarily be accurate for any given step. It represents the pH that would be achieved in a single infusion with all of the recipe water.", None))
#endif // QT_CONFIG(tooltip)
        self.group_ph.setTitle(QCoreApplication.translate("TabChemistry", u"Mash pH:", None))
        self.ph.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"7", None))
        self.lbl_ph52.setText(QCoreApplication.translate("TabChemistry", u"5.2", None))
        self.lbl_ph56.setText(QCoreApplication.translate("TabChemistry", u"5.6", None))
#if QT_CONFIG(tooltip)
        self.group_ratio.setToolTip(QCoreApplication.translate("TabChemistry", u"Chloride/Sulfate ratios greater than 1.0 tend to accentuate malt flavors.  Chloride/Sulfate ratios less than 1.0 tend to accentuate crisp bitterness. ", None))
#endif // QT_CONFIG(tooltip)
        self.group_ratio.setTitle(QCoreApplication.translate("TabChemistry", u"Chloride/Sulfide Ratio:", None))
        self.ratio.setPlaceholderText(QCoreApplication.translate("TabChemistry", u"N/A", None))
        self.lbl_ratioCrisp.setText(QCoreApplication.translate("TabChemistry", u"Crisp Bitterness", None))
        self.lbl_ratioMalty.setText(QCoreApplication.translate("TabChemistry", u"Malty", None))
    # retranslateUi

