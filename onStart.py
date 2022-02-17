import os


def firststart():
    f = open("data.txt", "x")


def checkfirststart():
    if not os.path.exists("data.txt") == True:
        firststart()
    else:
        return


def setDB(path):
    print(path)
    f = open("data.txt", "w")
    f.write(path)
    f.close()
    print("rdy")

def getDB():
    f = open("data.txt", "r")
    niceone = f.read()
    return niceone
