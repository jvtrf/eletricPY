'''import tkinter as tk
from Comodo import Square_comodo_in_dim
from Lampada import Lampada
from Janela import Janela
from Porta import Porta
from SaveAndLoad import SaveAndLoad

root = tk.Tk()


canvas = tk.Canvas(root,width=1300,height=700, background='white')
canvas.pack()

vertical_dim = 300 ; horizontal_dim = 300
eL = 5; eR = 5 ; eB = 5 ; eT = 5

comodo = Square_comodo_in_dim(eL = eL ,eR = eR, eT = eT, eB = eB,
                                horizotal_dim= horizontal_dim, vertical_dim = vertical_dim,
                                s_x = 500, s_y = 300,canvas=canvas, scale=100)

print(comodo)

comodo2 = comodo.join_left(eL = eL ,eR = eR, eT = eT, eB = eB,
                horizotal_dim = horizontal_dim/2, vertical_dim = vertical_dim/2,point= 'E')

janela1 = Janela(comodo, canvas, 200, side = "R")
porta1 = Porta(comodo, canvas, 10, 100, side = "B", orientation = "I")

saveAndLoad = SaveAndLoad(canvas)
save_btn = tk.Button(root, text="Save", command=lambda: saveAndLoad.json_save())
save_btn.place(x=0, y=0)
load_btn = tk.Button(root, text="Load", command=lambda: saveAndLoad.json_load())
load_btn.place(x=35,y=0)

root.mainloop()

'''