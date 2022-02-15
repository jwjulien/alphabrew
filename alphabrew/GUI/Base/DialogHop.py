# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogHop.ui'
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


class Ui_DialogHop(object):
    def setupUi(self, DialogHop):
        if DialogHop.objectName():
            DialogHop.setObjectName(u"DialogHop")
        DialogHop.resize(422, 460)
        DialogHop.setMinimumSize(QSize(422, 432))
        DialogHop.setMaximumSize(QSize(16777215, 460))
        self.verticalLayout = QVBoxLayout(DialogHop)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_name = QLabel(DialogHop)
        self.lbl_name.setObjectName(u"lbl_name")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_name)

        self.name = QLineEdit(DialogHop)
        self.name.setObjectName(u"name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name)

        self.lbl_type = QLabel(DialogHop)
        self.lbl_type.setObjectName(u"lbl_type")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_type)

        self.type = QComboBox(DialogHop)
        self.type.setObjectName(u"type")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.type)

        self.lbl_form = QLabel(DialogHop)
        self.lbl_form.setObjectName(u"lbl_form")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_form)

        self.form = QComboBox(DialogHop)
        self.form.setObjectName(u"form")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.form)

        self.lbl_alpha = QLabel(DialogHop)
        self.lbl_alpha.setObjectName(u"lbl_alpha")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_alpha)

        self.alpha = QDoubleSpinBox(DialogHop)
        self.alpha.setObjectName(u"alpha")
        self.alpha.setDecimals(1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.alpha)

        self.lbl_beta = QLabel(DialogHop)
        self.lbl_beta.setObjectName(u"lbl_beta")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_beta)

        self.beta = QDoubleSpinBox(DialogHop)
        self.beta.setObjectName(u"beta")
        self.beta.setDecimals(1)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.beta)

        self.lbl_hsi = QLabel(DialogHop)
        self.lbl_hsi.setObjectName(u"lbl_hsi")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_hsi)

        self.hsi = QDoubleSpinBox(DialogHop)
        self.hsi.setObjectName(u"hsi")
        self.hsi.setDecimals(1)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.hsi)

        self.lbl_origin = QLabel(DialogHop)
        self.lbl_origin.setObjectName(u"lbl_origin")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_origin)

        self.origin = QLineEdit(DialogHop)
        self.origin.setObjectName(u"origin")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.origin)

        self.caryophyllene = QDoubleSpinBox(DialogHop)
        self.caryophyllene.setObjectName(u"caryophyllene")
        self.caryophyllene.setDecimals(1)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.caryophyllene)

        self.cohumulone = QDoubleSpinBox(DialogHop)
        self.cohumulone.setObjectName(u"cohumulone")
        self.cohumulone.setDecimals(1)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.cohumulone)

        self.substitutes = QLineEdit(DialogHop)
        self.substitutes.setObjectName(u"substitutes")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.substitutes)

        self.lbl_substitutes = QLabel(DialogHop)
        self.lbl_substitutes.setObjectName(u"lbl_substitutes")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lbl_substitutes)

        self.lbl_humulene = QLabel(DialogHop)
        self.lbl_humulene.setObjectName(u"lbl_humulene")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.lbl_humulene)

        self.lbl_caryophyllene = QLabel(DialogHop)
        self.lbl_caryophyllene.setObjectName(u"lbl_caryophyllene")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.lbl_caryophyllene)

        self.lbl_cohumulone = QLabel(DialogHop)
        self.lbl_cohumulone.setObjectName(u"lbl_cohumulone")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.lbl_cohumulone)

        self.lbl_myrcene = QLabel(DialogHop)
        self.lbl_myrcene.setObjectName(u"lbl_myrcene")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.lbl_myrcene)

        self.myrcene = QDoubleSpinBox(DialogHop)
        self.myrcene.setObjectName(u"myrcene")
        self.myrcene.setDecimals(1)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.myrcene)

        self.humulene = QDoubleSpinBox(DialogHop)
        self.humulene.setObjectName(u"humulene")
        self.humulene.setDecimals(1)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.humulene)


        self.verticalLayout.addLayout(self.formLayout)

        self.notes = QPlainTextEdit(DialogHop)
        self.notes.setObjectName(u"notes")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.notes.sizePolicy().hasHeightForWidth())
        self.notes.setSizePolicy(sizePolicy)
        self.notes.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.notes)

        self.buttonBox = QDialogButtonBox(DialogHop)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogHop)
        self.buttonBox.accepted.connect(DialogHop.accept)
        self.buttonBox.rejected.connect(DialogHop.reject)

        QMetaObject.connectSlotsByName(DialogHop)
    # setupUi

    def retranslateUi(self, DialogHop):
        DialogHop.setWindowTitle(QCoreApplication.translate("DialogHop", u"Dialog", None))
        self.lbl_name.setText(QCoreApplication.translate("DialogHop", u"Name:", None))
        self.lbl_type.setText(QCoreApplication.translate("DialogHop", u"Type:", None))
        self.lbl_form.setText(QCoreApplication.translate("DialogHop", u"Form:", None))
        self.lbl_alpha.setText(QCoreApplication.translate("DialogHop", u"Alpha Acid:", None))
#if QT_CONFIG(tooltip)
        self.alpha.setToolTip(QCoreApplication.translate("DialogHop", u"Percentage yield compared to succrose.", None))
#endif // QT_CONFIG(tooltip)
        self.alpha.setSuffix(QCoreApplication.translate("DialogHop", u"%", None))
        self.lbl_beta.setText(QCoreApplication.translate("DialogHop", u"Beta Acid:", None))
        self.beta.setSuffix(QCoreApplication.translate("DialogHop", u"%", None))
#if QT_CONFIG(tooltip)
        self.lbl_hsi.setToolTip(QCoreApplication.translate("DialogHop", u"Hop Storage Index", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_hsi.setText(QCoreApplication.translate("DialogHop", u"HSI:", None))
#if QT_CONFIG(tooltip)
        self.hsi.setToolTip(QCoreApplication.translate("DialogHop", u"The percentage of protein. Higher values may indicate a possibility of haze, or lautering issues.", None))
#endif // QT_CONFIG(tooltip)
        self.hsi.setSuffix(QCoreApplication.translate("DialogHop", u"%", None))
        self.lbl_origin.setText(QCoreApplication.translate("DialogHop", u"Origin:", None))
#if QT_CONFIG(tooltip)
        self.caryophyllene.setToolTip(QCoreApplication.translate("DialogHop", u"The recommended maximum percentage to use in a grain bill.", None))
#endif // QT_CONFIG(tooltip)
        self.caryophyllene.setSuffix(QCoreApplication.translate("DialogHop", u"%", None))
#if QT_CONFIG(tooltip)
        self.cohumulone.setToolTip(QCoreApplication.translate("DialogHop", u"The difference between fine and coarse grind, a difference more than 2 percent can indicate a protein or step mash may be desirable.", None))
#endif // QT_CONFIG(tooltip)
        self.cohumulone.setSuffix(QCoreApplication.translate("DialogHop", u"%", None))
        self.lbl_substitutes.setText(QCoreApplication.translate("DialogHop", u"Substitutes:", None))
        self.lbl_humulene.setText(QCoreApplication.translate("DialogHop", u"Humulene:", None))
        self.lbl_caryophyllene.setText(QCoreApplication.translate("DialogHop", u"Caryophyllene:", None))
        self.lbl_cohumulone.setText(QCoreApplication.translate("DialogHop", u"Cohumulone:", None))
        self.lbl_myrcene.setText(QCoreApplication.translate("DialogHop", u"Myrcene:", None))
#if QT_CONFIG(tooltip)
        self.myrcene.setToolTip(QCoreApplication.translate("DialogHop", u"The difference between fine and coarse grind, a difference more than 2 percent can indicate a protein or step mash may be desirable.", None))
#endif // QT_CONFIG(tooltip)
        self.myrcene.setSuffix(QCoreApplication.translate("DialogHop", u"%", None))
#if QT_CONFIG(tooltip)
        self.humulene.setToolTip(QCoreApplication.translate("DialogHop", u"The difference between fine and coarse grind, a difference more than 2 percent can indicate a protein or step mash may be desirable.", None))
#endif // QT_CONFIG(tooltip)
        self.humulene.setSuffix(QCoreApplication.translate("DialogHop", u"%", None))
    # retranslateUi

