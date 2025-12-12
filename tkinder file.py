from tkinter import *
wind = Tk()
wind.geometry("1080x1080")
wind.title("tkinder")
wind.config(background='black')
text1 = Label(wind,
              text="hello",
              fg = 'red',
              relief=RAISED,
              padx= 4)
text1.pack()
wind.mainloop()