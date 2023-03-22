from tkinter import *

win=Tk()

def message(event):
    global a
    a+=int(entry.get())
    lbl['text'] = str(a)
a=0
def cl():
    global a
    lbl["text"] = str('0')
    a=0
entry=Entry(win)
btn=Button(win, text="clear",command=cl)
entry.bind("<Return>", message)
lbl =Label(win, text="0")
lbl.pack()
entry.pack()
btn.pack()
win.mainloop()