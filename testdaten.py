from tkinter import *
import sqlite3

conn = sqlite3.connect('ToDoList.db')
c = conn.cursor()


class InhaltIn:

    def __init__(self):
        self.root = Tk()
        self.label_anz = Label(self.root, text='Gib eine Überschrift ein',
                               padx=10, pady=10, width=20)
        self.ueberschrift = Entry(self.root, text='Eingabe hier...')

        self.label_anz.pack()
        self.ueberschrift.pack()

        self.ueberschrift.bind('<Return>', self.db_eintrag)
        self.root.mainloop()


    def db_eintrag(self, event):
        self.col_ueberschrift = self.ueberschrift.get()
        c.execute("INSERT INTO ToDoMain(headline, insertDateTime) VALUES (?, datetime('now', 'localtime'))", (self.col_ueberschrift,))
        conn.commit()
        print('Insert erfolgreich')


abc = InhaltIn()

conn.close()