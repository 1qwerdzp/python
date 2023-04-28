from tkinter import *

win=Tk()
win.title("나만의 사진첩")
img=PhotoImage(file="basic.png")
img_lbl=Label(win, image=img, width=500, hight=300,relief="solid")
info_lbl=Label(win, text="", width=45, hight=10, font=("consolas",15),bg="black", fg= "white")
guide_lbl=Label(win, text="", width=45, hight=10, font=("consolas",15),bg="black", fg= "white")
listbox=Listbox(win)

l=Label(win)
win.mainloop()