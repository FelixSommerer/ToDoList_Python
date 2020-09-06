from tkinter import *

import login


class App:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.grid()

        self.button = Button(self.frame, text="QUIT", fg="red", command=self.frame.quit)
        self.button.grid(row=0,column=0)

        self.hi_there = Button(self.frame, text="Hello", command=lambda: self.create_frame2(master))
        self.hi_there.grid(row=0,column=1)


    def create_frame2(self, master):
        self.frame.grid_forget()
        #login.Login(master)


root = Tk()

app2 = App(root)

root.mainloop()
