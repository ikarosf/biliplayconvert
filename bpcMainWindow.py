# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bpcMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject,
                            QRect)
from PySide2.QtWidgets import *

from DragListWidget import DragListWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1026, 805)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.audiopathlistWidget = DragListWidget(self.centralwidget)
        self.audiopathlistWidget.setObjectName(u"audiopathlistWidget")
        self.audiopathlistWidget.setGeometry(QRect(10, 40, 320, 480))
        self.xmlpathlistWidget = DragListWidget(self.centralwidget)
        self.xmlpathlistWidget.setObjectName(u"xmlpathlistWidget")
        self.xmlpathlistWidget.setGeometry(QRect(350, 40, 320, 480))
        self.titlesplainTextEdit = QPlainTextEdit(self.centralwidget)
        self.titlesplainTextEdit.setObjectName(u"titlesplainTextEdit")
        self.titlesplainTextEdit.setGeometry(QRect(690, 40, 320, 480))
        self.audiopathlabel = QLabel(self.centralwidget)
        self.audiopathlabel.setObjectName(u"audiopathlabel")
        self.audiopathlabel.setGeometry(QRect(10, 20, 54, 12))
        self.xmlpathlabel = QLabel(self.centralwidget)
        self.xmlpathlabel.setObjectName(u"xmlpathlabel")
        self.xmlpathlabel.setGeometry(QRect(350, 20, 54, 12))
        self.titlelabel = QLabel(self.centralwidget)
        self.titlelabel.setObjectName(u"titlelabel")
        self.titlelabel.setGeometry(QRect(690, 20, 211, 16))
        self.addaudiopathpushButton = QPushButton(self.centralwidget)
        self.addaudiopathpushButton.setObjectName(u"addaudiopathpushButton")
        self.addaudiopathpushButton.setGeometry(QRect(160, 530, 75, 23))
        self.delaudiopathpushButton = QPushButton(self.centralwidget)
        self.delaudiopathpushButton.setObjectName(u"delaudiopathpushButton")
        self.delaudiopathpushButton.setGeometry(QRect(250, 530, 75, 23))
        self.addxmlpathpushButton = QPushButton(self.centralwidget)
        self.addxmlpathpushButton.setObjectName(u"addxmlpathpushButton")
        self.addxmlpathpushButton.setGeometry(QRect(500, 530, 75, 23))
        self.delxmlpathpushButton = QPushButton(self.centralwidget)
        self.delxmlpathpushButton.setObjectName(u"delxmlpathpushButton")
        self.delxmlpathpushButton.setGeometry(QRect(590, 530, 75, 23))
        self.runpushButton = QPushButton(self.centralwidget)
        self.runpushButton.setObjectName(u"runpushButton")
        self.runpushButton.setGeometry(QRect(930, 530, 75, 23))
        self.namelabel = QLabel(self.centralwidget)
        self.namelabel.setObjectName(u"namelabel")
        self.namelabel.setGeometry(QRect(25, 595, 54, 12))
        self.namelineEdit = QLineEdit(self.centralwidget)
        self.namelineEdit.setObjectName(u"namelineEdit")
        self.namelineEdit.setGeometry(QRect(90, 590, 211, 20))
        self.tipstextBrowser = QTextBrowser(self.centralwidget)
        self.tipstextBrowser.setObjectName(u"tipstextBrowser")
        self.tipstextBrowser.setGeometry(QRect(490, 570, 491, 201))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1026, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"bili\u5b89\u5353\u64ad\u653e\u8f6c\u6362\u5668", None))
        self.audiopathlabel.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u6587\u4ef6", None))
        self.xmlpathlabel.setText(QCoreApplication.translate("MainWindow", u"\u5f39\u5e55\u6587\u4ef6", None))
        self.titlelabel.setText(
            QCoreApplication.translate("MainWindow", u"\u6bcf\u96c6\u6807\u9898\uff08\u4e00\u884c\u4e00\u96c6\uff09",
                                       None))
        self.addaudiopathpushButton.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.delaudiopathpushButton.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u9009\u4e2d", None))
        self.addxmlpathpushButton.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.delxmlpathpushButton.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u9009\u4e2d", None))
        self.runpushButton.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8", None))
        self.namelabel.setText(QCoreApplication.translate("MainWindow", u"\u5408\u96c6\u540d\u79f0\uff1a", None))
    # retranslateUi
