from tkinter import *

win=Tk()

def message(event):
    global a
    a=int(entry.get())
    lbl1['text']=str(a*0.39)

entry=Entry(win, width=120)
entry.bind("<Return>", message)
lbl =Label(win, width=10, text="cm입력:")
lbl1 =Label(win, width=120, text='0.00')
lbl2 =Label(win, width=10, text="inch:")
lbl.grid()
entry.grid(row=0,column=1)
lbl2.grid()
lbl1.grid(row=1,column=1)
win.mainloop()