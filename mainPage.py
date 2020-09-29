from tkinter import *
from tkinter import messagebox as mb
import sqlite3


class Main:

    def __init__(self, root, user_id, sort_by, active_1, active_2):
        print(sort_by)
        self.frame = Frame()
        self.frame.grid()

        user_id = user_id

        if user_id == 0:
            conn = sqlite3.connect('ToDoList.db')
            c = conn.cursor()
            c.execute('SELECT ID FROM user ORDER BY ID DESC')
            row = c.fetchone()
            conn.close()
            user_id = row[0]

        print(user_id)

        menu = Menu()
        root.config(menu=menu)
        menubar = Menu(menu, tearoff=0)
        menu.add_cascade(label="Menü", menu=menubar)
        menubar.add_command(label="Neuer Eintrag", command=lambda: self.create_new_to_do(root, user_id, sort_by,
                                                                                         active_1, active_2))
        menubar.add_separator()
        menubar.add_command(label="Beenden", command=lambda: exit())

        activebar = Menu(menu, tearoff=0)
        menu.add_cascade(label="Ansicht", menu=activebar)
        activebar.add_command(label="Alle ToDo's anzeigen", command=lambda: self.change_view(root, user_id, sort_by, 0,
                                                                                             1))
        activebar.add_command(label='Nur offene anzeigen', command=lambda: self.change_view(root, user_id, sort_by, 0,
                                                                                            0))
        activebar.add_command(label='Nur erledigte anzeigen', command=lambda: self.change_view(root, user_id, sort_by,
                                                                                               1, 1))

        sortbar = Menu(menu, tearoff=0)
        menu.add_cascade(label="Sortieren nach", menu=sortbar)
        sortbar.add_command(label='Alphabet', command=lambda: self.sort_to_do(root, user_id, 'headline', active_1,
                                                                              active_2))
        sortbar.add_command(label='Priorität', command=lambda: self.sort_to_do(root, user_id, 'priority', active_1,
                                                                               active_2))
        sortbar.add_command(label='zul. hinzugefügt', command=lambda: self.sort_to_do(root, user_id, 'insertDateTime',
                                                                                      active_1, active_2))
        sortbar.add_command(label='als nächst. fällig', command=lambda: self.sort_to_do(root, user_id, 'date', active_1,
                                                                                        active_2))
        conn = sqlite3.connect('ToDoList.db')
        c = conn.cursor()

        '''c.execute(
            "SELECT prename FROM user WHERE ID = ?", (user_id,)
        )
        user = c.fetchone()

        greeting = Label(text='Guten Tag, ' + user[0] + '!')
        greeting.grid(row=0, column=1)'''

        c.execute(
            "SELECT ToDoMain.ID, ToDoMain.headline, ToDoMain.text, ToDoMain.insertDateTime, ToDoMain.date, "
            "ToDoMain.priority, ToDoMain.status FROM ToDoMain JOIN user ON user.ID = ToDoMain.createdBy WHERE user.ID "
            "= ? AND status IN (?, ?) ORDER BY %s" % sort_by,
            (user_id, active_1, active_2))
        rows = c.fetchall()

        '''tdb_canvas = Canvas(self.frame, bg="red",width=255, height=710,)     Canvas
        tdb_canvas.grid(row=0, column=0, sticky="nsew")

        canvasFrame = Frame(tdb_canvas, bg="red")
        tdb_canvas.create_window(0, 0, window=canvasFrame, anchor='nw')'''

        i = 0
        for row in rows:
            i += 1
            button_info_text = '\n' + row[1] + '\n'
            button_info = Button(self.frame, text=button_info_text, width=35,
                                 command=lambda button_idx=row[0]: self.show_details(button_idx, root, user_id, sort_by,
                                                                                     active_1, active_2))
            button_info.grid(row=i, column=0)

        conn.close()

        '''tdbScroll = Scrollbar(self.frame, orient=VERTICAL)       Scrollbar
        tdbScroll.config(command=tdb_canvas.yview)
        tdb_canvas.config(yscrollcommand=tdbScroll.set)
        tdbScroll.grid(row=0, column=1, sticky="ns")'''


    def show_details(self, button_idx, root, user_id, sort_by, active_1, active_2):
        print(button_idx)
        conn = sqlite3.connect('ToDoList.db')
        c = conn.cursor()
        c.execute('SELECT * FROM ToDoMain WHERE ID = ?', (button_idx,))
        data = c.fetchone()
        headline = Label(self.frame, text=data[1], anchor=SW, width=100)
        headline.grid(row=1, column=1, padx=20)
        text = Label(self.frame, text=data[2], anchor=W, width=100)
        text.grid(row=2, column=1, padx=20)
        delete = Button(self.frame, text='Löschen', command=lambda: self.delete_to_do(button_idx, root, user_id,
                                                                                      sort_by, active_1, active_2))
        delete.grid(row=1, column=2)
        finish = Button(self.frame, text='Erledigt', command=lambda: self.finish_to_do(button_idx, root, user_id,
                                                                                       sort_by, active_1, active_2))
        finish.grid(row=1, column=3)
        conn.close()

    def delete_to_do(self, button_idx, root, user_id, sort_by, active_1, active_2):
        conn = sqlite3.connect('ToDoList.db')
        c = conn.cursor()
        c.execute('DELETE FROM ToDoMain WHERE ID = ?', (button_idx,))
        conn.commit()
        conn.close()
        print('ToDo-Eintrag gelöscht')
        self.frame.grid_forget()
        Main(root, user_id, sort_by, active_1, active_2)

    def finish_to_do(self, button_idx, root, user_id, sort_by, active_1, active_2):
        conn = sqlite3.connect('ToDoList.db')
        c = conn.cursor()
        c.execute('UPDATE ToDoMain SET status = 1 WHERE ID = ?', (button_idx,))
        conn.commit()
        conn.close()
        print('ToDo-Status: abgeschlossen')
        self.frame.grid_forget()
        Main(root, user_id, sort_by, active_1, active_2)

    def create_new_to_do(self, root, user_id, sort_by, active_1, active_2):
        self.frame.grid_forget()
        NewToDo(root, user_id, sort_by, active_1, active_2)

    def sort_to_do(self, root, user_id, sort_by, active_1, active_2):
        self.frame.grid_forget()
        Main(root, user_id, sort_by, active_1, active_2)

    def change_view(self, root, user_id, sort_by, active_1, active_2):
        self.frame.grid_forget()
        Main(root, user_id, sort_by, active_1, active_2)


class NewToDo:

    def __init__(self, root, user_id, sort_by, active_1, active_2):
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
        self.date_d = OptionMenu(app2, self.date_dv, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                                 '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                                 '27', '28', '29', '30', '31')
        self.date_m = OptionMenu(app2, self.date_mv, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        self.date_y = OptionMenu(app2, self.date_yv, '2020', '2021', '2022')
        self.prio_e = OptionMenu(app2, self.prio_v, "niedrig", "mittel", "hoch")
        self.headline = Label(app2, text='Überschrift: ')
        self.text = Label(app2, text='Text: ')
        self.date = Label(app2, text='Datum: ')
        self.prio = Label(app2, text='Priorität: ')
        self.button_add_user = Button(app2, text='Anlegen', command=lambda: self.create_to_do(root, user_id, app2,
                                                                                              sort_by, active_1,
                                                                                              active_2))

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

        app2.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root, user_id, app2, sort_by, active_1, active_2))
        app2.mainloop()

    def create_to_do(self, root, user_id, app2, sort_by, active_1, active_2):
        col_headline = self.headline_e.get()
        col_text = self.text_e.get()
        col_date_d = self.date_dv.get()
        col_date_m = self.date_mv.get()
        col_date_y = self.date_yv.get()
        col_prio = self.prio_v.get()
        date = self.merge_date(col_date_d, col_date_m, col_date_y)
        value_p = self.sort_prio(col_prio)

        if col_headline == '':
            mb.showerror('Neues ToDo anlegen fehlgeschlagen', 'Bitte geben Sie eine Überschrift an.')
        else:
            conn = sqlite3.connect('ToDoList.db')
            c = conn.cursor()
            c.execute(
                "INSERT INTO ToDoMain(headline, text, insertDateTime, date, priority, createdBy) VALUES (?, ?, "
                "datetime('now', 'localtime'), ?, ?, ?)",
                (col_headline, col_text, date, value_p, user_id,))
            conn.commit()
            conn.close()
            print('Insert erfolgreich')
            app2.destroy()
            Main(root, user_id, sort_by, active_1, active_2)

    def merge_date(self, day, month, year):
        date = year + '-' + month + '-' + day
        return date

    def sort_prio(self, prio_v):
        value_p = 0
        prio_list = {'niedrig': 1, 'mittel': 2, 'hoch': 3}
        for prio in prio_list:
            if prio == prio_v:
                value_p = prio_list[prio]
        return value_p

    def on_closing(self, root, user_id, app2, sort_by, active_1, active_2):
        app2.destroy()
        Main(root, user_id, sort_by, active_1, active_2)
