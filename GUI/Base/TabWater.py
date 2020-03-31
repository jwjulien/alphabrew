# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TabWater.ui'
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


class Ui_TabWater(object):
    def setupUi(self, TabWater):
        if TabWater.objectName():
            TabWater.setObjectName(u"TabWater")
        TabWater.resize(1130, 654)
        self.verticalLayout = QVBoxLayout(TabWater)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(TabWater)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.group_waters = QGroupBox(self.splitter)
        self.group_waters.setObjectName(u"group_waters")
        self.formLayout_3 = QFormLayout(self.group_waters)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_base = QLabel(self.group_waters)
        self.lbl_base.setObjectName(u"lbl_base")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lbl_base)

        self.base = QComboBox(self.group_waters)
        self.base.setObjectName(u"base")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.base)

        self.line_3 = QFrame(self.group_waters)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.formLayout_3.setWidget(1, QFormLayout.SpanningRole, self.line_3)

        self.lbl_strikeWater = QLabel(self.group_waters)
        self.lbl_strikeWater.setObjectName(u"lbl_strikeWater")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lbl_strikeWater)

        self.strikeVolume = QLineEdit(self.group_waters)
        self.strikeVolume.setObjectName(u"strikeVolume")
        self.strikeVolume.setReadOnly(True)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.strikeVolume)

        self.lbl_strikeDistilled = QLabel(self.group_waters)
        self.lbl_strikeDistilled.setObjectName(u"lbl_strikeDistilled")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.lbl_strikeDistilled)

        self.strikeDistilled = QSpinBox(self.group_waters)
        self.strikeDistilled.setObjectName(u"strikeDistilled")
        self.strikeDistilled.setMaximum(100)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.strikeDistilled)

        self.line_4 = QFrame(self.group_waters)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.formLayout_3.setWidget(4, QFormLayout.SpanningRole, self.line_4)

        self.spargeVolume = QLineEdit(self.group_waters)
        self.spargeVolume.setObjectName(u"spargeVolume")
        self.spargeVolume.setReadOnly(True)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.spargeVolume)

        self.lbl_spargeWater = QLabel(self.group_waters)
        self.lbl_spargeWater.setObjectName(u"lbl_spargeWater")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.lbl_spargeWater)

        self.lbl_spargeDistilled = QLabel(self.group_waters)
        self.lbl_spargeDistilled.setObjectName(u"lbl_spargeDistilled")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.lbl_spargeDistilled)

        self.spargeDistilled = QSpinBox(self.group_waters)
        self.spargeDistilled.setObjectName(u"spargeDistilled")
        self.spargeDistilled.setMaximum(100)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.spargeDistilled)

        self.splitter.addWidget(self.group_waters)
        self.group_targets = QGroupBox(self.splitter)
        self.group_targets.setObjectName(u"group_targets")
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

        self.splitter.addWidget(self.group_targets)
        self.group_acids = QGroupBox(self.splitter)
        self.group_acids.setObjectName(u"group_acids")
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
        self.acidMalt.setDecimals(1)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.acidMalt)

        self.splitter.addWidget(self.group_acids)

        self.verticalLayout.addWidget(self.splitter)

        self.group_salts = QGroupBox(TabWater)
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

        self.splitter_2 = QSplitter(TabWater)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.group_results = QGroupBox(self.splitter_2)
        self.group_results.setObjectName(u"group_results")
        self.gridLayout_2 = QGridLayout(self.group_results)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.mgSparge = QLineEdit(self.group_results)
        self.mgSparge.setObjectName(u"mgSparge")
        self.mgSparge.setAlignment(Qt.AlignCenter)
        self.mgSparge.setReadOnly(True)

        self.gridLayout_2.addWidget(self.mgSparge, 2, 2, 1, 1)

        self.mgMash = QLineEdit(self.group_results)
        self.mgMash.setObjectName(u"mgMash")
        self.mgMash.setAlignment(Qt.AlignCenter)
        self.mgMash.setReadOnly(True)

        self.gridLayout_2.addWidget(self.mgMash, 1, 2, 1, 1)

        self.mg = QLineEdit(self.group_results)
        self.mg.setObjectName(u"mg")
        self.mg.setAlignment(Qt.AlignCenter)
        self.mg.setReadOnly(True)

        self.gridLayout_2.addWidget(self.mg, 4, 2, 1, 1)

        self.so4Sparge = QLineEdit(self.group_results)
        self.so4Sparge.setObjectName(u"so4Sparge")
        self.so4Sparge.setAlignment(Qt.AlignCenter)
        self.so4Sparge.setReadOnly(True)

        self.gridLayout_2.addWidget(self.so4Sparge, 2, 5, 1, 1)

        self.clSparge = QLineEdit(self.group_results)
        self.clSparge.setObjectName(u"clSparge")
        self.clSparge.setAlignment(Qt.AlignCenter)
        self.clSparge.setReadOnly(True)

        self.gridLayout_2.addWidget(self.clSparge, 2, 4, 1, 1)

        self.clMash = QLineEdit(self.group_results)
        self.clMash.setObjectName(u"clMash")
        self.clMash.setAlignment(Qt.AlignCenter)
        self.clMash.setReadOnly(True)

        self.gridLayout_2.addWidget(self.clMash, 1, 4, 1, 1)

        self.hco3Mash = QLineEdit(self.group_results)
        self.hco3Mash.setObjectName(u"hco3Mash")
        self.hco3Mash.setAlignment(Qt.AlignCenter)
        self.hco3Mash.setReadOnly(True)

        self.gridLayout_2.addWidget(self.hco3Mash, 1, 6, 1, 1)

        self.ca = QLineEdit(self.group_results)
        self.ca.setObjectName(u"ca")
        self.ca.setAlignment(Qt.AlignCenter)
        self.ca.setReadOnly(True)

        self.gridLayout_2.addWidget(self.ca, 4, 1, 1, 1)

        self.caMash = QLineEdit(self.group_results)
        self.caMash.setObjectName(u"caMash")
        self.caMash.setAlignment(Qt.AlignCenter)
        self.caMash.setReadOnly(True)

        self.gridLayout_2.addWidget(self.caMash, 1, 1, 1, 1)

        self.lbl_so4 = QLabel(self.group_results)
        self.lbl_so4.setObjectName(u"lbl_so4")
        self.lbl_so4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_so4, 0, 5, 1, 1)

        self.lbl_ca = QLabel(self.group_results)
        self.lbl_ca.setObjectName(u"lbl_ca")
        self.lbl_ca.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_ca, 0, 1, 1, 1)

        self.naSparge = QLineEdit(self.group_results)
        self.naSparge.setObjectName(u"naSparge")
        self.naSparge.setAlignment(Qt.AlignCenter)
        self.naSparge.setReadOnly(True)

        self.gridLayout_2.addWidget(self.naSparge, 2, 3, 1, 1)

        self.lbl_mg = QLabel(self.group_results)
        self.lbl_mg.setObjectName(u"lbl_mg")
        self.lbl_mg.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_mg, 0, 2, 1, 1)

        self.naMash = QLineEdit(self.group_results)
        self.naMash.setObjectName(u"naMash")
        self.naMash.setAlignment(Qt.AlignCenter)
        self.naMash.setReadOnly(True)

        self.gridLayout_2.addWidget(self.naMash, 1, 3, 1, 1)

        self.lbl_na = QLabel(self.group_results)
        self.lbl_na.setObjectName(u"lbl_na")
        self.lbl_na.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_na, 0, 3, 1, 1)

        self.cl = QLineEdit(self.group_results)
        self.cl.setObjectName(u"cl")
        self.cl.setAlignment(Qt.AlignCenter)
        self.cl.setReadOnly(True)

        self.gridLayout_2.addWidget(self.cl, 4, 4, 1, 1)

        self.na = QLineEdit(self.group_results)
        self.na.setObjectName(u"na")
        self.na.setAlignment(Qt.AlignCenter)
        self.na.setReadOnly(True)

        self.gridLayout_2.addWidget(self.na, 4, 3, 1, 1)

        self.so4Mash = QLineEdit(self.group_results)
        self.so4Mash.setObjectName(u"so4Mash")
        self.so4Mash.setAlignment(Qt.AlignCenter)
        self.so4Mash.setReadOnly(True)

        self.gridLayout_2.addWidget(self.so4Mash, 1, 5, 1, 1)

        self.hco3Sparge = QLineEdit(self.group_results)
        self.hco3Sparge.setObjectName(u"hco3Sparge")
        self.hco3Sparge.setAlignment(Qt.AlignCenter)
        self.hco3Sparge.setReadOnly(True)

        self.gridLayout_2.addWidget(self.hco3Sparge, 2, 6, 1, 1)

        self.caSparge = QLineEdit(self.group_results)
        self.caSparge.setObjectName(u"caSparge")
        self.caSparge.setAlignment(Qt.AlignCenter)
        self.caSparge.setReadOnly(True)

        self.gridLayout_2.addWidget(self.caSparge, 2, 1, 1, 1)

        self.lbl_cl = QLabel(self.group_results)
        self.lbl_cl.setObjectName(u"lbl_cl")
        self.lbl_cl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_cl, 0, 4, 1, 1)

        self.lbl_hco3 = QLabel(self.group_results)
        self.lbl_hco3.setObjectName(u"lbl_hco3")
        self.lbl_hco3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_hco3, 0, 6, 1, 1)

        self.lbl_mashResults = QLabel(self.group_results)
        self.lbl_mashResults.setObjectName(u"lbl_mashResults")
        self.lbl_mashResults.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_mashResults, 1, 0, 1, 1)

        self.so4 = QLineEdit(self.group_results)
        self.so4.setObjectName(u"so4")
        self.so4.setAlignment(Qt.AlignCenter)
        self.so4.setReadOnly(True)

        self.gridLayout_2.addWidget(self.so4, 4, 5, 1, 1)

        self.lbl_spargeResults = QLabel(self.group_results)
        self.lbl_spargeResults.setObjectName(u"lbl_spargeResults")
        self.lbl_spargeResults.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_spargeResults, 2, 0, 1, 1)

        self.lbl_overallResults = QLabel(self.group_results)
        self.lbl_overallResults.setObjectName(u"lbl_overallResults")
        self.lbl_overallResults.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_overallResults, 4, 0, 1, 1)

        self.hco3 = QLineEdit(self.group_results)
        self.hco3.setObjectName(u"hco3")
        self.hco3.setAlignment(Qt.AlignCenter)
        self.hco3.setReadOnly(True)

        self.gridLayout_2.addWidget(self.hco3, 4, 6, 1, 1)

        self.line_5 = QFrame(self.group_results)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 3, 0, 1, 7)

        self.splitter_2.addWidget(self.group_results)
        self.groupBox = QGroupBox(self.splitter_2)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_4 = QFormLayout(self.groupBox)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_chlorideSulfideRatio = QLabel(self.groupBox)
        self.lbl_chlorideSulfideRatio.setObjectName(u"lbl_chlorideSulfideRatio")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.lbl_chlorideSulfideRatio)

        self.ratio = QLineEdit(self.groupBox)
        self.ratio.setObjectName(u"ratio")
        self.ratio.setAlignment(Qt.AlignCenter)
        self.ratio.setReadOnly(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.ratio)

        self.lbl_mashPh = QLabel(self.groupBox)
        self.lbl_mashPh.setObjectName(u"lbl_mashPh")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.lbl_mashPh)

        self.ph = QLineEdit(self.groupBox)
        self.ph.setObjectName(u"ph")
        self.ph.setAlignment(Qt.AlignCenter)
        self.ph.setReadOnly(True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.ph)

        self.splitter_2.addWidget(self.groupBox)

        self.verticalLayout.addWidget(self.splitter_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TabWater)

        QMetaObject.connectSlotsByName(TabWater)
    # setupUi

    def retranslateUi(self, TabWater):
        TabWater.setWindowTitle(QCoreApplication.translate("TabWater", u"Form", None))
        self.group_waters.setTitle(QCoreApplication.translate("TabWater", u"Waters:", None))
        self.lbl_base.setText(QCoreApplication.translate("TabWater", u"Base Water:", None))
        self.lbl_strikeWater.setText(QCoreApplication.translate("TabWater", u"Mash Water:", None))
        self.lbl_strikeDistilled.setText(QCoreApplication.translate("TabWater", u"Distilled:", None))
        self.strikeDistilled.setSuffix(QCoreApplication.translate("TabWater", u"%", None))
        self.lbl_spargeWater.setText(QCoreApplication.translate("TabWater", u"Mash Water:", None))
        self.lbl_spargeDistilled.setText(QCoreApplication.translate("TabWater", u"Distilled:", None))
        self.spargeDistilled.setSuffix(QCoreApplication.translate("TabWater", u"%", None))
        self.group_targets.setTitle(QCoreApplication.translate("TabWater", u"Target Characteristics:", None))
        self.lbl_pale.setText(QCoreApplication.translate("TabWater", u"Maintain Palest Color:", None))
        self.lbl_body.setText(QCoreApplication.translate("TabWater", u"Desired Body:", None))
        self.body.setCurrentText("")
        self.lbl_hopForward.setText(QCoreApplication.translate("TabWater", u"Hop Forward:", None))
        self.lbl_hazeDesired.setText(QCoreApplication.translate("TabWater", u"Haze Desired:", None))
        self.lbl_recommended.setText(QCoreApplication.translate("TabWater", u"Recommended pH:", None))
        self.group_acids.setTitle(QCoreApplication.translate("TabWater", u"Mash Acid Additions:", None))
        self.lbl_phosphoric.setText(QCoreApplication.translate("TabWater", u"Phosphoric Acid (10%):", None))
        self.phosphoric.setSuffix(QCoreApplication.translate("TabWater", u" tsp", None))
        self.lbl_lactic.setText(QCoreApplication.translate("TabWater", u"Lactic Acid (88%):", None))
        self.lactic.setSuffix(QCoreApplication.translate("TabWater", u" tsp", None))
        self.lbl_acidMalt.setText(QCoreApplication.translate("TabWater", u"Acid Malt (3%):", None))
        self.acidMalt.setSuffix(QCoreApplication.translate("TabWater", u" oz", None))
#if QT_CONFIG(tooltip)
        self.group_salts.setToolTip(QCoreApplication.translate("TabWater", u"Enter amounts of salts (in grams) that you'll add to the Mash and to the Kettle.  There is no reason that they need to be the same or proportional.\n"
"\n"
"Salts added to the mash will affect both pH and flavor (except NaCl, which only affects flavor).\n"
"\n"
"Salts added to the kettle will affect flavor. ", None))
#endif // QT_CONFIG(tooltip)
        self.group_salts.setTitle(QCoreApplication.translate("TabWater", u"Salt Additions:", None))
        self.lbl_neutral.setText(QCoreApplication.translate("TabWater", u"Neutral", None))
#if QT_CONFIG(tooltip)
        self.lbl_cacl2.setToolTip(QCoreApplication.translate("TabWater", u"Calcium chloride", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_cacl2.setText(QCoreApplication.translate("TabWater", u"<html><head/><body><p>CaCl<span style=\" vertical-align:sub;\">2</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lbl_caso4.setToolTip(QCoreApplication.translate("TabWater", u"Calcium sulfate (Gypsum)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_caso4.setText(QCoreApplication.translate("TabWater", u"<html><head/><body><p>CaSO<span style=\" vertical-align:sub;\">4</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lbl_mgcl2.setToolTip(QCoreApplication.translate("TabWater", u"Magnesium chloride", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_mgcl2.setText(QCoreApplication.translate("TabWater", u"<html><head/><body><p>MgCl<span style=\" vertical-align:sub;\">2</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lbl_mgso4.setToolTip(QCoreApplication.translate("TabWater", u"Magnesium sulfate (Epsom Salts)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_mgso4.setText(QCoreApplication.translate("TabWater", u"<html><head/><body><p>MgSO<span style=\" vertical-align:sub;\">4</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lbl_nacl.setToolTip(QCoreApplication.translate("TabWater", u"Sodium chloride (Table Salt)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_nacl.setText(QCoreApplication.translate("TabWater", u"NaCl", None))
#if QT_CONFIG(tooltip)
        self.lbl_nahco3.setToolTip(QCoreApplication.translate("TabWater", u"Sodum Bicarbonate (Baking Soda)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_nahco3.setText(QCoreApplication.translate("TabWater", u"<html><head/><body><p>NaHCO<span style=\" vertical-align:sub;\">3</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lbl_caoh2.setToolTip(QCoreApplication.translate("TabWater", u"Calcium hydroxide (Slaked Lime)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_caoh2.setText(QCoreApplication.translate("TabWater", u"<html><head/><body><p>Ca(OH)<span style=\" vertical-align:sub;\">2</span></p></body></html>", None))
        self.lbl_mashSalts.setText(QCoreApplication.translate("TabWater", u"Mash Amount:", None))
#if QT_CONFIG(tooltip)
        self.cacl2_mash.setToolTip(QCoreApplication.translate("TabWater", u"When adding to the mash to lower pH, consider the Chloride to Sulfate Ratio and its impact on flavor.  pH can also be lowered with CaSO4 (Gypsum), with a different flavor result, or with Acid additions, with little flavor impact.", None))
#endif // QT_CONFIG(tooltip)
        self.cacl2_mash.setSuffix(QCoreApplication.translate("TabWater", u" g", None))
#if QT_CONFIG(tooltip)
        self.caso4_mash.setToolTip(QCoreApplication.translate("TabWater", u"When adding to the mash to lower pH, consider the Chloride to Sulfate Ratio and its impact on flavor.  pH can also be lowered with CaCl2, with a different flavor result, or with Acid additions, with little flavor impact.", None))
#endif // QT_CONFIG(tooltip)
        self.caso4_mash.setSuffix(QCoreApplication.translate("TabWater", u" g", None))
#if QT_CONFIG(tooltip)
        self.mgcl2_mash.setToolTip(QCoreApplication.translate("TabWater", u"Beer wort naturally contains more Magnesium than the yeast need. Consider using CaCl2, CaSO4, or Acids to lower mash pH instead.", None))
#endif // QT_CONFIG(tooltip)
        self.mgcl2_mash.setSuffix(QCoreApplication.translate("TabWater", u" g", None))
#if QT_CONFIG(tooltip)
        self.mgso4_mash.setToolTip(QCoreApplication.translate("TabWater", u"Beer wort naturally contains more Magnesium than the yeast need. Consider using CaCl2, CaSO4, or Acids to lower mash pH instead.", None))
#endif // QT_CONFIG(tooltip)
        self.mgso4_mash.setSuffix(QCoreApplication.translate("TabWater", u" g", None))
        self.nacl_mash.setSuffix(QCoreApplication.translate("TabWater", u" g", None))
        self.nahco3_mash.setSuffix(QCoreApplication.translate("TabWater", u" g", None))
        self.caoh2_mash.setSuffix(QCoreApplication.translate("TabWater", u" g", None))
#if QT_CONFIG(tooltip)
        self.lbl_kettleSalts.setToolTip(QCoreApplication.translate("TabWater", u"The words 'Sparge' and 'Kettle' are used interchangeably.  Sparge/Kettle salts should normally be added to the Kettle rather than to the sparge/mashout water.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_kettleSalts.setText(QCoreApplication.translate("TabWater", u"Kettle Amount:", None))
        self.cacl2_kettle.setSuffix(QCoreApplication.translate("TabWater", u" g", None))
        self.caso4_kettle.setSuffix(QCoreApplication.translate("TabWater", u" g", None))
        self.mgcl2_kettle.setSuffix(QCoreApplication.translate("TabWater", u" g", None))
        self.mgso4_kettle.setSuffix(QCoreApplication.translate("TabWater", u" g", None))
        self.nacl_kettle.setSuffix(QCoreApplication.translate("TabWater", u" g", None))
        self.nahco3_kettle.setSuffix(QCoreApplication.translate("TabWater", u" g", None))
        self.caoh2_kettle.setSuffix(QCoreApplication.translate("TabWater", u" g", None))
        self.lbl_decrease.setText(QCoreApplication.translate("TabWater", u"Decrease pH", None))
        self.lbl_increase.setText(QCoreApplication.translate("TabWater", u"Increase pH", None))
        self.group_results.setTitle(QCoreApplication.translate("TabWater", u"Water Results:", None))
#if QT_CONFIG(tooltip)
        self.mgSparge.setToolTip(QCoreApplication.translate("TabWater", u"Beer wort naturally contains more Magnesium than the yeast need. ", None))
#endif // QT_CONFIG(tooltip)
        self.mgSparge.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.mgMash.setToolTip(QCoreApplication.translate("TabWater", u"Beer wort naturally contains more Magnesium than the yeast need. ", None))
#endif // QT_CONFIG(tooltip)
        self.mgMash.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.mg.setToolTip(QCoreApplication.translate("TabWater", u"Beer wort naturally contains more Magnesium than the yeast need. ", None))
#endif // QT_CONFIG(tooltip)
        self.mg.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.so4Sparge.setToolTip(QCoreApplication.translate("TabWater", u"Sulfate enhances the perception of crisp bitterness.", None))
#endif // QT_CONFIG(tooltip)
        self.so4Sparge.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.clSparge.setToolTip(QCoreApplication.translate("TabWater", u"Chloride enhances malty flavors.", None))
#endif // QT_CONFIG(tooltip)
        self.clSparge.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.clMash.setToolTip(QCoreApplication.translate("TabWater", u"Chloride enhances malty flavors.", None))
#endif // QT_CONFIG(tooltip)
        self.clMash.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.hco3Mash.setToolTip(QCoreApplication.translate("TabWater", u"Equivalent bicarbonate concentration.", None))
#endif // QT_CONFIG(tooltip)
        self.hco3Mash.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.ca.setToolTip(QCoreApplication.translate("TabWater", u"In general, at least 50 ppm of Calcium in the fermenter is recommended for yeast flocculation.", None))
#endif // QT_CONFIG(tooltip)
        self.ca.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.caMash.setToolTip(QCoreApplication.translate("TabWater", u"In general, at least 50 ppm of Calcium in the fermenter is recommended for yeast flocculation.", None))
#endif // QT_CONFIG(tooltip)
        self.caMash.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.lbl_so4.setToolTip(QCoreApplication.translate("TabWater", u"Sulfate enhances the perception of crisp bitterness.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_so4.setText(QCoreApplication.translate("TabWater", u"<html><head/><body><p>SO<span style=\" vertical-align:sub;\">4</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lbl_ca.setToolTip(QCoreApplication.translate("TabWater", u"In general, at least 50 ppm of Calcium in the fermenter is recommended for yeast flocculation.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_ca.setText(QCoreApplication.translate("TabWater", u"Ca", None))
#if QT_CONFIG(tooltip)
        self.naSparge.setToolTip(QCoreApplication.translate("TabWater", u"Sodium enhances flavors, but too much can cause a salty taste.", None))
#endif // QT_CONFIG(tooltip)
        self.naSparge.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.lbl_mg.setToolTip(QCoreApplication.translate("TabWater", u"Beer wort naturally contains more Magnesium than the yeast need. ", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_mg.setText(QCoreApplication.translate("TabWater", u"Mg", None))
#if QT_CONFIG(tooltip)
        self.naMash.setToolTip(QCoreApplication.translate("TabWater", u"Sodium enhances flavors, but too much can cause a salty taste.", None))
#endif // QT_CONFIG(tooltip)
        self.naMash.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.lbl_na.setToolTip(QCoreApplication.translate("TabWater", u"Sodium enhances flavors, but too much can cause a salty taste.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_na.setText(QCoreApplication.translate("TabWater", u"Na", None))
#if QT_CONFIG(tooltip)
        self.cl.setToolTip(QCoreApplication.translate("TabWater", u"Chloride enhances malty flavors.", None))
#endif // QT_CONFIG(tooltip)
        self.cl.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.na.setToolTip(QCoreApplication.translate("TabWater", u"Sodium enhances flavors, but too much can cause a salty taste.", None))
#endif // QT_CONFIG(tooltip)
        self.na.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.so4Mash.setToolTip(QCoreApplication.translate("TabWater", u"Sulfate enhances the perception of crisp bitterness.", None))
#endif // QT_CONFIG(tooltip)
        self.so4Mash.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.hco3Sparge.setToolTip(QCoreApplication.translate("TabWater", u"Equivalent bicarbonate concentration.", None))
#endif // QT_CONFIG(tooltip)
        self.hco3Sparge.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.caSparge.setToolTip(QCoreApplication.translate("TabWater", u"In general, at least 50 ppm of Calcium in the fermenter is recommended for yeast flocculation.", None))
#endif // QT_CONFIG(tooltip)
        self.caSparge.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.lbl_cl.setToolTip(QCoreApplication.translate("TabWater", u"Chloride enhances malty flavors.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_cl.setText(QCoreApplication.translate("TabWater", u"Cl", None))
#if QT_CONFIG(tooltip)
        self.lbl_hco3.setToolTip(QCoreApplication.translate("TabWater", u"Equivalent bicarbonate concentration.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_hco3.setText(QCoreApplication.translate("TabWater", u"<html><head/><body><p>HCO<span style=\" vertical-align:sub;\">3</span></p></body></html>", None))
        self.lbl_mashResults.setText(QCoreApplication.translate("TabWater", u"<html><head/><body><p>Mash H<span style=\" vertical-align:sub;\">2</span>O Concentrations:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.so4.setToolTip(QCoreApplication.translate("TabWater", u"Sulfate enhances the perception of crisp bitterness.", None))
#endif // QT_CONFIG(tooltip)
        self.so4.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
#if QT_CONFIG(tooltip)
        self.lbl_spargeResults.setToolTip(QCoreApplication.translate("TabWater", u"The words 'Sparge' and 'Kettle' are used somewhat interchangeably.  Sparge/Kettle salts should normally be added to the Kettle rather than to the sparge/mashout water.  The separate Sparge Water acidification calculation assumes these salts are added to the kettle (and so do not affect the sparge water acidification calculation).", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_spargeResults.setText(QCoreApplication.translate("TabWater", u"<html><head/><body><p>Sparge H<span style=\" vertical-align:sub;\">2</span>O Concentrations:</p></body></html>", None))
        self.lbl_overallResults.setText(QCoreApplication.translate("TabWater", u"<html><head/><body><p>Overall H<span style=\" vertical-align:sub;\">2</span>O Concentrations:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.hco3.setToolTip(QCoreApplication.translate("TabWater", u"Equivalent bicarbonate concentration.", None))
#endif // QT_CONFIG(tooltip)
        self.hco3.setPlaceholderText(QCoreApplication.translate("TabWater", u"0 ppm", None))
        self.groupBox.setTitle(QCoreApplication.translate("TabWater", u"Results:", None))
        self.lbl_chlorideSulfideRatio.setText(QCoreApplication.translate("TabWater", u"Chloride/Sulfide Ratio:", None))
#if QT_CONFIG(tooltip)
        self.ratio.setToolTip(QCoreApplication.translate("TabWater", u"Chloride/Sulfate ratios greater than 1.0 tend to accentuate malt flavors.  Chloride/Sulfate ratios less than 1.0 tend to accentuate crisp bitterness. ", None))
#endif // QT_CONFIG(tooltip)
        self.ratio.setPlaceholderText(QCoreApplication.translate("TabWater", u"N/A", None))
        self.lbl_mashPh.setText(QCoreApplication.translate("TabWater", u"Mash pH:", None))
#if QT_CONFIG(tooltip)
        self.ph.setToolTip(QCoreApplication.translate("TabWater", u"Ideally, mash pH should be in the range of 5.2 to 5.6, measured at room temperature.\n"
"\n"
"Note: For Step Mashes, this pH will not necessarily be accurate for any given step. It represents the pH that would be achieved in a single infusion with all of the recipe water.", None))
#endif // QT_CONFIG(tooltip)
        self.ph.setPlaceholderText(QCoreApplication.translate("TabWater", u"7", None))
    # retranslateUi

