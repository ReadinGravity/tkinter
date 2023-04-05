import tkinter as tk
win=tk.Tk()
import random

canvas=tk.Canvas(win, height=500, width=500, bg="white")
canvas.pack()

clr=["red","green","cyan","black","yellow"]
hx=100
hy=100 #horny roh
width=300
height=15
droty=[]
bum=0

def wires():
    global droty, bum
    for i in range (len(clr)):
        droty.append(canvas.create_rectangle(hx, hy+(height*i), hx+width, hy+height*(i+1), fill=clr[i]))
    bum=random.choice(droty)

def clicker(e):
    # zistim ci som klik na kabloch ak jj ci d objektu je same ako bum ak jj nieco napis na canvas





canvas.bind("<Button-1>", clicker)
wires()
win.mainloop()