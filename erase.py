from tkinter import Label, font
class erase:
    def __init__(self,canvas) -> None:
        
        self.canvas = canvas
        self.label = self.canvas.create_text(0,0,text='X',fill = 'red',font='10')
        pass

    def update_pos(self,x,y):
        self.canvas.coords(self.label,x,y)
        pass
    
    def delete(self):
        self.canvas.delete(self.label)