from tkinter import *

w = Tk()
w.title("suman")
w.geometry("1080x1080")
w.config(background="#faf9f7")
def info1 ():
    name = na.get()
    email = na1.get()
pa = Label(w,text = "enter your name",
           fg = "black",
           bg = "#cfc7c5",
           pady=3,
           padx=3,
           width=20)
na = Entry()
na.config(relief = SUNKEN,
          fg = "black",
          bg = "#faf9f7",
          width=20,
          )


pa1 = Label(w,text = "enter your email",
           fg = "black", 
           bg= "#cfc7c5",
           pady=3,
           padx=3,
           width=20)
na1 = Entry()
na1.config(relief=SUNKEN,
          fg = "black",
          bg = "#faf9f7",
          width=20)
bu1 = Button(w,
             text= "next",
             bg = "#1f21b5",
             command=info1)

pa.pack()
na.pack()
pa1.pack()
na1.pack()
bu1.pack(pady=70)
bu1.pack()

w.mainloop()