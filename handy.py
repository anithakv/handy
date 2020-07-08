# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

"""
Created on Thu Oct 24 01:50:47 2019

@author: Anitha Rathnam KV, Anulekha M, Devesh Gupta, Amulya Kathasagaram
"""

# Environment:
# OS    : Windows 10
# python: 3.6.8
# opencv: 4.1.2.30

from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import filedialog
from tkinter import *
import os.path
from os import path
import time

class Ui_Handy(object):
    def setupUi(self, Handy):
        Handy.setObjectName("Handy")
        Handy.resize(800, 600)
        Handy.setMinimumSize(QtCore.QSize(800, 600))
        Handy.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ICON/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Handy.setWindowIcon(icon)
        self.Background = QtWidgets.QLabel(Handy)
        self.Background.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.Background.setStyleSheet("#Background{\n"
"border-image: url(:/BACKGROUND/background.png);\n"
"}")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.label_4 = QtWidgets.QLabel(Handy)
        self.label_4.setGeometry(QtCore.QRect(350, 40, 391, 31))
        self.label_4.setStyleSheet("font: 25 19pt \"Calibri Light\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.app1 = QtWidgets.QLabel(Handy)
        self.app1.setGeometry(QtCore.QRect(430, 100, 311, 101))
        self.app1.setStyleSheet("font: 25 19pt \"Calibri Light\";\n"
"color: rgb(255, 255, 255);")
        self.app1.setAlignment(QtCore.Qt.AlignCenter)
        self.app1.setObjectName("app1")
        self.app2 = QtWidgets.QLabel(Handy)
        self.app2.setGeometry(QtCore.QRect(330, 220, 311, 101))
        self.app2.setStyleSheet("font: 25 19pt \"Calibri Light\";\n"
"color: rgb(255, 255, 255);")
        self.app2.setAlignment(QtCore.Qt.AlignCenter)
        self.app2.setObjectName("app2")
        self.app3 = QtWidgets.QLabel(Handy)
        self.app3.setGeometry(QtCore.QRect(430, 340, 311, 101))
        self.app3.setStyleSheet("font: 25 19pt \"Calibri Light\";\n"
"color: rgb(255, 255, 255);")
        self.app3.setAlignment(QtCore.Qt.AlignCenter)
        self.app3.setObjectName("app3")
        self.app4 = QtWidgets.QLabel(Handy)
        self.app4.setGeometry(QtCore.QRect(330, 460, 311, 101))
        self.app4.setStyleSheet("font: 25 19pt \"Calibri Light\";\n"
"color: rgb(255, 255, 255);")
        self.app4.setAlignment(QtCore.Qt.AlignCenter)
        self.app4.setObjectName("app4")
        self.fbg = QtWidgets.QLabel(Handy)
        self.fbg.setGeometry(QtCore.QRect(330, 100, 411, 101))
        self.fbg.setMouseTracking(False)
        self.fbg.setStyleSheet("#fbg{background-image: url(:/BACKGROUND/normal_black.png);\n"
"border: 1px;\n"
"border-color: transparent;\n"
"border-radius: 5px;}\n"
"")
        self.fbg.setText("")
        self.fbg.setObjectName("fbg")
        self.fbg_2 = QtWidgets.QLabel(Handy)
        self.fbg_2.setGeometry(QtCore.QRect(330, 220, 411, 101))
        self.fbg_2.setStyleSheet("background-image: url(:/BACKGROUND/normal_black.png);\n"
"border: 1px;\n"
"border-color: transparent;\n"
"border-radius: 5px;")
        self.fbg_2.setText("")
        self.fbg_2.setObjectName("fbg_2")
        self.fbg_3 = QtWidgets.QLabel(Handy)
        self.fbg_3.setGeometry(QtCore.QRect(330, 340, 411, 101))
        self.fbg_3.setStyleSheet("background-image: url(:/BACKGROUND/normal_black.png);\n"
"border: 1px;\n"
"border-color: transparent;\n"
"border-radius: 5px;")
        self.fbg_3.setText("")
        self.fbg_3.setObjectName("fbg_3")
        self.fbg_4 = QtWidgets.QLabel(Handy)
        self.fbg_4.setGeometry(QtCore.QRect(330, 460, 411, 101))
        self.fbg_4.setStyleSheet("background-image: url(:/BACKGROUND/normal_black.png);\n"
"border: 1px;\n"
"border-color: transparent;\n"
"border-radius: 5px;")
        self.fbg_4.setText("")
        self.fbg_4.setObjectName("fbg_4")
        self.finger1 = QtWidgets.QPushButton(Handy)
        self.finger1.setGeometry(QtCore.QRect(330, 100, 101, 101))
        self.finger1.setStyleSheet("#finger1{border-image: url(:/FINGERS/2.png);\n"
"}\n"
"#finger1:hover{\n"
"background-image: url(:/BACKGROUND/normal_black.png);\n"
"border: 1px;\n"
"border-color: transparent;\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"#finger1:pressed{\n"
"background-image: url(:/BACKGROUND/hovering_black.png);\n"
"border: 1px;\n"
"border-color: transparent;\n"
"border-radius: 5px;\n"
"\n"
"}")
        self.finger1.setText("")
        self.finger1.setObjectName("finger1")
        self.finger2 = QtWidgets.QPushButton(Handy)
        self.finger2.setGeometry(QtCore.QRect(640, 220, 101, 101))
        self.finger2.setStyleSheet("#finger2{border-image: url(:/FINGERS/3.png);\n"
"}\n"
"#finger2:hover{\n"
"background-image: url(:/BACKGROUND/normal_black.png);\n"
"border: 1px;\n"
"border-color: transparent;\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"#finger2:pressed{\n"
"background-image: url(:/BACKGROUND/hovering_black.png);\n"
"border: 1px;\n"
"border-color: transparent;\n"
"border-radius: 5px;\n"
"\n"
"}")
        self.finger2.setText("")
        self.finger2.setObjectName("finger2")
        self.finger3 = QtWidgets.QPushButton(Handy)
        self.finger3.setGeometry(QtCore.QRect(330, 340, 101, 101))
        self.finger3.setStyleSheet("#finger3{border-image: url(:/FINGERS/4.png);\n"
"}\n"
"#finger3:hover{\n"
"background-image: url(:/BACKGROUND/normal_black.png);\n"
"border: 1px;\n"
"border-color: transparent;\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"#finger3:pressed{\n"
"background-image: url(:/BACKGROUND/hovering_black.png);\n"
"border: 1px;\n"
"border-color: transparent;\n"
"border-radius: 5px;\n"
"\n"
"}")
        self.finger3.setText("")
        self.finger3.setObjectName("finger3")
        self.finger4 = QtWidgets.QPushButton(Handy)
        self.finger4.setGeometry(QtCore.QRect(640, 460, 101, 101))
        self.finger4.setStyleSheet("#finger4{border-image: url(:/FINGERS/5.png);\n"
"}\n"
"#finger4:hover{\n"
"background-image: url(:/BACKGROUND/normal_black.png);\n"
"border: 1px;\n"
"border-color: transparent;\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"#finger4:pressed{\n"
"background-image: url(:/BACKGROUND/hovering_black.png);\n"
"border: 1px;\n"
"border-color: transparent;\n"
"border-radius: 5px;\n"
"\n"
"}")
        self.finger4.setText("")
        self.finger4.setObjectName("finger4")
        self.label_5 = QtWidgets.QLabel(Handy)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 291, 61))
        self.label_5.setStyleSheet("font: 25 19pt \"Calibri Light\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.eyeLogo = QtWidgets.QPushButton(Handy)
        self.eyeLogo.setGeometry(QtCore.QRect(70, 260, 191, 201))
        self.eyeLogo.setStyleSheet("#eyeLogo{border-image: url(:/EYES/eye_close.png);}")
        self.eyeLogo.setText("")
        self.eyeLogo.setObjectName("eyeLogo")
        self.Background.raise_()
        self.fbg.raise_()
        self.fbg_3.raise_()
        self.fbg_4.raise_()
        self.fbg_2.raise_()
        self.label_4.raise_()
        self.app1.raise_()
        self.app2.raise_()
        self.app3.raise_()
        self.app4.raise_()
        self.finger1.raise_()
        self.finger2.raise_()
        self.finger3.raise_()
        self.finger4.raise_()
        self.label_5.raise_()
        self.eyeLogo.raise_()
        self.finger1.clicked.connect(lambda: self.selectapp1(Handy))
        self.finger2.clicked.connect(lambda: self.selectapp2(Handy))
        self.finger3.clicked.connect(lambda: self.selectapp3(Handy))
        self.finger4.clicked.connect(lambda: self.selectapp4(Handy))
        self.eyeLogo.clicked.connect(lambda: self.camSetup(Handy))
        self.retranslateUi(Handy)
        QtCore.QMetaObject.connectSlotsByName(Handy)

    def retranslateUi(self, Handy):
        _translate = QtCore.QCoreApplication.translate
        Handy.setWindowTitle(_translate("Handy", "Handy"))
        self.label_4.setText(_translate("Handy", "Select Application"))
        self.app1.setText(_translate("Handy", "Select Application"))
        self.app2.setText(_translate("Handy", "Select Application"))
        self.app3.setText(_translate("Handy", "Select Application"))
        self.app4.setText(_translate("Handy", "Select Application"))
        self.label_5.setText(_translate("Handy", "Wake me up by\nclicking on the eye"))
        if (path.exists("b1dir.boo"))==True:
            with open("b1dir.boo", "r") as f:
                lines = f.readlines()
                for l in lines:
                    dir=l.split("/")
                    x=dir[len(dir)-1]
                    x=x.split(".exe")
                    if not x:
                        self.app1.setText("Select Application")
                    else:
                        self.app1.setText(x[0])
        else:
            file=open("b1dir.boo", "w+")
            file.close()
        if (path.exists("b2dir.boo"))==True:
            with open("b2dir.boo", "r") as f:
                lines = f.readlines()
                for l in lines:
                    dir=l.split("/")
                    x=dir[len(dir)-1]
                    x=x.split(".exe")
                    if not x:
                        self.app2.setText("Select Application")
                    else:
                        self.app2.setText(x[0])
        else:
            file=open("b2dir.boo", "w+")
            file.close()
        if (path.exists("b3dir.boo"))==True:
            with open("b3dir.boo", "r") as f:
                lines = f.readlines()
                for l in lines:
                    dir=l.split("/")
                    x=dir[len(dir)-1]
                    x=x.split(".exe")
                    if not x:
                        self.app3.setText("Select Application")
                    else:
                        self.app3.setText(x[0])
        else:
            file=open("b3dir.boo", "w+")
            file.close()
        if (path.exists("b4dir.boo"))==True:
            with open("b4dir.boo", "r") as f:
                lines = f.readlines()
                for l in lines:
                    dir=l.split("/")
                    x=dir[len(dir)-1]
                    x=x.split(".exe")
                    if not x:
                        self.app4.setText("Select Application")
                    else:
                        self.app4.setText(x[0])
        else:
            file=open("b4dir.boo", "w+")
            file.close()
    
    # initialize apps to the selections
    def selectapp1(self, Handy):
        root = Tk()
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select executable file",filetypes = (("Executable Files","*.exe"),("All files","*.*")))
        file=open("b1dir.boo","w+")
        file.write("\""+root.filename+"\"")
        file.close()
        root.destroy()
        with open("b1dir.boo", "r") as f:
            lines = f.readlines()
            for l in lines:
                dir=l.split("/")
                x=dir[len(dir)-1]
                x=x.split(".exe")
                self.app1.setText(x[0])
        
    def selectapp2(self, Handy):
        root = Tk()
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select executable file",filetypes = (("Executable Files","*.exe"),("All files","*.*")))
        file=open("b2dir.boo","w+")
        file.write("\""+root.filename+"\"")
        file.close()
        root.destroy()
        with open("b2dir.boo", "r") as f:
            lines = f.readlines()
            for l in lines:
                dir=l.split("/")
                x=dir[len(dir)-1]
                x=x.split(".exe")
                self.app2.setText(x[0])
        
    def selectapp3(self, Handy):
        root = Tk()
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select executable file",filetypes = (("Executable Files","*.exe"),("All files","*.*")))
        file=open("b3dir.boo","w+")
        file.write("\""+root.filename+"\"")
        file.close()
        root.destroy()
        with open("b3dir.boo", "r") as f:
            lines = f.readlines()
            for l in lines:
                dir=l.split("/")
                x=dir[len(dir)-1]
                x=x.split(".exe")
                self.app3.setText(x[0])
        
    def selectapp4(self, Handy):
        root = Tk()
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select executable file",filetypes = (("Executable Files","*.exe"),("All files","*.*")))
        file=open("b4dir.boo","w+")
        file.write("\""+root.filename+"\"")
        file.close()
        root.destroy()
        with open("b4dir.boo", "r") as f:
            lines = f.readlines()
            for l in lines:
                dir=l.split("/")
                
                x=dir[len(dir)-1]
                x=x.split(".exe")
                self.app4.setText(x[0])

    # functioning the eye
    def camSetup(self, Handy):
        self.eyeLogo.setStyleSheet("#eyeLogo{border-image: url(:/EYES/eye.png);}")
        self.label_5.setText("I can read your\nsigns!!!")
        try:
            import handycam
        except SystemExit:
            print()
        self.label_5.setText("Ok!\nClick to wake me up again...")
        self.eyeLogo.setStyleSheet("#eyeLogo{border-image: url(:/EYES/eye_close.png);}")
        

                
        
        
import rscfile_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Handy = QtWidgets.QWidget()
    ui = Ui_Handy()
    ui.setupUi(Handy)
    Handy.show()
    sys.exit(app.exec_())
