# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TabRecipe.ui'
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


class Ui_TabRecipe(object):
    def setupUi(self, TabRecipe):
        if TabRecipe.objectName():
            TabRecipe.setObjectName(u"TabRecipe")
        TabRecipe.resize(400, 302)
        self.formLayout = QFormLayout(TabRecipe)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_name = QLabel(TabRecipe)
        self.lbl_name.setObjectName(u"lbl_name")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_name)

        self.name = QLineEdit(TabRecipe)
        self.name.setObjectName(u"name")
        self.name.setMaxLength(80)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name)

        self.lbl_author = QLabel(TabRecipe)
        self.lbl_author.setObjectName(u"lbl_author")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_author)

        self.author = QLineEdit(TabRecipe)
        self.author.setObjectName(u"author")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.author)

        self.lbl_style = QLabel(TabRecipe)
        self.lbl_style.setObjectName(u"lbl_style")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_style)

        self.style = QComboBox(TabRecipe)
        self.style.setObjectName(u"style")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.style)

        self.lbl_type = QLabel(TabRecipe)
        self.lbl_type.setObjectName(u"lbl_type")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_type)

        self.rtype = QComboBox(TabRecipe)
        self.rtype.setObjectName(u"rtype")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.rtype)

        self.lbl_equipment = QLabel(TabRecipe)
        self.lbl_equipment.setObjectName(u"lbl_equipment")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_equipment)

        self.equipment = QComboBox(TabRecipe)
        self.equipment.setObjectName(u"equipment")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.equipment)

        self.lbl_size = QLabel(TabRecipe)
        self.lbl_size.setObjectName(u"lbl_size")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_size)

        self.size = QDoubleSpinBox(TabRecipe)
        self.size.setObjectName(u"size")
        self.size.setDecimals(1)
        self.size.setMaximum(630.000000000000000)
        self.size.setSingleStep(0.100000000000000)
        self.size.setValue(6.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.size)

        self.lbl_boil_time = QLabel(TabRecipe)
        self.lbl_boil_time.setObjectName(u"lbl_boil_time")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_boil_time)

        self.time_boil = QSpinBox(TabRecipe)
        self.time_boil.setObjectName(u"time_boil")
        self.time_boil.setMaximum(240)
        self.time_boil.setValue(60)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.time_boil)

        self.lbl_ambient = QLabel(TabRecipe)
        self.lbl_ambient.setObjectName(u"lbl_ambient")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lbl_ambient)

        self.ambient = QSpinBox(TabRecipe)
        self.ambient.setObjectName(u"ambient")
        self.ambient.setMinimum(0)
        self.ambient.setMaximum(120)
        self.ambient.setValue(65)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.ambient)


        self.retranslateUi(TabRecipe)

        QMetaObject.connectSlotsByName(TabRecipe)
    # setupUi

    def retranslateUi(self, TabRecipe):
        TabRecipe.setWindowTitle(QCoreApplication.translate("TabRecipe", u"Form", None))
        self.lbl_name.setText(QCoreApplication.translate("TabRecipe", u"Name:", None))
        self.lbl_author.setText(QCoreApplication.translate("TabRecipe", u"Author:", None))
        self.lbl_style.setText(QCoreApplication.translate("TabRecipe", u"Style:", None))
        self.lbl_type.setText(QCoreApplication.translate("TabRecipe", u"Type:", None))
        self.lbl_equipment.setText(QCoreApplication.translate("TabRecipe", u"Equipment:", None))
        self.lbl_size.setText(QCoreApplication.translate("TabRecipe", u"Batch Size:", None))
#if QT_CONFIG(tooltip)
        self.size.setToolTip(QCoreApplication.translate("TabRecipe", u"Volume into the fermentor.", None))
#endif // QT_CONFIG(tooltip)
        self.size.setSuffix(QCoreApplication.translate("TabRecipe", u" gal", None))
        self.lbl_boil_time.setText(QCoreApplication.translate("TabRecipe", u"Boil Time:", None))
        self.time_boil.setSuffix(QCoreApplication.translate("TabRecipe", u" min", None))
        self.lbl_ambient.setText(QCoreApplication.translate("TabRecipe", u"Ambient Temperature:", None))
#if QT_CONFIG(tooltip)
        self.ambient.setToolTip(QCoreApplication.translate("TabRecipe", u"Starting temperature of the grains and mash tun.", None))
#endif // QT_CONFIG(tooltip)
        self.ambient.setSuffix(QCoreApplication.translate("TabRecipe", u" \u00b0F", None))
    # retranslateUi

