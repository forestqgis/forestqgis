# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\johnvoo\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\TFB-Tools3\imgpareCSV_dia.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IMGPairCSV_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 277)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(340, 140, 25, 25))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_4 = QtWidgets.QToolButton(Dialog)
        self.toolButton_4.setGeometry(QtCore.QRect(340, 30, 25, 25))
        self.toolButton_4.setObjectName("toolButton_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 30, 221, 25))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 140, 221, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton_5 = QtWidgets.QToolButton(Dialog)
        self.toolButton_5.setGeometry(QtCore.QRect(340, 90, 25, 25))
        self.toolButton_5.setObjectName("toolButton_5")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(30, 90, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 90, 221, 25))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.startPair = QtWidgets.QPushButton(Dialog)
        self.startPair.setGeometry(QtCore.QRect(160, 230, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startPair.sizePolicy().hasHeightForWidth())
        self.startPair.setSizePolicy(sizePolicy)
        self.startPair.setObjectName("ok")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 60, 72, 23))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.toolButton_3 = QtWidgets.QToolButton(Dialog)
        self.toolButton_3.setGeometry(QtCore.QRect(340, 190, 25, 25))
        self.toolButton_3.setObjectName("toolButton_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 190, 221, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 190, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "照片CSV比對"))
        self.label_2.setText(_translate("Dialog", "選取CSV文件"))
        self.label_9.setText(_translate("Dialog", "選取照片文件夾"))
        self.toolButton_2.setText(_translate("Dialog", "..."))
        self.toolButton_4.setText(_translate("Dialog", "..."))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "照片(.jpe)路徑"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "CSV檔路徑"))
        self.toolButton_5.setText(_translate("Dialog", "..."))
        self.label_10.setText(_translate("Dialog", "選取照片文件"))
        self.lineEdit_5.setPlaceholderText(_translate("Dialog", "照片(.jpe)路徑"))
        self.startPair.setText(_translate("Dialog", "開始比對"))
        self.label_3.setText(_translate("Dialog", "或"))
        self.toolButton_3.setText(_translate("Dialog", "..."))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", ".shp檔路徑"))
        self.label_4.setText(_translate("Dialog", "輸出檔案"))
