import math

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from functools import partial
from .Common import Utils
from .Settings import *
import http.client
import requests


class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.menu_bar_view()
        self.command_view()

        # Fill the content of the window

        self.geometry("300x200")
        self.title("MyFirstMenu V1.0")

        self.ip_active: str = ""

    def menu_bar_view(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Settings", command=self.settings_view)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=menu_file)

        self.config(menu=menu_bar)

    def settings_view(self):
        top: Toplevel = Toplevel()
        labelframe = LabelFrame(top, text="Connection")
        labelframe.pack(expand="no")

        text: StringVar = StringVar(labelframe)
        Label(labelframe, text="IP: ").pack(side=LEFT)
        entry_ip = Entry(labelframe, textvariable=text).pack(side=LEFT)
        test_connection = Button(labelframe, text="Test", command=partial(self.connexion, text)).pack(side=LEFT)

    def connexion(self, text: StringVar):
        result: bool = Utils.Connection_to_IP(text.get(), PORT)
        if result:
            messagebox.showinfo("information", "Connection ok")
            self.ip_active = text.get()
        else:
            messagebox.showerror("Error", "IP don't exist")

    def command_view(self):
        labelframe = LabelFrame(self, text="Command")
        labelframe.pack(expand="no")

        text_high: StringVar = StringVar(labelframe)
        text_high.set("H")
        text_left: StringVar = StringVar(labelframe)
        text_left.set("G")
        text_right: StringVar = StringVar(labelframe)
        text_right.set("D")
        text_low: StringVar = StringVar(labelframe)
        text_low.set("B")

        widget_high = Button(labelframe, text="H")
        widget_high.grid(row=0, column=1)
        widget_high.bind('<ButtonPress-1>', self.send(text_high))
        widget_high.bind('<ButtonRelease-1>', self.send(text_high))

        widget_left = Button(labelframe, text="G")
        widget_left.grid(row=1, column=0)
        widget_left.bind('<ButtonPress-1>', self.send(text_high))
        widget_left.bind('<ButtonRelease-1>', self.send(text_high))

        widget_right = Button(labelframe, text="D")
        widget_right.grid(row=1, column=2)
        widget_right.bind('<ButtonPress-1>', self.send(text_high))
        widget_right.bind('<ButtonRelease-1>', self.send(text_high))

        widget_low = Button(labelframe, text="B")
        widget_low.grid(row=2, column=1)
        widget_low.bind('<ButtonPress-1>', self.send(text_high))
        widget_low.bind('<ButtonRelease-1>', self.send(text_high))

    # def Send(self, order: StringVar):
    #     url = "http://192.168.1.12/" + order.get()
    #     payload = {}
    #     headers = {
    #         'content-type': 'application/json'
    #     }
    #
    #     response = requests.request("POST", url, headers=headers, data=payload)
    #
    #     print(response.text)

    def send(self, event: Event, text: StringVar):
        print(str.format("{0}::{1}", event, text))
