# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './dialog_umbenennen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Umbenennen(object):
    def setupUi(self, Dialog_Umbenennen):
        Dialog_Umbenennen.setObjectName("Dialog_Umbenennen")
        Dialog_Umbenennen.setWindowModality(QtCore.Qt.NonModal)
        Dialog_Umbenennen.resize(288, 84)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_Umbenennen.sizePolicy().hasHeightForWidth())
        Dialog_Umbenennen.setSizePolicy(sizePolicy)
        Dialog_Umbenennen.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_Umbenennen)
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_locationname = QtWidgets.QLineEdit(Dialog_Umbenennen)
        self.le_locationname.setObjectName("le_locationname")
        self.verticalLayout.addWidget(self.le_locationname)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Umbenennen)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog_Umbenennen)
        self.buttonBox.accepted.connect(Dialog_Umbenennen.accept)
        self.buttonBox.rejected.connect(Dialog_Umbenennen.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Umbenennen)

    def retranslateUi(self, Dialog_Umbenennen):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Umbenennen.setWindowTitle(_translate("Dialog_Umbenennen", "Umbennennen"))
        self.le_locationname.setPlaceholderText(_translate("Dialog_Umbenennen", "Neuer Name"))
