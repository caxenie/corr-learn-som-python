# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(1080, 750)
        self.groupBox1 = QtWidgets.QGroupBox(Dialog)
        self.groupBox1.setGeometry(QtCore.QRect(30, 20, 301, 301))
        self.groupBox1.setObjectName("groupBox1")
        self.pushbutton2 = QtWidgets.QPushButton(Dialog)
        self.pushbutton2.setGeometry(QtCore.QRect(960, 410, 99, 27))
        self.pushbutton2.setObjectName("pushbutton2")
        self.pushbutton1 = QtWidgets.QPushButton(Dialog)
        self.pushbutton1.setGeometry(QtCore.QRect(840, 410, 99, 27))
        self.pushbutton1.setObjectName("pushbutton1")
        self.groupBox2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox2.setGeometry(QtCore.QRect(510, 20, 301, 301))
        self.groupBox2.setObjectName("groupBox2")
        self.groupBox3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox3.setGeometry(QtCore.QRect(40, 360, 301, 301))
        self.groupBox3.setObjectName("groupBox3")
        self.groupBox4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox4.setGeometry(QtCore.QRect(510, 360, 301, 301))
        self.groupBox4.setObjectName("groupBox4")
        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(980, 36, 91, 21))
        self.label3.setObjectName("label3")
        self.pushbutton3 = QtWidgets.QPushButton(Dialog)
        self.pushbutton3.setGeometry(QtCore.QRect(850, 30, 99, 27))
        self.pushbutton3.setObjectName("pushbutton3")
        self.pushbutton4 = QtWidgets.QPushButton(Dialog)
        self.pushbutton4.setGeometry(QtCore.QRect(850, 70, 99, 27))
        self.pushbutton4.setObjectName("pushbutton4")
        self.pushbutton5 = QtWidgets.QPushButton(Dialog)
        self.pushbutton5.setGeometry(QtCore.QRect(850, 110, 99, 27))
        self.pushbutton5.setObjectName("pushbutton5")
        self.pushbutton6 = QtWidgets.QPushButton(Dialog)
        self.pushbutton6.setGeometry(QtCore.QRect(850, 150, 99, 27))
        self.pushbutton6.setObjectName("pushbutton6")
        self.pushbutton7 = QtWidgets.QPushButton(Dialog)
        self.pushbutton7.setGeometry(QtCore.QRect(850, 190, 99, 27))
        self.pushbutton7.setObjectName("pushbutton7")
        self.label4 = QtWidgets.QLabel(Dialog)
        self.label4.setGeometry(QtCore.QRect(980, 70, 91, 21))
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(Dialog)
        self.label5.setGeometry(QtCore.QRect(980, 110, 101, 21))
        self.label5.setObjectName("label5")
        self.label6 = QtWidgets.QLabel(Dialog)
        self.label6.setGeometry(QtCore.QRect(980, 150, 91, 21))
        self.label6.setObjectName("label6")
        self.label7 = QtWidgets.QLabel(Dialog)
        self.label7.setGeometry(QtCore.QRect(980, 190, 91, 21))
        self.label7.setObjectName("label7")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(840, 460, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(960, 460, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushbutton8 = QtWidgets.QPushButton(Dialog)
        self.pushbutton8.setGeometry(QtCore.QRect(850, 230, 99, 27))
        self.pushbutton8.setObjectName("pushbutton8")
        self.label8 = QtWidgets.QLabel(Dialog)
        self.label8.setGeometry(QtCore.QRect(980, 230, 91, 21))
        self.label8.setObjectName("label8")
        self.pushbutton9 = QtWidgets.QPushButton(Dialog)
        self.pushbutton9.setGeometry(QtCore.QRect(850, 270, 99, 27))
        self.pushbutton9.setObjectName("pushbutton9")
        self.label9 = QtWidgets.QLabel(Dialog)
        self.label9.setGeometry(QtCore.QRect(980, 270, 91, 21))
        self.label9.setObjectName("label9")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox1.setTitle(_translate("Dialog", "GroupBox"))
        self.pushbutton2.setText(_translate("Dialog", "Visua_off"))
        self.pushbutton1.setText(_translate("Dialog", "Visua_on"))
        self.groupBox2.setTitle(_translate("Dialog", "GroupBox"))
        self.groupBox3.setTitle(_translate("Dialog", "GroupBox"))
        self.groupBox4.setTitle(_translate("Dialog", "GroupBox"))
        self.label3.setText(_translate("Dialog", "Default=100"))
        self.pushbutton3.setText(_translate("Dialog", "N_NEURONS"))
        self.pushbutton4.setText(_translate("Dialog", "EPOCHS"))
        self.pushbutton5.setText(_translate("Dialog", "SAMPLES"))
        self.pushbutton6.setText(_translate("Dialog", "ETA"))
        self.pushbutton7.setText(_translate("Dialog", "XI"))
        self.label4.setText(_translate("Dialog", "Default=100"))
        self.label5.setText(_translate("Dialog", "Default=1500"))
        self.label6.setText(_translate("Dialog", "Default=1.0"))
        self.label7.setText(_translate("Dialog", "Default=1e-3"))
        self.pushButton.setText(_translate("Dialog", "start"))
        self.pushButton_2.setText(_translate("Dialog", "stop"))
        self.pushbutton8.setText(_translate("Dialog", "Sensory"))
        self.label8.setText(_translate("Dialog", "Default=1"))
        self.pushbutton9.setText(_translate("Dialog", "pref"))
        self.label9.setText(_translate("Dialog", "Default=1,6,13,40,45,85,90,98"))
