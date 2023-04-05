import tkinter as tk
win=tk.Tk()
width=500
height=500
x=0
y=0
canvas=tk.Canvas(win, height=height, width=width, bg="white")
canvas.pack()

def clicker(e):
    # ak som klikol na na nasom objekte zapatam si suradnice
    global x,y
    zoz=canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if obet1 in zoz:
        x=e.x
        y=e.y

def mover(e):
    global x,y
    if x!=0 and y!=0:
        dx=e.x-x
        dy=e.y-y
        canvas.move(obet1,dx,dy)
        x=e.x
        y=e.y

def releaser(e):
    global x,y
    x,y=0,0







obet1=canvas.create_polygon(10,10,50,80,140,82, fill="green")
canvas.bind("<Button-1>", clicker)
canvas.bind("<B1-Motion>", mover)
canvas.bind("<ButtonRelease-1>", releaser)


win.mainloop()