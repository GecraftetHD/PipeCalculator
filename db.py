import sqlite3
import onStart as onSt
import time

def newDB(dbname):
    con = sqlite3.connect(f'{dbname}.db')
    print("DB successfully created")
    cur = con.cursor()
    cur.execute('''CREATE TABLE materials (Nummerierung integer, Bezeichnung text, Dichte real)''')
    con.commit()
    con.close()

def insertDataDB(number, name, density):
    print("Insert DATA DB")
    dbpath = onSt.getDB()
    con = sqlite3.connect(f"{dbpath}")
    cur = con.cursor()
    cur.execute(f'''INSERT INTO materials VALUES ({number}, '{name}', {density})''')

    con.commit()
    con.close()

def getallMat():
    dbpath = onSt.getDB()
    con = sqlite3.connect(f"{dbpath}")
    cur = con.cursor()
    cur.execute(f'''SELECT Bezeichnung FROM materials''')
    allmat = cur.fetchall()

    return allmat

def getDensity(name):
    con = sqlite3.connect(f"{onSt.getDB()}")
    cur = con.cursor()
    cur.execute(f'''SELECT Dichte From materials Where Bezeichnung='{name}';''')
    raw_density = cur.fetchall()

    firstlist = raw_density[0]

    stringedfirstlist = str(firstlist)

    raw2_density = stringedfirstlist.replace('(', '')
    raw3_density = raw2_density.replace(',', '')
    density = raw3_density.replace(')', '')

    return float(density)

