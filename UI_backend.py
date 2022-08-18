import tkinter as tk
from Comodo import Square_comodo_in_dim as sqr_com
from Lampada import Lampada
from Porta import Porta
from Janela import Janela
import Tomada
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

def create_tom(canvas,pc,tipo = '',lado = '',percent = 50,label="100VA",amount = 1,tail_size=5 ,font_size=8):

    if tipo == 'media': tipo = Tomada.Tomada_media
    if tipo == 'baixa': tipo = Tomada.Tomada_baixa
    if tipo == 'alta': tipo = Tomada.Tomada_alta

    percent = percent/100

    if lado == 'right':
        tomada = pc.current_obj.add_right_tug(tipo,percent=percent,label=label,
                                                amount = amount,tail_size = tail_size,
                                                font_size = font_size)
    if lado == 'left':
        tomada = pc.current_obj.add_left_tug(tipo,percent=percent,label=label,
                                                amount = amount,tail_size = tail_size,
                                                font_size = font_size)
    if lado == 'top':
        tomada = pc.current_obj.add_top_tug(tipo,percent=percent,label=label,
                                                amount = amount,tail_size = tail_size,
                                                font_size = font_size)
    if lado == 'botton':
        tomada = pc.current_obj.add_botton_tug(tipo,percent=percent,label=label,
                                                amount = amount,tail_size = tail_size,
                                                font_size = font_size)
    
    return tomada

def create_interr(pc):

    interr = pc.current_obj.add_interruptor(wall    = pc.popup.wall.get(),
                                            inter   = pc.popup.tipo.get(),
                                            shift   = pc.popup.dis.get(),
                                            percent = pc.popup.percent.get()/100,
                                            radius  = pc.popup.radius.get(),
                                            label1  = pc.popup.label1.get(),
                                            label2  = pc.popup.label2.get(),
                                            label3  = pc.popup.label3.get(),
                                            pc = pc)
    
    return interr

def create_door(canvas, pc, cd = 0.8, w = 0.3, side = "esquerdo", orientation = "fora", clock = "antihorário"):
    lados = {
        "direito": "R",
        "esquerdo": "L",
        "cima": "T",
        "baixo": "B"
    }
    orientacoes = {
        "fora": "O",
        "dentro": "I"
    }
    sentidos = {
        "antihorário": "A",
        "horário": "H"
    }
    if cd == "":
        cd = 0.8
    if w == "":
        w = 0.3
    porta = Porta(canvas, pc.current_obj, float(cd)*scale, float(w)*scale, lados.get(side), orientacoes.get(orientation), sentidos.get(clock), pc)
    return porta

def create_window(canvas, pc, side, dim):
    lados = {
        "direito": "R",
        "esquerdo": "L",
        "cima": "T",
        "baixo": "B"
    }
    if dim == "":
        dim = 1
    janela = Janela(canvas, pc.current_obj, float(dim)*scale , lados.get(side), pc)
    return janela