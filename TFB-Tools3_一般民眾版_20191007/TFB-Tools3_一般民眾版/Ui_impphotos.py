# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\vincentlu\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\tfb_tools3\impphotos.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_photosImp_Dialog(object):
    def setupUi(self, photosImp):
        photosImp.setObjectName("photosImp")
        photosImp.setWindowModality(QtCore.Qt.NonModal)
        photosImp.resize(382, 283)
        photosImp.setMinimumSize(QtCore.QSize(382, 223))
        photosImp.setWhatsThis("")
        photosImp.setSizeGripEnabled(False)
        self.widget = QtWidgets.QWidget(photosImp)
        self.widget.setGeometry(QtCore.QRect(40, 31, 294, 218))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.imp = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imp.sizePolicy().hasHeightForWidth())
        self.imp.setSizePolicy(sizePolicy)
        self.imp.setObjectName("imp")
        self.gridLayout.addWidget(self.imp, 0, 1, 1, 2)
        self.toolButtonImport = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButtonImport.sizePolicy().hasHeightForWidth())
        self.toolButtonImport.setSizePolicy(sizePolicy)
        self.toolButtonImport.setObjectName("toolButtonImport")
        self.gridLayout.addWidget(self.toolButtonImport, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.out = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out.sizePolicy().hasHeightForWidth())
        self.out.setSizePolicy(sizePolicy)
        self.out.setObjectName("out")
        self.gridLayout.addWidget(self.out, 2, 1, 1, 2)
        self.toolButtonOut = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButtonOut.sizePolicy().hasHeightForWidth())
        self.toolButtonOut.setSizePolicy(sizePolicy)
        self.toolButtonOut.setObjectName("toolButtonOut")
        self.gridLayout.addWidget(self.toolButtonOut, 2, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.load_style_path = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_style_path.sizePolicy().hasHeightForWidth())
        self.load_style_path.setSizePolicy(sizePolicy)
        self.load_style_path.setObjectName("load_style_path")
        self.gridLayout.addWidget(self.load_style_path, 4, 1, 1, 2)
        self.input_load_style = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_load_style.sizePolicy().hasHeightForWidth())
        self.input_load_style.setSizePolicy(sizePolicy)
        self.input_load_style.setObjectName("input_load_style")
        self.gridLayout.addWidget(self.input_load_style, 4, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 5, 2, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 6, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 6, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 6, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.ok = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy)
        self.ok.setObjectName("ok")
        self.horizontalLayout_2.addWidget(self.ok)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 1, 1, 2)
        self.closebutton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closebutton.sizePolicy().hasHeightForWidth())
        self.closebutton.setSizePolicy(sizePolicy)
        self.closebutton.setObjectName("closebutton")
        self.gridLayout.addWidget(self.closebutton, 7, 3, 1, 1)

        self.retranslateUi(photosImp)
        QtCore.QMetaObject.connectSlotsByName(photosImp)

    def retranslateUi(self, photosImp):
        _translate = QtCore.QCoreApplication.translate
        photosImp.setWindowTitle(_translate("photosImp", "照片EXIF定位"))
        self.label.setText(_translate("photosImp", "照片路徑"))
        self.toolButtonImport.setText(_translate("photosImp", "選取"))
        self.label_2.setText(_translate("photosImp", "輸出檔案"))
        self.toolButtonOut.setText(_translate("photosImp", "選取"))
        self.label_3.setText(_translate("photosImp", "匯入點位樣式"))
        self.load_style_path.setPlaceholderText(_translate("photosImp", "選取qml檔(選填)"))
        self.input_load_style.setText(_translate("photosImp", "選取"))
        self.label_4.setText(_translate("photosImp", "請選擇輸出檔案坐標系統"))
        self.comboBox.setItemText(0, _translate("photosImp", "WGS 84"))
        self.comboBox.setItemText(1, _translate("photosImp", "TWD 97"))
        self.ok.setText(_translate("photosImp", "確認"))
        self.closebutton.setText(_translate("photosImp", "關閉"))


