import tkinter as tk
from Comodo import Square_comodo_in_dim as sqr_com
from Lampada import Lampada
from Tomada import Tomada_baixa,Tomada_media,Tomada_alta
from Fonte import Fonte
from Interruptor import Interruptor_s1
from Curva import Condutor
from util import create_circle

root = tk.Tk()

scale = 100 # quanto vale cada pixel ?

canvas = tk.Canvas(root,width=1300,height=700, background='white')
canvas.pack()

###############################################################################################################
#-------------------------------------------- COMODOS ---------------------------------------------------------
###############################################################################################################
#
#                                             QUARTO
#
quarto = sqr_com(e=0.15*scale,horizotal_dim = 3*scale, vertical_dim = 3*scale,
                    s_x = 250, s_y = 30, canvas=canvas,scale=scale)

#
#                                            BANHEIRO
#
banheiro = quarto.add_right(e=0.15*scale,horizotal_dim = 3*scale,vertical_dim = 3*scale)
#
#                                              SALA
#
sala = quarto.add_botton(e=0.15*scale,horizotal_dim = 3*scale,vertical_dim = 3*scale)
#
#                                             COZINHA
#
cozinha = sala.add_right(e=0.15*scale,horizotal_dim= 3*scale, vertical_dim = 3*scale)
#
#                                           - ELEMENTOS - 
#
#
#                                         JANELA DO QUARTO
#
quarto.create_left_window(2*scale)
#
#                                           PORTA DA SALA
#
sala.create_left_indoor(tp=(3 - 0.85)*scale,w=0.8*scale,clock='b')
#
#                                   ESPAÇO VAZIOM NA PARADE DA COZINHA
#
cozinha.create_left_space(0,3*scale)
#
#                                          PORTA DO BANHEIRO
#
banheiro.create_botton_indoor(ld=(3-0.85)*scale,w=0.8*scale)

###############################################################################################################
#------------------------------------------- LÂMPADAS ---------------------------------------------------------
###############################################################################################################
#
#                                             QUARTO
#
quarto.add_lamp(raio=20,pot='100',id = 'a',circ='1')
#
#                                            BANHEIRO
#
banheiro.add_lamp(raio=20,pot = "100",id = "b",circ = "1")
#
#                                              SALA
#
sala.add_lamp(raio=20,pot = "100",id = "c",circ = "1")
#
#                                             COZINHA
#
cozinha.add_lamp(raio=20,pot = "100",id = "d",circ = "1")
###############################################################################################################
#-------------------------------------------- TOMADAS --------------------------------------------------------
###############################################################################################################
#
#                                             QUARTO
#
tomada_1_quarto = quarto.add_right_tug(Tomada_media,percent=0.5,label="100VA",amount = 2,tail_size=5 ,font_size=8)
tomada_2_quarto = quarto.add_top_tug(Tomada_media,percent=0.8,label= "                  100VA",tail_size=5,font_size=8)
#
#                                            BANHEIRO
#
tomada_1_banheiro = banheiro.add_botton_tug(Tomada_media,percent=0.8,label="600VA             ",tail_size=5,amount=2 ,font_size=8)
tomada_2_banheiro = banheiro.add_right_tug(Tomada_alta,percent=0.8,label="6500W",tail_size=5 ,font_size = 8)
#
#                                              SALA
#
tomada_1_sala = sala.add_botton_tug(Tomada_media,percent=0.2,label="             100VA",tail_size=5,font_size= 8)
tomada_2_sala = sala.add_botton_tug(Tomada_media,percent=0.5,label="             100VA",tail_size=5,font_size = 8)
tomada_3_sala = sala.add_left_tug(Tomada_media,percent=0.9,label="100VA",tail_size=5,font_size = 8)
#
#                                             COZINHA
#
tomada_1_cozinha = cozinha.add_botton_tug(Tomada_baixa,percent = 0.2 ,label='100VA                ',amount=3,tail_size=5,font_size = 8)
tomada_2_cozinha = cozinha.add_right_tug(Tomada_media,percent=0.8,label="100VA     ",tail_size=5,font_size = 8)

###############################################################################################################
#----------------------------------------- INTERRUPTORES-------------------------------------------------------
###############################################################################################################
#
#                                             QUARTO

interruptor_1_quarto = quarto.add_interruptor(wall='top',inter="s1",shift=5,percent=0.2,radius=10,label1='a')
#
#                                            BANHEIRO
#
interruptor_1_banheiro = banheiro.add_interruptor(wall='top',inter="s1",shift=5,percent=0.8,radius=10,label1='b')
#
#                                              SALA
#
interruptor_1_sala = sala.add_interruptor(wall='top',inter="s1",shift=5,percent=0.1,radius=10,label1='c')
#
#                                             COZINHA
#
interruptor_1_cozinha = cozinha.add_interruptor(wall='top',inter="s1",shift=5,percent=0.9,radius=10,label1='d')

###############################################################################################################
#--------------------------------------------- FONTE ----------------------------------------------------------
###############################################################################################################
#
#                                             QUARTO
#
fonte = quarto.add_botton_fonte(Fonte,dim = 0.60*scale,percent = 0.6)
#
#
#
###############################################################################################################
#------------------------------------------- CONDUTORES -------------------------------------------------------
###############################################################################################################
#
#
#
'''
cond_quarto_1 = Condutor(canvas=canvas,A = fonte.mt,B = lampada_quarto.botton,curve=0)
cond_quarto_1.set_arm()

cond_quarto_2 = Condutor(canvas=canvas,A=lampada_quarto.top,B = tomada_2_quarto.head,curve = 50,orientation=1)
cond_quarto_2.set_arm()

cond_quarto_3 = Condutor(canvas=canvas,A=lampada_quarto.right,B = interruptor_1_quarto.botton,curve = 50,orientation=1)
cond_quarto_3.set_arm(base_angle=-135)
#
#
'''
#quarto.delete()
#banheiro.delete()
root.mainloop()

