from tkinter import *

win = Tk()
lb11=Label(win,width=10,height=5,bg="red")
lb12=Label(win,width=10,height=5,bg="orange")
lb13=Label(win,width=10,height=5,bg="yelloW")
lb14=Label(win,width=10,height=5,bg="green")
lb15=Label(win,width=10,height=5,bg="blue")
lb16=Label(win,width=10,height=5,bg="purple")

lb11.grid()
lb12.grid(row=0,column=1)
lb13.grid(row=0,column=2)
lb14.grid()
lb15.grid(row=1,column=1)
lb16.grid(row=1,column=2)
win.mainloop()