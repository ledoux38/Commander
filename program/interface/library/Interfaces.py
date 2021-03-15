import math

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from functools import partial
from .Common import Utils


class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.Menu_bar_view()
        self.Command_view()

        # Fill the content of the window

        self.geometry("300x200")
        self.title("MyFirstMenu V1.0")

        self.ip_active: str = ""

    def Menu_bar_view(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Settings", command=self.Settings_view)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=menu_file)

        self.config(menu=menu_bar)

    def Settings_view(self):
        top: Toplevel = Toplevel()
        labelframe = LabelFrame(top, text="Connection")
        labelframe.pack(expand="no")

        text: StringVar = StringVar(labelframe)
        Label(labelframe, text="IP: ").pack(side=LEFT)
        entry_ip = Entry(labelframe, textvariable=text).pack(side=LEFT)
        test_connection = Button(labelframe, text="Test", command=partial(self.Connexion, text)).pack(side=LEFT)

    def Connexion(self, text: StringVar):
        result: bool = Utils.Connection_to_IP(text.get(), PORT)
        if result:
            messagebox.showinfo("information", "Connection ok")
            self.ip_active = text.get()
        else:
            messagebox.showerror("Error", "IP don't exist")

    def Command_view(self):
        labelframe = LabelFrame(self, text="Command")
        labelframe.pack(expand="no")
        redbutton = Button(labelframe, text="Red", fg="red").pack(side=LEFT)

        greenbutton = Button(labelframe, text="Brown", fg="brown").pack(side=LEFT)

        bluebutton = Button(labelframe, text="Blue", fg="blue").pack(side=LEFT)

        blackbutton = Button(labelframe, text="Black", fg="black").pack(side=BOTTOM)
