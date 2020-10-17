# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogWater.ui'
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


class Ui_DialogWater(object):
    def setupUi(self, DialogWater):
        if DialogWater.objectName():
            DialogWater.setObjectName(u"DialogWater")
        DialogWater.resize(400, 358)
        DialogWater.setMinimumSize(QSize(400, 358))
        DialogWater.setMaximumSize(QSize(16777215, 460))
        self.verticalLayout = QVBoxLayout(DialogWater)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_name = QLabel(DialogWater)
        self.lbl_name.setObjectName(u"lbl_name")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_name)

        self.name = QLineEdit(DialogWater)
        self.name.setObjectName(u"name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name)

        self.lbl_calcium = QLabel(DialogWater)
        self.lbl_calcium.setObjectName(u"lbl_calcium")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_calcium)

        self.calcium = QDoubleSpinBox(DialogWater)
        self.calcium.setObjectName(u"calcium")
        self.calcium.setDecimals(1)
        self.calcium.setMaximum(1000.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.calcium)

        self.lbl_magnesium = QLabel(DialogWater)
        self.lbl_magnesium.setObjectName(u"lbl_magnesium")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_magnesium)

        self.magnesium = QDoubleSpinBox(DialogWater)
        self.magnesium.setObjectName(u"magnesium")
        self.magnesium.setDecimals(1)
        self.magnesium.setMaximum(1000.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.magnesium)

        self.lbl_sodium = QLabel(DialogWater)
        self.lbl_sodium.setObjectName(u"lbl_sodium")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_sodium)

        self.sodium = QDoubleSpinBox(DialogWater)
        self.sodium.setObjectName(u"sodium")
        self.sodium.setDecimals(1)
        self.sodium.setMaximum(1000.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sodium)

        self.lbl_chloride = QLabel(DialogWater)
        self.lbl_chloride.setObjectName(u"lbl_chloride")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_chloride)

        self.chloride = QDoubleSpinBox(DialogWater)
        self.chloride.setObjectName(u"chloride")
        self.chloride.setDecimals(1)
        self.chloride.setMaximum(1000.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.chloride)

        self.lbl_sulfate = QLabel(DialogWater)
        self.lbl_sulfate.setObjectName(u"lbl_sulfate")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_sulfate)

        self.sulfate = QDoubleSpinBox(DialogWater)
        self.sulfate.setObjectName(u"sulfate")
        self.sulfate.setDecimals(1)
        self.sulfate.setMaximum(1000.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.sulfate)

        self.lbl_bicarbonate = QLabel(DialogWater)
        self.lbl_bicarbonate.setObjectName(u"lbl_bicarbonate")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_bicarbonate)

        self.bicarbonate = QDoubleSpinBox(DialogWater)
        self.bicarbonate.setObjectName(u"bicarbonate")
        self.bicarbonate.setDecimals(1)
        self.bicarbonate.setMaximum(1000.000000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.bicarbonate)

        self.lbl_ph = QLabel(DialogWater)
        self.lbl_ph.setObjectName(u"lbl_ph")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lbl_ph)

        self.ph = QDoubleSpinBox(DialogWater)
        self.ph.setObjectName(u"ph")
        self.ph.setDecimals(1)
        self.ph.setMinimum(1.000000000000000)
        self.ph.setMaximum(14.000000000000000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.ph)


        self.verticalLayout.addLayout(self.formLayout)

        self.notes = QPlainTextEdit(DialogWater)
        self.notes.setObjectName(u"notes")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.notes.sizePolicy().hasHeightForWidth())
        self.notes.setSizePolicy(sizePolicy)
        self.notes.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.notes)

        self.buttonBox = QDialogButtonBox(DialogWater)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogWater)
        self.buttonBox.accepted.connect(DialogWater.accept)
        self.buttonBox.rejected.connect(DialogWater.reject)

        QMetaObject.connectSlotsByName(DialogWater)
    # setupUi

    def retranslateUi(self, DialogWater):
        DialogWater.setWindowTitle(QCoreApplication.translate("DialogWater", u"Dialog", None))
        self.lbl_name.setText(QCoreApplication.translate("DialogWater", u"Name:", None))
        self.lbl_calcium.setText(QCoreApplication.translate("DialogWater", u"Calcium:", None))
#if QT_CONFIG(tooltip)
        self.calcium.setToolTip(QCoreApplication.translate("DialogWater", u"Percentage yield compared to succrose.", None))
#endif // QT_CONFIG(tooltip)
        self.calcium.setSuffix(QCoreApplication.translate("DialogWater", u" ppm", None))
        self.lbl_magnesium.setText(QCoreApplication.translate("DialogWater", u"Magnesium:", None))
#if QT_CONFIG(tooltip)
        self.magnesium.setToolTip(QCoreApplication.translate("DialogWater", u"Percentage yield compared to succrose.", None))
#endif // QT_CONFIG(tooltip)
        self.magnesium.setSuffix(QCoreApplication.translate("DialogWater", u" ppm", None))
#if QT_CONFIG(tooltip)
        self.lbl_sodium.setToolTip(QCoreApplication.translate("DialogWater", u"Hop Storage Index", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_sodium.setText(QCoreApplication.translate("DialogWater", u"Sodium:", None))
#if QT_CONFIG(tooltip)
        self.sodium.setToolTip(QCoreApplication.translate("DialogWater", u"Percentage yield compared to succrose.", None))
#endif // QT_CONFIG(tooltip)
        self.sodium.setSuffix(QCoreApplication.translate("DialogWater", u" ppm", None))
        self.lbl_chloride.setText(QCoreApplication.translate("DialogWater", u"Chloride:", None))
#if QT_CONFIG(tooltip)
        self.chloride.setToolTip(QCoreApplication.translate("DialogWater", u"Percentage yield compared to succrose.", None))
#endif // QT_CONFIG(tooltip)
        self.chloride.setSuffix(QCoreApplication.translate("DialogWater", u" ppm", None))
        self.lbl_sulfate.setText(QCoreApplication.translate("DialogWater", u"Sulfate:", None))
#if QT_CONFIG(tooltip)
        self.sulfate.setToolTip(QCoreApplication.translate("DialogWater", u"Percentage yield compared to succrose.", None))
#endif // QT_CONFIG(tooltip)
        self.sulfate.setSuffix(QCoreApplication.translate("DialogWater", u" ppm", None))
        self.lbl_bicarbonate.setText(QCoreApplication.translate("DialogWater", u"Bicarbonate:", None))
#if QT_CONFIG(tooltip)
        self.bicarbonate.setToolTip(QCoreApplication.translate("DialogWater", u"Percentage yield compared to succrose.", None))
#endif // QT_CONFIG(tooltip)
        self.bicarbonate.setSuffix(QCoreApplication.translate("DialogWater", u" ppm", None))
        self.lbl_ph.setText(QCoreApplication.translate("DialogWater", u"pH:", None))
#if QT_CONFIG(tooltip)
        self.ph.setToolTip(QCoreApplication.translate("DialogWater", u"Percentage yield compared to succrose.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

