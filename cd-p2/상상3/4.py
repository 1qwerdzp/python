from tkinter import *

win=Tk()

def Cl():
    a1=entry1.get()
    a=entry.get()
    enter['text']="My name is "+a+", and I'm "+a1+"years old"

entry=Entry(win, width=50)
entry1=Entry(win, width=50)
name =Label(win, width=5, text="name:")
wo =Label(win, width=5, bitmap="info")
age =Label(win, width=5, text="age:")
enter =Label(win, width=50, text=' ')
btn=Button(win, text="Ok",command=Cl)
name.grid()
entry.grid(row=0,column=1)
age.grid()
entry1.grid(row=1,column=1)
wo.grid()
enter.grid(row=2,column=1)
btn.grid(column=1)
win.mainloop()