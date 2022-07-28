from tkinter import Label, font,SW
from PIL import Image,ImageTk
import EletricPyCanvas

class tool:
    def __init__(self,canvas,state) -> None:
        for st_p in [(st , 'images/icons/'+st+'_icon.png') for st in EletricPyCanvas.mouse_follow]:
            if state == st_p[0]:
                self.photo = ImageTk.PhotoImage(Image.open(st_p[1]).resize((40,40)))     
        
        self.canvas = canvas
        self.label = self.canvas.create_image(0,0,image = self.photo,anchor=SW)
        pass

    def update_pos(self,x,y):
        self.canvas.coords(self.label,x,y)
        pass
    
    def delete(self):
        self.canvas.delete(self.label)