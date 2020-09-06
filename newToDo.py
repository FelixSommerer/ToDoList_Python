import sqlite3
from tkinter import *


class NewToDo:

    def __init__(self):
        app2 = Tk()
        app2.geometry('640x480')

        self.prio_v = StringVar(app2)
        self.prio_v.set("niedrig")
        self.date_dv = StringVar(app2)
        self.date_dv.set("1")
        self.date_mv = StringVar(app2)
        self.date_mv.set("1")
        self.date_yv = StringVar(app2)
        self.date_yv.set("2020")

        self.headline_e = Entry(app2)
        self.text_e = Entry(app2)
        self.date_d = OptionMenu(app2, self.date_dv, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                                 '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                                 '28', '29', '30', '31')
        self.date_m = OptionMenu(app2, self.date_mv, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        self.date_y = OptionMenu(app2, self.date_yv, '2020', '2021', '2022')
        self.prio_e = OptionMenu(app2, self.prio_v, "niedrig", "mittel", "hoch")
        self.headline = Label(app2, text='Überschrift: ')
        self.text = Label(app2, text='Text: ')
        self.date = Label(app2, text='Datum: ')
        self.prio = Label(app2, text='Priorität: ')
        self.button_add_user = Button(app2, text='Anlegen', command=self.create_to_do)

        self.headline.grid(row=1, column=0)
        self.text.grid(row=2, column=0)
        self.date.grid(row=3, column=0)
        self.prio.grid(row=4, column=0)
        self.headline_e.grid(row=1, column=1, sticky=W)
        self.text_e.grid(row=2, column=1)
        self.date_d.grid(row=3, column=1, sticky=W)
        self.date_m.grid(row=3, column=2, sticky=W)
        self.date_y.grid(row=3, column=3, sticky=W)
        self.prio_e.grid(row=4, column=1, sticky=W)
        self.button_add_user.grid(row=5, column=1)

        app2.mainloop()

    def create_to_do(self):
        col_headline = self.headline_e.get()
        col_text = self.text_e.get()
        col_date_d = self.date_dv.get()
        col_date_m = self.date_mv.get()
        col_date_y = self.date_yv.get()
        col_prio = self.prio_v.get()
        date = self.merge_date(col_date_d, col_date_m, col_date_y)
        value_p = self.sort_prio(col_prio)

        conn = sqlite3.connect('ToDoList.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO ToDoMain(headline, text, insertDateTime, date, priority) VALUES (?, ?, datetime('now', 'localtime'), ?, ?)",
            (col_headline, col_text, date, value_p,))
        conn.commit()
        conn.close()
        print('Insert erfolgreich')

    def merge_date(self, day, month, year):
        date = day + '. ' + month + '. ' + year
        return date

    def sort_prio(self, prio_v):
        value_p = 0
        prio_list = {'niedrig': 1, 'mittel': 2, 'hoch': 3}
        for prio in prio_list:
            if prio == prio_v:
                value_p = prio_list[prio]
        return value_p
