import tkinter as tk

from util import *

root = tk.Tk()


canvas = tk.Canvas(root,width=1300,height=700, background='white')
canvas.pack()


A = 100,500 
B = 400,100 # Head

X = 100,100
Y = 500,500 #Head

lado = 50
sx,sy = 100,100

canvas.create_line(A,B)

points, head, angles = draw_curve(A,B, d = 100,dir=1)

canvas.create_line(points)

create_circle(canvas,head,r=5)

root.mainloop()