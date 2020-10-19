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
        TabWater.resize(793, 518)
        self.gridLayout_3 = QGridLayout(TabWater)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.splitter_2 = QSplitter(TabWater)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.sourceWaterGroup = QGroupBox(self.splitter_2)
        self.sourceWaterGroup.setObjectName(u"sourceWaterGroup")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceWaterGroup.sizePolicy().hasHeightForWidth())
        self.sourceWaterGroup.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.sourceWaterGroup)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_name = QLabel(self.sourceWaterGroup)
        self.lbl_name.setObjectName(u"lbl_name")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_name)

        self.sourceName = QLineEdit(self.sourceWaterGroup)
        self.sourceName.setObjectName(u"sourceName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.sourceName)

        self.lbl_calcium = QLabel(self.sourceWaterGroup)
        self.lbl_calcium.setObjectName(u"lbl_calcium")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_calcium)

        self.sourceCalcium = QDoubleSpinBox(self.sourceWaterGroup)
        self.sourceCalcium.setObjectName(u"sourceCalcium")
        self.sourceCalcium.setDecimals(1)
        self.sourceCalcium.setMaximum(1000.000000000000000)
        self.sourceCalcium.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sourceCalcium)

        self.lbl_magnesium = QLabel(self.sourceWaterGroup)
        self.lbl_magnesium.setObjectName(u"lbl_magnesium")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_magnesium)

        self.sourceMagnesium = QDoubleSpinBox(self.sourceWaterGroup)
        self.sourceMagnesium.setObjectName(u"sourceMagnesium")
        self.sourceMagnesium.setDecimals(1)
        self.sourceMagnesium.setMaximum(1000.000000000000000)
        self.sourceMagnesium.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sourceMagnesium)

        self.lbl_sodium = QLabel(self.sourceWaterGroup)
        self.lbl_sodium.setObjectName(u"lbl_sodium")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_sodium)

        self.sourceSodium = QDoubleSpinBox(self.sourceWaterGroup)
        self.sourceSodium.setObjectName(u"sourceSodium")
        self.sourceSodium.setDecimals(1)
        self.sourceSodium.setMaximum(1000.000000000000000)
        self.sourceSodium.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sourceSodium)

        self.lbl_chloride = QLabel(self.sourceWaterGroup)
        self.lbl_chloride.setObjectName(u"lbl_chloride")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_chloride)

        self.sourceChloride = QDoubleSpinBox(self.sourceWaterGroup)
        self.sourceChloride.setObjectName(u"sourceChloride")
        self.sourceChloride.setDecimals(1)
        self.sourceChloride.setMaximum(1000.000000000000000)
        self.sourceChloride.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.sourceChloride)

        self.lbl_sulfate = QLabel(self.sourceWaterGroup)
        self.lbl_sulfate.setObjectName(u"lbl_sulfate")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_sulfate)

        self.sourceSulfate = QDoubleSpinBox(self.sourceWaterGroup)
        self.sourceSulfate.setObjectName(u"sourceSulfate")
        self.sourceSulfate.setDecimals(1)
        self.sourceSulfate.setMaximum(1000.000000000000000)
        self.sourceSulfate.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.sourceSulfate)

        self.lbl_bicarbonate = QLabel(self.sourceWaterGroup)
        self.lbl_bicarbonate.setObjectName(u"lbl_bicarbonate")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_bicarbonate)

        self.sourceBicarbonate = QDoubleSpinBox(self.sourceWaterGroup)
        self.sourceBicarbonate.setObjectName(u"sourceBicarbonate")
        self.sourceBicarbonate.setDecimals(1)
        self.sourceBicarbonate.setMaximum(1000.000000000000000)
        self.sourceBicarbonate.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.sourceBicarbonate)

        self.lbl_ph = QLabel(self.sourceWaterGroup)
        self.lbl_ph.setObjectName(u"lbl_ph")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lbl_ph)

        self.sourcePh = QDoubleSpinBox(self.sourceWaterGroup)
        self.sourcePh.setObjectName(u"sourcePh")
        self.sourcePh.setDecimals(1)
        self.sourcePh.setMaximum(14.000000000000000)
        self.sourcePh.setSingleStep(0.100000000000000)
        self.sourcePh.setValue(7.000000000000000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.sourcePh)

        self.splitter_2.addWidget(self.sourceWaterGroup)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ratioGroup = QGroupBox(self.layoutWidget)
        self.ratioGroup.setObjectName(u"ratioGroup")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ratioGroup.sizePolicy().hasHeightForWidth())
        self.ratioGroup.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.ratioGroup)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_source = QLabel(self.ratioGroup)
        self.lbl_source.setObjectName(u"lbl_source")

        self.gridLayout.addWidget(self.lbl_source, 1, 0, 1, 1)

        self.distilledPercent = QLineEdit(self.ratioGroup)
        self.distilledPercent.setObjectName(u"distilledPercent")
        self.distilledPercent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.distilledPercent.setReadOnly(True)

        self.gridLayout.addWidget(self.distilledPercent, 2, 1, 1, 1)

        self.sourcePercent = QLineEdit(self.ratioGroup)
        self.sourcePercent.setObjectName(u"sourcePercent")
        self.sourcePercent.setReadOnly(True)

        self.gridLayout.addWidget(self.sourcePercent, 2, 0, 1, 1)

        self.ratio = QSlider(self.ratioGroup)
        self.ratio.setObjectName(u"ratio")
        self.ratio.setMaximum(100)
        self.ratio.setValue(100)
        self.ratio.setOrientation(Qt.Horizontal)
        self.ratio.setInvertedAppearance(True)

        self.gridLayout.addWidget(self.ratio, 0, 0, 1, 2)

        self.lbl_distilled = QLabel(self.ratioGroup)
        self.lbl_distilled.setObjectName(u"lbl_distilled")
        self.lbl_distilled.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_distilled, 1, 1, 1, 1)

        self.sourceVolume = QLineEdit(self.ratioGroup)
        self.sourceVolume.setObjectName(u"sourceVolume")
        self.sourceVolume.setReadOnly(True)

        self.gridLayout.addWidget(self.sourceVolume, 3, 0, 1, 1)

        self.distilledVolume = QLineEdit(self.ratioGroup)
        self.distilledVolume.setObjectName(u"distilledVolume")
        self.distilledVolume.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.distilledVolume.setReadOnly(True)

        self.gridLayout.addWidget(self.distilledVolume, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.ratioGroup)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.splitter_2.addWidget(self.layoutWidget)
        self.sourceWaterGroup_2 = QGroupBox(self.splitter_2)
        self.sourceWaterGroup_2.setObjectName(u"sourceWaterGroup_2")
        sizePolicy1.setHeightForWidth(self.sourceWaterGroup_2.sizePolicy().hasHeightForWidth())
        self.sourceWaterGroup_2.setSizePolicy(sizePolicy1)
        self.formLayout_2 = QFormLayout(self.sourceWaterGroup_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_calcium_2 = QLabel(self.sourceWaterGroup_2)
        self.lbl_calcium_2.setObjectName(u"lbl_calcium_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_calcium_2)

        self.lbl_magnesium_2 = QLabel(self.sourceWaterGroup_2)
        self.lbl_magnesium_2.setObjectName(u"lbl_magnesium_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbl_magnesium_2)

        self.lbl_sodium_2 = QLabel(self.sourceWaterGroup_2)
        self.lbl_sodium_2.setObjectName(u"lbl_sodium_2")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lbl_sodium_2)

        self.lbl_chloride_2 = QLabel(self.sourceWaterGroup_2)
        self.lbl_chloride_2.setObjectName(u"lbl_chloride_2")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lbl_chloride_2)

        self.lbl_sulfate_2 = QLabel(self.sourceWaterGroup_2)
        self.lbl_sulfate_2.setObjectName(u"lbl_sulfate_2")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.lbl_sulfate_2)

        self.lbl_bicarbonate_2 = QLabel(self.sourceWaterGroup_2)
        self.lbl_bicarbonate_2.setObjectName(u"lbl_bicarbonate_2")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.lbl_bicarbonate_2)

        self.lbl_ph_2 = QLabel(self.sourceWaterGroup_2)
        self.lbl_ph_2.setObjectName(u"lbl_ph_2")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.lbl_ph_2)

        self.mixedCalcium = QLineEdit(self.sourceWaterGroup_2)
        self.mixedCalcium.setObjectName(u"mixedCalcium")
        self.mixedCalcium.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.mixedCalcium)

        self.mixedMagnesium = QLineEdit(self.sourceWaterGroup_2)
        self.mixedMagnesium.setObjectName(u"mixedMagnesium")
        self.mixedMagnesium.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.mixedMagnesium)

        self.mixedSodium = QLineEdit(self.sourceWaterGroup_2)
        self.mixedSodium.setObjectName(u"mixedSodium")
        self.mixedSodium.setReadOnly(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.mixedSodium)

        self.mixedChloride = QLineEdit(self.sourceWaterGroup_2)
        self.mixedChloride.setObjectName(u"mixedChloride")
        self.mixedChloride.setReadOnly(True)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.mixedChloride)

        self.mixedSulfate = QLineEdit(self.sourceWaterGroup_2)
        self.mixedSulfate.setObjectName(u"mixedSulfate")
        self.mixedSulfate.setReadOnly(True)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.mixedSulfate)

        self.mixedBicarbonate = QLineEdit(self.sourceWaterGroup_2)
        self.mixedBicarbonate.setObjectName(u"mixedBicarbonate")
        self.mixedBicarbonate.setReadOnly(True)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.mixedBicarbonate)

        self.mixedPh = QLineEdit(self.sourceWaterGroup_2)
        self.mixedPh.setObjectName(u"mixedPh")
        self.mixedPh.setReadOnly(True)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.mixedPh)

        self.splitter_2.addWidget(self.sourceWaterGroup_2)

        self.gridLayout_3.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.splitter = QSplitter(TabWater)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.load = QPushButton(self.splitter)
        self.load.setObjectName(u"load")
        self.load.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.load.sizePolicy().hasHeightForWidth())
        self.load.setSizePolicy(sizePolicy2)
        self.splitter.addWidget(self.load)

        self.gridLayout_3.addWidget(self.splitter, 1, 0, 1, 1)

        self.group_fermentables = QGroupBox(TabWater)
        self.group_fermentables.setObjectName(u"group_fermentables")
        self.gridLayout_2 = QGridLayout(self.group_fermentables)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.filter = QLineEdit(self.group_fermentables)
        self.filter.setObjectName(u"filter")

        self.gridLayout_2.addWidget(self.filter, 0, 0, 1, 1)

        self.library = QTableView(self.group_fermentables)
        self.library.setObjectName(u"library")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.library.sizePolicy().hasHeightForWidth())
        self.library.setSizePolicy(sizePolicy3)
        self.library.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.library.setAlternatingRowColors(True)
        self.library.setSelectionMode(QAbstractItemView.SingleSelection)
        self.library.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.library.setSortingEnabled(True)

        self.gridLayout_2.addWidget(self.library, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.group_fermentables, 2, 0, 1, 1)

        QWidget.setTabOrder(self.sourceName, self.sourceCalcium)
        QWidget.setTabOrder(self.sourceCalcium, self.sourceMagnesium)
        QWidget.setTabOrder(self.sourceMagnesium, self.sourceSodium)
        QWidget.setTabOrder(self.sourceSodium, self.sourceChloride)
        QWidget.setTabOrder(self.sourceChloride, self.sourceSulfate)
        QWidget.setTabOrder(self.sourceSulfate, self.sourceBicarbonate)
        QWidget.setTabOrder(self.sourceBicarbonate, self.sourcePh)
        QWidget.setTabOrder(self.sourcePh, self.ratio)
        QWidget.setTabOrder(self.ratio, self.load)
        QWidget.setTabOrder(self.load, self.filter)
        QWidget.setTabOrder(self.filter, self.library)
        QWidget.setTabOrder(self.library, self.sourcePercent)
        QWidget.setTabOrder(self.sourcePercent, self.distilledPercent)
        QWidget.setTabOrder(self.distilledPercent, self.mixedCalcium)
        QWidget.setTabOrder(self.mixedCalcium, self.mixedMagnesium)
        QWidget.setTabOrder(self.mixedMagnesium, self.mixedSodium)
        QWidget.setTabOrder(self.mixedSodium, self.mixedChloride)
        QWidget.setTabOrder(self.mixedChloride, self.mixedSulfate)
        QWidget.setTabOrder(self.mixedSulfate, self.mixedBicarbonate)
        QWidget.setTabOrder(self.mixedBicarbonate, self.mixedPh)

        self.retranslateUi(TabWater)

        QMetaObject.connectSlotsByName(TabWater)
    # setupUi

    def retranslateUi(self, TabWater):
        TabWater.setWindowTitle(QCoreApplication.translate("TabWater", u"Form", None))
        self.sourceWaterGroup.setTitle(QCoreApplication.translate("TabWater", u"Source Water Profile", None))
        self.lbl_name.setText(QCoreApplication.translate("TabWater", u"Name:", None))
        self.sourceName.setText(QCoreApplication.translate("TabWater", u"Distilled Water", None))
        self.lbl_calcium.setText(QCoreApplication.translate("TabWater", u"Calcium:", None))
        self.sourceCalcium.setSuffix(QCoreApplication.translate("TabWater", u" ppm", None))
        self.lbl_magnesium.setText(QCoreApplication.translate("TabWater", u"Magnesium:", None))
        self.sourceMagnesium.setSuffix(QCoreApplication.translate("TabWater", u" ppm", None))
        self.lbl_sodium.setText(QCoreApplication.translate("TabWater", u"Sodium:", None))
        self.sourceSodium.setSuffix(QCoreApplication.translate("TabWater", u" ppm", None))
        self.lbl_chloride.setText(QCoreApplication.translate("TabWater", u"Chloride:", None))
        self.sourceChloride.setSuffix(QCoreApplication.translate("TabWater", u" ppm", None))
        self.lbl_sulfate.setText(QCoreApplication.translate("TabWater", u"Sulfate:", None))
        self.sourceSulfate.setSuffix(QCoreApplication.translate("TabWater", u" ppm", None))
        self.lbl_bicarbonate.setText(QCoreApplication.translate("TabWater", u"Bicarbonate:", None))
        self.sourceBicarbonate.setSuffix(QCoreApplication.translate("TabWater", u" ppm", None))
        self.lbl_ph.setText(QCoreApplication.translate("TabWater", u"pH:", None))
        self.ratioGroup.setTitle(QCoreApplication.translate("TabWater", u"Source/Distilled Mix Ratio", None))
        self.lbl_source.setText(QCoreApplication.translate("TabWater", u"Source", None))
        self.distilledPercent.setText(QCoreApplication.translate("TabWater", u"0%", None))
        self.sourcePercent.setText(QCoreApplication.translate("TabWater", u"100%", None))
        self.lbl_distilled.setText(QCoreApplication.translate("TabWater", u"Distilled", None))
        self.sourceVolume.setText(QCoreApplication.translate("TabWater", u"0.0 gal", None))
        self.distilledVolume.setText(QCoreApplication.translate("TabWater", u"0.0 gal", None))
        self.sourceWaterGroup_2.setTitle(QCoreApplication.translate("TabWater", u"Brewing Water Profile", None))
        self.lbl_calcium_2.setText(QCoreApplication.translate("TabWater", u"Calcium:", None))
        self.lbl_magnesium_2.setText(QCoreApplication.translate("TabWater", u"Magnesium:", None))
        self.lbl_sodium_2.setText(QCoreApplication.translate("TabWater", u"Sodium:", None))
        self.lbl_chloride_2.setText(QCoreApplication.translate("TabWater", u"Chloride:", None))
        self.lbl_sulfate_2.setText(QCoreApplication.translate("TabWater", u"Sulfate:", None))
        self.lbl_bicarbonate_2.setText(QCoreApplication.translate("TabWater", u"Bicarbonate:", None))
        self.lbl_ph_2.setText(QCoreApplication.translate("TabWater", u"pH:", None))
        self.mixedCalcium.setText(QCoreApplication.translate("TabWater", u"0.0 ppm", None))
        self.mixedMagnesium.setText(QCoreApplication.translate("TabWater", u"0.0 ppm", None))
        self.mixedSodium.setText(QCoreApplication.translate("TabWater", u"0.0 ppm", None))
        self.mixedChloride.setText(QCoreApplication.translate("TabWater", u"0.0 ppm", None))
        self.mixedSulfate.setText(QCoreApplication.translate("TabWater", u"0.0 ppm", None))
        self.mixedBicarbonate.setText(QCoreApplication.translate("TabWater", u"0.0 ppm", None))
        self.mixedPh.setText(QCoreApplication.translate("TabWater", u"7.0", None))
        self.load.setText(QCoreApplication.translate("TabWater", u"Load Selected Profile", None))
        self.group_fermentables.setTitle(QCoreApplication.translate("TabWater", u"Ingredient Library", None))
        self.filter.setPlaceholderText(QCoreApplication.translate("TabWater", u"Filter...", None))
    # retranslateUi

