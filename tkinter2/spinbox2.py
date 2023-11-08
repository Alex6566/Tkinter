import tkinter as tk
from  tkinter import *
root=tk.Tk()
root.geometry("300x200")
root.resizable(False,False)
root.title('spinbox2')
def seasonchanged():
    lblSeason.configure(text="Your favorite season is: " + spnSeason.get())
strSeason=StringVar
seasons=['Spring','Summer','Autumn','Winter']
spnSeason=Spinbox(root, values=seasons ,textvariable=strSeason, command=seasonchanged)
spnSeason.place(height=20,width=100,x=110,y=80)
lblSeason=Label(root, text="What is your favorite season?")
lblSeason.place(height=20,width=200,x=70,y=40)
root.mainloop()