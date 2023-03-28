from tkinter import *
from random import *

def game(com, user):
    if com+1==user:        
        lblr['text']="User wins!"
    elif user+1==com:
        lblr['text']="com wins!"

def ch(user):
    List=["a21.png", "a22.png", "a23.png"]

    com=randint(0,2)
    comi=PhotoImage()
    useri=PhotoImage()

win= Tk()

basic=PhotoImage()

lblc=Label()
lblu=Label()

lblr=Label(width=20,height=20)

lbln1=Label(width=15,height=2,)
lbln2=Label(width=15,height=2)

btns=Button(width=15,height=2)
btnr=Button(width=15,height=2)
btnp=Button(width=15,height=2)

lblc.grid(row=0,column=0)
lblr.grid(row=0, column=1)
lblu.grid(row=0, column=2)
lbln1.grid(row=1, column=0)
lbln2.grid(row=1, column=2)

btns.grid(row=1, column=2)

win.mainloop()