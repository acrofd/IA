# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaAux.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 472)
        MainWindow.setStyleSheet("background-color: rgb(82, 73, 204);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RutaCalculada = QtWidgets.QLabel(self.centralwidget)
        self.RutaCalculada.setGeometry(QtCore.QRect(-100, 0, 681, 101))
        self.RutaCalculada.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.RutaCalculada.setObjectName("RutaCalculada")
        self.ruta = QtWidgets.QLabel(self.centralwidget)
        self.ruta.setGeometry(QtCore.QRect(110, 130, 230, 265))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ruta.setFont(font)
        self.ruta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ruta.setObjectName("ruta")
        self.OkButton = QtWidgets.QPushButton(self.centralwidget)
        self.OkButton.setGeometry(QtCore.QRect(180, 420, 88, 28))
        self.OkButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OkButton.setObjectName("OkButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 30))
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
        self.RutaCalculada.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">RUTA CALCULADA:</span></p></body></html>"))
        self.ruta.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.OkButton.setText(_translate("MainWindow", "OK"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
