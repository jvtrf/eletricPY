import tkinter as tk
from tkinter import ttk
import world


class UiComodoInsert:
    def __init__(self,master,draw_canvas = None):
        self.master = master
        self.frame = tk.Frame(master=master)
        self.add_comodo = ttk.Button(master = self.frame,text='adicionar comodo',command=self.select_para)
        self.add_comodo.pack()
        pass
    
    def delete(self):
        self.frame.destroy()
    
    def select_para(self):
        self.add_comodo.destroy()
        self.e   = tk.StringVar()
        e_entry = ttk.Entry(self.frame, textvariable=self.e)
        l_e = ttk.Label(self.frame,text='espessura(todos):')
        l_e.grid(row=0,column=0,pady=5)
        e_entry.grid(row=0,column=1)

        self.outros_but = ttk.Button(master=self.frame,text = 'OUTROS ▷',command=self.add_outros)
        self.outros_but.grid(row=1,column=0)

        self.outros_frame = tk.Frame(self.frame)


        self.horizontal_dim   = tk.StringVar()
        self.vertical_dim     = tk.StringVar()
        
        horizontal_entry = ttk.Entry(self.frame, textvariable=self.horizontal_dim)
        l_e = ttk.Label(self.frame,text='dimensão horizontal:')
        l_e.grid(row=3,column=0,pady=5)
        horizontal_entry.grid(row=3,column=1)

        vertical_entry = ttk.Entry(self.frame, textvariable=self.vertical_dim)
        l_e = ttk.Label(self.frame,text='dimensão vertical:')
        l_e.grid(row=3,column=2,pady=5)
        vertical_entry.grid(row=3,column=3)

        create_button = ttk.Button(self.frame,text='criar comodo 👍',command=self.create_comodo)
        create_button.grid(row=4,column=0,pady=10,padx=0)

        pass

    def add_outros(self):
        self.eL  = tk.StringVar()
        self.eR  = tk.StringVar()
        self.eT  = tk.StringVar()
        self.eB  = tk.StringVar()
        
        eL_entry = ttk.Entry(self.frame, textvariable=self.eL)
        l_e = ttk.Label(self.frame,text='eL:')
        l_e.grid(row=1,column=0,pady=5)
        eL_entry.grid(row=1,column=1)

        eR_entry = ttk.Entry(self.frame, textvariable=self.eR)
        l_e = ttk.Label(self.frame,text='eR:')
        l_e.grid(row=1,column=2,pady=5)
        eR_entry.grid(row=1,column=3)

        eT_entry = ttk.Entry(self.frame, textvariable=self.eT)
        l_e = ttk.Label(self.frame,text='eT:')
        l_e.grid(row=2,column=0,pady=5)
        eT_entry.grid(row=2,column=1)

        eB_entry = ttk.Entry(self.frame, textvariable=self.eB)
        l_e = ttk.Label(self.frame,text='eB:')
        l_e.grid(row=2,column=2,pady=5)
        eB_entry.grid(row=2,column=3)

        self.outros_but.destroy()

        self.outros_frame.grid(row=1,column=0)
        pass

    def create_comodo(self):
        world.e = float(self.e.get())
        world.horizontal_dim = float(self.horizontal_dim.get())
        world.vertical_dim = float(self.vertical_dim.get())
        world.create_comodo(self.master)
        self.frame.destroy()
        world.grid.delete_all_circles()
        pass

    
