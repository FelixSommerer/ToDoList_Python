import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb, Text
import sqlite3


class Main(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        conn = sqlite3.connect('ToDoList.db')
        c = conn.cursor()
        c.execute('SELECT * FROM ToDoMain')
        rows = c.fetchall()
        i = 0

        for row in rows:
            i += 1
            button_info_text = '\n' + row[1] + '\n'
            button_info = Button(text=button_info_text, width=35,
                                 command=lambda button_idx = row[0]: self.show_details(button_idx))
            button_info.grid(row=i, column=0)

        conn.close()

    def show_details(self, button_idx):
        print(button_idx)
        conn = sqlite3.connect('ToDoList.db')
        c = conn.cursor()
        c.execute('SELECT * FROM ToDoMain WHERE ID = ?', (button_idx,))
        data = c.fetchone()
        headline = Label(text=data[1], anchor=SW, width=100)
        headline.grid(row=1, column=1, padx=20)
        text = Label(text=data[2], anchor=W, width=100)
        text.grid(row=2, column=1, padx=20)
        conn.close()

