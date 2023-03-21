from tkinter import *

win = Tk()
lb11=Label(win, text="orange",width=20,height=3,relief="solid")
lb12=Label(win, text="banana",font=("Elephant", 20),bg="yelloW")
lb13=Label(win, text="apple", fg="red")
lb11.pack()
lb12.pack()
lb13.pack()
win.mainloop()