import sqlite3
from sqlite3 import Error

DB = 'data.sqlite'

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB)
        conn.row_factory = dict_factory
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_item(conn, item):
    sql = ''' INSERT INTO items(type, name, anzahl, minAnzahl, kategorie, mainLocation, subLocation,mhd,menge,portionen,kcal,notes) 
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'''

    cursor = conn.cursor()
    cursor.execute(sql, item)
    return cursor.lastrowid


def checkDb():

    sql_create_item_table = """ CREATE TABLE IF NOT EXISTS items
                                (
                                    id INTEGER primary key autoincrement,
                                    type text not null,
                                    name text not null,
                                    anzahl INTEGER default 1 not null,
                                    minAnzahl INTEGER,
                                    kategorie text,
                                    mainLocation INTEGER,
                                    subLocation INTEGER,
                                    mhd date,
                                    menge text,
                                    portionen INTEGER,
                                    kcal INTEGER,
                                    notes TEXT
                                ); """

    sql_create_mainLocation_table = """ CREATE TABLE IF NOT EXISTS mainLocation
                                    (
                                        id INTEGER primary key autoincrement,
                                        name text not null
                                    );
                                    """

    sql_create_subLocation_table = """ CREATE TABLE IF NOT EXISTS subLocation
                                       (
                                           id INTEGER primary key autoincrement,
                                           mainLocation INTEGER not null,
                                           name text
                                       );
                                       """

    conn = create_connection()

    if conn is not None:
        create_table(conn, sql_create_item_table)
        create_table(conn, sql_create_mainLocation_table)
        create_table(conn, sql_create_subLocation_table)
        conn.close()
    else:
        print("Error! cannot create the database connection.")


def writeToDb(item):
    conn = create_connection()
    try:
        with conn:
            lastid = create_item(conn, item.getDetails())
        conn.close()
    except Error as e:
        print(e)
        return False

    return True


def getAllItems(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items;")

    rows = cursor.fetchall()
    return rows


def getMainLocations(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mainLocation;")
    rows = cursor.fetchall()
    return rows

def getItem(conn, id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = {id};".format(id=id))
    rows = cursor.fetchone()
    return rows

def getSubLocations(conn, index):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subLocation WHERE mainLocation = {id};".format(id=index))
    rows = cursor.fetchall()
    return rows


def readDb():
    conn = create_connection()
    with conn:
        result = getAllItems(conn)
    conn.close()
    return result


def readItem(id):
    conn = create_connection()
    with conn:
        result = getItem(conn, id)
    conn.close()
    return result


def removeMainLocation(conn, id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subLocation WHERE mainLocation = {id};".format(id=id))
    conn.commit()
    cursor.execute("DELETE FROM mainLocation WHERE id = {id};".format(id=id))
    conn.commit()
    cursor.execute("UPDATE items SET mainLocation = {main} , subLocation = {sub} WHERE mainLocation = {id};".format(main='null', sub='null', id=id))
    conn.commit()
    return True


def removeSubLocation(conn, id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subLocation WHERE id = {id};".format(id=id))
    conn.commit()
    cursor.execute("UPDATE items SET subLocation = null WHERE subLocation = {id};".format(id=id))
    conn.commit()
    return True


def getMainLocationFromId(conn, id):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM mainLocation WHERE id = {id};".format(id=id))
    row = cursor.fetchone()
    return row


def getSubLocationFromId(conn, id):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM subLocation WHERE id = {id};".format(id=id))
    row = cursor.fetchone()
    return row


def addMainLocation(conn, location):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO mainLocation ( name )  VALUES ( '{location}' ); ".format(location=location))
        conn.commit()
        return True
    except sqlite3.Error as e:
        return False


def removeLocation(loc, id):
    conn = create_connection()
    with conn:
        if loc == 'main':
            result = removeMainLocation(conn, id)
        if loc == 'sub':
            result = removeSubLocation(conn, id)
    conn.close()
    return result

def renameLocation(conn, type, id, name):
    cursor = conn.cursor()
    try:
        if type == 'main':
            print("rename MainLocation")
            cursor.execute("UPDATE mainLocation SET name = '{name}' WHERE id = {id};".format(name=name, id=id))
            conn.commit()
            return True
        elif type == 'sub':
            print("rename SubLocation")
            cursor.execute("UPDATE subLocation SET name = '{name}' WHERE id = {id};".format(name=name, id=id))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(e)
        return False


def addSubLocation(conn, location, mainlocation):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO subLocation ( mainLocation, name )  VALUES ( '{mainlocation}', '{location}' ); ".format(mainlocation=mainlocation, location=location))
        conn.commit()
        return True
    except sqlite3.Error as e:
        return False


def addLocation(loc, name, mainlocation=None):
    conn = create_connection()
    with conn:
        if loc == 'main':
            result = addMainLocation(conn, name)
        if loc == 'sub':
            result = addSubLocation(conn, name, mainlocation)
    conn.close()
    return result


def locationfromid(loc, id):
    conn = create_connection()
    with conn:
        if loc == 'main':
            result = getMainLocationFromId(conn, id)
        if loc == 'sub':
            result = getSubLocationFromId(conn, id)
    conn.close()
    return result


def renameLocations(loc, id, name):
    conn = create_connection()
    with conn:
        result = renameLocation(conn, loc, id, name)
    conn.close()
    return result


def readLocations(loc, index=0):
    conn = create_connection()
    with conn:
        if loc == 'main':
            result = getMainLocations(conn)
        elif loc == 'sub':
            result = getSubLocations(conn, index)
    conn.close()
    return result