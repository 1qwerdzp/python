from tkinter import *

win=Tk()

def message(event):
    global a
    global aa
    if aa==0:
        a=0
    a+=int(entry.get())
    lbl['text'] = str(a)
def cl():
    aa=1
aa=1
a=0
entry=Entry(win)
entry.bind("<Return>", message)
lbl =Label(win, text="")
lbl.pack()
entry.pack()
btn=Button(win, text="clear",command=cl)
btn.pack()
win.mainloop()