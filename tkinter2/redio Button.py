

from ast import Break

from logging import RootLogger, root

from logging import root

from multiprocessing import Value

from random import *

import tkinter

from tkinter import *    

from sys import *

from time import *

root=Tk()

root.geometry("500x400")

root.title("multi calculator")

root.configure(background="pink")

label = Label(root, text ="* * * * * * * * * * * * * * * * * * * * * * * * *  * * *",bg="pink").pack()

label = Label(root, text ="*                                                      *",bg="pink").pack()

label = Label(root, text ="*               به این برنامه خوش آمدید              *",bg="pink").pack()

label = Label(root, text ="* امیدواریم که این برنامه به سوالات شما جواب بدهد *",bg="pink").pack()

label = Label(root, text ="*          برای اطلاعات بیشتر و نحوه آموزش           *",bg="pink").pack()

label = Label(root, text ="*                    به بخش راهنایی بروید                      *",bg="pink").pack()

label = Label(root, text ="*                                                                           *",bg="pink").pack()

label = Label(root, text ="*           این برنامه توسط :محمد سبحان و           *",bg="pink").pack()

label = Label(root, text ="*               وصال کشاورز ساخته شده است              *",bg="pink").pack()

label = Label(root, text ="* * * * * * * * * * * * * * * * * * * * * * * *  * * * *",bg="pink").pack()

radbtn = IntVar()

Label(root,text="نوع ماشین حساب خود را انتخاب کنید",justify= CENTER,padx= 20).pack()

mashinhesab = Radiobutton(root,text="ماشین حساب",justify= CENTER ,padx= 20, variable=radbtn, value=1).pack(anchor=W)

zavie = Radiobutton(root,text="محاسبه زاویه داخلی چند ضلعی ها",justify= CENTER ,padx= 20, variable=radbtn, value=2).pack(anchor=W)

ghotr = Radiobutton(root,text="محاسبه تعداد قطر چند ضلعی ها",justify= CENTER ,padx= 20, variable=radbtn, value=3).pack(anchor=W)

miangin = Radiobutton(root,text="گرفتن میانگین دو عدد",justify= CENTER ,padx= 20, variable=radbtn, value=4).pack(anchor=W)

game = Radiobutton(root,text="مینی گیم",justify= CENTER ,padx= 20, variable=radbtn, value=5).pack(anchor=W)

 

mainloop()

 

root.mainloop()