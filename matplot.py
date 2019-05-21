from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
from UI import Ui_Dialog

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import function as fun_c
from PyQt5.QtCore import pyqtSignal, QObject, Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QCheckBox, QSpinBox, QHBoxLayout, QComboBox, QGridLayout
import mainthread as Mainthread
from time import ctime, sleep


class MyFigure(FigureCanvas):
    def __init__(self,width=5, height=4, dpi=100):

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyFigure,self).__init__(self.fig) 
        self.axes = self.fig.add_subplot(111)


class MainDialogImgBW(QDialog,Ui_Dialog):
   
    #define signals
    valueChanged = pyqtSignal()    
    
    
    
    def __init__(self):
        super(MainDialogImgBW,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("CorrLearnSom")
        self.setMinimumSize(0,0)  
        self.gridlayout1 = QGridLayout(self.groupBox1)
        self.gridlayout2 = QGridLayout(self.groupBox2)
        self.gridlayout3 = QGridLayout(self.groupBox3)
        self.gridlayout4 = QGridLayout(self.groupBox4)
        
    def Init(self):
        #difine thread
        Thread = Mainthread.myThread()
        
        #define signals and connects 
        self.valueChanged.connect(self.handle_valueChanged)   # self.valueChanged.emit()
        Thread.F.senddata[dict,dict,int].connect(self.plotdata)
        Thread.F.senddata1[dict,dict,int].connect(self.plotdata1)
        self.pushbutton1.clicked.connect(Thread.F.changevisualize)
        self.pushbutton2.clicked.connect(Thread.F.changevisualize1)
#        self.plotother()
        Thread.start()

    #slot    
    def setvisualize(self):
        print("chengaopigo asjfajiogajopseg")
    
    def handle_valueChanged(self):
        print('dasdasfasfasfas')
        
    def plotdata(self,pop,sdata,index):
        print('the first sensor pic is drawing')
        F = MyFigure(width=3, height=2, dpi=100)     
        self.gridlayout1.addWidget(F,0,1)
        F.axes = F.fig.add_subplot(411)
        #####   ax1 = plt.subplot(4,1,1) 
        if pop['idx'] == 1:
            F.axes.hist(sdata['x'],bins=50,facecolor="blue", edgecolor="black", alpha=0.7)            
        elif pop['idx'] == 2:
            F.axes.hist(sdata['y'],bins=50,facecolor="blue", edgecolor="black", alpha=0.7)
        #####ax2 = plt.subplot(4,1,2)
        F.axes = F.fig.add_subplot(412)
        x = np.linspace(-sdata['range'],sdata['range'],pop['lsize'])
        for idx in range(pop['lsize']):
            # extract the preferred values (wight vector) of each neuron
            v_pref = pop['Winput'][idx]
            fx = np.exp(-(x - v_pref)**2/(2*pop['s'][idx]**2))
            F.axes.plot([x for x in range(100)],fx,linewidth=3)
        pop['Winput'] = np.sort(pop['Winput'],axis=0)  #notice keng

        # ax3 = plt.subplot(4,1,3)
        F.axes = F.fig.add_subplot(413)
        F.axes.hist(pop['Winput'],bins=50,facecolor="blue", edgecolor="black", alpha=0.7)
        # ax4 = plt.subplot(4,1,4)
        F.axes = F.fig.add_subplot(414)
        F.axes.plot(pop['s'],'.r')
        F1 = MyFigure(width=3, height=2, dpi=100)        
        self.gridlayout2.addWidget(F1,0,1)
        F1.axes = F1.fig.add_subplot(211)      
        F1.axes.plot(sdata['x'],sdata['y'],'.g')
        F1.axes2 = F1.fig.add_subplot(212)
        id_maxv = np.zeros((pop['lsize'],1))   #(100,1)
        for idx in range(pop['lsize']):
            arr =  pop['Wcross'][idx,:]
            id_maxv[idx] = np.where(arr==np.max(arr))
        F1.axes2.imshow(pop['Wcross'].T)

    def plotdata1(self,pop,sdata,index):
        print('the second sensor pic is drawing')
        F = MyFigure(width=3, height=2, dpi=100)     
        self.gridlayout3.addWidget(F,0,1)
        F.axes = F.fig.add_subplot(411)
        #####   ax1 = plt.subplot(4,1,1) 
        if pop['idx'] == 1:
            F.axes.hist(sdata['x'],bins=50,facecolor="blue", edgecolor="black", alpha=0.7)            
        elif pop['idx'] == 2:
            F.axes.hist(sdata['y'],bins=50,facecolor="blue", edgecolor="black", alpha=0.7)
        #####ax2 = plt.subplot(4,1,2)

        F.axes = F.fig.add_subplot(412)
        x = np.linspace(-sdata['range'],sdata['range'],pop['lsize'])
        for idx in range(pop['lsize']):
            # extract the preferred values (wight vector) of each neuron
            v_pref = pop['Winput'][idx]
            fx = np.exp(-(x - v_pref)**2/(2*pop['s'][idx]**2))
            F.axes.plot([x for x in range(100)],fx,linewidth=3)
        pop['Winput'] = np.sort(pop['Winput'],axis=0)  #notice keng

        # ax3 = plt.subplot(4,1,3)
        F.axes = F.fig.add_subplot(413)
        F.axes.hist(pop['Winput'],bins=50,facecolor="blue", edgecolor="black", alpha=0.7)
        # ax4 = plt.subplot(4,1,4)
        F.axes = F.fig.add_subplot(414)
        F.axes.plot(pop['s'],'.r')
        F1 = MyFigure(width=3, height=2, dpi=100)        
        self.gridlayout4.addWidget(F1,0,1)
        F1.axes = F1.fig.add_subplot(211)      
        F1.axes.plot(sdata['x'],sdata['y'],'.g')
        F1.axes2 = F1.fig.add_subplot(212)
        id_maxv = np.zeros((pop['lsize'],1))   #(100,1)
        for idx in range(pop['lsize']):
            arr =  pop['Wcross'][idx,:]
            id_maxv[idx] = np.where(arr==np.max(arr))
        F1.axes2.imshow(pop['Wcross'].T)
        
























