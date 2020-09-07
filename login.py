from tkinter import *
from tkinter import messagebox as mb
import sqlite3
import mainPage


class Login:

    def __init__(self, root):

        self.frame = Frame()
        self.frame.grid()

        self.label_anz = Label(self.frame, text='ToDo Liste', font=('Calibri', 20))
        self.username_e = Entry(self.frame)
        self.loginpassword_e = Entry(self.frame)
        self.username = Label(self.frame, text='Benutzername: ')
        self.loginpassword = Label(self.frame, text='Passwort: ')
        self.button_add_user = Button(self.frame, text='Anmelden', command=lambda: self.try_login(root))

        self.label_anz.grid(row=0)
        self.username_e.grid(row=1, column=1)
        self.loginpassword_e.grid(row=2, column=1)
        self.username.grid(row=1, column=0, sticky=W)
        self.loginpassword.grid(row=2, column=0, sticky=W)
        self.button_add_user.grid(row=3, column=1)

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
                print('Nutzer existiert')
                if loginpassword == row[4]:
                    print('Login erfolgreich')
                    user_id = row[0]
                    self.create_frame_main(root, user_id)
                else:
                    print('Falsches Passwort')

        conn.close()

    def create_frame_main(self, root, user_id):
        self.frame.grid_forget()
        mainPage.Main(root, user_id, 'headline')


