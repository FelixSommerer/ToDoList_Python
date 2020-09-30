from tkinter import *
from tkinter import messagebox as mb
import sqlite3

from PIL import Image, ImageTk

import mainPage


class Login:

    # Aufbau der Login Seite mit Entrys für Username und Passwort
    # Button Anmelden ruft onClick Methode try_login() auf
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
        self.label_anz = Label(frame_center, text='ToDo Liste', font=('Calibri', 20))
        self.username_e = Entry(frame_center, font=('Calibri', 12))
        self.loginpassword_e = Entry(frame_center, font=('Calibri', 12), width=20)
        self.username = Label(frame_center, text='Benutzername: ', font=('Calibri', 15))
        self.loginpassword = Label(frame_center, text='Passwort: ',  font=('Calibri', 15))
        self.button_add_user = Button(frame_center, text='Anmelden', font=('Calibri', 13), command=lambda: self.try_login(root))

        self.label_anz.grid(row=1, column=0, columnspan=2, sticky=N, pady=20)
        self.username.grid(row=2, column=0, sticky=W)
        self.username_e.grid(row=2, column=1, pady=5, padx=20, sticky=W)
        self.loginpassword.grid(row=3, column=0, sticky=W)
        self.loginpassword_e.grid(row=3, column=1, padx=20, pady=5, sticky=W)
        self.button_add_user.grid(row=4, column=0, columnspan=2, pady=20, sticky=N)

    # Username auf Existenz in Datenbank überprüfen
    # Wenn existent, prüfen auf korrektes Passwort
    # Falls Fehler in einer der beiden Überprüfungen, Aufruf tkinter Messagebox
    def try_login(self, root):
        conn = sqlite3.connect('ToDoList.db')
        c = conn.cursor()
        username = self.username_e.get()
        loginpassword = self.loginpassword_e.get()

        i = 0

        c.execute('SELECT * FROM user')
        rows = c.fetchall()
        for row in rows:
            if username == row[1]:
                if loginpassword == row[4]:
                    user_id = row[0]
                    self.create_frame_main(root, user_id)
                else:
                    mb.showerror('Anmeldung fehlgeschlagen', 'Falsches Passwort.')
            else:
                i += 1
                if i == len(rows):
                    mb.showerror('Anmeldung fehlgeschlagen', 'Benutzer existiert nicht.')

        conn.close()

    # Schließen des aktuellen Frames
    # Aufruf der mainPage und Übergabe Parameter
    def create_frame_main(self, root, user_id):
        self.frame.grid_forget()
        mainPage.Main(root, user_id, 'headline', 0, 0)
