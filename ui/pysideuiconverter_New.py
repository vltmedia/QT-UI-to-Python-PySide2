# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pysideuiconverter.ui'
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
        MainWindow.resize(627, 250)
        MainWindow.setStyleSheet(u"background-color: rgb(37, 50, 63);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.actionSave_Template = QAction(MainWindow)
        self.actionSave_Template.setObjectName(u"actionSave_Template")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 160, 571, 31))
        self.pushButton.setStyleSheet(u"border: 1px solid white;\n"
"color: rgb(0, 170, 255);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 50, 431, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 141, 21))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(40, 450, 431, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 420, 141, 21))
        self.FindFileButton = QPushButton(self.centralwidget)
        self.FindFileButton.setObjectName(u"FindFileButton")
        self.FindFileButton.setGeometry(QRect(460, 50, 21, 21))
        self.FindFileButton.setStyleSheet(u"border: 1px solid white;\n"
"color: rgb(0, 170, 255);")
        self.FindFileButton.setFlat(False)
        self.FindpysideButton = QPushButton(self.centralwidget)
        self.FindpysideButton.setObjectName(u"FindpysideButton")
        self.FindpysideButton.setGeometry(QRect(480, 450, 21, 21))
        self.FindpysideButton.setStyleSheet(u"border: 1px solid white;\n"
"color: rgb(0, 170, 255);")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 120, 431, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 90, 141, 21))
        self.FindFileButton_2 = QPushButton(self.centralwidget)
        self.FindFileButton_2.setObjectName(u"FindFileButton_2")
        self.FindFileButton_2.setGeometry(QRect(460, 120, 21, 21))
        self.FindFileButton_2.setStyleSheet(u"border: 1px solid white;\n"
"color: rgb(0, 170, 255);")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(490, 120, 101, 17))
        self.recentscomboBox = QComboBox(self.centralwidget)
        self.recentscomboBox.setObjectName(u"recentscomboBox")
        self.recentscomboBox.setGeometry(QRect(498, 0, 121, 22))
        self.loadRecentButton = QPushButton(self.centralwidget)
        self.loadRecentButton.setObjectName(u"loadRecentButton")
        self.loadRecentButton.setGeometry(QRect(400, 0, 91, 21))
        self.loadRecentButton.setStyleSheet(u"border: 1px solid white;\n"
"color: rgb(0, 170, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 627, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSave_Template)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave_Template.setText(QCoreApplication.translate("MainWindow", u"Save Template", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Convert File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"File to Convert:", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"C:\\Python\\Scripts\\pyside2-uic.exe", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"pyside2-uic.exe Location:", None))
        self.FindFileButton.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.FindpysideButton.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Export Path:", None))
        self.FindFileButton_2.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Same as Source", None))
        self.loadRecentButton.setText(QCoreApplication.translate("MainWindow", u"Load Recent", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

