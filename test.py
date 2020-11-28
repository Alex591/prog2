# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerLwWUrb.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"MainWindow {\n"
"        background-image: url(\"photos/otos_backround.png\"); \n"
"        background-repeat: no-repeat; \n"
"        background-position: center;\n"
"    }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(140, 80, 451, 331))
        self.toolButton.setStyleSheet(u"\n"
"\n"
"\n"
".QToolButton {\n"
"	box-shadow:inset 0px 1px 0px 0px #f5f5f5;\n"
"	background-color:transparent;\n"
"	border:1px solid #fa0505;\n"
"	display:inline-block;\n"
"	cursor:pointer;\n"
"	color:#ff0303;\n"
"	font-family:Arial;\n"
"	font-size:17px;\n"
"	font-weight:bold;\n"
"	padding:16px 21px;\n"
"	text-decoration:none;\n"
"}\n"
".QToolButton:checked {\n"
"	\n"
"	\n"
"	box-shadow: 0px 0px 0px 0px #3dc21b;\n"
"	background:linear-gradient(to bottom, #44c767 5%, #6fdb34 100%);\n"
"	background-color:#44c767;\n"
"	display:inline-block;\n"
"	cursor:pointer;\n"
"	color:#ffffff;\n"
"	font-family:Arial;\n"
"	font-size:17px;\n"
"	font-weight:bold;\n"
"	\n"
"	text-decoration:none;\n"
"}\n"
".QToolButton:active {\n"
"	position:relative;\n"
"	top:1px;\n"
"}\n"
"")
        self.toolButton.setCheckable(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 800, 600))
        self.label.setPixmap(QPixmap(u"Screenshot 2020-11-11 203513.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.toolButton.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label.setText("")
    # retranslateUi



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
