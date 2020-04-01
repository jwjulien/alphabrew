# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TabFermentation.ui'
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


class Ui_TabFermentation(object):
    def setupUi(self, TabFermentation):
        if TabFermentation.objectName():
            TabFermentation.setObjectName(u"TabFermentation")
        TabFermentation.resize(809, 629)
        self.gridLayout = QGridLayout(TabFermentation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.steps = QTableView(TabFermentation)
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

        self.gridLayout.addWidget(self.steps, 0, 0, 1, 1)

        self.s = QSplitter(TabFermentation)
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

        self.gridLayout.addWidget(self.s, 1, 0, 1, 1)


        self.retranslateUi(TabFermentation)

        QMetaObject.connectSlotsByName(TabFermentation)
    # setupUi

    def retranslateUi(self, TabFermentation):
        TabFermentation.setWindowTitle(QCoreApplication.translate("TabFermentation", u"Form", None))
        self.add.setText(QCoreApplication.translate("TabFermentation", u"Add Step", None))
        self.remove.setText(QCoreApplication.translate("TabFermentation", u"Remove Step", None))
    # retranslateUi

