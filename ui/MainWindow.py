# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(862, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pB_hinzufuegen = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_hinzufuegen.sizePolicy().hasHeightForWidth())
        self.pB_hinzufuegen.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/emblem-new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_hinzufuegen.setIcon(icon)
        self.pB_hinzufuegen.setFlat(True)
        self.pB_hinzufuegen.setObjectName("pB_hinzufuegen")
        self.horizontalLayout.addWidget(self.pB_hinzufuegen)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(32, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout.addWidget(self.comboBox_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setIconSize(QtCore.QSize(20, 20))
        self.listWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setLayoutMode(QtWidgets.QListView.Batched)
        self.listWidget.setGridSize(QtCore.QSize(0, 22))
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/emblem-synchronizing.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ItemDetailframe = QtWidgets.QFrame(self.centralwidget)
        self.ItemDetailframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ItemDetailframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ItemDetailframe.setObjectName("ItemDetailframe")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ItemDetailframe)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ItemDetailLayout = QtWidgets.QVBoxLayout()
        self.ItemDetailLayout.setObjectName("ItemDetailLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.detailIcon = QtWidgets.QLabel(self.ItemDetailframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detailIcon.sizePolicy().hasHeightForWidth())
        self.detailIcon.setSizePolicy(sizePolicy)
        self.detailIcon.setMaximumSize(QtCore.QSize(64, 64))
        self.detailIcon.setBaseSize(QtCore.QSize(0, 0))
        self.detailIcon.setText("")
        self.detailIcon.setPixmap(QtGui.QPixmap(":/icon/spoon-and-a-fork.svg"))
        self.detailIcon.setScaledContents(True)
        self.detailIcon.setObjectName("detailIcon")
        self.horizontalLayout_4.addWidget(self.detailIcon)
        self.lbl_DetailName_2 = QtWidgets.QLabel(self.ItemDetailframe)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lbl_DetailName_2.setFont(font)
        self.lbl_DetailName_2.setObjectName("lbl_DetailName_2")
        self.horizontalLayout_4.addWidget(self.lbl_DetailName_2)
        self.ItemDetailLayout.addLayout(self.horizontalLayout_4)
        self.LagerplatzLayout = QtWidgets.QHBoxLayout()
        self.LagerplatzLayout.setObjectName("LagerplatzLayout")
        self.lbl_DetailMainLagerplatz = QtWidgets.QLabel(self.ItemDetailframe)
        self.lbl_DetailMainLagerplatz.setObjectName("lbl_DetailMainLagerplatz")
        self.LagerplatzLayout.addWidget(self.lbl_DetailMainLagerplatz)
        self.lbl_DetailPfeilLocation = QtWidgets.QLabel(self.ItemDetailframe)
        self.lbl_DetailPfeilLocation.setObjectName("lbl_DetailPfeilLocation")
        self.LagerplatzLayout.addWidget(self.lbl_DetailPfeilLocation)
        self.lbl_DetailSubLagerplatz = QtWidgets.QLabel(self.ItemDetailframe)
        self.lbl_DetailSubLagerplatz.setObjectName("lbl_DetailSubLagerplatz")
        self.LagerplatzLayout.addWidget(self.lbl_DetailSubLagerplatz)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LagerplatzLayout.addItem(spacerItem1)
        self.lbl_DetailMHD_2 = QtWidgets.QLabel(self.ItemDetailframe)
        self.lbl_DetailMHD_2.setObjectName("lbl_DetailMHD_2")
        self.LagerplatzLayout.addWidget(self.lbl_DetailMHD_2)
        self.lbl_DetailMHD = QtWidgets.QLabel(self.ItemDetailframe)
        self.lbl_DetailMHD.setObjectName("lbl_DetailMHD")
        self.LagerplatzLayout.addWidget(self.lbl_DetailMHD)
        self.ItemDetailLayout.addLayout(self.LagerplatzLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lbl_DetailMenge = QtWidgets.QLabel(self.ItemDetailframe)
        self.lbl_DetailMenge.setObjectName("lbl_DetailMenge")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_DetailMenge)
        self.le_DetailMenge = QtWidgets.QLineEdit(self.ItemDetailframe)
        self.le_DetailMenge.setReadOnly(True)
        self.le_DetailMenge.setObjectName("le_DetailMenge")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_DetailMenge)
        self.le_DetailPortionen = QtWidgets.QLineEdit(self.ItemDetailframe)
        self.le_DetailPortionen.setReadOnly(True)
        self.le_DetailPortionen.setObjectName("le_DetailPortionen")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_DetailPortionen)
        self.label_2 = QtWidgets.QLabel(self.ItemDetailframe)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_3.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.ItemDetailframe)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinBox = QtWidgets.QSpinBox(self.ItemDetailframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setWrapping(False)
        self.spinBox.setObjectName("spinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_4 = QtWidgets.QLabel(self.ItemDetailframe)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.le_kcalPortion = QtWidgets.QLineEdit(self.ItemDetailframe)
        self.le_kcalPortion.setReadOnly(True)
        self.le_kcalPortion.setObjectName("le_kcalPortion")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_kcalPortion)
        self.horizontalLayout_3.addLayout(self.formLayout_2)
        self.ItemDetailLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.ItemDetailLayout)
        self.verticalLayout_2.addWidget(self.ItemDetailframe)
        self.tW_Items = QtWidgets.QTableWidget(self.centralwidget)
        self.tW_Items.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tW_Items.setAlternatingRowColors(True)
        self.tW_Items.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tW_Items.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tW_Items.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tW_Items.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tW_Items.setShowGrid(False)
        self.tW_Items.setColumnCount(0)
        self.tW_Items.setObjectName("tW_Items")
        self.tW_Items.setRowCount(0)
        self.tW_Items.horizontalHeader().setCascadingSectionResizes(True)
        self.tW_Items.horizontalHeader().setStretchLastSection(True)
        self.tW_Items.verticalHeader().setCascadingSectionResizes(True)
        self.tW_Items.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout_2.addWidget(self.tW_Items)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 862, 30))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        self.menuProdukte = QtWidgets.QMenu(self.menubar)
        self.menuProdukte.setObjectName("menuProdukte")
        self.menuNahrungsmittel = QtWidgets.QMenu(self.menuProdukte)
        self.menuNahrungsmittel.setObjectName("menuNahrungsmittel")
        self.menuKategorien_2 = QtWidgets.QMenu(self.menuNahrungsmittel)
        self.menuKategorien_2.setObjectName("menuKategorien_2")
        self.menuLagerorte = QtWidgets.QMenu(self.menubar)
        self.menuLagerorte.setObjectName("menuLagerorte")
        self.menuKategorien = QtWidgets.QMenu(self.menubar)
        self.menuKategorien.setObjectName("menuKategorien")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNon_Food = QtWidgets.QAction(MainWindow)
        self.actionNon_Food.setObjectName("actionNon_Food")
        self.actionSonstiges = QtWidgets.QAction(MainWindow)
        self.actionSonstiges.setObjectName("actionSonstiges")
        self.actionBearbeiten = QtWidgets.QAction(MainWindow)
        self.actionBearbeiten.setObjectName("actionBearbeiten")
        self.actionBeenden = QtWidgets.QAction(MainWindow)
        self.actionBeenden.setObjectName("actionBeenden")
        self.actionAddFood = QtWidgets.QAction(MainWindow)
        self.actionAddFood.setIcon(icon)
        self.actionAddFood.setObjectName("actionAddFood")
        self.actionAlles_anzeigen_2 = QtWidgets.QAction(MainWindow)
        self.actionAlles_anzeigen_2.setObjectName("actionAlles_anzeigen_2")
        self.actionSonstiges_2 = QtWidgets.QAction(MainWindow)
        self.actionSonstiges_2.setObjectName("actionSonstiges_2")
        self.actionHinzuf_gen_2 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/emblem-new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHinzuf_gen_2.setIcon(icon2)
        self.actionHinzuf_gen_2.setObjectName("actionHinzuf_gen_2")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setIcon(icon1)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionKategorienBearbeiten = QtWidgets.QAction(MainWindow)
        self.actionKategorienBearbeiten.setObjectName("actionKategorienBearbeiten")
        self.menuDatei.addAction(self.actionBeenden)
        self.menuKategorien_2.addAction(self.actionSonstiges_2)
        self.menuNahrungsmittel.addAction(self.actionAddFood)
        self.menuNahrungsmittel.addAction(self.menuKategorien_2.menuAction())
        self.menuNahrungsmittel.addAction(self.actionAlles_anzeigen_2)
        self.menuProdukte.addAction(self.menuNahrungsmittel.menuAction())
        self.menuProdukte.addAction(self.actionNon_Food)
        self.menuProdukte.addAction(self.actionHinzuf_gen_2)
        self.menuLagerorte.addAction(self.actionKategorienBearbeiten)
        self.menuKategorien.addAction(self.actionSonstiges)
        self.menuKategorien.addSeparator()
        self.menuKategorien.addAction(self.actionBearbeiten)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuProdukte.menuAction())
        self.menubar.addAction(self.menuLagerorte.menuAction())
        self.menubar.addAction(self.menuKategorien.menuAction())
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAddFood)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pB_hinzufuegen.setStatusTip(_translate("MainWindow", "Neues Item hinzufügen"))
        self.pB_hinzufuegen.setText(_translate("MainWindow", "Hinzufügen"))
        self.label_5.setText(_translate("MainWindow", "Filter"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Äpfel"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Birnen"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Doesenwurst"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.lbl_DetailName_2.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_DetailMainLagerplatz.setText(_translate("MainWindow", "MainLagerplatz"))
        self.lbl_DetailPfeilLocation.setText(_translate("MainWindow", ">"))
        self.lbl_DetailSubLagerplatz.setText(_translate("MainWindow", "Sublagerplatz"))
        self.lbl_DetailMHD_2.setText(_translate("MainWindow", "MHD:"))
        self.lbl_DetailMHD.setText(_translate("MainWindow", "MHD-Datum"))
        self.lbl_DetailMenge.setText(_translate("MainWindow", "Menge:"))
        self.label_2.setText(_translate("MainWindow", "Portionen:"))
        self.label_3.setText(_translate("MainWindow", "Anzahl:"))
        self.label_4.setText(_translate("MainWindow", "kcal/Portion:"))
        self.tW_Items.setSortingEnabled(True)
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.menuProdukte.setTitle(_translate("MainWindow", "Produkte"))
        self.menuNahrungsmittel.setTitle(_translate("MainWindow", "Nahrungsmittel"))
        self.menuKategorien_2.setTitle(_translate("MainWindow", "Kategorien"))
        self.menuLagerorte.setTitle(_translate("MainWindow", "Lagerorte"))
        self.menuKategorien.setTitle(_translate("MainWindow", "Kategorien"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNon_Food.setText(_translate("MainWindow", "Non-Food"))
        self.actionSonstiges.setText(_translate("MainWindow", "Sonstiges"))
        self.actionBearbeiten.setText(_translate("MainWindow", "Bearbeiten"))
        self.actionBeenden.setText(_translate("MainWindow", "&Beenden"))
        self.actionBeenden.setStatusTip(_translate("MainWindow", "Beendet das Programm"))
        self.actionBeenden.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionAddFood.setText(_translate("MainWindow", "Hinzufügen..."))
        self.actionAddFood.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionAlles_anzeigen_2.setText(_translate("MainWindow", "Alles anzeigen..."))
        self.actionSonstiges_2.setText(_translate("MainWindow", "Sonstiges"))
        self.actionHinzuf_gen_2.setText(_translate("MainWindow", "Hinzufügen"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionRefresh.setToolTip(_translate("MainWindow", "Daten neu einlesen"))
        self.actionRefresh.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionKategorienBearbeiten.setText(_translate("MainWindow", "Bearbeiten..."))
        self.actionKategorienBearbeiten.setToolTip(_translate("MainWindow", "Kategorien bearbeiten"))
from ui import icons_rc
