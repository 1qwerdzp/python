from tkinter import *

def Click(shape):
    if shape == "circle" :
        img = PhotoImage(file="a2.png")
    elif shape == "triangle" :
        img = PhotoImage(file="a13.png")
    else :
        img = PhotoImage(file="a3.png")

    lbl['image']=img
    lbl.image=img

win = Tk()

img = PhotoImage(file="2.png")
lbl = Label(win, image=img)

btn1 = Button(win, text= "circle", command=lambda : Click("circle"))
btn2 = Button(win, text= "triangle", command=lambda : Click("triangle"))
btn3 = Button(win, text= "star", command=lambda : Click("star"))

lbl.grid(row=0,column=0,columnspan=3)
btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)

win.mainloop()