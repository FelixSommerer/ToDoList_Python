import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import sqlite3
import mainPage
import register

conn = sqlite3.connect('ToDoList.db')
c = conn.cursor()


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label_anz = Label(self, text='ToDo Liste', font=('Calibri', 20))
        self.username_e = Entry(self)
        self.loginpassword_e = Entry(self)
        self.username = Label(self, text='Benutzername: ')
        self.loginpassword = Label(self, text='Passwort: ')
        self.go_to_register = Label(self, text='Noch kein Profil? Hier kannst du dich registrieren.', fg='blue',
                                    cursor='hand2')
        self.button_add_user = Button(self, text='Anmelden', command=self.try_login)
        self.button2 = tk.Button(self, text="Page One",
                                 command=lambda: controller.show_frame(register.Register))

        self.label_anz.grid(row=0)
        self.username_e.grid(row=1, column=1)
        self.loginpassword_e.grid(row=2, column=1)
        self.username.grid(row=1, column=0, sticky=W)
        self.loginpassword.grid(row=2, column=0, sticky=W)
        self.go_to_register.grid(row=3, column=0)
        self.button_add_user.grid(row=3, column=1)
        self.button2.grid(row=4, column=1)




    def try_login(self, parent, controller):

        self.username = self.username_e.get()
        self.loginpassword = self.loginpassword_e.get()

        c.execute('SELECT * FROM user')
        rows = c.fetchall()
        for row in rows:
            if self.username == row[1]:
                print('Nutzer existiert')
                if self.loginpassword == row[4]:
                    print('Login erfolgreich')
                    controller.show_frame(mainPage.Main)
                else:
                    print('Falsches Passwort')


conn.close()
