# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timerzAoZWr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from colorbutton import ColorButton


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1110, 878)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(True)
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.currentTimerLabel = QLabel(self.groupBox)
        self.currentTimerLabel.setObjectName(u"currentTimerLabel")
        font = QFont()
        font.setPointSize(20)
        self.currentTimerLabel.setFont(font)

        self.horizontalLayout_8.addWidget(self.currentTimerLabel)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.groupBox_2.setFlat(True)
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.clockLabel = QLabel(self.groupBox_2)
        self.clockLabel.setObjectName(u"clockLabel")
        self.clockLabel.setFont(font)
        self.clockLabel.setFrameShape(QFrame.NoFrame)
        self.clockLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.clockLabel)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_3.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFlat(True)
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.activeTimerLabel = QLabel(self.groupBox_3)
        self.activeTimerLabel.setObjectName(u"activeTimerLabel")
        font1 = QFont()
        font1.setPointSize(100)
        self.activeTimerLabel.setFont(font1)
        self.activeTimerLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.activeTimerLabel)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_7 = QGroupBox(Form)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFlat(True)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.messageLabel = QLabel(self.groupBox_7)
        self.messageLabel.setObjectName(u"messageLabel")
        font2 = QFont()
        font2.setPointSize(16)
        self.messageLabel.setFont(font2)
        self.messageLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.messageLabel)


        self.verticalLayout.addWidget(self.groupBox_7)

        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFlat(True)
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(15)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.custom_s = QSpinBox(self.groupBox_4)
        self.custom_s.setObjectName(u"custom_s")
        self.custom_s.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.custom_s.setMaximum(59)

        self.gridLayout.addWidget(self.custom_s, 1, 2, 1, 1)

        self.btnAddTimer = QPushButton(self.groupBox_4)
        self.btnAddTimer.setObjectName(u"btnAddTimer")
        self.btnAddTimer.setFont(font3)

        self.gridLayout.addWidget(self.btnAddTimer, 3, 0, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.btnDelTimer = QPushButton(self.groupBox_4)
        self.btnDelTimer.setObjectName(u"btnDelTimer")
        self.btnDelTimer.setFont(font3)

        self.gridLayout.addWidget(self.btnDelTimer, 3, 2, 1, 1)

        self.custom_h = QSpinBox(self.groupBox_4)
        self.custom_h.setObjectName(u"custom_h")
        self.custom_h.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.custom_h.setProperty("showGroupSeparator", False)
        self.custom_h.setMaximum(59)
        self.custom_h.setSingleStep(1)

        self.gridLayout.addWidget(self.custom_h, 1, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.custom_m = QSpinBox(self.groupBox_4)
        self.custom_m.setObjectName(u"custom_m")
        self.custom_m.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.custom_m.setMaximum(59)

        self.gridLayout.addWidget(self.custom_m, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(2, 1)

        self.horizontalLayout_4.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnPause = QPushButton(self.groupBox_4)
        self.btnPause.setObjectName(u"btnPause")
        self.btnPause.setIconSize(QSize(90, 90))

        self.gridLayout_2.addWidget(self.btnPause, 0, 1, 1, 1)

        self.btnReset = QPushButton(self.groupBox_4)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setIconSize(QSize(90, 90))

        self.gridLayout_2.addWidget(self.btnReset, 0, 2, 1, 1)

        self.btnStart = QPushButton(self.groupBox_4)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setIconSize(QSize(90, 90))

        self.gridLayout_2.addWidget(self.btnStart, 0, 0, 1, 1)

        self.btnAdd5 = QPushButton(self.groupBox_4)
        self.btnAdd5.setObjectName(u"btnAdd5")
        self.btnAdd5.setFont(font3)

        self.gridLayout_2.addWidget(self.btnAdd5, 1, 0, 1, 1)

        self.btnAdd10 = QPushButton(self.groupBox_4)
        self.btnAdd10.setObjectName(u"btnAdd10")
        self.btnAdd10.setFont(font3)

        self.gridLayout_2.addWidget(self.btnAdd10, 1, 1, 1, 1)

        self.btnAdd30 = QPushButton(self.groupBox_4)
        self.btnAdd30.setObjectName(u"btnAdd30")
        self.btnAdd30.setFont(font3)

        self.gridLayout_2.addWidget(self.btnAdd30, 1, 2, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_2)

        self.horizontalLayout_4.setStretch(1, 1)

        self.horizontalLayout_14.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.groupBox_6 = QGroupBox(Form)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFlat(True)
        self.groupBox_6.setCheckable(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.timersList = QListWidget(self.groupBox_6)
        self.timersList.setObjectName(u"timersList")
        self.timersList.setFont(font2)
        self.timersList.setProperty("showDropIndicator", False)
        self.timersList.setFlow(QListView.TopToBottom)
        self.timersList.setProperty("isWrapping", True)
        self.timersList.setWordWrap(False)
        self.timersList.setSelectionRectVisible(True)

        self.verticalLayout_4.addWidget(self.timersList)


        self.horizontalLayout_5.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(Form)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFlat(True)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.message = QLineEdit(self.groupBox_5)
        self.message.setObjectName(u"message")

        self.horizontalLayout_6.addWidget(self.message)

        self.btnSendMessage = QPushButton(self.groupBox_5)
        self.btnSendMessage.setObjectName(u"btnSendMessage")

        self.horizontalLayout_6.addWidget(self.btnSendMessage)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.messagesList = QListWidget(self.groupBox_5)
        self.messagesList.setObjectName(u"messagesList")

        self.verticalLayout_5.addWidget(self.messagesList)

        self.btnDelMessage = QPushButton(self.groupBox_5)
        self.btnDelMessage.setObjectName(u"btnDelMessage")

        self.verticalLayout_5.addWidget(self.btnDelMessage)


        self.horizontalLayout_5.addWidget(self.groupBox_5)

        self.groupBox_8 = QGroupBox(Form)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setFlat(True)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.groupBox_8)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.e_screen = QComboBox(self.groupBox_8)
        self.e_screen.setObjectName(u"e_screen")

        self.horizontalLayout.addWidget(self.e_screen)

        self.btnReloadScreens = QPushButton(self.groupBox_8)
        self.btnReloadScreens.setObjectName(u"btnReloadScreens")

        self.horizontalLayout.addWidget(self.btnReloadScreens)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.btnFullscreen = QPushButton(self.groupBox_8)
        self.btnFullscreen.setObjectName(u"btnFullscreen")

        self.verticalLayout_2.addWidget(self.btnFullscreen)

        self.groupBox_9 = QGroupBox(self.groupBox_8)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_3 = QGridLayout(self.groupBox_9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.groupBox_9)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.colorBackground = ColorButton(self.groupBox_9)
        self.colorBackground.setObjectName(u"colorBackground")

        self.gridLayout_3.addWidget(self.colorBackground, 1, 0, 1, 1)

        self.colorText = ColorButton(self.groupBox_9)
        self.colorText.setObjectName(u"colorText")

        self.gridLayout_3.addWidget(self.colorText, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_9)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_5.addWidget(self.groupBox_8)

        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 1)
#if QT_CONFIG(shortcut)
        self.label_4.setBuddy(self.label_4)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.custom_m, self.btnAddTimer)
        QWidget.setTabOrder(self.btnAddTimer, self.timersList)
        QWidget.setTabOrder(self.timersList, self.message)
        QWidget.setTabOrder(self.message, self.btnSendMessage)
        QWidget.setTabOrder(self.btnSendMessage, self.messagesList)
        QWidget.setTabOrder(self.messagesList, self.btnDelMessage)
        QWidget.setTabOrder(self.btnDelMessage, self.custom_h)
        QWidget.setTabOrder(self.custom_h, self.custom_s)
        QWidget.setTabOrder(self.custom_s, self.btnDelTimer)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Current timer", None))
        self.currentTimerLabel.setText(QCoreApplication.translate("Form", u"00:00:00", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Clock ", None))
        self.clockLabel.setText(QCoreApplication.translate("Form", u"00:00:00", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Active timer", None))
        self.activeTimerLabel.setText(QCoreApplication.translate("Form", u"00:00:00", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"Message", None))
        self.messageLabel.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Controlls", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Minutes", None))
        self.btnAddTimer.setText(QCoreApplication.translate("Form", u"+", None))
        self.label.setText(QCoreApplication.translate("Form", u"Hours", None))
        self.btnDelTimer.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Seconds", None))
        self.btnPause.setText(QCoreApplication.translate("Form", u"Pause", None))
        self.btnReset.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.btnStart.setText(QCoreApplication.translate("Form", u"Start", None))
        self.btnAdd5.setText(QCoreApplication.translate("Form", u"+5m", None))
        self.btnAdd10.setText(QCoreApplication.translate("Form", u"+10m", None))
        self.btnAdd30.setText(QCoreApplication.translate("Form", u"+30m", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"Timers", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"Messages", None))
        self.btnSendMessage.setText(QCoreApplication.translate("Form", u"Send", None))
        self.btnDelMessage.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Form", u"External screen", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Screen", None))
        self.btnReloadScreens.setText("")
        self.btnFullscreen.setText(QCoreApplication.translate("Form", u"Fullscreen", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Form", u"Color", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Background", None))
        self.colorBackground.setText(QCoreApplication.translate("Form", u"Background", None))
        self.colorText.setText(QCoreApplication.translate("Form", u"Text", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Text", None))
    # retranslateUi

