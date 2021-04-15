from library import *

if __name__ == '__main__':
    program: MainWindow = MainWindow()
    program.mainloop()


    # !/usr/bin/python3
    # write tkinter as Tkinter to be Python 2.x compatible
    # from tkinter import *
    #
    #
    # def hello(event):
    #     print("ButtonPress")
    #
    # def hella(event):
    #     print("ButtonRelease")
    #
    #
    # def quit(event):
    #     print("Double Click, so let's stop")
    #     import sys;
    #     sys.exit()
    #
    #
    # widget = Button(None, text='Mouse Clicks')
    # widget.pack()
    # widget.bind('<ButtonPress-1>', hello)
    # widget.bind('<ButtonRelease-1>', hella)
    # widget.bind('<Double-1>', quit)
    # widget.mainloop()