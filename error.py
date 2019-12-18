# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(526, 213)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 471, 71))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.okBoton = QtWidgets.QPushButton(self.centralwidget)
        self.okBoton.setGeometry(QtCore.QRect(220, 130, 85, 31))
        self.okBoton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.okBoton.setObjectName("okBoton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 20, 121, 41))
        self.label_2.setObjectName("label_2")
        self.x = QtWidgets.QLabel(self.centralwidget)
        self.x.setGeometry(QtCore.QRect(20, 10, 51, 51))
        self.x.setText("")
        path = os.path.dirname(os.path.abspath(__file__))
        print(path)
        self.x.setPixmap(QPixmap(os.path.join(path, 'error.png')))
        self.x.setScaledContents(True)
        self.x.setObjectName("x")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 526, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">La estación de origen y de destino no puede ser la misma</span></p></body></html>"))
        self.okBoton.setText(_translate("MainWindow", "OK"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">ERROR</span></p></body></html>"))
