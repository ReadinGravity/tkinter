import tkinter as tk
import random

win = tk.Tk()

cas=60
width=300
sirka=15
ux=20
uy=150

farby=["red","green","gray","yellow","blue"]
vyber=0
temp=False

canvas=tk.Canvas(win, width=500,height=500,bg = "white")
canvas.pack()

def draw_wires():
    global vyber
    for i in range(5):
        canvas.create_rectangle(ux,uy+(i*sirka),ux+width,uy+sirka+(i*sirka),fill=farby[i])
    vyber = random.choice(farby)
    print(vyber)

def stlacenie(e):
    global temp
    overlap=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    color=canvas.itemcget(overlap,"fill")
    if color==vyber:
        string=canvas.create_text(width/2,250,text ="Vyhral si!",fill="black")
        temp=True
    else:
        canvas.delete("all")

t=canvas.create_text(10,10, text=ftime)

def changer:
    global ftime
    ftime-=1
    canvas.itemconfig(t,text=ftime)
    canvas.after (100, changer)



changer()
draw_wires()
casovac()
canvas.bind("<Button-1>",stlacenie)


win.mainloop()