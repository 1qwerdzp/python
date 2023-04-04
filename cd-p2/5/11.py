from tkinter import *

def getC():
    lbl2['text'] = txtb.get(1.0,END)
def insC():
    txtb.insert(1.0,lbl2['text'])
def delC():
    txtb.delete(1.0,END)

win = Tk()
txtb=Text(win, width=40,height=5)
lbl1=Label(win, text="Click the 'insert'button to insert this string.",width=40, height=5,bg="skyblue")
lbl2=Label(win, text="Click the 'get'button to import textbox strings\ninto this label.",width=40, height=5,bg="pink")
btng = Button(win, text= "get", width=10,command=getC)
btni = Button(win, text= "insert", width=10,command=insC)
btnd = Button(win, text= "delete", width=10,command=delC)

txtb.grid(row=0,column=0,columnspan=3)
lbl1.grid(row=1,column=0,columnspan=3)
lbl2.grid(row=2,column=0,columnspan=3)
btng.grid(row=3, column=0)
btni.grid(row=3, column=1)
btnd.grid(row=3, column=2)

win.mainloop()