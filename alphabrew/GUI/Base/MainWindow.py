# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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

from GUI.Widgets.StyleRange import StyleRangeWidget
from GUI.Widgets.IbuGuRange import IbuGuRangeWidget
from GUI.Widgets.SrmRange import SrmRangeWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1135, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        icon = QIcon()
        icon.addFile(u"alphabrew/beer.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSaveAs = QAction(MainWindow)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionContents = QAction(MainWindow)
        self.actionContents.setObjectName(u"actionContents")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.group_calculations = QGroupBox(self.centralwidget)
        self.group_calculations.setObjectName(u"group_calculations")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.group_calculations.sizePolicy().hasHeightForWidth())
        self.group_calculations.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.group_calculations)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_boil_size = QLabel(self.group_calculations)
        self.lbl_boil_size.setObjectName(u"lbl_boil_size")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_boil_size)

        self.calcBoilSize = QLineEdit(self.group_calculations)
        self.calcBoilSize.setObjectName(u"calcBoilSize")
        self.calcBoilSize.setFrame(False)
        self.calcBoilSize.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.calcBoilSize)

        self.lbl_boil_sg = QLabel(self.group_calculations)
        self.lbl_boil_sg.setObjectName(u"lbl_boil_sg")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_boil_sg)

        self.calcBoilSg = QLineEdit(self.group_calculations)
        self.calcBoilSg.setObjectName(u"calcBoilSg")
        self.calcBoilSg.setFrame(False)
        self.calcBoilSg.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.calcBoilSg)

        self.lbl_calories = QLabel(self.group_calculations)
        self.lbl_calories.setObjectName(u"lbl_calories")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_calories)

        self.calcCalories = QLineEdit(self.group_calculations)
        self.calcCalories.setObjectName(u"calcCalories")
        self.calcCalories.setFrame(False)
        self.calcCalories.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.calcCalories)


        self.gridLayout.addWidget(self.group_calculations, 1, 1, 1, 1)

        self.group_ranges = QGroupBox(self.centralwidget)
        self.group_ranges.setObjectName(u"group_ranges")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.group_ranges.sizePolicy().hasHeightForWidth())
        self.group_ranges.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.group_ranges)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_og = QLabel(self.group_ranges)
        self.lbl_og.setObjectName(u"lbl_og")

        self.verticalLayout.addWidget(self.lbl_og)

        self.og = StyleRangeWidget(self.group_ranges)
        self.og.setObjectName(u"og")
        self.og.setMinimumSize(QSize(0, 32))

        self.verticalLayout.addWidget(self.og)

        self.lbl_fg = QLabel(self.group_ranges)
        self.lbl_fg.setObjectName(u"lbl_fg")

        self.verticalLayout.addWidget(self.lbl_fg)

        self.fg = StyleRangeWidget(self.group_ranges)
        self.fg.setObjectName(u"fg")
        self.fg.setMinimumSize(QSize(0, 32))

        self.verticalLayout.addWidget(self.fg)

        self.lbl_abv = QLabel(self.group_ranges)
        self.lbl_abv.setObjectName(u"lbl_abv")

        self.verticalLayout.addWidget(self.lbl_abv)

        self.abv = StyleRangeWidget(self.group_ranges)
        self.abv.setObjectName(u"abv")
        self.abv.setMinimumSize(QSize(0, 32))

        self.verticalLayout.addWidget(self.abv)

        self.lbl_ibu = QLabel(self.group_ranges)
        self.lbl_ibu.setObjectName(u"lbl_ibu")

        self.verticalLayout.addWidget(self.lbl_ibu)

        self.ibu = StyleRangeWidget(self.group_ranges)
        self.ibu.setObjectName(u"ibu")
        self.ibu.setMinimumSize(QSize(0, 32))

        self.verticalLayout.addWidget(self.ibu)

        self.lbl_srm = QLabel(self.group_ranges)
        self.lbl_srm.setObjectName(u"lbl_srm")

        self.verticalLayout.addWidget(self.lbl_srm)

        self.srm = SrmRangeWidget(self.group_ranges)
        self.srm.setObjectName(u"srm")
        self.srm.setMinimumSize(QSize(0, 32))

        self.verticalLayout.addWidget(self.srm)

        self.lbl_ibu_gu = QLabel(self.group_ranges)
        self.lbl_ibu_gu.setObjectName(u"lbl_ibu_gu")

        self.verticalLayout.addWidget(self.lbl_ibu_gu)

        self.ibu_gu = IbuGuRangeWidget(self.group_ranges)
        self.ibu_gu.setObjectName(u"ibu_gu")
        self.ibu_gu.setMinimumSize(QSize(0, 32))

        self.verticalLayout.addWidget(self.ibu_gu)


        self.gridLayout.addWidget(self.group_ranges, 0, 1, 1, 1)

        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(5)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy2)
        self.tabs.setTabShape(QTabWidget.Rounded)

        self.gridLayout.addWidget(self.tabs, 0, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1135, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionContents)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AlphaBrew", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSaveAs.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
#if QT_CONFIG(shortcut)
        self.actionSaveAs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionContents.setText(QCoreApplication.translate("MainWindow", u"Contents", None))
#if QT_CONFIG(shortcut)
        self.actionContents.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.group_calculations.setTitle(QCoreApplication.translate("MainWindow", u"Calculations:", None))
        self.lbl_boil_size.setText(QCoreApplication.translate("MainWindow", u"Boil Size:", None))
        self.lbl_boil_sg.setText(QCoreApplication.translate("MainWindow", u"Boil SG:", None))
        self.lbl_calories.setText(QCoreApplication.translate("MainWindow", u"Calories:", None))
        self.group_ranges.setTitle(QCoreApplication.translate("MainWindow", u"Ranges:", None))
        self.lbl_og.setText(QCoreApplication.translate("MainWindow", u"Original Gravity:", None))
        self.lbl_fg.setText(QCoreApplication.translate("MainWindow", u"Final Gravity:", None))
        self.lbl_abv.setText(QCoreApplication.translate("MainWindow", u"ABV (%)", None))
        self.lbl_ibu.setText(QCoreApplication.translate("MainWindow", u"Bitterness (IBU):", None))
        self.lbl_srm.setText(QCoreApplication.translate("MainWindow", u"Color (SRM):", None))
        self.lbl_ibu_gu.setText(QCoreApplication.translate("MainWindow", u"IBU/GU:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

