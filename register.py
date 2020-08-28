import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import sqlite3
import login
import mainPage

conn = sqlite3.connect('ToDoList.db')
c = conn.cursor()


class Register(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        label_anz = Label(text='ToDo Liste', font=('Calibri', 20))
        self.prename_e = Entry()
        self.name_e = Entry()
        self.username_e = Entry()
        self.loginpassword_e = Entry()
        prename = Label(text='Vorname: ')
        name = Label(text='Nachname: ')
        username = Label(text='Benutzername: ')
        loginpassword = Label(text='Passwort: ')
        go_to_login = Label(text='Bereits ein Profil? Hier geht\'s zum Login', fg='blue',
                                 cursor='hand2')
        button_add_user = Button(text='Registrieren', command=self.db_eintrag)

        label_anz.grid(row=0)
        self.prename_e.grid(row=1, column=1)
        self.name_e.grid(row=2, column=1)
        self.username_e.grid(row=3, column=1)
        self.loginpassword_e.grid(row=4, column=1)
        prename.grid(row=1, column=0, sticky=W)
        name.grid(row=2, column=0, sticky=W)
        username.grid(row=3, column=0, sticky=W)
        loginpassword.grid(row=4, column=0, sticky=W)
        go_to_login.grid(row=5, column=0)
        button_add_user.grid(row=5, column=1)


    def db_eintrag(self):
        self.col_prename = self.prename_e.get()
        self.col_name = self.name_e.get()
        self.col_username = self.username_e.get()
        self.col_loginpassword = self.loginpassword_e.get()

        if len(self.prename_e.get()) == 0 or len(self.username_e.get()) == 0 or len(self.loginpassword_e.get()) == 0:
            mb.showwarning('Neuen User anlegen nicht möglich', 'Bitte füllen Sie alle Pflichtfelder aus.')
            print('Insert nicht möglich')
        else:
            if len(self.name_e.get()) == 0:
                c.execute("INSERT INTO user(username, prename, loginpassword) VALUES (?, ?, ?)",
                          (self.col_username, self.col_prename, self.col_loginpassword))
                conn.commit()
            else:
                c.execute("INSERT INTO user(username, prename, lastname, loginpassword) VALUES (?, ?, ?, ?)",
                          (self.col_username, self.col_prename, self.col_name, self.col_loginpassword))
                conn.commit()
            print('Insert erfolgreich')



conn.close()
