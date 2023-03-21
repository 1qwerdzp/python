from tkinter import *

win = Tk()

def Cl(bt):
    if bt=="button":
        bt=Label(win, text="hello",bg="yelloW")
    else :
        bt=Label(win, text="pythion",bg="green")
bt=Label(win, height=5,text="hello",bg="yelloW")
btn=Button(win, text="butten",command=Cl(bt))
btn.pack()
bt.pack()
win.mainloop()