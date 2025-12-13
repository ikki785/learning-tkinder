from tkinter import *
import random
nv = random.choice(["jon35","suman5236","you are dumass"])
w = Tk()
w.title("suman")
w.geometry("300x300")

def click():
    
    a.config(text = "you just click it")


c = Checkbutton(w,text= "this is a checkbuton",command=click)
a = Label(w,text = "click it")

c.pack()
a.pack()
w.mainloop()