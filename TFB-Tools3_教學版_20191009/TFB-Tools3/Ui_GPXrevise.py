# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\vincentlu\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\tfb_tools3\GPXrevise.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GPXrevise_Dialog(object):
    def setupUi(self, TFBToolsDialogBase):
        TFBToolsDialogBase.setObjectName("TFBToolsDialogBase")
        TFBToolsDialogBase.resize(545, 332)
        self.groupBox = QtWidgets.QGroupBox(TFBToolsDialogBase)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 481, 291))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 230, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 30, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 230, 101, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 451, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.imp = QtWidgets.QLineEdit(self.groupBox)
        self.imp.setGeometry(QtCore.QRect(190, 190, 81, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imp.sizePolicy().hasHeightForWidth())
        self.imp.setSizePolicy(sizePolicy)
        self.imp.setObjectName("imp")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(280, 190, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 30, 221, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 100, 111, 21))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 130, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 160, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(70, 130, 141, 21))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 160, 131, 21))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(130, 230, 221, 31))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.retranslateUi(TFBToolsDialogBase)
        QtCore.QMetaObject.connectSlotsByName(TFBToolsDialogBase)

    def retranslateUi(self, TFBToolsDialogBase):
        _translate = QtCore.QCoreApplication.translate
        TFBToolsDialogBase.setWindowTitle(_translate("TFBToolsDialogBase", "林務局圖資操作工具"))
        self.groupBox.setTitle(_translate("TFBToolsDialogBase", "GPX飄移點處理"))
        self.pushButton.setText(_translate("TFBToolsDialogBase", "匯入GPX檔"))
        self.pushButton_2.setText(_translate("TFBToolsDialogBase", "刪除飄移點並匯出"))
        self.pushButton_3.setText(_translate("TFBToolsDialogBase", "檢測飄移點"))
        self.pushButton_4.setText(_translate("TFBToolsDialogBase", "匯出路徑"))
        self.label_3.setText(_translate("TFBToolsDialogBase", "檢視與飄移點處理"))
        self.label_4.setText(_translate("TFBToolsDialogBase", "檢測結果: 總距離 =                                          公里"))
        self.label_5.setText(_translate("TFBToolsDialogBase", "刪除條件: \'建議\'當移動速率大於"))
        self.label_6.setText(_translate("TFBToolsDialogBase", "(公里/小時)，視為飄移點位。"))
        self.lineEdit_3.setPlaceholderText(_translate("TFBToolsDialogBase", "匯入GPX(.gpx)路徑"))
        self.label_7.setText(_translate("TFBToolsDialogBase", "總時間 =                                                   小時"))
        self.label_8.setText(_translate("TFBToolsDialogBase", "平均速率 =                                               (公里/小時)。"))
        self.lineEdit_7.setPlaceholderText(_translate("TFBToolsDialogBase", "匯出GPX(.gpx)路徑"))


