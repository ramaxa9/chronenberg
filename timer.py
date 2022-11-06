import sys
from datetime import timedelta
from string import Template

from PySide6 import QtWidgets
from PySide6.QtCore import QTime, QTimer, Qt
from PySide6.QtGui import QGuiApplication, QFont
from PySide6.QtWidgets import QApplication, QStyle

import ui_timer
import ui_external_screen


class ExternalScreen(QtWidgets.QWidget, ui_external_screen.Ui_ExternalScreen):
    def __init__(self):
        # TODO: Message - increase font size
        # TODO: Message - play with fonts

        super(ExternalScreen, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle("Chronenberg external screen")
        self.move(0, 0)
        self.resize(800, 600)
        self.e_currentTimerLabel.setText("")

        self.offset = None
        self.setDefaultColors()

    def setDefaultColors(self):
        style = "ExternalScreen{background-color: #2f4154;} QLabel{color: #d0ddea; }"
        self.setStyleSheet(style)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()
        if event.button() == Qt.LeftButton:
            self.offset = event.position().toPoint()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.position().toPoint() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)


class MainWindow(QtWidgets.QWidget, ui_timer.Ui_Form):
    # TODO: Add time buttons
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setMinimumSize(800, 800)
        self.resize(800, 800)
        self.setWindowTitle("Chronenberg timers")

        self.externalScreen = ExternalScreen()
        self.externalScreen.show()
        self.btnReloadScreens.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_BrowserReload))

        self.btnStart.setText("")
        self.btnPause.setText("")
        self.btnReset.setText("")
        self.btnStart.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self.btnPause.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause))
        self.btnReset.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_BrowserReload))

        clock = QTimer(self)
        clock.timeout.connect(self.updateClock)
        clock.start(1000)

        self.activeTimerLabel.clear()
        self.externalScreen.e_activeTimerLabel.clear()
        self.colorBackground.setText("")
        self.colorText.setText("")
        self.colorBackground.setColor("#2f4154")
        self.colorText.setColor("#d0ddea")
        print(self.colorText.color())
        self.colorBackground.colorChanged.connect(self.applyColors)
        self.colorText.colorChanged.connect(self.applyColors)

        self.activeTimer = QTimer(self)
        self.activeTimer.timeout.connect(self.updateActiveTimer)
        self.btnStart.clicked.connect(lambda: self.activeTimer.start(1000))
        self.btnPause.clicked.connect(lambda: self.activeTimer.stop())
        self.btnReset.clicked.connect(self.resetActiveTimer)
        self.timersList.itemDoubleClicked.connect(self.setCurrentTimer)
        self.btnAddTimer.clicked.connect(self.addTimerToList)
        self.btnDelTimer.clicked.connect(self.delTimerFromList)
        self.btnSendMessage.clicked.connect(self.sendMessage)
        self.btnReloadScreens.clicked.connect(self.reloadScreens)
        self.btnFullscreen.clicked.connect(lambda: self.externalScreen.showMaximized())
        self.messagesList.itemDoubleClicked.connect(self.repeatMessage)
        self.e_screen.currentIndexChanged.connect(self.moveExternalScreen)
        self.btnDelMessage.clicked.connect(self.delMessage)
        self.message.returnPressed.connect(self.sendMessage)

        self.reloadScreens()
        self.e_screen.setCurrentIndex(1)

    def delMessage(self):
        self.messagesList.takeItem(self.messagesList.currentRow())
        self.externalScreen.e_messages.clear()
        self.messageLabel.clear()

    def applyColors(self):
        bgColor = self.colorBackground.color()
        textColor = self.colorText.color()

        style = Template("ExternalScreen{background-color: $bgColor;} QLabel{color: $textColor; }")
        stylesheet = style.substitute(bgColor=bgColor, textColor=textColor)
        print(stylesheet)
        self.externalScreen.setStyleSheet(str(stylesheet))

    def closeEvent(self, event):
        if event.spontaneous():
            reply = QtWidgets.QMessageBox.question(
                self, 'QUIT',
                'Do you really want to quit?',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                sys.exit()
            else:
                event.ignore()

    def reloadScreens(self):
        self.e_screen.clear()
        for screen in QApplication.screens():
            self.e_screen.addItem(screen.name())

    def moveExternalScreen(self, index):
        screens = QGuiApplication.screens()
        if len(screens) > 1:
            screenGeometry = screens[index].geometry()
            self.externalScreen.move(screenGeometry.left(), screenGeometry.top())
            if index > 0:
                self.externalScreen.showMaximized()
            else:
                self.externalScreen.resize(800, 600)

    def delTimerFromList(self):
        self.timersList.takeItem(self.timersList.currentRow())

    def deleteMessageFromList(self):
        self.messagesList.takeItem(self.messagesList.currentRow())

    def repeatMessage(self, message):
        self.externalScreen.e_messages.setText(message.text())
        self.messageLabel.setText(message.text())

    def sendMessage(self):
        message = self.message.text()
        if message:
            self.message.clear()
            self.messagesList.addItem(message)
            self.messageLabel.setText(message)
        self.externalScreen.e_messages.setText(message)
        self.messageLabel.setText(message)

    def addTimerToList(self):
        hours = self.custom_h.value()
        if self.custom_h.value() < 10:
            hours = f"0{self.custom_h.value()}"

        minutes = self.custom_m.value()
        if self.custom_m.value() < 10:
            minutes = f"0{self.custom_m.value()}"

        seconds = self.custom_s.value()
        if self.custom_s.value() < 10:
            seconds = f"0{self.custom_s.value()}"

        self.custom_h.setValue(0)
        self.custom_m.setValue(0)
        self.custom_s.setValue(0)

        time = f"{hours}:{minutes}:{seconds}"
        if time != "00:00:00":
            items = list()
            for i in range(0, self.timersList.count()):
                item = self.timersList.item(i)
                items.append(item.text())
            if time not in items:
                self.timersList.addItem(time)

    def resetActiveTimer(self):
        self.activeTimer.stop()
        current = self.currentTimerLabel.text()
        self.activeTimerLabel.setText(current)
        self.externalScreen.e_activeTimerLabel.setText(current)

    def updateClock(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('h:mm:ss')
        self.clockLabel.setText(label_time)
        self.externalScreen.e_clockLabel.setText(label_time)

    def updateActiveTimer(self):
        seconds = QTime(0, 0, 0).secsTo(QTime.fromString(str(self.activeTimerLabel.text()).split('-')[-1], 'h:mm:ss'))
        if seconds > 0:
            time = timedelta(seconds=round(seconds - 1))
            self.activeTimerLabel.setText(str(time))
            self.externalScreen.e_activeTimerLabel.setText(str(time))
        else:
            self.activeTimer.stop()

    def setCurrentTimer(self, timer):
        time = QTime.fromString(timer.text(), "hh:mm:ss").toString("hh:mm:ss")
        self.currentTimerLabel.setText(time)
        self.activeTimerLabel.setText(time)
        self.externalScreen.e_activeTimerLabel.setText(time)
        seconds = QTime(0, 0, 0).secsTo(QTime.fromString(self.activeTimerLabel.text(), 'h:mm:ss'))
        self.externalScreen.e_currentTimerLabel.setText(f"You have {round(seconds / 60)} minutes")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer = MainWindow()
    timer.show()
    sys.exit(app.exec())
