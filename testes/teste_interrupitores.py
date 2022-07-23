import tkinter as tk
from Interruptor import Interruptor_s1,Interruptor_s2,Interruptor_s3,Interruptor_3way,Interruptor_4way
from util import create_circle

root = tk.Tk()


canvas = tk.Canvas(root,width=1300,height=700, background='white')
canvas.pack()

#Adicionando um interruptor simples na posição (100,100)
int_s1 = Interruptor_s1(canvas=canvas, center= (100,100),raio=10,label='a')
int_s1.set_labe(shift=10,angle=-45)

#Adicionando um interruptor simples na posição (200,100)
int_s1 = Interruptor_s1(canvas=canvas, center= (200,100),raio=10,label='b')
int_s1.set_labe(shift=10,angle=45)

#Adicionando um interruptor simples na posição (300,100)
int_s1 = Interruptor_s1(canvas=canvas, center= (300,100),raio=10,label='c')
int_s1.set_labe(shift=10,angle=135)

#Adicionando um interruptor simples na posição (400,100)
int_s1 = Interruptor_s1(canvas=canvas, center= (400,100),raio=10,label='c')
int_s1.set_labe(shift=10,angle=-135)

#---------------------------- INTERRUPTORES DE DUAS SEÇÕES --------------------------------------------

#Adicionando um interruptor de duas seções na posição (100,200)
int_s2 = Interruptor_s2(canvas=canvas, center= (100,200),raio=10,label1='a',label2='b')
int_s2.set_labe(shift=10,angle=-135)

#Adicionando um interruptor de duas seções na posição (200,200)
int_s2 = Interruptor_s2(canvas=canvas, center= (200,200),raio=10,label1='b',label2='a')
int_s2.set_labe(shift=10,angle=45)

#---------------------------- INTERRUPTORES DE TRÊS SEÇÕES ----------------------------------------------
int_s3 = Interruptor_s3(canvas=canvas, center = (100,300),raio=10,label1='c',label2='a',label3='b')
int_s3.set_labe(shift=10)
#-------------------------------- INTERRUPTORES 3 WAY ---------------------------------------------------
int_3way = Interruptor_3way(canvas=canvas,center = (100,400),raio = 10,label='a')
int_3way.set_labe(shift=10,angle=-45)

#-------------------------------- INTERRUPTORES 4 WAY ---------------------------------------------------
int_4way = Interruptor_4way(canvas=canvas,center = (100,500),raio = 10,label='a')
int_4way.set_labe(shift=10,angle=-45)

root.mainloop()