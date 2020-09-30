import tkinter as tk
from tkinter import messagebox as mb
import sqlite3


class Main:

    def __init__(self, root, user_id, sort_by, active_1, active_2):
        print(sort_by)
        self.frame = tk.Frame(root, bg='White')
        self.frame.grid(sticky=tk.NSEW)

        user_id = user_id

        if user_id == 0:
            conn = sqlite3.connect('ToDoList.db')
            c = conn.cursor()
            c.execute('SELECT ID FROM user ORDER BY ID DESC')
            row = c.fetchone()
            conn.close()
            user_id = row[0]

        print(user_id)

        menu = tk.Menu()
        root.config(menu=menu)
        menubar = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Menü", menu=menubar)
        menubar.add_command(label="Neuer Eintrag", command=lambda: self.create_new_to_do(root, user_id, sort_by,
                                                                                         active_1, active_2))
        menubar.add_separator()
        menubar.add_command(label="Beenden", command=lambda: exit())

        activebar = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Ansicht", menu=activebar)
        activebar.add_command(label="Alle ToDo's anzeigen", command=lambda: self.change_view(root, user_id, sort_by, 0,
                                                                                             1))
        activebar.add_command(label='Nur offene anzeigen', command=lambda: self.change_view(root, user_id, sort_by, 0,
                                                                                            0))
        activebar.add_command(label='Nur erledigte anzeigen', command=lambda: self.change_view(root, user_id, sort_by,
                                                                                               1, 1))

        sortbar = tk.Menu(menu, tearoff=0)
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

        # Linke Seite
        frame_left = tk.Frame(self.frame, relief=tk.RAISED, bd=2)
        frame_left.grid(row=0, column=0, columnspan=2, sticky=tk.NW, pady=5)

        canvas_left = tk.Canvas(frame_left, bg="Light Grey", width=400, height=720)
        canvas_left.grid(row=0, column=0)

        vscrollbar_left = tk.Scrollbar(frame_left, orient=tk.VERTICAL, command=canvas_left.yview)
        vscrollbar_left.grid(row=0, column=1, sticky=tk.NS)
        canvas_left.configure(yscrollcommand=vscrollbar_left.set)

        buttons_frame = tk.Frame(canvas_left, bg="Red")

        # Rechte Seite
        frame_right = tk.Frame(self.frame, relief=tk.SUNKEN, bg="White", bd=2)  # Test
        frame_right.grid(row=0, column=2, rowspan=2, sticky=tk.NW, pady=5, padx=10)

        canvas_text = tk.Canvas(frame_right, width=880, height=750)
        canvas_text.grid(row=0, column=0)

        text_frame = tk.Frame(canvas_text, bg="White")
        text_frame.grid(row=0, column=0)

        i = 0
        for row in rows:
            i += 1
            button_info_text = '\n' + row[1] + '\n'
            button_info = tk.Button(buttons_frame, text=button_info_text, width=35,
                                    command=lambda button_idx=row[0]: self.show_details(self.frame, text_frame,
                                                                                        button_idx, root,
                                                                                        user_id, sort_by,
                                                                                        active_1, active_2))
            button_info.pack()

        conn.close()

        """for i in range(50):
            button = tk.Button(buttons_frame, text="Button Nr." + str(i))
            button.pack()"""
        if len(rows) is not 0:
            canvas_left.create_window((0, 0), window=buttons_frame, anchor=tk.NW)
            buttons_frame.update_idletasks()
            bbox_left = canvas_left.bbox(tk.ALL)
            w_left, h_left = bbox_left[2] - bbox_left[1], bbox_left[3] - bbox_left[1]

            dw_left, dh_left = int((w_left / 1) * 1), int((h_left / len(rows)) * 13)
            canvas_left.configure(scrollregion=bbox_left, width=dw_left, height=dh_left)

        '''tdbScroll = Scrollbar(self.frame, orient=VERTICAL)       Scrollbar
        tdbScroll.config(command=tdb_canvas.yview)
        tdb_canvas.config(yscrollcommand=tdbScroll.set)
        tdbScroll.grid(row=0, column=1, sticky="ns")'''

    def show_details(self, master_frame, frame2, button_idx, root, user_id, sort_by, active_1, active_2):
        print(button_idx)
        conn = sqlite3.connect('ToDoList.db')
        c = conn.cursor()
        c.execute('SELECT * FROM ToDoMain WHERE ID = ?', (button_idx,))
        data = c.fetchone()
        # headline = tk.Label(frame2, text=data[1], anchor=tk.SW, width=100)
        # headline.grid(row=0, column=1, padx=20, sticky=tk.NW)

        headline_box = tk.Text(frame2, height=1, width=125)
        headline_box.insert(tk.END, data[1])
        headline_box.grid(row=0, column=0, sticky=tk.NW)
        headline_box.configure(state="disabled")

        text_box = tk.Text(frame2, height=53, width=127)
        text_box.insert(tk.END, data[2])
        text_box.grid(row=1, column=0, sticky=tk.NW, pady=5)
        text_box.configure(state="disabled")

        """text = tk.Label(frame2, text=data[2], anchor=tk.W, width=100)
        text.grid(row=1, column=1, padx=20, sticky=tk.N)"""
        delete = tk.Button(master_frame, text='Löschen', font=("Calibri", 15), width=16, height=1,
                           command=lambda: self.delete_to_do(button_idx, root, user_id,
                                                             sort_by, active_1, active_2))
        delete.grid(row=1, column=0, sticky=tk.N)
        finish = tk.Button(master_frame, text='Erledigt', font=("Calibri", 15), width=16, height=1,
                           command=lambda: self.finish_to_do(button_idx, root, user_id,
                                                             sort_by, active_1, active_2))
        finish.grid(row=1, column=1, sticky=tk.N)
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
        app2 = tk.Tk()
        app2.geometry('640x480')

        self.prio_v = tk.StringVar(app2)
        self.prio_v.set("niedrig")
        self.date_dv = tk.StringVar(app2)
        self.date_dv.set("1")
        self.date_mv = tk.StringVar(app2)
        self.date_mv.set("1")
        self.date_yv = tk.StringVar(app2)
        self.date_yv.set("2020")

        self.headline_e = tk.Entry(app2)
        self.text_e = tk.Text(app2, height=10, width=50, font=('Calibri'))
        self.date_d = tk.OptionMenu(app2, self.date_dv, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                                    '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                                    '27', '28', '29', '30', '31')
        self.date_m = tk.OptionMenu(app2, self.date_mv, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        self.date_y = tk.OptionMenu(app2, self.date_yv, '2020', '2021', '2022')
        self.prio_e = tk.OptionMenu(app2, self.prio_v, "niedrig", "mittel", "hoch")
        self.headline = tk.Label(app2, text='Überschrift: ')
        self.text = tk.Label(app2, text='Text: ')
        self.date = tk.Label(app2, text='Datum: ')
        self.prio = tk.Label(app2, text='Priorität: ')
        self.button_add_user = tk.Button(app2, text='Anlegen', command=lambda: self.create_to_do(root, user_id, app2,
                                                                                                 sort_by, active_1,
                                                                                                 active_2))

        self.headline.grid(row=1, column=0)
        self.text.grid(row=2, column=0)
        self.date.grid(row=3, column=0)
        self.prio.grid(row=4, column=0)
        self.headline_e.grid(row=1, column=1, sticky=tk.W)
        self.text_e.grid(row=2, column=1)
        self.date_d.grid(row=3, column=1, sticky=tk.W)
        self.date_m.grid(row=3, column=2, sticky=tk.W)
        self.date_y.grid(row=3, column=3, sticky=tk.W)
        self.prio_e.grid(row=4, column=1, sticky=tk.W)
        self.button_add_user.grid(row=5, column=1)

        app2.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root, user_id, app2, sort_by, active_1, active_2))
        app2.mainloop()

    def create_to_do(self, root, user_id, app2, sort_by, active_1, active_2):
        col_headline = self.headline_e.get()
        col_text = self.text_e.get("1.0",'end-1c')
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
