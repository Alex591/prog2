# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUIOSFPXP.ui'
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

from OtosLotto_UI import Ui_otoslotto
from SkandinavLotto_UI import Ui_skandinavlotto

class Ui_Lottozomasina(object):
    def openotos(self):
        self.window = QMainWindow()
        self.ui = Ui_otoslotto()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openskandinav(self):
        self.window = QMainWindow()
        self.ui = Ui_skandinavlotto()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()


    def openhelp(self):
        pass




    def setupUi(self, Lottozomasina):
        if Lottozomasina.objectName():
            Lottozomasina.setObjectName(u"Lottozomasina")
        Lottozomasina.resize(643, 392)
        Lottozomasina.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u"photos/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Lottozomasina.setWindowIcon(icon)
        Lottozomasina.setDocumentMode(False)
        Lottozomasina.setDockNestingEnabled(False)
        Lottozomasina.setUnifiedTitleAndToolBarOnMac(False)
        self.actionInform_ci = QAction(Lottozomasina)
        self.actionInform_ci.setObjectName(u"actionInform_ci")
        self.centralwidget = QWidget(Lottozomasina)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 320, 191, 41))

        self.pushButton.clicked.connect(self.openotos)


        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 320, 191, 41))

        self.pushButton_2.clicked.connect(self.openskandinav)

        self.welcomeLabel = QLabel(self.centralwidget)
        self.welcomeLabel.setObjectName(u"welcomeLabel")
        self.welcomeLabel.setGeometry(QRect(180, 290, 263, 13))
        self.photoLabel = QLabel(self.centralwidget)
        self.photoLabel.setObjectName(u"photoLabel")
        self.photoLabel.setGeometry(QRect(100, 10, 441, 261))
        self.photoLabel.setPixmap(QPixmap(u"photos/Logo_full.png"))
        self.photoLabel.setScaledContents(True)
        Lottozomasina.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(Lottozomasina)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 643, 21))
        self.menuSegits_g = QMenu(self.menuBar)
        self.menuSegits_g.setObjectName(u"menuSegits_g")
        Lottozomasina.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuSegits_g.menuAction())
        self.menuSegits_g.addAction(self.actionInform_ci)

        self.retranslateUi(Lottozomasina)

        QMetaObject.connectSlotsByName(Lottozomasina)
        # setupUi

    def retranslateUi(self, Lottozomasina):
        Lottozomasina.setWindowTitle(QCoreApplication.translate("Lottozomasina",
                                                                u"Szerencs\u00e9tlenj\u00e1t\u00e9k Zrt. Lott\u00f3z\u00f3masina",
                                                                None))
        self.actionInform_ci.setText(QCoreApplication.translate("Lottozomasina", u"Inform\u00e1ci\u00f3", None))
        self.pushButton.setText(QCoreApplication.translate("Lottozomasina", u"\u00d6t\u00f6slott\u00f3", None))
        self.pushButton_2.setText(QCoreApplication.translate("Lottozomasina", u"Skandin\u00e1v Lott\u00f3", None))
        self.welcomeLabel.setText(QCoreApplication.translate("Lottozomasina",
                                                             u"\u00dcdv\u00f6z\u00f6lj\u00fck a Szerencs\u00e9tlenj\u00e1t\u00e9k Zrt. Lott\u00f3z\u00f3g\u00e9p\u00e9ben!",
                                                             None))
        self.photoLabel.setText("")
        self.menuSegits_g.setTitle(QCoreApplication.translate("Lottozomasina", u"Segits\u00e9g", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Lottozomasina()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
