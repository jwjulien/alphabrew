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
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_ambient = QLabel(TabMash)
        self.lbl_ambient.setObjectName(u"lbl_ambient")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_ambient)

        self.ambient = QSpinBox(TabMash)
        self.ambient.setObjectName(u"ambient")
        self.ambient.setMinimum(0)
        self.ambient.setMaximum(120)
        self.ambient.setValue(65)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ambient)

        self.lbl_ratio = QLabel(TabMash)
        self.lbl_ratio.setObjectName(u"lbl_ratio")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_ratio)

        self.ratio = QDoubleSpinBox(TabMash)
        self.ratio.setObjectName(u"ratio")
        self.ratio.setMinimum(0.750000000000000)
        self.ratio.setMaximum(2.500000000000000)
        self.ratio.setSingleStep(0.250000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ratio)


        self.verticalLayout.addLayout(self.formLayout)

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
        self.lbl_ambient.setText(QCoreApplication.translate("TabMash", u"Ambient Temperature:", None))
#if QT_CONFIG(tooltip)
        self.ambient.setToolTip(QCoreApplication.translate("TabMash", u"Starting temperature of the grains and mash tun.", None))
#endif // QT_CONFIG(tooltip)
        self.ambient.setSuffix(QCoreApplication.translate("TabMash", u" \u00b0F", None))
        self.lbl_ratio.setText(QCoreApplication.translate("TabMash", u"Strike Water/Grain Ratio:", None))
        self.ratio.setSuffix(QCoreApplication.translate("TabMash", u" qt/lb", None))
        self.add.setText(QCoreApplication.translate("TabMash", u"Add Step", None))
        self.remove.setText(QCoreApplication.translate("TabMash", u"Remove Step", None))
    # retranslateUi

