from tkinter import *
from tkinter import messagebox as mb
import sqlite3

conn = sqlite3.connect('ToDoList.db')
c = conn.cursor()

class Login:

    def __init__(self):
        self.root = Tk()
        self.label_anz = Label(self.root, text='ToDo Liste',font=('Calibri', 20))
        self.username_e = Entry(self.root)
        self.loginpassword_e = Entry(self.root)
        self.username = Label(self.root, text='Benutzername: ')
        self.loginpassword = Label(self.root, text='Passwort: ')
        self.go_to_register = Label(self.root, text='Noch kein Profil? Hier kannst du dich registrieren.', fg='blue', cursor='hand2')
        self.button_add_user = Button(self.root, text='Anmelden', command=self.try_login)

        self.label_anz.grid(row=0)
        self.username_e.grid(row=1, column=1)
        self.loginpassword_e.grid(row=2, column=1)
        self.username.grid(row=1, column=0, sticky=W)
        self.loginpassword.grid(row=2, column=0, sticky=W)
        self.go_to_register.grid(row=3, column=0)
        self.button_add_user.grid(row=3, column=1)

        self.root.mainloop()

    def try_login(self):

        self.username = self.username_e.get()
        self.loginpassword = self.loginpassword_e.get()

        c.execute('SELECT * FROM user')
        rows = c.fetchall()
        for row in rows:
            if self.username == row[1]:
                print('Nutzer existiert')
                if self.loginpassword == row[4]:
                    print('Login erfolgreich')
                else:
                    print('Falsches Passwort')


abc = Login()

conn.close()