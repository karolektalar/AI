from tkinter import *

window = Tk()

l1 = Label(window, text="AI Project of prediction of results of premier league matches")
l1.grid(row=0, column=0)

l2 = Label(window, text="Authors: Tomasz Fejcak, Piotr Moreń, Karol Talarek")
l2.grid(row=1, column=0)

l3 = Label(window, text="home team")
l3.grid(row=2, column=0)

home_team=StringVar()
e1 = Entry(window, textvariable=home_team)
e1.grid(row=3, column=0)

l4 = Label(window, text="away team")
l4.grid(row=4, column=0)

away_team=StringVar()
e1 = Entry(window, textvariable=away_team)
e1.grid(row=5, column=0)

b1 = Button(window, text="run")
b1.grid(row=6, column=0)

window.mainloop()