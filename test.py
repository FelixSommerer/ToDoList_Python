from tkinter import *

from PIL import Image, ImageTk

import login
import mainPage
import register


class App:

    def __init__(self):
        root = Tk()
        root.geometry('1280x800')
        root.wm_iconbitmap('toDo_Logo.ico')
        root.winfo_toplevel().title("To-do-Liste")
        self.frame = Frame()
        self.frame.pack()

        logo = Image.open('toDo_Logo.png')
        logo = logo.resize((225, 225), Image.ANTIALIAS)
        logoTk = ImageTk.PhotoImage(logo)

        self.image_label = Label(self.frame, image=logoTk)
        self.image_label.image = logoTk
        self.welcome_text = Label(self.frame, text='Willkommen bei der ToDo-Liste', font=('Calibri', 28))
        self.go_to_register = Button(self.frame, text='Registrieren', font=('Calibri', 15),
                                     command=lambda: self.change_frame_register(root))
        self.go_to_login = Button(self.frame, text='Login', font=('Calibri', 15),
                                  command=lambda: self.change_frame_login(root))

        self.image_label.pack(pady=60)
        self.welcome_text.pack()
        self.go_to_register.pack(side=LEFT, pady=60)
        self.go_to_register.config(width=15, height=1)
        self.go_to_login.pack(side=RIGHT, pady=60)
        self.go_to_login.config(width=15, height=1)

        root.mainloop()

    def change_frame_login(self, root):
        self.frame.pack_forget()
        login.Login(root)

    def change_frame_register(self, root):
        self.frame.pack_forget()
        register.Register(root)

    def change_frame_main(self, root):
        self.frame.grid_forget()
        mainPage.Main(root, 1, 'headline', 0, 0)


app = App()