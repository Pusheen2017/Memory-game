from tkinter import *
tk = Tk()
txt="Kliknij mnie"
def witaj():
   btn1=Button(tk,text="Witaj!")
   btn1.pack()
btn2 = Button(tk,text=txt,command=witaj)
btn2.pack()
tk.mainloop()