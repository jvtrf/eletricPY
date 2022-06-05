import tkinter as tk
from Comodos import Square_comodo_in_dim
from Lampada import Lampada

root = tk.Tk()


canvas = tk.Canvas(root,width=1300,height=700, background='white')
canvas.pack()

vertical_dim = 100 ; horizontal_dim = 100
eL = 5; eR = 5 ; eB = 5 ; eT = 5

comodo = Square_comodo_in_dim(eL = eL ,eR = eR, eT = eT, eB = eB,
                                horizotal_dim= horizontal_dim, vertical_dim = vertical_dim,
                                s_x = 500, s_y = 300,canvas=canvas)

print(comodo.area)

comodo2 = comodo.join_left(eL = eL ,eR = eR, eT = eT, eB = eB,
                horizotal_dim = horizontal_dim/2, vertical_dim = vertical_dim/2,point= 'E')

print(comodo2.area)

print(comodo.area)
root.mainloop()

