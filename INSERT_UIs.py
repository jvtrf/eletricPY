
import tkinter as tk
from tkinter import ttk

class new_comodo:
    def __init__(self,pc,master) -> None:
        pop_w = tk.Toplevel(master)
        pop_w.title("Criar Novo Comodo")
        pop_w.geometry("300x200+550+200")

        main_frame = tk.Frame(pop_w)

        frameL = tk.Frame(main_frame)
        frameE = tk.Frame(main_frame)

        espL = tk.Label(frameL,text='Espessura:')
        espL.pack(anchor=tk.NW,pady=5)
        larguraL = tk.Label(frameL,text='Largura:')
        larguraL.pack(anchor=tk.NW,pady=5)
        AlturaL = tk.Label(frameL,text='Altura:')
        AlturaL.pack(anchor=tk.NW,pady=5)

        espE = ttk.Entry(frameE)
        espE.pack(anchor=tk.NW,pady=5)
        larguraE = ttk.Entry(frameE)
        larguraE.pack(anchor=tk.NW,pady=5)
        AlturaE = ttk.Entry(frameE)
        AlturaE.pack(anchor=tk.NW,pady=5)

        frameL.grid(row=0,column=0,padx=20,pady=20)
        frameE.grid(row=0,column=1,padx=20,pady=20)

        main_frame.pack(anchor=tk.CENTER,pady=10)

        createB = ttk.Button(pop_w,text='create')
        createB.pack()
        pass

master = tk.Tk()
tk.Button(master,command=lambda: new_comodo(pc=None,master=master),text= 'teste').pack()

master.mainloop()
