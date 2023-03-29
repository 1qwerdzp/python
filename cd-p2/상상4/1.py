from tkinter import *
from random import *

def game(com, user):
    if com==user:        
        lblr['text']="draw!"
    elif (com=="a21.png"and user=="a23.png") or (com=="a22.png"and user=="a21.png") or (com=="a23.png"and user=="a22.png") :
        lblr['text']="com wins!"
    else :
        lblr['text']="user wins!"

def ch(user):
    List=["a21.png", "a22.png", "a23.png"]

    com=randint(0,2)
    global comi
    global useri
    comi=PhotoImage(file=List[com])
    useri=PhotoImage(file=user)
    lblc['image']=comi
    lblu['image']=useri
    
    game(List[com], user)

win= Tk()

basic=PhotoImage(file="ready.png")

lblc=Label(win,image=basic,width=109,height=105,bd=5,relief="solid")
lblu=Label(win,image=basic,width=109,height=105,bd=5,relief="solid")

lblr=Label(win,width=20,height=20)

lbln1=Label(win,text='Computer',width=10)
lbln2=Label(win,text='User',width=10)

btnr=Button(win,text='rock',width=15,height=2,bd=3,relief="solid",command=lambda:ch("a22.png"))
btns=Button(win,text='scissors',width=15,height=2,bd=3,relief="solid",command=lambda:ch("a21.png"))
btnp=Button(win,text='paper',width=15,height=2,bd=3,relief="solid",command=lambda:ch("a23.png"))

lblc.grid(row=0, column=0)
lblr.grid(row=0, column=1)
lblu.grid(row=0, column=2)
lbln1.grid(row=1, column=0)
lbln2.grid(row=1, column=2)

btns.grid(row=2, column=0)
btnr.grid(row=2, column=1)
btnp.grid(row=2, column=2)

win.mainloop()