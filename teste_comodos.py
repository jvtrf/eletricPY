import tkinter as tk
from Comodo import Square_comodo_in_dim as sqr_com
from Lampada import Lampada

root = tk.Tk()

scale = 100 # quanto vale cada pixel ?

canvas = tk.Canvas(root,width=1300,height=700, background='white')
canvas.pack()

quarto = sqr_com(e=0.15*scale,horizotal_dim = 3*scale, vertical_dim = 3*scale,
                    s_x = 70, s_y = 30, canvas=canvas)


banheiro = quarto.add_right(e=0.15*scale,horizotal_dim = 3*scale,vertical_dim = 3*scale)

sala = quarto.add_botton(e=0.15*scale,horizotal_dim = 6.15*scale,vertical_dim = 3*scale)

quarto.create_left_window(2*scale)
quarto.create_botton_indoor(ld= 2.15 *scale,w = 0.8 *scale,clock='b')


root.mainloop()

