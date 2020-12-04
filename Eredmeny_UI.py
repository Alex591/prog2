# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledrTuNsC.ui'
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
    def __init__(self, mennyi, nyero, lottolista):
        self.mennyi = mennyi
        self.nyero = nyero
        self.lottolista = lottolista

    def isgood(self):
        for x in self.lottolista:
            if x.hanyjo() > 0:
                return True
        return False

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(390, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 110, 111, 41))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        icon = QIcon()
        icon.addFile(u"photos/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 140, 161, 31))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(11)
        self.label_2.setFont(font1)
        self.WinningsLabel = QLabel(self.centralwidget)
        self.WinningsLabel.setObjectName(u"WinningsLabel")
        self.WinningsLabel.setGeometry(QRect(10, 580, 151, 17))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(11)
        self.WinningsLabel.setFont(font2)
        self.szelveny_1 = QLabel(self.centralwidget)
        self.szelveny_1.setObjectName(u"szelveny_1")
        self.szelveny_1.setGeometry(QRect(30, 180, 331, 16))
        self.szelveny_1.setFont(font2)
        self.szelveny_2 = QLabel(self.centralwidget)
        self.szelveny_2.setObjectName(u"szelveny_2")
        self.szelveny_2.setGeometry(QRect(30, 200, 331, 16))
        self.szelveny_2.setFont(font2)
        self.szelveny_3 = QLabel(self.centralwidget)
        self.szelveny_3.setObjectName(u"szelveny_3")
        self.szelveny_3.setGeometry(QRect(30, 220, 331, 16))
        self.szelveny_3.setFont(font2)
        self.szelveny_4 = QLabel(self.centralwidget)
        self.szelveny_4.setObjectName(u"szelveny_4")
        self.szelveny_4.setGeometry(QRect(30, 240, 331, 16))
        self.szelveny_4.setFont(font2)
        self.szelveny_5 = QLabel(self.centralwidget)
        self.szelveny_5.setObjectName(u"szelveny_5")
        self.szelveny_5.setGeometry(QRect(30, 260, 331, 16))
        self.szelveny_5.setFont(font2)
        self.szelveny_6 = QLabel(self.centralwidget)
        self.szelveny_6.setObjectName(u"szelveny_6")
        self.szelveny_6.setGeometry(QRect(30, 280, 331, 16))
        self.szelveny_6.setFont(font2)
        self.szelveny_7 = QLabel(self.centralwidget)
        self.szelveny_7.setObjectName(u"szelveny_7")
        self.szelveny_7.setGeometry(QRect(30, 300, 331, 16))
        self.szelveny_7.setFont(font2)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 391, 121))
        self.label_3.setScaledContents(True)
        self.szelveny_8 = QLabel(self.centralwidget)
        self.szelveny_8.setObjectName(u"szelveny_8")
        self.szelveny_8.setGeometry(QRect(30, 320, 331, 16))
        self.szelveny_8.setFont(font2)
        self.szelveny_9 = QLabel(self.centralwidget)
        self.szelveny_9.setObjectName(u"szelveny_9")
        self.szelveny_9.setGeometry(QRect(30, 340, 331, 16))
        self.szelveny_9.setFont(font2)
        self.szelveny_10 = QLabel(self.centralwidget)
        self.szelveny_10.setObjectName(u"szelveny_10")
        self.szelveny_10.setGeometry(QRect(30, 360, 331, 16))
        self.szelveny_10.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Eredm\u00e9nyek", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"A nyer\u0151 sz\u00e1mok:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", f"{self.nyero}", None))
        self.WinningsLabel.setText(
            QCoreApplication.translate("MainWindow", f"F\u0151nyerem\u00e9ny: ${self.lottolista[0].prizepool / 2}",
                                       None))
        if self.lottolista[0].isvalid():
            self.szelveny_1.setText(QCoreApplication.translate("MainWindow",
                                                               f"{self.lottolista[0].valasztott} ból {self.lottolista[0].hanyjo()} jó és nyert vele {int(self.lottolista[0].penznyereseg())}-et",
                                                               None))


        else:
            self.szelveny_1.setText(QCoreApplication.translate("MainWindow", f"Első szelvény nem játszható", None))
        if self.lottolista[1].isvalid():
            self.szelveny_2.setText(QCoreApplication.translate("MainWindow",
                                                               f"{self.lottolista[1].valasztott} ból {self.lottolista[1].hanyjo()} jó és nyert vele {int(self.lottolista[1].penznyereseg())}-et",
                                                               None))
        else:
            self.szelveny_2.setText(QCoreApplication.translate("MainWindow", f"Második szelvény nem játszható", None))
        if self.lottolista[2].isvalid():
            self.szelveny_3.setText(QCoreApplication.translate("MainWindow",
                                                               f"{self.lottolista[2].valasztott} ból {self.lottolista[2].hanyjo()} jó és nyert vele {int(self.lottolista[2].penznyereseg())}-et",
                                                               None))
        else:
            self.szelveny_3.setText(QCoreApplication.translate("MainWindow", f"Harmadik szelvény nem játszható", None))
        if self.lottolista[3].isvalid():
            self.szelveny_4.setText(QCoreApplication.translate("MainWindow",
                                                               f"{self.lottolista[3].valasztott} ból {self.lottolista[3].hanyjo()} jó és nyert vele {int(self.lottolista[3].penznyereseg())}-et",
                                                               None))
        else:
            self.szelveny_4.setText(QCoreApplication.translate("MainWindow", f"Negyedik szelvény nem játszható", None))
        if self.lottolista[4].isvalid():
            self.szelveny_5.setText(QCoreApplication.translate("MainWindow",
                                                               f"{self.lottolista[4].valasztott} ból {self.lottolista[4].hanyjo()} jó és nyert vele {int(self.lottolista[4].penznyereseg())}-et",
                                                               None))
        else:
            self.szelveny_5.setText(QCoreApplication.translate("MainWindow", f"Ötödik szelvény nem játszható", None))
        if self.lottolista[5].isvalid():
            self.szelveny_6.setText(QCoreApplication.translate("MainWindow",
                                                               f"{self.lottolista[5].valasztott} ból {self.lottolista[5].hanyjo()} jó és nyert vele {int(self.lottolista[5].penznyereseg())}-et",
                                                               None))
        else:
            self.szelveny_6.setText(QCoreApplication.translate("MainWindow", f"Hatodik szelvény nem játszható", None))
        self.szelveny_7.setText(QCoreApplication.translate("MainWindow", u"", None))

        self.szelveny_8.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.szelveny_9.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.szelveny_10.setText(QCoreApplication.translate("MainWindow", u"", None))

        if len(self.lottolista) == 10:
            if self.lottolista[6].isvalid():
                self.szelveny_7.setText(QCoreApplication.translate("MainWindow",
                                                                   f"{self.lottolista[6].valasztott} ból {self.lottolista[6].hanyjo()} jó és nyert vele {int(self.lottolista[6].penznyereseg())}-et",
                                                                   None))
            else:
                self.szelveny_7.setText(
                    QCoreApplication.translate("MainWindow", f"Hetedik szelvény nem játszható", None))
            if self.lottolista[7].isvalid():
                self.szelveny_8.setText(QCoreApplication.translate("MainWindow",
                                                                   f"{self.lottolista[7].valasztott} ból {self.lottolista[7].hanyjo()} jó és nyert vele {int(self.lottolista[7].penznyereseg())}-et",
                                                                   None))
            else:
                self.szelveny_8.setText(
                    QCoreApplication.translate("MainWindow", f"Nyolcadik szelvény nem játszható", None))
            if self.lottolista[8].isvalid():
                self.szelveny_9.setText(QCoreApplication.translate("MainWindow",
                                                                   f"{self.lottolista[8].valasztott} ból {self.lottolista[8].hanyjo()} jó és nyert vele {int(self.lottolista[8].penznyereseg())}-et",
                                                                   None))
            else:
                self.szelveny_9.setText(
                    QCoreApplication.translate("MainWindow", f"Kilencedik szelvény nem játszható", None))
            if self.lottolista[9].isvalid():
                self.szelveny_10.setText(QCoreApplication.translate("MainWindow",
                                                                    f"{self.lottolista[9].valasztott} ból {self.lottolista[9].hanyjo()} jó és nyert vele {int(self.lottolista[9].penznyereseg())}-et",
                                                                    None))
            else:
                self.szelveny_10.setText(
                    QCoreApplication.translate("MainWindow", f"Tizedik szelvény nem játszható", None))
        if self.isgood():
            self.label_3.setPixmap(QPixmap(u"photos/eredmeny_igen.jpg"))
        else:
            self.label_3.setPixmap(QPixmap(u"photos/eredmeny_nem.jpg"))

    # retranslateUi


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
