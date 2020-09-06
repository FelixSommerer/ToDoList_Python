from tkinter import *


class App:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.button = Button(self.frame, text="QUIT", fg="red", command=self.frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(self.frame, text="Hello", command=lambda: self.create_frame2(master))
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("hi there, everyone!")

    def create_frame2(self, master):
        self.frame.pack_forget()
        frame2 = Frame(master)
        frame2.pack()
        self.hi_there = Button(frame2, text="Hi", command=self.say_hi)
        self.hi_there.pack(side=LEFT)


root = Tk()

app = App(root)

root.mainloop()
