from tkinter import *
import random
nv = random.choice(["jon35","suman5236","you are dumass"])
w = Tk()
w.title("suman")
w.geometry("300x300")

var = IntVar()
def toggle():
    if var.get() == 1:
        a.config(text="you just clicked it")
    else:
        a.config(text="you just unclicked it")

c = Checkbutton(w,text= "this is a checkbuton",variable=var,command=toggle)

a = Label(w,text = "click it")

c.pack()
a.pack()
w.mainloop()