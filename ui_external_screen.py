# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'external_screenXvKIvi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_ExternalScreen(object):
    def setupUi(self, ExternalScreen):
        if not ExternalScreen.objectName():
            ExternalScreen.setObjectName(u"ExternalScreen")
        ExternalScreen.resize(941, 682)
        self.verticalLayout = QVBoxLayout(ExternalScreen)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.e_currentTimerLabel = QLabel(ExternalScreen)
        self.e_currentTimerLabel.setObjectName(u"e_currentTimerLabel")
        font = QFont()
        font.setPointSize(20)
        self.e_currentTimerLabel.setFont(font)
        self.e_currentTimerLabel.setMargin(10)

        self.horizontalLayout.addWidget(self.e_currentTimerLabel)

        self.e_clockLabel = QLabel(ExternalScreen)
        self.e_clockLabel.setObjectName(u"e_clockLabel")
        font1 = QFont()
        font1.setPointSize(50)
        self.e_clockLabel.setFont(font1)
        self.e_clockLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.e_clockLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.e_activeTimerLabel = QLabel(ExternalScreen)
        self.e_activeTimerLabel.setObjectName(u"e_activeTimerLabel")
        font2 = QFont()
        font2.setPointSize(150)
        self.e_activeTimerLabel.setFont(font2)
        self.e_activeTimerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.e_activeTimerLabel)

        self.e_messages = QLabel(ExternalScreen)
        self.e_messages.setObjectName(u"e_messages")
        self.e_messages.setFont(font)
        self.e_messages.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.e_messages)

        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(ExternalScreen)

        QMetaObject.connectSlotsByName(ExternalScreen)
    # setupUi

    def retranslateUi(self, ExternalScreen):
        ExternalScreen.setWindowTitle(QCoreApplication.translate("ExternalScreen", u"Form", None))
        self.e_currentTimerLabel.setText(QCoreApplication.translate("ExternalScreen", u"You speak time is 60minutes", None))
        self.e_clockLabel.setText(QCoreApplication.translate("ExternalScreen", u"19:20:20", None))
        self.e_activeTimerLabel.setText(QCoreApplication.translate("ExternalScreen", u"00:00:00", None))
        self.e_messages.setText("")
    # retranslateUi

