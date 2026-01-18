from tkinter import *
import random
tk = Tk()
canvas=Canvas(tk,width=400,height=400)
canvas.pack()
for x in range(0,100):
    x1=random.randrange(400)
    y1=random.randrange(400)
    x2=x1+random.randrange(400)
    y2=y1+random.randrange(400)
    canvas.create_rectangle(x1,y1,x2,y2)
tk.mainloop()