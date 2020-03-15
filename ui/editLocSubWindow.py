from ui.editLocationDialog import Ui_Dialog as ui
from ui.dialog_umbenennen import Ui_Dialog_Umbenennen as renameDialog
from PyQt5 import QtWidgets, Qt
from PyQt5.QtWidgets import QMessageBox, QDialogButtonBox, QDialog
from PyQt5.QtCore import Qt as qt, QObject, pyqtSignal
from db import db


class editLocSubWindow(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = ui()
        self.ui.setupUi(self)

        self.setWindowTitle("Lagerorte bearbeiten")
        self.ui.lbl_SubLocation.clear()
        self.mainlocationlist = self.ui.lw_MainLocation
        self.sublocationlist = self.ui.lw_Sublocation
        self.newmainlocationtextbox = self.ui.le_newMainLocation
        self.buttonwritenewmainlocation = self.ui.pb_addnewMainLocation
        self.buttonwritenewsublocation = self.ui.pb_addnewSubLocation
        self.newsublocationtextbox = self.ui.le_newSubLocation
        self.newsublocationtextbox.setEnabled(False)

        self.initUi()

    def initUi(self):

        self.mainlocationlist.currentItemChanged.connect(self.mainlocationchanged)
        self.sublocationlist.currentItemChanged.connect(self.sublocationchanged)
        self.ui.pb_removeMainLocation.clicked.connect(self.removemainlocation)
        self.ui.pb_removeSubLocation.clicked.connect(self.removesublocation)
        self.newmainlocationtextbox.textChanged.connect(self.enableAddnewMainButton)
        self.newsublocationtextbox.textChanged.connect(self.enableAddnewSubButton)
        self.buttonwritenewmainlocation.clicked.connect(self.writenewmainlocation)
        self.buttonwritenewsublocation.clicked.connect(self.writenewsublocation)
        self.ui.le_newMainLocation.returnPressed.connect(self.writenewmainlocation)
        self.ui.le_newSubLocation.returnPressed.connect(self.writenewsublocation)
        self.ui.pb_editMainLocation.clicked.connect(self.renameLocation)
        self.ui.pb_editSubLocation.clicked.connect(self.renameLocation)
        self.readMainLocationinListWidget()



    def updatesignal(self):
        print("updatesignal")

    def renameLocation(self):
        print(self.sender())
        sender = self.sender().objectName()

        if sender == 'pb_editMainLocation':
            print("renameMain")
            currentitem = self.mainlocationlist.selectedItems()
            location = currentitem[0].data(qt.UserRole)
            self.renDialog = renameWindow('main', location)
            if self.renDialog.exec() == QDialog.Accepted:
                print("ok geklickt")
                self.update()
            else:
                print("Abgebrochen")

        elif sender == 'pb_editSubLocation':
            print("renameSub")
            currentitem = self.sublocationlist.selectedItems()
            location = currentitem[0].data(qt.UserRole)
            self.renDialog = renameWindow('sub', location)
            if self.renDialog.exec() == QDialog.Accepted:
                print("ok geklickt")
                self.updateSubLocationlist()
            else:
                print("Abgebrochen")

    def writenewmainlocation(self):
        newlocation = self.newmainlocationtextbox.text().strip()
        if len(str.replace(newlocation," ","")) > 0:
            if db.addLocation('main', newlocation):
                print("Erfolgreich gespeichert")
                self.update()
            else:
                QMessageBox.critical(self, 'Fehler!',
                                     "Fehler beim schreiben. {location} ist bereits vorhanden! Bitte anderen Namen wählen.".format(location=newlocation),
                                     QMessageBox.Ok)
        else:
            print("Leerzeichen")

    def writenewsublocation(self):
        newlocation = self.newsublocationtextbox.text().strip()
        currentmainitem = self.mainlocationlist.selectedItems()
        mainlocation = currentmainitem[0].data(qt.UserRole)
        if len(str.replace(newlocation," ","")) > 0:
            if db.addLocation('sub', newlocation, mainlocation[0]):
                print("Erfolgreich gespeichert")
                self.newsublocationtextbox.clear()
                self.updateSubLocationlist()
            else:
                #Nicht mehr implementiert da das feld name nicht mehr unique ist
                QMessageBox.critical(self, 'Fehler!',
                                     "Fehler beim schreiben. {location} ist bereits vorhanden! Bitte anderen Namen wählen.".format(location=newlocation),
                                     QMessageBox.Ok)
        else:
            print("Leerzeichen")

    def enableAddnewMainButton(self):
        if len(self.newmainlocationtextbox.text()) > 0:
            self.ui.pb_addnewMainLocation.setEnabled(True)
        else:
            self.ui.pb_addnewMainLocation.setEnabled(False)

    def enableAddnewSubButton(self):
        if len(self.newsublocationtextbox.text()) > 0:
            self.ui.pb_addnewSubLocation.setEnabled(True)
        else:
            self.ui.pb_addnewSubLocation.setEnabled(False)

    def removesublocation(self):
        currentitem = self.sublocationlist.selectedItems()
        locationtoremove = currentitem[0].data(qt.UserRole)
        buttonReply = QMessageBox.question(self, 'Löschen!',
                                           "Willst du den Lagerunterort \"{ort}\" wirklich löschen?".format(
                                               ort=locationtoremove[1]),
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            if db.removeLocation('sub', locationtoremove[0]):
                print('erfolgreich gelöscht')
            self.updateSubLocationlist()
        else:
            pass

    def removemainlocation(self):

        currentitem = self.mainlocationlist.selectedItems()
        locationtoremove = currentitem[0].data(qt.UserRole)
        buttonReply = QMessageBox.question(self, 'Löschen!',
                                           "Willst du den Lagerort \"{ort}\" wirklich löschen?".format(ort=locationtoremove[1]),
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            if db.removeLocation('main', locationtoremove[0]):
                print('erfolgreich gelöscht')
            self.update()
        else:
            pass
        #print(locationtoremove)

    def sublocationchanged(self, item):
        self.ui.pb_removeSubLocation.setEnabled(True)
        self.ui.pb_editSubLocation.setEnabled(True)
        print('test')

    def mainlocationchanged(self, item):
        if item:
            self.sublocationlist.clear()
            self.ui.pb_removeSubLocation.setEnabled(False)
            self.ui.pb_editSubLocation.setEnabled(False)
            self.ui.pb_editMainLocation.setEnabled(True)
            self.ui.pb_removeMainLocation.setEnabled(True)
            self.newsublocationtextbox.setEnabled(True)
            mainLocation = item.data(qt.UserRole)
            sublocations = db.readLocations('sub', mainLocation[0])
            self.ui.lbl_SubLocation.setText(mainLocation[1])

            for e in sublocations:
                self.sublocationlist.addItem(self.makeListItem(e))

        else:
            pass

    def updateSubLocationlist(self):
        self.sublocationlist.clear()
        mainlocation = self.mainlocationlist.selectedItems()[0].data(qt.UserRole)[0]
        sublocations = db.readLocations('sub', mainlocation)

        for e in sublocations:
            self.sublocationlist.addItem(self.makeListItem(e))

        if self.sublocationlist.count() == 0:
            self.ui.pb_removeSubLocation.setEnabled(False)
            self.ui.pb_editSubLocation.setEnabled(False)

    def readMainLocationinListWidget(self):
        self.mainlocationlist.clear()
        mainLocation = db.readLocations('main')
        for e in mainLocation:
            self.mainlocationlist.addItem(self.makeListItem(e))

    def makeListItem(self,daten):
        data = []
        listItem = Qt.QListWidgetItem()
        listItem.setText(daten['name'])
        for i in daten:
            data.append(daten[i])
        listItem.setData(qt.UserRole, data)
        return listItem

    def update(self, *__args):
        print('update')
        self.newmainlocationtextbox.clear()
        self.readMainLocationinListWidget()
        self.ui.pb_removeSubLocation.setEnabled(False)
        self.ui.pb_editSubLocation.setEnabled(False)
        if self.mainlocationlist.count() == 0:
            self.ui.pb_removeMainLocation.setEnabled(False)
            self.ui.pb_editMainLocation.setEnabled(False)
        self.sublocationlist.clear()


class renameWindow(QtWidgets.QDialog):
    def __init__(self, type, data, parent = None):
        super().__init__(parent)
        self.type = type
        self.ui = renameDialog()
        self.ui.setupUi(self)
        self.data = data
        self.setWindowTitle("Umbenennen")
        self.initUi()

    def initUi(self):

        if self.type == 'main':
            currentname = self.data[1]
            self.locationid = self.data[0]
            self.ui.le_locationname.setText(str(currentname))
            print("mainitem")

        elif self.type == 'sub':
            currentname = self.data[2]
            self.locationid = self.data[0]
            self.ui.le_locationname.setText(str(currentname))
            print("subitem")

        self.ui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.rename)

    def rename(self):
        newname = self.ui.le_locationname.text()
        if db.renameLocations(self.type, self.locationid, newname):
            print("Erfolgreich umbenannt")
