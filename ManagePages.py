import tkinter as tk
import mainPage
import register
import login


class ManageWindows(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (mainPage.Main, register.Register, login.Login):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(login.Login)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = ManageWindows()
app.mainloop()
