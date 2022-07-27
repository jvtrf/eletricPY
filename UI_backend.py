import tkinter as tk
from Comodo import Square_comodo_in_dim as sqr_com
from Lampada import Lampada
from Tomada import Tomada_baixa,Tomada_media,Tomada_alta
from Fonte import Fonte
from Interruptor import Interruptor_s1
from Curva import Condutor
from util import create_circle

scale = 100

e   = None
eL  = None
eR  = None
eT  = None
eB  = None

horizontal_dim = None
vertical_dim = None

# Ponto inicial do comodo
x = None
y = None

grid = None
pc = None

def create_comodo(canvas,pc):
    comodo = sqr_com(e=e*scale,horizotal_dim = horizontal_dim*scale, vertical_dim = vertical_dim*scale,
                        s_x = x, s_y = y, canvas=canvas,scale=scale,pc=pc)
    return comodo

def create_lamp(canvas,pc,raio,pot,com,circ):
    lampada = pc.current_obj.add_lamp(raio=raio,pot=pot,id = com,circ = circ,pc = pc)
    return lampada