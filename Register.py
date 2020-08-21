from tkinter import *
from tkinter import messagebox as mb
import sqlite3

from Testdaten import InhaltIn

conn = sqlite3.connect('ToDoList.db')
c = conn.cursor()

class Register(InhaltIn):

    print(agb)

    def __init__(self):
        self.root = Tk()
        self.label_anz = Label(self.root, text='ToDo Liste',font=('Calibri', 20))
        self.prename_e = Entry(self.root)
        self.name_e = Entry(self.root)
        self.username_e = Entry(self.root)
        self.loginpassword_e = Entry(self.root)
        self.prename = Label(self.root, text = 'Vorname: ')
        self.name = Label(self.root, text='Nachname: ')
        self.username = Label(self.root, text='Benutzername: ')
        self.loginpassword = Label(self.root, text='Passwort: ')
        self.go_to_login = Label(self.root, text='Bereits ein Profil? Hier geht\'s zum Login', fg='blue', cursor='hand2')
        self.button_add_user = Button(self.root, text='Registrieren', command=self.db_eintrag)

        self.label_anz.grid(row=0)
        self.prename_e.grid(row=1, column=1)
        self.name_e.grid(row=2, column=1)
        self.username_e.grid(row=3, column=1)
        self.loginpassword_e.grid(row=4, column=1)
        self.prename.grid(row=1, column=0, sticky=W)
        self.name.grid(row=2, column=0, sticky=W)
        self.username.grid(row=3, column=0, sticky=W)
        self.loginpassword.grid(row=4, column=0, sticky=W)
        self.go_to_login.grid(row = 5, column=0)
        self.button_add_user.grid(row=5, column=1)

        self.root.mainloop()

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


abc = Register()

conn.close()