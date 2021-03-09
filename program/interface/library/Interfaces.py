import math

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.createMenuBar()

        # Fill the content of the window

        self.geometry("300x200")
        self.title("MyFirstMenu V1.0")

    def createMenuBar(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Settings", command=self.Settings)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=menu_file)

        self.config(menu=menu_bar)

    def Settings(self):
        top: Toplevel = Toplevel()
        labelframe = LabelFrame(top, text="Connection")
        labelframe.pack(expand="no")

        Label(labelframe, text="IP: ").pack(side=LEFT)
        entry_ip = Entry(labelframe).pack(side=LEFT)
        test_connection = Button(labelframe, text="Test").pack(side=LEFT)
