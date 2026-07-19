import sys
import os

from PySide6.QtCore import Qt, QPoint, QSize
from PySide6.QtGui import QIcon, QAction, QGuiApplication
from PySide6.QtWidgets import (QWidget, QMenu, QSystemTrayIcon, QHBoxLayout, QPushButton,
    QMessageBox, QMainWindow)

basedir = os.path.dirname(__file__)

class SamplePopupWnd(QMainWindow):
    def __init__(self):
        super().__init__()
        self.popupwidth = 300
        self.popupheight = 400

        # Menu bar extra icon.
        icon = self.getSystemTrayIcon()
        self.systray = QSystemTrayIcon()
        self.systray.setIcon(icon)
        self.systray.setVisible(True)
        self.systray.activated.connect(self.togglePopup)

        self.button = QPushButton("button", self)
        self.button.clicked.connect(self.showButtonMessage)

        # Actions for a menu that is opened by a menu button
        self.settings = QAction("settings", self)
        self.settings.triggered.connect(self.showMenuMessage)
        self.about_act = QAction("about", self)
        self.about_act.triggered.connect(self.aboutActionSelected)
        self.quit_act = QAction("quit", self)
        self.quit_act.triggered.connect(self.quitActionSelected)

        self.menu = QMenu(self)
        self.menu.addAction(self.settings)
        self.menu.addAction(self.about_act)
        self.menu.addSeparator()
        self.menu.addAction(self.quit_act)
        self.menubutton = QPushButton("≡ menu", self)
        self.menubutton.setMenu(self.menu)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.button)
        hbox.addStretch(2)
        hbox.addWidget(self.menubutton)

        # Add to a QWidget that is styled with rounded corners.
        self.popup = QWidget(self)
        self.popup.setObjectName("popup")
        self.popup.resize(QSize(self.popupwidth, self.popupheight))
        self.popup.setLayout(hbox)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.WindowType.Popup)
        self.setGeometry(200, 100, self.popupwidth, self.popupheight)
        self.setStyleSheet("""
            #popup {
                border-radius: 16px;
                background-color: #fefefe;
            }
        """)


    def showButtonMessage(self):
        QMessageBox.information(self, "demo", "the Button was clicked!", QMessageBox.StandardButton.Ok)

    def showMenuMessage(self):
        QMessageBox.information(self, "demo", "the Menu Action was clicked!", QMessageBox.StandardButton.Ok)

    def aboutActionSelected(self):
        QMessageBox.about(self, "about", "qt for python popup demo 1.0")

    def quitActionSelected(self):
        sys.exit()

    def getSystemTrayIcon(self):
        icon = QIcon(os.path.join(basedir, "systray.png"))
        return icon

    def togglePopup(self, reason):
        # Handle click on system tray icon.
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            if self.isVisible():
                self.close()
            else:
                self.openPopup()

    def openPopup(self):
        systray_geom = self.systray.geometry()

        x = systray_geom.x()
        y = 0 if systray_geom.y() < 0 else systray_geom.y()
        currscreen = QGuiApplication.screenAt(QPoint(x, y))
        screen_avail_geom = currscreen.availableGeometry()
        top = screen_avail_geom.y()
        left1 = systray_geom.x()
        left2 = screen_avail_geom.width() - self.popupwidth

        # Align popup left coords with the system tray icon.
        left = left1 if left1 < left2 else left2
        self.setGeometry(left, top, self.popupwidth, self.popupheight)
        self.show()
        self.activateWindow()

