from tkinter import *
wind = Tk()
wind.geometry("1080x1080")
wind.title("tkinder")
wind.config(background='black')
c = 0
def click():
    global c
    c += 1
    text1.config(text = c)
text1 = Label(wind,
              text = c,
              fg = 'red',
              relief=RAISED,
              padx= 3,
              width=5,
              height=2)

bu1 = Button(wind,
             text="click me",
             bg = "#1500ff",
             width=10,
             height=5,
             padx=20,
             command=click
             )

bu1.config(activebackground='red')
bu1.pack()

text1.pack()
wind.mainloop()