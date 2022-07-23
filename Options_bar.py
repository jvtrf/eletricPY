import tkinter as tk
from tkinter import ANCHOR, PhotoImage, ttk

class option_bar:
    def __init__(self,root,project_canvas = None) -> None:
        self.pc = project_canvas
        self.op_frame = tk.Frame(root,bg='black')
        self.save_photo = tk.PhotoImage(file = r"images/save_icon.png")
        self.erease_photo = tk.PhotoImage(file=r'images/erease_icon.png')
        self.load_photo = tk.PhotoImage(file=r'images/load_icon.png')
        self.condu_photo = tk.PhotoImage(file=r'images/condu_icon.png')

        self.save = ttk.Button(self.op_frame,text='Save',image = self.save_photo,command = lambda: self.pc.set_state('save'))
        self.erease = ttk.Button(self.op_frame,text='Erease',image = self.erease_photo, command = lambda: self.pc.set_state('erease'))
        self.load = ttk.Button(self.op_frame,text='Load',image = self.load_photo,command = lambda: self.pc.set_state('load'))
        self.condu = ttk.Button(self.op_frame,text='Load',image = self.condu_photo, command = lambda: self.pc.set_state('condu'))


        self.save.grid(row=0,column=0)
        self.load.grid(row=0,column=1)
        self.erease.grid(row=0,column=2)
        self.condu.grid(row=0,column=3)

        self.op_frame.update()

        pass

    def get_op_bar(self):
        return self.op_frame

