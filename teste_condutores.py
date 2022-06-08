import tkinter as tk
from Condutor import Condutor

root = tk.Tk()


canvas = tk.Canvas(root,width=1300,height=700, background='white')
canvas.pack()


A = 100,500 
B = 400,100 # Head

X = 100,100
Y = 500,500 #Head


cond = Condutor(canvas,A,B,100,1)
# Criando um condutor ligando A e B.
# Curvatura de 100
# Direção (dir) 1 (pode ser 0 ou 1)

cond.add_circuito(angle_index=15)
#Desenha circuito no index 15 (pode ser de 0 a 19)

cond.add_circuito(angle_index=7,circ='NR',dim=20)
#Desenha circuito Com Neutro e Retorno no Index 7 (pode ser de 0 a 19)


root.mainloop()