# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diplom.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 203)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 30, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 101, 20))
        self.label_2.setObjectName("label_2")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(270, 40, 51, 21))
        self.input.setObjectName("input")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 211, 21))
        self.comboBox.setObjectName("comboBox")
        self.TEXT_IN = QtWidgets.QLabel(self.centralwidget)
        self.TEXT_IN.setGeometry(QtCore.QRect(30, 70, 47, 13))
        self.TEXT_IN.setText("")
        self.TEXT_IN.setObjectName("TEXT_IN")
        self.TEXT_OUT_SIN = QtWidgets.QLabel(self.centralwidget)
        self.TEXT_OUT_SIN.setGeometry(QtCore.QRect(30, 100, 47, 13))
        self.TEXT_OUT_SIN.setText("")
        self.TEXT_OUT_SIN.setObjectName("TEXT_OUT_SIN")
        self.TEXT_OUT_S = QtWidgets.QLabel(self.centralwidget)
        self.TEXT_OUT_S.setGeometry(QtCore.QRect(30, 130, 47, 13))
        self.TEXT_OUT_S.setText("")
        self.TEXT_OUT_S.setObjectName("TEXT_OUT_S")
        self.TEXT_OUT_X = QtWidgets.QLabel(self.centralwidget)
        self.TEXT_OUT_X.setGeometry(QtCore.QRect(30, 160, 47, 13))
        self.TEXT_OUT_X.setText("")
        self.TEXT_OUT_X.setObjectName("TEXT_OUT_X")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Диплом"))
        self.pushButton.setText(_translate("MainWindow", "Результат"))
        self.label.setText(_translate("MainWindow", "Выберите объект"))
        self.label_2.setText(_translate("MainWindow", "Количество часов"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
