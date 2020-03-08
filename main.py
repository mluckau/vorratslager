import sys
from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import QDate, Qt as qt
from PyQt5.QtGui import QIcon
import ciso8601
#
# Resourcendatei aktualisieren
# pyrcc5 icons.qrc -o icons_rc.py
#
from items import newItem, item
from db import db
from ui.MainWindow import Ui_MainWindow
from ui.NewEntry import Ui_Dialog as NewEntryWindow
import ui.editLocSubWindow
import time, datetime
from datetime import date
import pandas as pd
from dateutil.relativedelta import relativedelta

app = QtWidgets.QApplication(sys.argv)


def calculateHaltbarkeitinTagen(mhd):
    #aktuelleZeit = pd.Timestamp.now(tz="Europe/Berlin")
    aktuelleZeit = pd.Timestamp.now()
    mhDatum = pd.to_datetime(mhd)
    diff = mhDatum - aktuelleZeit
    return diff

def calculateHaltbarkeit(mhd):
    mhdate = datetime.datetime.strptime(mhd, '%d.%m.%Y').date()
    diff = relativedelta(mhdate, date.today())
    return diff

def getTimestamp(date):
    return time.mktime(datetime.datetime.strptime(date, "%d.%m.%Y").timetuple())


class newEntryWindow(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = NewEntryWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Neuer Eintrag")
        self.ui.dE_MHD.setDisplayFormat("dd.MM.yyyy")
        self.ui.dE_MHD.setDate(QDate.currentDate())
        self.ui.PB_createItem.clicked.connect(self.setItem)
        self.ui.pB_Abbrechen.clicked.connect(self.cancel)
        self.ui.pb_addLocation.clicked.connect(self.openLocationWindow)
        self.initUi()

    def initUi(self):
        self.ui.cb_mainLocation.clear()
        mainLocation = db.readLocations('main')
        for e in mainLocation:
            self.ui.cb_mainLocation.addItem(str(e['name']), e['id'])
        self.ui.cb_mainLocation.setCurrentIndex(-1)
        self.ui.cb_mainLocation.currentIndexChanged.connect(self.getSubLocations)

    def getSubLocations(self, index):
        self.ui.cb_subLocation.clear()
        mainLocation = self.ui.cb_mainLocation.itemData(index)
        if not mainLocation == None:
            subLocations = db.readLocations('sub', mainLocation)
            for e in subLocations:
                self.ui.cb_subLocation.addItem(str(e['name']), e['id'])
            self.ui.cb_subLocation.setCurrentIndex(0)

    def cancel(self):
        self.clearLe()
        self.close()

    def clearLe(self):
        self.ui.Le_Name.clear()
        self.ui.Le_Kategorie.clear()
        self.ui.Le_Anzahl.clear()
        self.ui.le_Menge.clear()
        self.ui.le_Kalorien.clear()
        self.ui.le_portionen.clear()
        self.ui.dE_MHD.setDate(datetime.datetime.today())
        self.ui.cb_mainLocation.setCurrentIndex(-1)
        self.ui.cb_subLocation.setCurrentIndex(-1)
        self.ui.le_minMenge.clear()


    def setItem(self):
        newitem = item.foodItem(self.ui.Le_Name.text(), self.ui.Le_Anzahl.text(), self.ui.le_minMenge.text())
        newitem.setLocation(self.ui.cb_mainLocation.itemData(self.ui.cb_mainLocation.currentIndex()), self.ui.cb_subLocation.itemData(self.ui.cb_subLocation.currentIndex()))
        newitem.setDetails(self.ui.Le_Kategorie.text())
        date = self.ui.dE_MHD.date().toString('dd.MM.yyyy')
        newitem.setFoodDetails(date, self.ui.le_Menge.text(), self.ui.le_portionen.text(), self.ui.le_Kalorien.text())
        if newItem.addItemToDb(newitem):
            self.ui.lbl_StatusText.setText("Eintrag erfolgreich angelegt")
            self.clearLe()

    def openLocationWindow(self):
        self.editLocationWindow = ui.editLocSubWindow.editLocSubWindow()
        self.editLocationWindow.exec()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.newEntry = newEntryWindow()
        self.MainWindow = Ui_MainWindow()
        self.editLocationWindow = ui.editLocSubWindow.editLocSubWindow()

        self.initMe()

    def initMe(self):
        self.MainWindow.setupUi(self)
        self.statusBar().showMessage('Hallo und Willkommen!')
        self.setWindowTitle("Vorratslager")
        self.MainWindow.pB_hinzufuegen.clicked.connect(self.addNewEntry)
        self.itemDetailFrame = self.MainWindow.ItemDetailframe
        self.itemDetailFrame.setEnabled(False)
        self.itemDetailFrame.hide()

        #Menubar Actions
        self.MainWindow.actionBeenden.triggered.connect(self.close)
        self.MainWindow.actionAddFood.triggered.connect(self.addNewEntry)
        self.MainWindow.actionRefresh.triggered.connect(self.readDataIntoTable)
        self.MainWindow.actionKategorienBearbeiten.triggered.connect(self.openEditLocationWindow)

        #Database einlesen
        self.readDataIntoTable()
        self.MainWindow.listWidget.itemClicked.connect(self.listItemClicked)

    def listItemClicked(self, item):
        listdata = item.data(qt.UserRole)

        itemdetails = db.readItem(listdata[0])

        self.MainWindow.lbl_DetailName_2.setText(itemdetails['name'])
        self.MainWindow.lbl_DetailMHD.setText(itemdetails['mhd'])
        print(itemdetails['mhd'])
        mainlocation = listdata[5]
        if mainlocation is not None:
            self.MainWindow.lbl_DetailMainLagerplatz.setText(db.locationfromid('main', listdata[5])['name'])
        if not itemdetails['subLocation'] is None:
            self.MainWindow.lbl_DetailSubLagerplatz.show()
            self.MainWindow.lbl_DetailPfeilLocation.show()
            self.MainWindow.lbl_DetailSubLagerplatz.setText(db.locationfromid('sub', listdata[6])['name'])
        else:
            self.MainWindow.lbl_DetailSubLagerplatz.hide()
            self.MainWindow.lbl_DetailPfeilLocation.hide()
        self.itemDetailFrame.setEnabled(True)
        self.itemDetailFrame.show()
        print(listdata[11])

    def readDataIntoTable(self):
        items = db.readDb()
        if not (len(items) <= 0):
            columnCount = len(items[0])
            self.MainWindow.tW_Items.setColumnCount(columnCount)
            self.MainWindow.tW_Items.setRowCount(0)
            header = self.MainWindow.tW_Items.horizontalHeader()
            self.MainWindow.listWidget.clear()
            for i in items:
                data = []
                listItem = Qt.QListWidgetItem()
                listItem.setText(i['name'] + ' ' + str(i['menge']))
                for e in i:
                    data.append(i[e])
                if i['type'] == 'food':
                    listItem.setIcon(QIcon(item.icon_food))
                    #Haltbarkeit in Tage ausrechnen
                    haltbarkeit = []
                    #tagenochHaltbar = calculateHaltbarkeitinTagen(i[7])
                    haltbarkeit = calculateHaltbarkeit(i['mhd'])
                    data.append(haltbarkeit)
                elif i['type'] == 'nonfood':
                    listItem.setIcon(QIcon(item.icon_nonfood))
                listItem.setData(qt.UserRole, data)
                self.MainWindow.listWidget.addItem(listItem)

            for row_number, row_data in enumerate(items):
                self.MainWindow.tW_Items.insertRow(row_number)

                for column_number, data in enumerate(row_data):

                    self.MainWindow.tW_Items.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    def addNewEntry(self):
        self.newEntry.exec()

    def openEditLocationWindow(self):
        self.editLocationWindow.exec()

db.checkDb()
window = MainWindow()
window.show()

sys.exit(app.exec_())