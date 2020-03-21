import sys
from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import QDate, Qt as qt
from PyQt5.QtGui import QIcon, QPalette, QImage, QPixmap

# Resourcendatei aktualisieren
# pyrcc5 icons.qrc -o icons_rc.py
#
from PyQt5.QtWidgets import QDialog, QSizePolicy, QFileDialog, QMessageBox

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

        self.image = None
        self.ui = NewEntryWindow()
        self.ui.setupUi(self)

        self.ui.imageLabel.setBackgroundRole(QPalette.Base)
        self.ui.imageLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.imageLabel.setMaximumHeight(200)
        self.ui.imageLabel.setMaximumWidth(200)

        self.setWindowTitle("Neuer Eintrag")
        self.ui.dE_MHD.setDisplayFormat("dd.MM.yyyy")
        self.ui.dE_MHD.setDate(QDate.currentDate())
        self.ui.PB_createItem.clicked.connect(self.setItem)
        self.ui.pB_Abbrechen.clicked.connect(self.cancel)
        self.ui.pb_addLocation.clicked.connect(self.openLocationWindow)
        self.initUi()

    def initUi(self):
        self.ui.cb_mainLocation.clear()
        self.ui.cb_subLocation.setEnabled(False)
        mainLocation = db.readLocations('main')
        self.ui.cb_mainLocation.addItem('', -1)
        for e in mainLocation:
            self.ui.cb_mainLocation.addItem(str(e['name']), e['id'])
        self.ui.cb_mainLocation.setCurrentIndex(-1)
        self.ui.cb_mainLocation.currentIndexChanged.connect(self.getSubLocations)
        self.ui.pB_loadImage.clicked.connect(self.openImage)

    def openImage(self):
        #https://gist.github.com/acbetter/32c575803ec361c3e82064e60db4e3e0
        options = QFileDialog.Options()

        filename, _ = QFileDialog.getOpenFileName(self, 'Bild laden', '', 'Bilder (*.png *.jpg *.gif)', options=options)

        if filename:
            image = QImage(filename)
            if image.isNull():
                QMessageBox.information(self, "Image Viewer", "Cannot load %s." % filename)
                return

            #self.ui.imageLabel.setPixmap(QPixmap.fromImage(image).scaled(self.ui.imageLabel.maximumHeight(),self.ui.imageLabel.maximumWidth(), Qt.KeepAspectRatio))
            self.ui.imageLabel.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0
            self.ui.imageLabel.setScaledContents(True)
            self.ui.imageLabel.adjustSize()
            self.filename = filename
            self.image = image
            self.imagedata = self.convertToBinaryData(filename)

    def convertToBinaryData(self, filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData

    def getSubLocations(self, index):
        mainLocation = self.ui.cb_mainLocation.itemData(index)
        if mainLocation == -1:
            self.ui.cb_subLocation.clear()
            self.ui.cb_subLocation.setEnabled(False)
        elif not self.ui.cb_mainLocation.currentIndex() == -1:
            self.ui.cb_subLocation.setEnabled(True)
            self.ui.cb_subLocation.clear()
            self.ui.cb_subLocation.addItem('', -1)
            if not mainLocation == None:
                subLocations = db.readLocations('sub', mainLocation)
                for e in subLocations:
                    self.ui.cb_subLocation.addItem(str(e['name']), e['id'])
                self.ui.cb_subLocation.setCurrentIndex(0)
        else:
            self.ui.cb_subLocation.setEnabled(False)

    def cancel(self):
        self.clearLe()
        self.reject()

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
        self.ui.te_notes.clear()
        self.ui.le_minMenge.clear()


    def setItem(self):
        newitem = item.foodItem(self.ui.Le_Name.text(), self.ui.Le_Anzahl.text(), self.ui.le_minMenge.text())
        newitem.setLocation(self.getLocation())
        newitem.setDetails(self.ui.Le_Kategorie.text(), self.ui.te_notes.toPlainText())
        date = self.ui.dE_MHD.date().toString('dd.MM.yyyy')
        newitem.setFoodDetails(date, self.ui.le_Menge.text(), self.ui.le_portionen.text(), self.ui.le_Kalorien.text())

        if not self.image:
            itemid = newItem.addItemToDb(newitem)
            self.ui.lbl_StatusText.setText("Eintrag erfolgreich angelegt")
            self.clearLe()
        else:
            newitem.sethasImage(1)
            itemid = newItem.addItemToDb(newitem)
            imgdata = (itemid, self.filename, self.imagedata)
            result = newItem.addImageToDb(imgdata)
            if result:
                print("ID: " + str(itemid))
                print("Bild erfolgreich gespeichert")
                self.ui.lbl_StatusText.setText("Eintrag erfolgreich angelegt")
                self.clearLe()
            else:
                print("Da is was schief gelaufen")


    def getLocation(self):
        mainLocation = self.ui.cb_mainLocation.itemData(self.ui.cb_mainLocation.currentIndex())
        subLocation = self.ui.cb_subLocation.itemData(self.ui.cb_subLocation.currentIndex())
        if mainLocation == -1:
            mainLocation = ''
        if subLocation == -1:
            subLocation = ''
        return (mainLocation, subLocation)


    def openLocationWindow(self):
        self.editLocationWindow = ui.editLocSubWindow.editLocSubWindow()
        if self.editLocationWindow.exec() == QDialog.Accepted:
            print("fertig")


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
                listItem.setText(str(i['anzahl']) + 'x ' + i['name'] + ' ' + str(i['menge']))
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
        if self.newEntry.exec() == QDialog.Rejected:
            print("fertig")
            self.readDataIntoTable()


    def openEditLocationWindow(self):
        self.editLocationWindow.exec()

db.checkDb()
window = MainWindow()
window.show()

sys.exit(app.exec_())