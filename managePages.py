import tkinter as tk
from tkinter import *
import mainPage
import register
import login
import sqlite3


class ManageWindows(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(login.Login)


    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
            #print(1)
        self._frame = new_frame
        self._frame.grid()


app = ManageWindows()
app.mainloop()

