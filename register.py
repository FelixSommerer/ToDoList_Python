from tkinter import *
from tkinter import messagebox as mb
import sqlite3
import mainPage
from PIL import Image, ImageTk


class Register:

    # Aufbau der Register Seite mit Entrys für Registrierungsdaten
    # Button Anmelden ruft Methode db_eintrag() auf
    def __init__(self, root):

        self.frame = Frame()
        self.frame.grid()

        frame_center = Frame(self.frame, relief=GROOVE)
        frame_center.grid(column=0, row=0, padx=500, pady=50)

        logo = Image.open('toDo_Logo.png')
        logo = logo.resize((225, 225), Image.ANTIALIAS)
        logoTk = ImageTk.PhotoImage(logo)

        self.image_label = Label(frame_center, image=logoTk)
        self.image_label.image = logoTk

        self.image_label.grid(column=0, row=0, columnspan=2)
        self.label_anz = Label(frame_center, text='ToDo Liste - Registrieren', font=('Calibri', 20))
        self.prename_e = Entry(frame_center, font=('Calibri', 12))
        self.name_e = Entry(frame_center, font=('Calibri', 12))
        self.username_e = Entry(frame_center, font=('Calibri', 12))
        self.loginpassword_e = Entry(frame_center, font=('Calibri', 12))
        self.prename = Label(frame_center, text='Vorname: ',  font=('Calibri', 15))
        self.name = Label(frame_center, text='Nachname: ',  font=('Calibri', 15))
        self.username = Label(frame_center, text='Benutzername: ',  font=('Calibri', 15))
        self.loginpassword = Label(frame_center, text='Passwort: ',  font=('Calibri', 15))
        self.button_add_user = Button(frame_center, text='Registrieren', font=('Calibri', 13), border=1, command=lambda: self.db_eintrag(root))

        self.label_anz.grid(row=1, column=0, columnspan=2, sticky=N, pady=20)
        self.prename.grid(row=2, column=0, sticky=W)
        self.prename_e.grid(row=2, column=1, sticky=W, pady=15, padx=35)
        self.name.grid(row=3, column=0, sticky=W)
        self.name_e.grid(row=3, column=1, sticky=W, padx=35, pady=5)
        self.username.grid(row=4, column=0, sticky=W)
        self.username_e.grid(row=4, column=1, sticky=W, pady=15, padx=35)
        self.loginpassword.grid(row=5, column=0, sticky=W)
        self.loginpassword_e.grid(row=5, column=1, sticky=W, padx=35, pady=5)
        self.button_add_user.grid(row=6, column=1, pady=20)

    # Versuch neuen Benutzer anzulegen
    # Vorname, Benutzername und Passwort als Pflichtfelder
    # Falls Pflichtfelder nicht angegeben Fehler und Aufruf tkinter Messagebox
    # Bei Erfolg Datenbankeintrag mit neuem User, Aufruf Methode create_frame_main()
    def db_eintrag(self, root):
        conn = sqlite3.connect('ToDoList.db')
        c = conn.cursor()

        col_prename = self.prename_e.get()
        col_name = self.name_e.get()
        col_username = self.username_e.get()
        col_loginpassword = self.loginpassword_e.get()

        if len(self.prename_e.get()) == 0 or len(self.username_e.get()) == 0 or len(self.loginpassword_e.get()) == 0:
            mb.showwarning('Neuen User anlegen nicht möglich', 'Bitte füllen Sie alle Pflichtfelder aus.')
            print('Insert nicht möglich')
        else:
            if len(self.name_e.get()) == 0:
                c.execute("INSERT INTO user(username, prename, loginpassword) VALUES (?, ?, ?)",
                          (col_username, col_prename, col_loginpassword))
                conn.commit()
            else:
                c.execute("INSERT INTO user(username, prename, lastname, loginpassword) VALUES (?, ?, ?, ?)",
                          (col_username, col_prename, col_name, col_loginpassword))
                conn.commit()
            print('Insert erfolgreich')

        conn.close()
        self.create_frame_main(root)

    # Schließen des aktuellen Frames
    # Aufruf Seite MainPage
    def create_frame_main(self, root):
        self.frame.grid_forget()
        mainPage.Main(root, 0, 'headline', 0, 0)
