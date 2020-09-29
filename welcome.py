from tkinter import *
#from PIL import Image, ImageTk
import login
import mainPage
import register


class Welcome:

    def __init__(self):
        root = Tk()
        root.geometry('1280x720')
        root.wm_iconbitmap('toDo_Logo.ico')
        root.winfo_toplevel().title("To-do-Liste")
        self.frame = Frame()
        self.frame.grid()
        self.frame.columnconfigure((0,1,2), weight=2)
       # self.frame.rowconfigure((0), weight=1)

        """logo = Image.open('toDo_Logo.png')
        logo = logo.resize((225, 225), Image.ANTIALIAS)
        logoTk = ImageTk.PhotoImage(logo)"""

        """self.image_label = Label(self.frame, image=logoTk)
        self.image_label.image = logoTk"""
        self.welcome_text = Label(self.frame, text='Willkommen bei der ToDo-Liste', font=('Calibri', 28))
        self.go_to_register = Button(self.frame, text='Registrieren', font=('Calibri', 15), command=lambda: self.change_frame_register(root))
        self.go_to_login = Button(self.frame, text='Login', font=('Calibri', 15), command=lambda: self.change_frame_login(root))


        #self.image_label.grid_columnconfigure(0, weight=1)
        #self.image_label.grid_rowconfigure(0, weight=1)
        #self.image_label.grid(row=0, column=1, columnspan=2, pady=60)
        #self.image_label.place( relx=0.5, rely=0.5, anchor='center')
        #self.welcome_text.grid_columnconfigure(0, weight=1)
        #self.welcome_text.grid_rowconfigure(1, )
        self.welcome_text.grid(row=1, column=0, sticky='nesw')
        #self.go_to_register.grid_columnconfigure(0, weight=1)
        #self.go_to_register.grid_rowconfigure(2, weight=1)
        self.go_to_register.grid(row=2, column=0, pady=65)
        self.go_to_register.config(width=15, height=1)
        #self.go_to_login.grid_columnconfigure(1, weight=1)
        #self.go_to_login.grid_rowconfigure(2, weight=1)
        self.go_to_login.grid(row=2, column=2, pady=65, sticky='e')
        self.go_to_login.config(width=15, height=1)

        #self.frame.rowconfigure(1,weight=1)

        root.mainloop()

    def change_frame_login(self, root):
        self.frame.grid_forget()
        login.Login(root)

    def change_frame_register(self, root):
        self.frame.grid_forget()
        register.Register(root)

    def change_frame_main(self, root):
        self.frame.grid_forget()
        mainPage.Main(root, 1, 'headline', 0, 0)


app = Welcome()
