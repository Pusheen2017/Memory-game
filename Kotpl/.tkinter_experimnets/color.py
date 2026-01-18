from tkinter import *
from tkinter import colorchooser

tk = Tk()
tk.title("Colors")

canvas = Canvas(tk, width=200, height=200)
canvas.pack()

color = colorchooser.askcolor()

if color[1] is not None:  # gdy użytkownik nie kliknie "Cancel"
    canvas.create_rectangle(10, 10, 150, 150, fill=color[1])

tk.mainloop()
