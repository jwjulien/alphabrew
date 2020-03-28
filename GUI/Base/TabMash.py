# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TabMash.ui'
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


class Ui_TabMash(object):
    def setupUi(self, TabMash):
        if TabMash.objectName():
            TabMash.setObjectName(u"TabMash")
        TabMash.resize(694, 300)
        self.time_mash = QSpinBox(TabMash)
        self.time_mash.setObjectName(u"time_mash")
        self.time_mash.setGeometry(QRect(80, 20, 656, 20))
        self.time_mash.setMaximum(240)
        self.time_mash.setValue(60)
        self.lbl_mash_time = QLabel(TabMash)
        self.lbl_mash_time.setObjectName(u"lbl_mash_time")
        self.lbl_mash_time.setGeometry(QRect(20, 20, 54, 20))

        self.retranslateUi(TabMash)

        QMetaObject.connectSlotsByName(TabMash)
    # setupUi

    def retranslateUi(self, TabMash):
        TabMash.setWindowTitle(QCoreApplication.translate("TabMash", u"Form", None))
        self.time_mash.setSuffix(QCoreApplication.translate("TabMash", u" min", None))
        self.lbl_mash_time.setText(QCoreApplication.translate("TabMash", u"Mash Time:", None))
    # retranslateUi

