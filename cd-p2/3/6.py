from tkinter import *

win = Tk()
img=PhotoImage(file='pizza.gif')
lbl=Label(win, image= img)
lbl.pack()
l=Label(win, text="pazza",bg="yelloW")
l.pack()
win.mainloop()