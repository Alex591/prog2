# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerNOdeND.ui'
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
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(770, 239)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.skandinav = QPushButton(self.centralwidget)
        self.skandinav.setObjectName(u"skandinav")
        self.skandinav.setGeometry(QRect(120, 110, 191, 81))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(400, 110, 201, 81))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.skandinav.clicked.connect(self.show_popup)




    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.skandinav.setText(QCoreApplication.translate("MainWindow", u"SKANDIN\u00c1V", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u00d6T\u00d6SLOTT\u00d3", None))
    # retranslateUi

    def show_popup(self):
        print("n")
        msg=QMessageBox()
        msg.setWindowTitle("Bitch")
        msg.setText("kk")
        msg.setIcon(QMessageBox.Critical)
        x=msg.exec_()

if __name__== '__main__':
    import sys

    app = QApplication()
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())