from sys import implementation
from Tomada import Tomada_baixa,Tomada_media,Tomada_alta
from util import create_circle
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root,width=1300,height=700, background='white')
canvas.pack()


#------------------------Tomada Baixa----------------------------------
# Ângulos diferentes: 0
tomada = Tomada_baixa(canvas = canvas,tail_size=10,label='100 w               ')

#Angulo diferentes: -90
tomada = Tomada_baixa(canvas = canvas,tail_pos = (200,100),tail_size=10,angle=-90,label="300 w")

#Angulos diferentes: 90
tomada = Tomada_baixa(canvas = canvas,tail_pos = (300,100),tail_size=10,angle=90)
create_circle(canvas=canvas,c = tomada.head, r = 5)

#Angulos diferentes: 180
tomada = Tomada_baixa(canvas = canvas,tail_pos = (400,100),tail_size=10,angle=180)
create_circle(canvas=canvas,c = tomada.head, r = 5)


#------------------------  Tomada Media  --------------------------------

tomada = Tomada_media(canvas=canvas,angle=0,tail_pos=(100,200),tail_size=10)
tomada = Tomada_media(canvas=canvas,angle=-90,tail_pos=(200,200),tail_size=10)
tomada = Tomada_media(canvas=canvas,angle=90,tail_pos=(300,200),tail_size=10)
tomada = Tomada_media(canvas=canvas,angle=180,tail_pos=(400,200),tail_size=10,label="                  100 w")

#------------------------  Tomada Alta  --------------------------------

tomada = Tomada_alta(canvas=canvas,angle=0,tail_pos=(100,300),tail_size=10)
tomada = Tomada_alta(canvas=canvas,angle=-90,tail_pos=(200,300),tail_size=10)
tomada = Tomada_alta(canvas=canvas,angle=90,tail_pos=(300,300),tail_size=10)
tomada = Tomada_alta(canvas=canvas,angle=180,tail_pos=(400,300),tail_size=10,label="100 w              ")

root.mainloop()