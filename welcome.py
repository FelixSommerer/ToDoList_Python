from tkinter import *
import login
import mainPage
import register


class Welcome:

    def __init__(self):

        root = Tk()
        root.geometry('1280x720')
        self.frame = Frame()
        self.frame.grid()

        self.label_anz = Label(self.frame, text='ToDo Liste', font=('Calibri', 20))
        self.welcome_text = Label(self.frame, text='Willkommen bei der ToDo-Liste')
        self.go_to_register = Button(self.frame, text='Registrieren', command=lambda: self.change_frame_register(root))
        self.go_to_login = Button(self.frame, text='Anmelden', command=lambda: self.change_frame_login(root))
        self.go_to_main = Button(self.frame, text='Anmelden', command=lambda: self.change_frame_main(root))

        self.label_anz.grid(row=0)
        self.welcome_text.grid(row=1, column=1)
        self.go_to_register.grid(row=2, column=0)
        self.go_to_login.grid(row=2, column=1)
        self.go_to_main.grid(row=2, column=2)

        root.mainloop()

    def change_frame_login(self,root):
        self.frame.grid_forget()
        login.Login(root)

    def change_frame_register(self,root):
        self.frame.grid_forget()
        register.Register(root)

    def change_frame_main(self,root):
        self.frame.grid_forget()
        mainPage.Main(root,1,'headline desc')


app = Welcome()