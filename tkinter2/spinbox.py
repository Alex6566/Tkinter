import tkinter as tk
from  tkinter import *
root=tk.Tk()
root.geometry("300x200")
root.resizable(False,False)
root.title('spinbox')
def agechanged():
    lblAge.configure(text="Your age is: " + spnAge.get() + " years")
intAge=IntVar
spnAge=Spinbox(root, from_=18, to = 99 ,textvariable=intAge, command=agechanged)
spnAge.place(height=20,width=50,x=110,y=80)
lblAge=Label(root, text="How old are You?")
lblAge.place(height=20,width=120,x=100,y=40)
root.mainloop()