import tkinter as tk
from tkinter import ANCHOR, PhotoImage, ttk
from PIL import Image,ImageTk
import glob
from util_.util import open_config

class option_bar:
    def __init__(self,root,project_canvas = None) -> None:
        self.pc = project_canvas
        self.op_frame = tk.Frame(root)#, highlightbackground="black", highlightthickness=2)
        
        path_images = ([(p.split('/')[-1].split('_')[0].split('\\')[-1],p.replace('\\','/')) for p in glob.glob("images/icons/*")])
        
        for p in path_images:
            cmd1 = "self.{}_photo = ImageTk.PhotoImage(Image.open('{}').resize((40,40)))".format(p[0],p[1])
            cmd2 = "self.{} = ttk.Button(self.op_frame,image = self.{}_photo,command = lambda: self.pc.set_state('{}'))".format(p[0],p[0],p[0])
            exec(cmd1)
            exec(cmd2,{'self':self,'ttk':ttk})
        
        for l in open_config('UI/OP_BAR/button_config'):
            exec("self.{}L = ttk.Label(self.op_frame,text='{}',font=('Arial', 7))".format(l.split('-')[0],l.split('-')[1]))

        padx = 16
        aux = 0
        for ic in [ic.split('-')[0] for ic in open_config('UI/OP_BAR/button_config')]:
            exec("self.{}.grid(row=0,column={},padx=padx)".format(ic,aux))
            exec("self.{}L.grid(row=1,column={})".format(ic,aux))
            aux += 1
        
        self.op_frame.update()
        
        pass

    def get_op_bar(self):
        return self.op_frame

    def bind(self):
        self.pc.draw_canvas.bind('<Motion>',self.canvas_loop)
    
    def canvas_loop(self,event):

        self.pc.mouse_position = (event.x,event.y)

        for st in self.pc.mouse_follow:
            if self.pc.state == st: 
                self.pc.tool_mouse.update_pos(event.x+1,event.y-1)
                self.pc.unpack()
                self.pc.pack()
