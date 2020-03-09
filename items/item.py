import time
import datetime

icon_food = 'ui/spoon-and-a-fork.svg'
icon_nonfood = 'ui/tool.svg'


class item():
    def __init__(self, name, anzahl, minAnzahl, kategorie, lagerfach):
        self.name = name
        self.anzahl = anzahl
        self.minAnzahl = minAnzahl
        self.kategorie = kategorie
        self.lagerfach = lagerfach

    def getName(self):
        return self.name

    def setAnzahl(self, anzahl):
        self.anzahl = anzahl

    def getAnzahl(self):
        return self.anzahl

    def setminAnzahl(self, minAnzahl):
        self.minAnzahl = minAnzahl

    def getminAnzahl(self):
        return self.minAnzahl

    def getMainLocation(self):
        return self.mainLocation

    def setLocation(self, mainLocation, subLocation):
        self.mainLocation = mainLocation
        self.subLocation = subLocation

    def getSubLocation(self):
        return self.subLocation

    def setDetails(self, kategorie, notes):
        self.kategorie = kategorie
        self.notes = notes




class foodItem(item):

    def __init__(self, name, anzahl, minAnzahl=None, kategorie=None, lagerfach = None):
        item.__init__(self, name, anzahl, minAnzahl, kategorie, lagerfach)
        self.type = 'food'

    #TODO Food spezifische Details hinzufügen
    def setFoodDetails(self, mhd, menge, portionen, kalorien):
        self.mhd = mhd
        self.menge = menge
        self.portionen = portionen
        self.kalorien = kalorien

    def getDetails(self):
        return (self.type,
                self.name,
                self.anzahl,
                self.minAnzahl,
                self.kategorie,
                self.mainLocation,
                self.subLocation,
                self.mhd,
                self.menge,
                self.portionen,
                self.kalorien,
                self.notes)



class nonFoodItem(item):

    def __init__(self, name, anzahl):
        item.__init__(self, name, anzahl)
        self.type = 'nonFood'

    # TODO Non-Food spezifische Details hinzufügen
    def setNonFoodDetails(self):
        self.needPower = True

    def getDetails(self):
        return (self.type,
                self.name,
                self.anzahl,
                self.kategorie,
                self.mainLocation,
                self.subLocation)
