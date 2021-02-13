# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'circularProgressBarSplashScreenqbMWpg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(333, 334)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 311, 311))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(53, 0, 80,100);\n"
"border-radius:150px;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.ProgressBar = QLabel(self.frame_2)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setGeometry(QRect(0, 0, 311, 311))
        self.ProgressBar.setStyleSheet(u"QLabel{\n"
"border-radius:150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.747082 rgba(255, 53, 53, 0), stop:0.749027 rgba(255, 245, 53, 255));\n"
"}")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 291, 291))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"border-radius:145px;\n"
"	\n"
"	background-color: rgb(33, 36, 83);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 40, 191, 71))
        font = QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(33, 36, 83);")
        self.PercentLabel = QLabel(self.frame_3)
        self.PercentLabel.setObjectName(u"PercentLabel")
        self.PercentLabel.setGeometry(QRect(40, 90, 221, 111))
        self.PercentLabel.setStyleSheet(u"color: rgb(255, 135, 235);")
        self.PercentLabel.setFrameShape(QFrame.NoFrame)
        self.LoadingLabel = QLabel(self.frame_3)
        self.LoadingLabel.setObjectName(u"LoadingLabel")
        self.LoadingLabel.setGeometry(QRect(50, 200, 201, 21))
        self.LoadingLabel.setFont(font)
        self.LoadingLabel.setStyleSheet(u"QLabel{\n"
"border-radius:10px;\n"
"	color: rgb(255, 170, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 250, 131, 21))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"QLabel{\n"
"border-radius:10px;\n"
"	\n"
"	color: rgb(88, 96, 221);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}")

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ProgressBar.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">O</span><span style=\" font-size:26pt;\">-</span><span style=\" font-size:26pt; font-weight:600;\">M</span><span style=\" font-size:26pt;\">itra</span></p></body></html>", None))
        self.PercentLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600;\">0</span><span style=\" font-size:24pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.LoadingLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Processing....</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600;\">Created</span><span style=\" font-size:7pt;\"> - Kaladhar Gopal</span></p></body></html>", None))
    # retranslateUi

