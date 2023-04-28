from tkinter import *

def dc(event):
    index=listbox.curselection()
    l["text"]=day[index[0]]
day=["rose", "lily", "pansy", "sunflower"]

win=Tk()
listbox=Listbox(win)
l=Label(win)
for i in range(4) :
    listbox.insert(i, day[i])
listbox.bind("<Double-Button-1>", dc)
l.pack()
listbox.pack()
win.mainloop()