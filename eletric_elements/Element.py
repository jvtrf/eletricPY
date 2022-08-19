from tkinter import Canvas 
from util_ import util

class Element:
    def __init__(self,pc=None) -> None:
        self.codekey = util.generate_key('element') 
        self.id_list = []
        self.pc = pc
    
    def create_rectangle(self,p1,p2,fill = 'white', outline = 'black', width = 1):
        canvas = self.pc.canvas
        rect = canvas.create_rectangle(p1[0],p1[1],p2[0],p2[1], fill=fill, outline=outline,width=width)
        self.id_list.append(rect)

    def create_line(self,points,fill = 'black', width = 1):
        canvas = self.pc.canvas
        line = canvas.create_line(points,fill=fill,width=width)
        self.id_list.append(line)

    def create_polygon(self,points,fill = 'white',outline = 'black',width = 1):
        canvas = self.pc.canvas
        poly = canvas.create_polygon(points , fill = fill, outline = outline,width = width)
        self.id_list.append(poly)
        
        return poly
    
    def bind_left(self,func):
        for id in self.id_list:
            self.pc.canvas.tag_bind(id,"<Button-1>",func)
    
    def die(self):
        for id in self.id_list:
            self.pc.canvas.delete(id)
    
    def bind_enter(self,func):
        for id in self.id_list:
            self.pc.canvas.tag_bind(id,"<Enter>",func)
    
    def bind_leave(self,func):
        for id in self.id_list:
            self.pc.canvas.tag_bind(id,"<Leave>",func)