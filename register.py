import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import sqlite3
import mainPage


class Register:

    def __init__(self, root):

        self.frame = Frame()
        self.frame.grid()

        self.label_anz = Label(self.frame, text='ToDo Liste', font=('Calibri', 20))
        self.prename_e = Entry(self.frame)
        self.name_e = Entry(self.frame)
        self.username_e = Entry(self.frame)
        self.loginpassword_e = Entry(self.frame)
        self.prename = Label(self.frame, text='Vorname: ')
        self.name = Label(self.frame, text='Nachname: ')
        self.username = Label(self.frame, text='Benutzername: ')
        self.loginpassword = Label(self.frame, text='Passwort: ')
        self.button_add_user = Button(self.frame, text='Registrieren', command= lambda: self.db_eintrag(root))

        self.label_anz.grid(row=0)
        self.prename_e.grid(row=1, column=1)
        self.name_e.grid(row=2, column=1)
        self.username_e.grid(row=3, column=1)
        self.loginpassword_e.grid(row=4, column=1)
        self.prename.grid(row=1, column=0, sticky=W)
        self.name.grid(row=2, column=0, sticky=W)
        self.username.grid(row=3, column=0, sticky=W)
        self.loginpassword.grid(row=4, column=0, sticky=W)
        self.button_add_user.grid(row=5, column=1)

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

    def create_frame_main(self, root):
        self.frame.grid_forget()
        mainPage.Main(root, 0, 'headline')
