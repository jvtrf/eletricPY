import tkinter as tk

from util import *

root = tk.Tk()


canvas = tk.Canvas(root,width=1300,height=700, background='white')
canvas.pack()


A = 0,0
B = 400,500

canvas.create_line(A,B)

inter,head = perpendicular_point(A,B,d=40)

create_circle(canvas,head,5)

canvas.create_line(inter,head)

root.mainloop()