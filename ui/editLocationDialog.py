# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './editLocationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(836, 614)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.le_newMainLocation = QtWidgets.QLineEdit(Dialog)
        self.le_newMainLocation.setEnabled(True)
        self.le_newMainLocation.setObjectName("le_newMainLocation")
        self.verticalLayout_5.addWidget(self.le_newMainLocation)
        self.lw_MainLocation = QtWidgets.QListWidget(Dialog)
        self.lw_MainLocation.setObjectName("lw_MainLocation")
        self.verticalLayout_5.addWidget(self.lw_MainLocation)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_addnewMainLocation = QtWidgets.QPushButton(Dialog)
        self.pb_addnewMainLocation.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_addnewMainLocation.sizePolicy().hasHeightForWidth())
        self.pb_addnewMainLocation.setSizePolicy(sizePolicy)
        self.pb_addnewMainLocation.setMaximumSize(QtCore.QSize(16000, 16000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/emblem-new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_addnewMainLocation.setIcon(icon)
        self.pb_addnewMainLocation.setIconSize(QtCore.QSize(22, 22))
        self.pb_addnewMainLocation.setFlat(True)
        self.pb_addnewMainLocation.setObjectName("pb_addnewMainLocation")
        self.verticalLayout.addWidget(self.pb_addnewMainLocation)
        self.pb_removeMainLocation = QtWidgets.QPushButton(Dialog)
        self.pb_removeMainLocation.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_removeMainLocation.sizePolicy().hasHeightForWidth())
        self.pb_removeMainLocation.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/emblem-remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_removeMainLocation.setIcon(icon1)
        self.pb_removeMainLocation.setIconSize(QtCore.QSize(22, 22))
        self.pb_removeMainLocation.setFlat(True)
        self.pb_removeMainLocation.setObjectName("pb_removeMainLocation")
        self.verticalLayout.addWidget(self.pb_removeMainLocation)
        self.pb_editMainLocation = QtWidgets.QPushButton(Dialog)
        self.pb_editMainLocation.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_editMainLocation.sizePolicy().hasHeightForWidth())
        self.pb_editMainLocation.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/emblem-system.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_editMainLocation.setIcon(icon2)
        self.pb_editMainLocation.setIconSize(QtCore.QSize(22, 22))
        self.pb_editMainLocation.setFlat(True)
        self.pb_editMainLocation.setObjectName("pb_editMainLocation")
        self.verticalLayout.addWidget(self.pb_editMainLocation)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_SubLocation = QtWidgets.QLabel(Dialog)
        self.lbl_SubLocation.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_SubLocation.setFont(font)
        self.lbl_SubLocation.setScaledContents(False)
        self.lbl_SubLocation.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_SubLocation.setWordWrap(False)
        self.lbl_SubLocation.setObjectName("lbl_SubLocation")
        self.verticalLayout_4.addWidget(self.lbl_SubLocation)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.le_newSubLocation = QtWidgets.QLineEdit(Dialog)
        self.le_newSubLocation.setEnabled(True)
        self.le_newSubLocation.setObjectName("le_newSubLocation")
        self.verticalLayout_6.addWidget(self.le_newSubLocation)
        self.lw_Sublocation = QtWidgets.QListWidget(Dialog)
        self.lw_Sublocation.setObjectName("lw_Sublocation")
        self.verticalLayout_6.addWidget(self.lw_Sublocation)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pb_addnewSubLocation = QtWidgets.QPushButton(Dialog)
        self.pb_addnewSubLocation.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_addnewSubLocation.sizePolicy().hasHeightForWidth())
        self.pb_addnewSubLocation.setSizePolicy(sizePolicy)
        self.pb_addnewSubLocation.setIcon(icon)
        self.pb_addnewSubLocation.setIconSize(QtCore.QSize(22, 22))
        self.pb_addnewSubLocation.setFlat(True)
        self.pb_addnewSubLocation.setObjectName("pb_addnewSubLocation")
        self.verticalLayout_2.addWidget(self.pb_addnewSubLocation)
        self.pb_removeSubLocation = QtWidgets.QPushButton(Dialog)
        self.pb_removeSubLocation.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_removeSubLocation.sizePolicy().hasHeightForWidth())
        self.pb_removeSubLocation.setSizePolicy(sizePolicy)
        self.pb_removeSubLocation.setIcon(icon1)
        self.pb_removeSubLocation.setIconSize(QtCore.QSize(22, 22))
        self.pb_removeSubLocation.setFlat(True)
        self.pb_removeSubLocation.setObjectName("pb_removeSubLocation")
        self.verticalLayout_2.addWidget(self.pb_removeSubLocation)
        self.pb_editSubLocation = QtWidgets.QPushButton(Dialog)
        self.pb_editSubLocation.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_editSubLocation.sizePolicy().hasHeightForWidth())
        self.pb_editSubLocation.setSizePolicy(sizePolicy)
        self.pb_editSubLocation.setIcon(icon2)
        self.pb_editSubLocation.setIconSize(QtCore.QSize(22, 22))
        self.pb_editSubLocation.setFlat(True)
        self.pb_editSubLocation.setObjectName("pb_editSubLocation")
        self.verticalLayout_2.addWidget(self.pb_editSubLocation)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_7.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Hauptlagerorte"))
        self.le_newMainLocation.setToolTip(_translate("Dialog", "Name des neuen Lagerortes"))
        self.le_newMainLocation.setPlaceholderText(_translate("Dialog", "Name vom Hauptlagerort"))
        self.lbl_SubLocation.setText(_translate("Dialog", "Lagerunterorte"))
        self.le_newSubLocation.setToolTip(_translate("Dialog", "Name des neuen Lagerunterortes"))
        self.le_newSubLocation.setPlaceholderText(_translate("Dialog", "Name vom Lagerunterort"))
from ui import icons_rc
