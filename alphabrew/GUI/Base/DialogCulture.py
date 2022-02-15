# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogCulture.ui'
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


class Ui_DialogCulture(object):
    def setupUi(self, DialogCulture):
        if DialogCulture.objectName():
            DialogCulture.setObjectName(u"DialogCulture")
        DialogCulture.resize(422, 304)
        DialogCulture.setMinimumSize(QSize(422, 304))
        DialogCulture.setMaximumSize(QSize(16777215, 330))
        self.verticalLayout = QVBoxLayout(DialogCulture)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_name = QLabel(DialogCulture)
        self.lbl_name.setObjectName(u"lbl_name")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_name)

        self.name = QLineEdit(DialogCulture)
        self.name.setObjectName(u"name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name)

        self.lbl_type = QLabel(DialogCulture)
        self.lbl_type.setObjectName(u"lbl_type")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_type)

        self.type = QComboBox(DialogCulture)
        self.type.setObjectName(u"type")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.type)

        self.lbl_form = QLabel(DialogCulture)
        self.lbl_form.setObjectName(u"lbl_form")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_form)

        self.form = QComboBox(DialogCulture)
        self.form.setObjectName(u"form")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.form)

        self.lbl_producer = QLabel(DialogCulture)
        self.lbl_producer.setObjectName(u"lbl_producer")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_producer)

        self.producer = QLineEdit(DialogCulture)
        self.producer.setObjectName(u"producer")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.producer)

        self.lbl_productId = QLabel(DialogCulture)
        self.lbl_productId.setObjectName(u"lbl_productId")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_productId)

        self.productId = QLineEdit(DialogCulture)
        self.productId.setObjectName(u"productId")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.productId)

        self.lbl_attenuation_min = QLabel(DialogCulture)
        self.lbl_attenuation_min.setObjectName(u"lbl_attenuation_min")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_attenuation_min)

        self.lbl_attenuation_max = QLabel(DialogCulture)
        self.lbl_attenuation_max.setObjectName(u"lbl_attenuation_max")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_attenuation_max)

        self.minAttenuation = QDoubleSpinBox(DialogCulture)
        self.minAttenuation.setObjectName(u"minAttenuation")
        self.minAttenuation.setDecimals(0)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.minAttenuation)

        self.maxAttenuation = QDoubleSpinBox(DialogCulture)
        self.maxAttenuation.setObjectName(u"maxAttenuation")
        self.maxAttenuation.setDecimals(0)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.maxAttenuation)


        self.verticalLayout.addLayout(self.formLayout)

        self.notes = QPlainTextEdit(DialogCulture)
        self.notes.setObjectName(u"notes")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.notes.sizePolicy().hasHeightForWidth())
        self.notes.setSizePolicy(sizePolicy)
        self.notes.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.notes)

        self.buttonBox = QDialogButtonBox(DialogCulture)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogCulture)
        self.buttonBox.accepted.connect(DialogCulture.accept)
        self.buttonBox.rejected.connect(DialogCulture.reject)

        QMetaObject.connectSlotsByName(DialogCulture)
    # setupUi

    def retranslateUi(self, DialogCulture):
        DialogCulture.setWindowTitle(QCoreApplication.translate("DialogCulture", u"Dialog", None))
        self.lbl_name.setText(QCoreApplication.translate("DialogCulture", u"Name:", None))
        self.lbl_type.setText(QCoreApplication.translate("DialogCulture", u"Type:", None))
        self.lbl_form.setText(QCoreApplication.translate("DialogCulture", u"Form:", None))
        self.lbl_producer.setText(QCoreApplication.translate("DialogCulture", u"Producer:", None))
        self.lbl_productId.setText(QCoreApplication.translate("DialogCulture", u"Product ID:", None))
        self.lbl_attenuation_min.setText(QCoreApplication.translate("DialogCulture", u"Min Attenuation:", None))
        self.lbl_attenuation_max.setText(QCoreApplication.translate("DialogCulture", u"Max Attenuation:", None))
        self.minAttenuation.setSuffix(QCoreApplication.translate("DialogCulture", u"%", None))
        self.maxAttenuation.setSuffix(QCoreApplication.translate("DialogCulture", u"%", None))
    # retranslateUi

