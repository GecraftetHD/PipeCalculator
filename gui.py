import time
import tkinter as tk
import RohrCalc as rc
import db
import subFunc as sFc
from tkinter import ttk
import onStart as onSt
from tkinter import filedialog as fd

onSt.checkfirststart()


def choosedb():
    filename = fd.askopenfilename()

    onSt.setDB(filename)



def materialdatenbank():


    def newDBgui():
        def setupNewDb():
            db.newDB(newdb_wert.get())

        print("Oma abi was geht")
        newdbWindow = tk.Toplevel(matWindow)
        newdbLabel = tk.Label(newdbWindow, text="Name der neuen Datenbank:").grid(row=0, column=0)


        newdb_wert = tk.StringVar()
        newdb = tk.Entry(newdbWindow, textvariable=newdb_wert).grid(row=0, column=2)
        newdbbutton = tk.Button(newdbWindow, text="Datenbank erstellen", command=setupNewDb).grid(row=1, column=1)

    def addMat():
        addMatWindow = tk.Toplevel(matWindow)
        addMatWindowHead = tk.Label(addMatWindow, text="Material hinzufügen").grid(row=0, column=1)


        addMatWindowlabel1 = tk.Label(addMatWindow, text="Zuordnungszahl").grid(row=1, column=0)
        addMatzahl_wert = tk.StringVar()
        addMatzahl_entry = tk.Entry(addMatWindow, textvariable=addMatzahl_wert).grid(row=1, column=1)

        addMatWindowlabel2 = tk.Label(addMatWindow, text="Bezeichnung").grid(row=2, column=0)
        addMatname_wert = tk.StringVar()
        addMatname_entry = tk.Entry(addMatWindow, textvariable=addMatname_wert).grid(row=2, column=1)

        addMatWindowlabel3 = tk.Label(addMatWindow, text="Dichte").grid(row=3, column=0)
        addMatdichte_wert = tk.StringVar()
        addMatdichte_entry = tk.Entry(addMatWindow, textvariable=addMatdichte_wert).grid(row=3, column=1)

        def addDatatoDB():
            db.insertDataDB(addMatzahl_wert.get(), addMatname_wert.get(), addMatdichte_wert.get())
            time.sleep(1)
            addMatWindow.destroy()

        submit = tk.Button(addMatWindow, command=addDatatoDB, text="Send").grid(row=4, column=1)

    matWindow = tk.Toplevel(root)
    matWindow.geometry("260x200")
    menu = tk.Menu(matWindow)
    matWindow.config(menu=menu)
    filemenu = tk.Menu(menu)

    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Datenbank auswählen", command=choosedb)
    filemenu.add_command(label="About", command=infoWindowCommand)
    filemenu.add_command(label="Neue Datenbank erstellen", command=newDBgui)
    filemenu.add_command(label="Material hinzufügen", command=addMat)

    matWindowLabel = tk.Label(matWindow, text="Materialdatenbank", font=('arial', 16, 'bold'), bg="grey").grid(row=0,
                                                                                                               column=1)


def rechner():
    rechnerWindow = tk.Toplevel(root)
    rechnerWindow.geometry('330x165')
    rechnerWindow.resizable(False, False)

    matvalues = db.getallMat()

    #Überschrift
    label1 = tk.Label(rechnerWindow, text="Neue Berechnung").grid(row=0, column=1)

    # Eingabefeld Radius
    radiuslabel = tk.Label(rechnerWindow, text="Radius in m").grid(row=1, column=0)
    radiusfeld_wert = tk.StringVar()
    radiusfeld = tk.Entry(rechnerWindow, textvariable=radiusfeld_wert).grid(row=1, column=1)

    # Eingabefeld  Rohrdicke
    dickelabel = tk.Label(rechnerWindow, text="Wanddicke in mm").grid(row=2, column=0)
    dickefeld_wert = tk.StringVar()
    dickefeld = tk.Entry(rechnerWindow, textvariable=dickefeld_wert).grid(row=2, column=1)


    #Dropdownmenü Materialliste
    dropdownvar = tk.StringVar()
    dropdown = ttk.Combobox(rechnerWindow, textvariable=dropdownvar, values=matvalues).grid(row=3, column=1)

    # Ergebnisfeld Volumen
    textlabel = tk.Label(rechnerWindow, text="Volumen des Rohres:").grid(row=4, column=0)
    outputentry_wert = tk.StringVar()
    outputentry = tk.Entry(rechnerWindow, textvariable=outputentry_wert, state="disabled").grid(row=5, column=1)


    #Gewichtlabel + Ausgabe
    gewichtlabel = tk.Label(rechnerWindow, text="Gewicht von einem Meter Rohr").grid(row=6, column=0)
    gewichtoutput_wert = tk.StringVar()
    gewichtoutput = tk.Entry(rechnerWindow, textvariable=gewichtoutput_wert, state="disabled").grid(row=6, column=1)






    def calculate():
        try:
            volumenresult = rc.RohrVolumen(dickefeld_wert.get(), radiusfeld_wert.get())

            outputentry_wert.set(f"{volumenresult}")

            gewichtoutput_wert.set(rc.RohrGewicht(volumenresult, db.getDensity(dropdownvar.get())))

        except:
            print("Exception")
            message = "Ungültige Eingabe"



    # Knopf Berechnen
    berechnenButton = tk.Button(rechnerWindow, text="Berechnen", command=calculate).grid(row=4, column=1)


def infoWindowCommand():
    infoWindow = tk.Toplevel(root)
    infoWindow.geometry("300x50")
    label1 = tk.Label(infoWindow, text="Rohrberechner von Jost Bemmann").pack()


root = tk.Tk()
root.iconbitmap(r"C:\Users\Gecra\Documents\Devolopment\Python\Berechnung_eines_Rohres\Rohrberechner.ico")
root.title("Berechnung eines Rohres")
root.resizable(False, False)
headline = tk.Label(root, text="Rohrberechner v1", font=('arial', 25, 'bold'), bg="orange")
headline.pack()

button1 = tk.Button(root, text="Rechner", command=rechner).pack(side="left")

button2 = tk.Button(root, text="Materialdatenbank", command=materialdatenbank).pack(side="right")

menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)

menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Google :D", command=sFc.google)
filemenu.add_command(label="About", command=infoWindowCommand)

root.mainloop()
