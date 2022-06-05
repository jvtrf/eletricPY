import tkinter as tk

from util import *

root = tk.Tk()


canvas = tk.Canvas(root,width=1300,height=700, background='white')
canvas.pack()


A = 100,500 # Funciona
B = 400,100 #

X = 100,100
Y = 500,500

canvas.create_line(A,B)

points,head = draw_curve(A,B,d = 40,dir=1)

create_circle(canvas,head,5)

canvas.create_line(points)

#canvas.create_line(A,B)

#points,head = draw_curve(A,B,d = 40,dir=0)

#canvas.create_line(points)

#create_circle(canvas,head,5)

#create_circle(canvas,point,5)

#canvas.create_line((0,0),(A))



#inter,head = perpendicular_point(B,A,d=40)

#create_circle(canvas,head,5)

#canvas.create_line(inter,head)

root.mainloop()