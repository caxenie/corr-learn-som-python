# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 820)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(900, 700, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 1070, 890))
        
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10,1060 , 880))
        self.groupBox.setObjectName("groupBox")
        
        self.widget.setObjectName("widget")
        self.groupBox1 = QtWidgets.QGroupBox(self.widget)
        self.groupBox1.setGeometry(QtCore.QRect(10, 10, 431, 381))
        self.groupBox1.setObjectName("groupBox1")
        
        
        self.widget.setObjectName("widget")
        self.groupBox2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox2.setGeometry(QtCore.QRect(550, 10, 431, 381))
        self.groupBox2.setObjectName("groupBox2")

        self.widget.setObjectName("widget")
        self.groupBox3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox3.setGeometry(QtCore.QRect(10, 420, 431, 381))
        self.groupBox3.setObjectName("groupBox3")
        
        
        self.widget.setObjectName("widget")
        self.groupBox4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox4.setGeometry(QtCore.QRect(550, 420, 431, 381))
        self.groupBox4.setObjectName("groupBox4")

        self.widget.setObjectName("widget")
        self.pushbutton1 = QtWidgets.QPushButton('Visua_on',self.widget)
        self.pushbutton1.setGeometry(QtCore.QRect(830, 840, 121, 41))
        self.pushbutton1.setObjectName("pushbutton1")
        
        self.widget.setObjectName("widget")
        self.pushbutton2 = QtWidgets.QPushButton('Visua_off',self.widget)
        self.pushbutton2.setGeometry(QtCore.QRect(530, 840, 121, 41))
        self.pushbutton2.setObjectName("pushbutton2")


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "SOM_UI："))

