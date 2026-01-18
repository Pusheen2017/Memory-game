from tkinter import *
#konfiguracja
tk = Tk()
canvas = Canvas(tk,width=500,height=500)
canvas.pack()
ln = canvas.create_rectangle(10,10,50,50)
tk.mainloop()