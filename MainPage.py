from tkinter import *
from tkinter import messagebox as mb
import sqlite3

conn = sqlite3.connect('ToDoList.db')
c = conn.cursor()

class Main:

    def __init__(self):
        self.root = Tk()


        c.execute('SELECT * FROM ToDoMain')
        rows = c.fetchall()
        i = 0
        for row in rows:
            i += 1
            headline = 'headline' + str(i)
            text = 'text' + str(i)
            self.headline = Label(text=row[1])
            self.headline.grid(row=i-1, column=0, sticky=W)
            self.text = Label(text=row[2])
            self.text.grid(row=i - 1, column=1, sticky=W)


        self.root.mainloop()



abc = Main()

conn.close()