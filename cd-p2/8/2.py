from tkinter import *

def dc(event):
    index=listbox.curselection()
    print("Tdday :",listbox.get(index[0]))
def lc(event):
    index=listbox.curselection()
    if index:
        if index[0]==0:
            print("Yesterday:Sun")
        else:
            print("Yesterday:", listbox.get(index[0]-1))
def rc(event):
    index=listbox.curselection()
    if index:
        if index[0]==6:
            print("Tomorrow:Mon")
        else:
            print("Tomorrow:", listbox.get(index[0]+1))

day=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

win=Tk()
listbox=Listbox(win)
for i in range(7) :
    listbox.insert(i, day[i])

listbox.bind("<Double-Button-1>", dc)
listbox.bind("<Button-1>", lc)
listbox.bind("<Button-3>",rc)

listbox.pack()
win.mainloop()