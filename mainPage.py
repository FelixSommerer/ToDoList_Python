import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import sqlite3

conn = sqlite3.connect('ToDoList.db')
c = conn.cursor()


class Main(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        '''self.minsize(width=1000, height=600)
        self.maxsize(width=1000, height=600)

        self.extext = Text()
        self.extext.grid(row=0)
        self.extext.insert(END,
                           'hkjahjdhfhajkhfhdfhashfjscsaeiofjdsfdsafiohewfndsvhsidfhdsnshisahljdsljfihsiogsdidshiadsahidsjvsdvhgihsfiojdsfjiasdojfidshfierhfierwhiofdsifhiofidsjfjdsfjdasjcdcnghhlafdhlfhahklfdhfe')

        c.execute('SELECT * FROM ToDoMain')
        rows = c.fetchall()
        i = 0
        
        for row in rows:
            i += 1
            headline = 'headline' + str(i)
            text = 'text' + str(i)
            self.headline = Text(text=row[1])
            self.headline.grid(row=i-1, column=0, sticky=W)
            self.text = Text(text=row[2])
            self.text.grid(row=i - 1, column=1, sticky=W)
'''






conn.close()
