import tkinter as tk
from rotormachine import *

class RotorApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        self.machine = RotorMachine()
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            text="Hello, Tkinter",
            fg="white",
            bg="black",
            width=10,
            height=10
        )
        label.pack()


app = RotorApp()
app.mainloop()
