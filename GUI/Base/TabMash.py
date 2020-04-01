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
        TabMash.resize(763, 478)
        self.verticalLayout = QVBoxLayout(TabMash)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.steps = QTableView(TabMash)
        self.steps.setObjectName(u"steps")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.steps.sizePolicy().hasHeightForWidth())
        self.steps.setSizePolicy(sizePolicy)
        self.steps.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.steps.setProperty("showDropIndicator", False)
        self.steps.setAlternatingRowColors(True)
        self.steps.setSelectionMode(QAbstractItemView.SingleSelection)
        self.steps.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.steps.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.steps)

        self.s = QSplitter(TabMash)
        self.s.setObjectName(u"s")
        self.s.setOrientation(Qt.Horizontal)
        self.add = QPushButton(self.s)
        self.add.setObjectName(u"add")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy1)
        self.s.addWidget(self.add)
        self.remove = QPushButton(self.s)
        self.remove.setObjectName(u"remove")
        self.remove.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.remove.sizePolicy().hasHeightForWidth())
        self.remove.setSizePolicy(sizePolicy1)
        self.s.addWidget(self.remove)

        self.verticalLayout.addWidget(self.s)


        self.retranslateUi(TabMash)

        QMetaObject.connectSlotsByName(TabMash)
    # setupUi

    def retranslateUi(self, TabMash):
        TabMash.setWindowTitle(QCoreApplication.translate("TabMash", u"Form", None))
        self.add.setText(QCoreApplication.translate("TabMash", u"Add Step", None))
        self.remove.setText(QCoreApplication.translate("TabMash", u"Remove Step", None))
    # retranslateUi

