import tkinter as tk
from tkinter import *
from tkinter import messagebox
root = tk.Tk()
root.geometry('300x150')
root.resizable(False, False)
root.title('Menu sobhan')
def sayhello():
    tk.messagebox.showinfo(title=' message', message='Hello world!')
def showabout():
    tk.messagebox.showinfo(title=' Menu', message='This program is made by sobhan to show you how to add menus to your GUI.')
menubar = Menu(root)
root.config(menu=menubar)
mainmenu=Menu(menubar)
menubar.add_cascade(label="Main", menu=mainmenu)
mainmenu.add_command(label="Hello", command=sayhello)
mainmenu.add_separator()
mainmenu.add_command(label="Quit!", command=root.quit)
helpmenu=Menu(menubar)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=showabout)
root.mainloop()