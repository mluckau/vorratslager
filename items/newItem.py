from items import item
from db import db

def newItem():
    items = []
    neuesItem = item.foodItem('Apfel', 3)
    neuesItem.setDetails('Obst', 'Keller')
    items.append(neuesItem)
    neuesItem = item.nonFoodItem('Birne', 6)
    #neuesItem.setDetail('Obst', 'Küche')
    items.append(neuesItem)
    for i in items:
        print(i.getName())
        print(i.getDetails())
    #print(neuesItem.getFoodItem())

def addItemToDb(item):
    print(item.getDetails())
    #db.create_connection('data.sqlite')
    itemid = db.writeToDb(item)
    if itemid:
        return itemid
    else:
        return False


def addImageToDb(imgdata):
    print("Speichere Bilddaten")
    result = db.writeImgToDb(imgdata)
    if result:
        return True
    else:
        return False