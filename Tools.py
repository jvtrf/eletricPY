from tkinter import Label, font,SW
from PIL import Image,ImageTk
class tool:
    def __init__(self,canvas,state) -> None:
        
        if state == 'erease':
            self.erease_photo = ImageTk.PhotoImage(Image.open("images/Erease_icon.png").resize((40,40)))
        
        self.canvas = canvas
        self.label = self.canvas.create_image(0,0,image = self.erease_photo,anchor=SW)
        pass

    def update_pos(self,x,y):
        self.canvas.coords(self.label,x,y)
        pass
    
    def delete(self):
        self.canvas.delete(self.label)