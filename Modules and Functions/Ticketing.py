from tkinter import *

gui = Tk()
gui.configure(background="light green")
gui.geometry("1350x750+0+0")

bg = "light green"


Top = Frame(gui, background=bg, width=1350, height=100, bd=14, relief="raised")
Top.pack(side=TOP)

f1 = Frame(gui, background=bg, width=900, height=650, bd=8, relief="raised")
f1.pack(side=LEFT)
f2 = Frame(gui, background=bg, width=440, height=650, bd=8, relief="raised")
f2.pack(side=RIGHT)

ft2 = Frame(f2, background=bg, width=440, height=650, bd=12, relief="raised")
ft2.pack(side=TOP)
fb2 = Frame(f2, background=bg, width=440, height=50, bd=16, relief="raised")
fb2.pack(side=BOTTOM)

f1a = Frame(f1, background=bg, width=900, height=330, bd=8, relief="raised")
f1a.pack(side=TOP)
f2a = Frame(f1, background=bg, width=900, height=320, bd=6, relief="raised")
f2a.pack(side=BOTTOM)


topLeft1 = Frame(f1a, background=bg, width=300, height=200, bd=16, relief="raised")
topLeft1.pack(side=LEFT)
topLeft2 = Frame(f1a, background=bg, width=300, height=200, bd=16, relief="raised")
topLeft2.pack(side=RIGHT)
topLeft3 = Frame(f1a, background=bg, width=300, height=200, bd=16, relief="raised")
topLeft3.pack(side=RIGHT)

bottomLeft1 = Frame(f2a, background=bg, width=450, height=450, bd=14, relief="raised")
bottomLeft1.pack(side=LEFT)
bottomLeft2 = Frame(f2a, background=bg, width=450, height=450, bd=14, relief="raised")
bottomLeft2.pack(side=RIGHT)


lblTitle = Label(Top, font=("Arial", 25, "bold"), background=bg, text="Train Ticketing System", anchor="w")
lblTitle.grid(row=0, column=0)

gui.mainloop()