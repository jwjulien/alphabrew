# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TabMiscellaneous.ui'
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


class Ui_TabMiscellaneous(object):
    def setupUi(self, TabMiscellaneous):
        if TabMiscellaneous.objectName():
            TabMiscellaneous.setObjectName(u"TabMiscellaneous")
        TabMiscellaneous.resize(793, 518)
        self.gridLayout = QGridLayout(TabMiscellaneous)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(TabMiscellaneous)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.add = QPushButton(self.splitter)
        self.add.setObjectName(u"add")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.add)
        self.remove = QPushButton(self.splitter)
        self.remove.setObjectName(u"remove")
        self.remove.setEnabled(False)
        sizePolicy.setHeightForWidth(self.remove.sizePolicy().hasHeightForWidth())
        self.remove.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.remove)

        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)

        self.ingredients = QTableView(TabMiscellaneous)
        self.ingredients.setObjectName(u"ingredients")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ingredients.sizePolicy().hasHeightForWidth())
        self.ingredients.setSizePolicy(sizePolicy1)
        self.ingredients.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.ingredients.setProperty("showDropIndicator", False)
        self.ingredients.setAlternatingRowColors(True)
        self.ingredients.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ingredients.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.ingredients, 0, 0, 1, 1)


        self.retranslateUi(TabMiscellaneous)

        QMetaObject.connectSlotsByName(TabMiscellaneous)
    # setupUi

    def retranslateUi(self, TabMiscellaneous):
        TabMiscellaneous.setWindowTitle(QCoreApplication.translate("TabMiscellaneous", u"Form", None))
        self.add.setText(QCoreApplication.translate("TabMiscellaneous", u"Add Item", None))
        self.remove.setText(QCoreApplication.translate("TabMiscellaneous", u"Remove Selected Item", None))
    # retranslateUi

