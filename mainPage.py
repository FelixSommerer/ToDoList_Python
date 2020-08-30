import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb, Text
import sqlite3


class Main(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        menubar = tk.Menu()
        menu = tk.Menu(menubar)
        menu.add_command(label="Neuer Eintrag")
        menu.add_command(label="Abmelden")
        menu.add_command(label="Beenden")

        menubar.add_cascade(label="Menü", menu=menu)

        master.config(menu=menu)

        conn = sqlite3.connect('ToDoList.db')
        c = conn.cursor()
        c.execute('SELECT * FROM ToDoMain')
        rows = c.fetchall()
        i = 0

        for row in rows:
            i += 1
            button_info_text = '\n' + row[1] + '\n'
            button_info = Button(text=button_info_text, width=35,
                                 command=lambda button_idx=row[0]: self.show_details(button_idx))
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
        delete = Button(text='Löschen', command=lambda: self.delete_to_do(button_idx))
        delete.grid(row=1, column=2)
        finish = Button(text='Erledigt', command=lambda: self.finish_to_do(button_idx))
        finish.grid(row=1, column=3)
        conn.close()

    def delete_to_do(self, button_idx):
        conn = sqlite3.connect('ToDoList.db')
        c = conn.cursor()
        c.execute('DELETE FROM ToDoMain WHERE ID = ?', (button_idx,))
        conn.commit()
        conn.close()
        print('ToDo-Eintrag gelöscht')

    def finish_to_do(self, button_idx):
        conn = sqlite3.connect('ToDoList.db')
        c = conn.cursor()
        c.execute('UPDATE ToDoMain SET status = 1 WHERE ID = ?', (button_idx,))
        conn.commit()
        conn.close()
        print('ToDo-Status: abgeschlossen')
