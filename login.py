import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import sqlite3
import mainPage
import register


class Login(tk.Frame):

    def __init__(self, master):

        tk.Frame.__init__(self, master)

        self.label_anz = Label(text='ToDo Liste', font=('Calibri', 20))
        self.username_e = Entry()
        self.loginpassword_e = Entry()
        self.username = Label(text='Benutzername: ')
        self.loginpassword = Label(text='Passwort: ')
        self.go_to_register = Label(text='Noch kein Profil? Hier kannst du dich registrieren.', fg='blue',
                                    cursor='hand2')
        self.button_add_user = Button(text='Anmelden', command=lambda: self.try_login(master))

        self.label_anz.grid(row=0)
        self.username_e.grid(row=1, column=1)
        self.loginpassword_e.grid(row=2, column=1)
        self.username.grid(row=1, column=0, sticky=W)
        self.loginpassword.grid(row=2, column=0, sticky=W)
        self.go_to_register.grid(row=3, column=0)
        self.button_add_user.grid(row=3, column=1)

    def try_login(self, master):
        conn = sqlite3.connect('ToDoList.db')
        c = conn.cursor()
        username = self.username_e.get()
        loginpassword = self.loginpassword_e.get()

        i = 0

        c.execute('SELECT * FROM user')
        rows = c.fetchall()
        for row in rows:
            if username == row[1]:
                print('Nutzer existiert')
                if loginpassword == row[4]:
                    print('Login erfolgreich')
                    master.switch_frame(mainPage.Main)
                else:
                    print('Falsches Passwort')

        conn.close()
