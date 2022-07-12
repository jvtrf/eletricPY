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

x = None
y = None

grid = None

def create_comodo(canvas):
    comodo = sqr_com(e=0.15*scale,horizotal_dim = horizontal_dim*scale, vertical_dim = vertical_dim*scale,
                        s_x = x, s_y = y, canvas=canvas,scale=scale)
    return comodo