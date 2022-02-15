# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogFermentable.ui'
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


class Ui_DialogFermentable(object):
    def setupUi(self, DialogFermentable):
        if DialogFermentable.objectName():
            DialogFermentable.setObjectName(u"DialogFermentable")
        DialogFermentable.resize(422, 470)
        DialogFermentable.setMinimumSize(QSize(422, 470))
        DialogFermentable.setMaximumSize(QSize(16777215, 470))
        self.verticalLayout = QVBoxLayout(DialogFermentable)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_name = QLabel(DialogFermentable)
        self.lbl_name.setObjectName(u"lbl_name")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_name)

        self.name = QLineEdit(DialogFermentable)
        self.name.setObjectName(u"name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name)

        self.lbl_type = QLabel(DialogFermentable)
        self.lbl_type.setObjectName(u"lbl_type")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_type)

        self.type = QComboBox(DialogFermentable)
        self.type.setObjectName(u"type")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.type)

        self.lbl_group = QLabel(DialogFermentable)
        self.lbl_group.setObjectName(u"lbl_group")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_group)

        self.group = QComboBox(DialogFermentable)
        self.group.setObjectName(u"group")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.group)

        self.lbl_producer = QLabel(DialogFermentable)
        self.lbl_producer.setObjectName(u"lbl_producer")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_producer)

        self.producer = QLineEdit(DialogFermentable)
        self.producer.setObjectName(u"producer")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.producer)

        self.lbl_origin = QLabel(DialogFermentable)
        self.lbl_origin.setObjectName(u"lbl_origin")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_origin)

        self.origin = QLineEdit(DialogFermentable)
        self.origin.setObjectName(u"origin")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.origin)

        self.lbl_yield = QLabel(DialogFermentable)
        self.lbl_yield.setObjectName(u"lbl_yield")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_yield)

        self.fyield = QDoubleSpinBox(DialogFermentable)
        self.fyield.setObjectName(u"fyield")
        self.fyield.setDecimals(1)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.fyield)

        self.lbl_color = QLabel(DialogFermentable)
        self.lbl_color.setObjectName(u"lbl_color")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_color)

        self.color = QDoubleSpinBox(DialogFermentable)
        self.color.setObjectName(u"color")
        self.color.setDecimals(1)
        self.color.setMaximum(1000.000000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.color)

        self.lbl_moisture = QLabel(DialogFermentable)
        self.lbl_moisture.setObjectName(u"lbl_moisture")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lbl_moisture)

        self.moisture = QDoubleSpinBox(DialogFermentable)
        self.moisture.setObjectName(u"moisture")
        self.moisture.setDecimals(1)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.moisture)

        self.lbl_diastatic_power = QLabel(DialogFermentable)
        self.lbl_diastatic_power.setObjectName(u"lbl_diastatic_power")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.lbl_diastatic_power)

        self.diastaticPower = QSpinBox(DialogFermentable)
        self.diastaticPower.setObjectName(u"diastaticPower")
        self.diastaticPower.setMaximum(200)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.diastaticPower)

        self.lbl_addAfterBoil = QLabel(DialogFermentable)
        self.lbl_addAfterBoil.setObjectName(u"lbl_addAfterBoil")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.lbl_addAfterBoil)

        self.addAfterBoil = QCheckBox(DialogFermentable)
        self.addAfterBoil.setObjectName(u"addAfterBoil")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.addAfterBoil)

        self.lbl_mashed = QLabel(DialogFermentable)
        self.lbl_mashed.setObjectName(u"lbl_mashed")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.lbl_mashed)

        self.mashed = QCheckBox(DialogFermentable)
        self.mashed.setObjectName(u"mashed")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.mashed)

        self.lbl_phi = QLabel(DialogFermentable)
        self.lbl_phi.setObjectName(u"lbl_phi")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.lbl_phi)

        self.lbl_bi = QLabel(DialogFermentable)
        self.lbl_bi.setObjectName(u"lbl_bi")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.lbl_bi)

        self.phi = QDoubleSpinBox(DialogFermentable)
        self.phi.setObjectName(u"phi")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.phi)

        self.bi = QDoubleSpinBox(DialogFermentable)
        self.bi.setObjectName(u"bi")
        self.bi.setMaximum(500.000000000000000)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.bi)


        self.verticalLayout.addLayout(self.formLayout)

        self.notes = QPlainTextEdit(DialogFermentable)
        self.notes.setObjectName(u"notes")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.notes.sizePolicy().hasHeightForWidth())
        self.notes.setSizePolicy(sizePolicy)
        self.notes.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.notes)

        self.buttonBox = QDialogButtonBox(DialogFermentable)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogFermentable)
        self.buttonBox.accepted.connect(DialogFermentable.accept)
        self.buttonBox.rejected.connect(DialogFermentable.reject)

        QMetaObject.connectSlotsByName(DialogFermentable)
    # setupUi

    def retranslateUi(self, DialogFermentable):
        DialogFermentable.setWindowTitle(QCoreApplication.translate("DialogFermentable", u"Dialog", None))
        self.lbl_name.setText(QCoreApplication.translate("DialogFermentable", u"Name:", None))
        self.lbl_type.setText(QCoreApplication.translate("DialogFermentable", u"Type:", None))
        self.lbl_group.setText(QCoreApplication.translate("DialogFermentable", u"Grain Group:", None))
        self.lbl_producer.setText(QCoreApplication.translate("DialogFermentable", u"Producer:", None))
        self.lbl_origin.setText(QCoreApplication.translate("DialogFermentable", u"Origin:", None))
        self.lbl_yield.setText(QCoreApplication.translate("DialogFermentable", u"Yield:", None))
#if QT_CONFIG(tooltip)
        self.fyield.setToolTip(QCoreApplication.translate("DialogFermentable", u"Percentage yield compared to succrose.", None))
#endif // QT_CONFIG(tooltip)
        self.fyield.setSuffix(QCoreApplication.translate("DialogFermentable", u"%", None))
        self.lbl_color.setText(QCoreApplication.translate("DialogFermentable", u"Color:", None))
        self.color.setSuffix(QCoreApplication.translate("DialogFermentable", u" srm", None))
        self.lbl_moisture.setText(QCoreApplication.translate("DialogFermentable", u"Moisture:", None))
        self.moisture.setSuffix(QCoreApplication.translate("DialogFermentable", u"%", None))
        self.lbl_diastatic_power.setText(QCoreApplication.translate("DialogFermentable", u"Diastatic Power:", None))
#if QT_CONFIG(tooltip)
        self.diastaticPower.setToolTip(QCoreApplication.translate("DialogFermentable", u"Diastatic power is a measurement of malted grains enzymatic content. A value of 35 Lintner is needed to self convert, while a value of 100 or more is desirable.", None))
#endif // QT_CONFIG(tooltip)
        self.diastaticPower.setSuffix(QCoreApplication.translate("DialogFermentable", u" Lintner", None))
        self.lbl_addAfterBoil.setText(QCoreApplication.translate("DialogFermentable", u"Add After Boil:", None))
        self.lbl_mashed.setText(QCoreApplication.translate("DialogFermentable", u"Mash Required:", None))
#if QT_CONFIG(tooltip)
        self.mashed.setToolTip(QCoreApplication.translate("DialogFermentable", u"True if the fermentable must be mashed, false if it can be steeped.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_phi.setText(QCoreApplication.translate("DialogFermentable", u"pH_i:", None))
        self.lbl_bi.setText(QCoreApplication.translate("DialogFermentable", u"B_i:", None))
#if QT_CONFIG(tooltip)
        self.phi.setToolTip(QCoreApplication.translate("DialogFermentable", u"This is the distilled water mash pH for this grain.  A value of zero is expected when unknown.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.bi.setToolTip(QCoreApplication.translate("DialogFermentable", u"Distilled water mash buffering capacity of this grain - zero implies unknown.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

