# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\�L�ȧ�_180908\TFB-Tools_180908\TFB-Tools\positioning_dia.ui'
#
# Created: Sat Sep 08 16:19:53 2018
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QComboBox, QGroupBox, QLineEdit, QPushButton, QTabWidget)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_positioning_Dialog(object):
    def setupUi(self, Dialog_2):
        Dialog_2.setObjectName(_fromUtf8("Dialog_2"))
        Dialog_2.resize(535, 718)
        self.groupBox = QGroupBox(Dialog_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 341, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(70, 30, 131, 25))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 30, 121, 25))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_3 = QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(70, 60, 131, 25))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.label = QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 61, 21))
        font = QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 41, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox_2 = QGroupBox(Dialog_2)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 170, 341, 151))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.comboBox_5 = QComboBox(self.groupBox_2)
        self.comboBox_5.setGeometry(QtCore.QRect(70, 20, 131, 25))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_6 = QComboBox(self.groupBox_2)
        self.comboBox_6.setEnabled(False)
        self.comboBox_6.setGeometry(QtCore.QRect(210, 20, 121, 25))
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 41, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboBox_7 = QComboBox(self.groupBox_2)
        self.comboBox_7.setEnabled(False)
        self.comboBox_7.setGeometry(QtCore.QRect(70, 50, 151, 25))
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 61, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.comboBox_8 = QComboBox(self.groupBox_2)
        self.comboBox_8.setEnabled(False)
        self.comboBox_8.setGeometry(QtCore.QRect(70, 80, 131, 25))
        self.comboBox_8.setObjectName(_fromUtf8("comboBox_8"))
        self.comboBox_9 = QComboBox(self.groupBox_2)
        self.comboBox_9.setEnabled(False)
        self.comboBox_9.setGeometry(QtCore.QRect(210, 80, 121, 25))
        self.comboBox_9.setObjectName(_fromUtf8("comboBox_9"))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 31, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(10, 110, 61, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(70, 110, 131, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 110, 75, 25))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.groupBox_3 = QGroupBox(Dialog_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 340, 341, 131))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 91, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox_10 = QComboBox(self.groupBox_3)
        self.comboBox_10.setGeometry(QtCore.QRect(110, 30, 221, 25))
        self.comboBox_10.setEditable(True)
        self.comboBox_10.setObjectName(_fromUtf8("comboBox_10"))
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 41, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.comboBox_11 = QComboBox(self.groupBox_3)
        self.comboBox_11.setGeometry(QtCore.QRect(110, 60, 221, 25))
        self.comboBox_11.setEditable(True)
        self.comboBox_11.setObjectName(_fromUtf8("comboBox_11"))
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 90, 91, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.comboBox_12 = QComboBox(self.groupBox_3)
        self.comboBox_12.setGeometry(QtCore.QRect(110, 90, 221, 25))
        self.comboBox_12.setEditable(True)
        self.comboBox_12.setObjectName(_fromUtf8("comboBox_12"))
        self.comboBox_19 = QComboBox(Dialog_2)
        self.comboBox_19.setGeometry(QtCore.QRect(20, 20, 231, 31))
        font = QFont()
        font.setPointSize(9)
        self.comboBox_19.setFont(font)
        self.comboBox_19.setObjectName(_fromUtf8("comboBox_19"))
        self.comboBox_19.addItem(_fromUtf8(""))
        self.comboBox_19.addItem(_fromUtf8(""))
        self.comboBox_19.addItem(_fromUtf8(""))
        self.comboBox_19.addItem(_fromUtf8(""))
        self.tabWidget = QTabWidget(Dialog_2)
        self.tabWidget.setGeometry(QtCore.QRect(20, 480, 501, 231))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(330, 330, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 471, 191))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        #self.comboBox_14 = QComboBox(self.groupBox_4)
        self.comboBox_14 = CustomComboBox(self.groupBox_4)
        self.comboBox_14.setGeometry(QtCore.QRect(200, 110, 251, 25))
        self.comboBox_14.setObjectName(_fromUtf8("comboBox_14"))
        self.comboBox_14.addItem(_fromUtf8(""))
        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(10, 110, 191, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 101, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        #self.comboBox_16 = QComboBox(self.groupBox_4)
        self.comboBox_16 = CustomComboBox(self.groupBox_4)
        self.comboBox_16.setGeometry(QtCore.QRect(110, 20, 341, 25))
        self.comboBox_16.setObjectName(_fromUtf8("comboBox_16"))
        self.comboBox_16.addItem(_fromUtf8(""))
        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(10, 50, 101, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        #self.comboBox_17 = QComboBox(self.groupBox_4)
        self.comboBox_17 = CustomComboBox(self.groupBox_4)
        self.comboBox_17.setGeometry(QtCore.QRect(110, 50, 341, 25))
        self.comboBox_17.setObjectName(_fromUtf8("comboBox_17"))
        self.comboBox_17.addItem(_fromUtf8(""))
        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(10, 80, 141, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        #self.comboBox_18 = QComboBox(self.groupBox_4)
        self.comboBox_18 = CustomComboBox(self.groupBox_4)
        self.comboBox_18.setGeometry(QtCore.QRect(150, 80, 301, 25))
        self.comboBox_18.setObjectName(_fromUtf8("comboBox_18"))
        self.comboBox_18.addItem(_fromUtf8(""))
        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(10, 140, 171, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        #self.comboBox_20 = QComboBox(self.groupBox_4)
        self.comboBox_20 = CustomComboBox(self.groupBox_4)
        self.comboBox_20.setGeometry(QtCore.QRect(90, 140, 361, 25))
        self.comboBox_20.setObjectName(_fromUtf8("comboBox_20"))
        self.comboBox_20.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.pushButton_4 = QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 330, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 330, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(14, 330, 81, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.groupBox_5 = QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 471, 191))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setGeometry(QtCore.QRect(10, 80, 111, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 111, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        #self.comboBox_13 = QComboBox(self.groupBox_5)
        self.comboBox_13 = CustomComboBox(self.groupBox_5)
        self.comboBox_13.setGeometry(QtCore.QRect(130, 50, 331, 25))
        self.comboBox_13.setObjectName(_fromUtf8("comboBox_13"))
        self.comboBox_13.addItem(_fromUtf8(""))
        #self.comboBox_15 = QComboBox(self.groupBox_5)
        self.comboBox_15 = CustomComboBox(self.groupBox_5)
        self.comboBox_15.setGeometry(QtCore.QRect(130, 80, 331, 25))
        self.comboBox_15.setObjectName(_fromUtf8("comboBox_15"))
        self.comboBox_15.addItem(_fromUtf8(""))
        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 91, 21))
        font = QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        #self.comboBox_4 = QComboBox(self.groupBox_5)
        self.comboBox_4 = CustomComboBox(self.groupBox_5)
        self.comboBox_4.setGeometry(QtCore.QRect(130, 20, 331, 25))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(Dialog_2)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_2)

    def retranslateUi(self, Dialog_2):
        Dialog_2.setWindowTitle(_translate("Dialog_2", "林務局圖資操作工具", None))
        self.groupBox.setTitle(_translate("Dialog_2", "轄管範圍定位", None))
        self.label.setText(_translate("Dialog_2", "事業區", None))
        self.label_2.setText(_translate("Dialog_2", "林班", None))
        self.groupBox_2.setTitle(_translate("Dialog_2", "國有林地籍圖定位", None))
        self.comboBox_5.setItemText(0, _translate("Dialog_2", "請選擇縣市", None))
        self.label_4.setText(_translate("Dialog_2", "縣市", None))
        self.label_5.setText(_translate("Dialog_2", "事務所", None))
        self.label_6.setText(_translate("Dialog_2", "段", None))
        self.label_17.setText(_translate("Dialog_2", "地號", None))
        self.pushButton_2.setText(_translate("Dialog_2", "查詢", None))
        self.groupBox_3.setTitle(_translate("Dialog_2", "保安林定位", None))
        self.label_7.setText(_translate("Dialog_2", "保安林編號", None))
        self.label_8.setText(_translate("Dialog_2", "段號", None))
        self.label_9.setText(_translate("Dialog_2", "地號 - 母號", None))
        self.comboBox_19.setItemText(0, _translate("Dialog_2", "請選擇欲定位類別", None))
        self.comboBox_19.setItemText(1, _translate("Dialog_2", "轄管範圍定位", None))
        self.comboBox_19.setItemText(2, _translate("Dialog_2", "保安林定位", None))
        self.comboBox_19.setItemText(3, _translate("Dialog_2", "保護區與育樂園區定位", None))
        self.pushButton.setText(_translate("Dialog_2", "套疊圖層", None))
        self.groupBox_4.setTitle(_translate("Dialog_2", "保護區定位", None))
        self.comboBox_14.setItemText(0, _translate("Dialog_2", "請選擇欲定位區位", None))
        self.label_11.setText(_translate("Dialog_2", "野生動物重要棲息環境", None))
        self.label_13.setText(_translate("Dialog_2", "自然保護區", None))
        self.comboBox_16.setItemText(0, _translate("Dialog_2", "請選擇欲定位區位", None))
        self.label_14.setText(_translate("Dialog_2", "自然保留區", None))
        self.comboBox_17.setItemText(0, _translate("Dialog_2", "請選擇欲定位區位", None))
        self.label_15.setText(_translate("Dialog_2", "野生動物保護區", None))
        self.comboBox_18.setItemText(0, _translate("Dialog_2", "請選擇欲定位區位", None))
        self.label_16.setText(_translate("Dialog_2", "國家公園", None))
        self.comboBox_20.setItemText(0, _translate("Dialog_2", "請選擇欲定位區位", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog_2", "保護區", None))
        self.pushButton_4.setText(_translate("Dialog_2", "套疊圖層", None))
        self.pushButton_5.setText(_translate("Dialog_2", "儲存列表", None))
        self.pushButton_6.setText(_translate("Dialog_2", "從列表移除", None))
        self.groupBox_5.setTitle(_translate("Dialog_2", "育樂園區定位", None))
        self.label_12.setText(_translate("Dialog_2", "林業文化園區", None))
        self.label_10.setText(_translate("Dialog_2", "平地森林園區", None))
        self.comboBox_13.setItemText(0, _translate("Dialog_2", "請選擇欲定位區位", None))
        self.comboBox_15.setItemText(0, _translate("Dialog_2", "請選擇欲定位區位", None))
        self.label_3.setText(_translate("Dialog_2", "森林遊樂區", None))
        self.comboBox_4.setItemText(0, _translate("Dialog_2", "請選擇欲定位區位", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog_2", "育樂區", None))


class CustomComboBox(QComboBox):
    popupAboutToBeShown = QtCore.pyqtSignal()

    def __init__(self, parent = None):
        super(CustomComboBox,self).__init__(parent)

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        QComboBox.showPopup(self)
