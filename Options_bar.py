from ctypes import resize
import tkinter as tk
from tkinter import ANCHOR, PhotoImage, ttk
from PIL import Image,ImageTk

class option_bar:
    def __init__(self,root,project_canvas = None) -> None:
        self.pc = project_canvas
        self.op_frame = tk.Frame(root)#, highlightbackground="black", highlightthickness=2)

        self.save_photo = ImageTk.PhotoImage(Image.open("images/saving_icon.png").resize((40,40)))
        self.erease_photo = ImageTk.PhotoImage(Image.open("images/erease_icon.png").resize((40,40)))
        self.load_photo = ImageTk.PhotoImage(Image.open("images/load_icon.png").resize((40,40)))
        self.condu_photo = ImageTk.PhotoImage(Image.open("images/condu_icon.png").resize((40,40)))
        self.room_photo = ImageTk.PhotoImage(Image.open("images/room_icon.png").resize((40,40)))
        self.lamp_photo = ImageTk.PhotoImage(Image.open("images/lamp_icon.png").resize((40,40)))

        self.save = ttk.Button(self.op_frame,text='Save',image = self.save_photo,command = lambda: self.pc.set_state('save'))
        self.erease = ttk.Button(self.op_frame,text='Erease',image = self.erease_photo, command = lambda: self.pc.set_state('erease'))
        self.load = ttk.Button(self.op_frame,text='Load',image = self.load_photo,command = lambda: self.pc.set_state('load'))
        self.condu = ttk.Button(self.op_frame,text='Condu',image = self.condu_photo, command = lambda: self.pc.set_state('condu'))
        self.room = ttk.Button(self.op_frame,text='Room',image = self.room_photo, command = lambda: self.pc.set_state('room'))
        self.lamp = ttk.Button(self.op_frame,text='Lamp',image = self.lamp_photo, command = lambda: self.pc.set_state('lamp'))

        self.saveL = ttk.Label(self.op_frame,text="SAVE")
        self.loadL = ttk.Label(self.op_frame,text="LOAD")
        self.ereaseL = ttk.Label(self.op_frame,text="EREASE")
        self.conduL = ttk.Label(self.op_frame,text="CONECTION")
        self.roomL = ttk.Label(self.op_frame,text="ADD ROOM")
        self.lampL = ttk.Label(self.op_frame,text="ADD LAMP")


        padx = 12

        self.save.grid(row=0,column=0,padx=padx)
        self.saveL.grid(row=1,column=0)

        self.load.grid(row=0,column=1,padx=padx)
        self.loadL.grid(row=1,column=1)

        self.room.grid(row=0,column=2,padx=padx)
        self.roomL.grid(row=1,column=2)

        self.condu.grid(row=0,column=3,padx=padx)
        self.conduL.grid(row=1,column=3)

        self.erease.grid(row=0,column=4,padx=padx)
        self.ereaseL.grid(row=1,column=4)

        self.lamp.grid(row=0,column=5,padx=padx)
        self.lampL.grid(row=1,column=5)

        self.op_frame.update()
        
        pass

    def get_op_bar(self):
        return self.op_frame

    def bind(self):
        self.pc.draw_canvas.bind('<Motion>',self.canvas_loop)
    
    def canvas_loop(self,event):
        for st in self.pc.mouse_follow:
            if self.pc.state == st: 
                self.pc.tool_mouse.update_pos(event.x+1,event.y-1)
                self.pc.unpack()
                self.pc.pack()
