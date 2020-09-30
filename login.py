from tkinter import *
from tkinter import messagebox as mb
import sqlite3
import mainPage


class Login:

    def __init__(self, root):

        self.frame = Frame()
        self.frame.grid()

        self.label_anz = Label(self.frame, text='ToDo Liste', font=('Calibri', 20))
        self.username_e = Entry(self.frame, font=('Calibri', 12))
        self.loginpassword_e = Entry(self.frame, font=('Calibri', 12))
        self.username = Label(self.frame, text='Benutzername: ', font=('Calibri', 15))
        self.loginpassword = Label(self.frame, text='Passwort: ',  font=('Calibri', 15))
        self.button_add_user = Button(self.frame, text='Anmelden', font=('Calibri', 13), command=lambda: self.try_login(root))

        self.label_anz.grid(row=0, column=0, columnspan=1, sticky=N)
        self.username_e.grid(row=1, column=1, pady=15, ipadx=35, ipady=5)
        self.loginpassword_e.grid(row=2, column=1, ipadx=35, ipady=5)
        self.username.grid(row=1, column=0, sticky=W)
        self.loginpassword.grid(row=2, column=0, sticky=W)
        self.button_add_user.grid(row=3, column=1, pady=20)

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

    def create_frame_main(self, root, user_id):
        self.frame.grid_forget()
        mainPage.Main(root, user_id, 'headline', 0, 0)
