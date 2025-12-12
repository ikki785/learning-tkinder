from tkinter import *
wind = Tk()
wind.geometry("1080x1080")
wind.title("tkinder")
wind.config(background='black')
def click():
    print("hello")
text1 = Label(wind,
              text="hello",
              fg = 'red',
              relief=RAISED,
              padx= 4)

bu1 = Button(wind,
             text="click me",
             bg = "#1500ff",
             width=10,
             height=5,
             padx=20,
             
             )

bu1.config(activebackground='red')
bu1.pack()
bu1.bind("<Button-1>", lambda e: click())

wind.mainloop()