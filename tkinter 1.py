import tkinter as tk

win=tk.Tk() #constructor

def executor():
    print(a.get(), b.get(), c.get())
    ka=int(a.get())
    kb=int(b.get())
    kc=int(c.get())
    d=kb**2-4*ka*kc
    if d<0:
        print ("nema riesenie v R")
    elif d==0:
        print(-kb/(2*ka))
    else:
        print("x1= ", (-kb+d**0.5)/(2*ka)) #b+- odm b
        print ("x2= ",(-kb-d**0.5)/(2*ka))


at=tk.Label(win, text="koeficient a:")
at.pack()
a=tk.Entry(win)
a.pack()

bt=tk.Label(win, text="koeficient b:")
bt.pack()
b=tk.Entry(win)
b.pack()

ct=tk.Label(win, text="koeficient c:")
ct.pack()
c=tk.Entry(win)
c.pack()

button=tk.Button(win, text="click meeee", command=executor)
button.pack()


win.mainloop()

# vypis vysledky v gui nie cli