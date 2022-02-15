# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TabIngredients.ui'
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


class Ui_TabIngredients(object):
    def setupUi(self, TabIngredients):
        if TabIngredients.objectName():
            TabIngredients.setObjectName(u"TabIngredients")
        TabIngredients.resize(793, 518)
        self.gridLayout = QGridLayout(TabIngredients)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ingredients = QTableView(TabIngredients)
        self.ingredients.setObjectName(u"ingredients")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ingredients.sizePolicy().hasHeightForWidth())
        self.ingredients.setSizePolicy(sizePolicy)
        self.ingredients.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.ingredients.setProperty("showDropIndicator", False)
        self.ingredients.setAlternatingRowColors(True)
        self.ingredients.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ingredients.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.ingredients, 0, 0, 1, 1)

        self.splitter = QSplitter(TabIngredients)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.add = QPushButton(self.splitter)
        self.add.setObjectName(u"add")
        self.add.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy1)
        self.splitter.addWidget(self.add)
        self.edit = QPushButton(self.splitter)
        self.edit.setObjectName(u"edit")
        self.edit.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.edit.sizePolicy().hasHeightForWidth())
        self.edit.setSizePolicy(sizePolicy1)
        self.splitter.addWidget(self.edit)
        self.remove = QPushButton(self.splitter)
        self.remove.setObjectName(u"remove")
        self.remove.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.remove.sizePolicy().hasHeightForWidth())
        self.remove.setSizePolicy(sizePolicy1)
        self.splitter.addWidget(self.remove)

        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)

        self.group_fermentables = QGroupBox(TabIngredients)
        self.group_fermentables.setObjectName(u"group_fermentables")
        self.gridLayout_2 = QGridLayout(self.group_fermentables)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.filter = QLineEdit(self.group_fermentables)
        self.filter.setObjectName(u"filter")

        self.gridLayout_2.addWidget(self.filter, 0, 0, 1, 1)

        self.library = QTableView(self.group_fermentables)
        self.library.setObjectName(u"library")
        sizePolicy.setHeightForWidth(self.library.sizePolicy().hasHeightForWidth())
        self.library.setSizePolicy(sizePolicy)
        self.library.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.library.setAlternatingRowColors(True)
        self.library.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.library.setSortingEnabled(True)

        self.gridLayout_2.addWidget(self.library, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.group_fermentables, 2, 0, 1, 1)


        self.retranslateUi(TabIngredients)

        QMetaObject.connectSlotsByName(TabIngredients)
    # setupUi

    def retranslateUi(self, TabIngredients):
        TabIngredients.setWindowTitle(QCoreApplication.translate("TabIngredients", u"Form", None))
        self.add.setText(QCoreApplication.translate("TabIngredients", u"Add to Recipe", None))
        self.edit.setText(QCoreApplication.translate("TabIngredients", u"Edit Details", None))
        self.remove.setText(QCoreApplication.translate("TabIngredients", u"Remove from Recipe", None))
        self.group_fermentables.setTitle(QCoreApplication.translate("TabIngredients", u"Ingredient Library", None))
        self.filter.setPlaceholderText(QCoreApplication.translate("TabIngredients", u"Filter...", None))
    # retranslateUi

