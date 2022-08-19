import tkinter as tk
from tkinter import ttk
import UI_backend
from util_.util import open_config,create_tk_labels,create_tk_drop_down,create_double_frame_ui_by_text,polynomial_fit,generate_key
from UI_Interface.popupModel import popup_ui
from scipy.interpolate import interp1d
from numpy import linspace,array
from eletric_elements.Curva import Condutor

class new_comodo:
    def __init__(self,pc,master,pos = None) -> None:
        self.pop_w = tk.Toplevel(master)
        self.pop_w.title("Criar Novo Comodo")
        self.pop_w.geometry("300x250+550+200")
        self.pos = pos
        self.pc = pc
        self.pc.popup = self
        self.id = generate_key('popup')


        main_frame = tk.Frame(self.pop_w)

        self.frameL = tk.Frame(main_frame)
        self.frameE = tk.Frame(main_frame)

        create_double_frame_ui_by_text(frame1=self.frameL,self=self,frame2=self.frameE,txt='UI/POPUP/comodo_ui')

        self.esp.set(0.1)
        self.largura.set(5)
        self.altura.set(3)
        


        self.frameL.grid(row=0,column=0,padx=20,pady=20)
        self.frameE.grid(row=0,column=1,padx=20,pady=20)

        main_frame.pack(anchor=tk.CENTER,pady=10)

        createB = ttk.Button(self.pop_w,text='create',command=self.create_comodo)
        createB.pack()
        pass
    
    def create_comodo(self,delete = True):
        if delete:
            self.pop_w.destroy()
            self.pop_w.update()

        UI_backend.e = float(self.esp.get()) ; UI_backend.horizontal_dim = float(self.largura.get())
        UI_backend.vertical_dim = float(self.altura.get()) ; UI_backend.x = float(self.pos[0]) 
        UI_backend.y = float(self.pos[1])
        
        UI_backend.create_comodo(canvas=self.pc.draw_canvas,pc = self.pc)
    
    def update(self,var):
        None

class new_lamp(popup_ui):
    def __init__(self, pc=None, master=None, title='Título', width='370', height='250', leftdis='550', topdis='200') -> None:
        super().__init__(pc, master, title, width, height, leftdis, topdis)

        self.create_popup_ui('lamp_ui')
        self.create(False)
    
    def element_creator(self):
        return UI_backend.create_lamp(self.pc)

class new_tom(popup_ui):
    def __init__(self, pc=None, master=None, title='Título', width='370', height='250', leftdis='550', topdis='200') -> None:
        super().__init__(pc, master, title, width, height, leftdis, topdis)

        self.create_popup_ui('tom_ui')
        
        #Começa a posição da tomada sempre no midpoint da parede.
        self.percent.set(50)
        self.tail_size.set(10)
        
        self.create(False)
    
    def element_creator(self):
        self.ui_element = UI_backend.create_tom(self.pc)
        return self.ui_element

class new_interr(popup_ui):
    def __init__(self, pc=None, master=None, title='Título', width='370', height='250', leftdis='550', topdis='200') -> None:
        super().__init__(pc, master, title, width, height, leftdis, topdis)

        self.create_popup_ui('interr_ui')
        self.create(False)
    
    def element_creator(self):
        return UI_backend.create_interr(self.pc)


class new_space(popup_ui):
    def __init__(self, pc=None, master=None, width='370', height='380', leftdis='550', topdis='200') -> None:
        super().__init__(pc, master, width, height, leftdis, topdis)

        self.create_popup_ui('space_ui')
        
        self.create(delete=False)

    def element_creator(self):
        return UI_backend.create_space(self.pc)

class new_connection:
    def __init__(self,pc) -> None:
        self.pc = pc
        self.points = []
        self.condutor = None
        pc.canvas_functions.append(self.set_point)
        pass

    def set_point(self):
        #self.pc.conect_p.append(self.pc.mouse_position)
        print("pontos na lista: ",self.pc.conect_p)
        
        if len(self.pc.conect_p) % 2 == 0:
            
            print("Conection")
            connection_ui(self.pc,self.pc.master)
            
class connection_ui(popup_ui):
    def __init__(self, pc=None, master=None, title='Título', width='370', height='250', leftdis='550', topdis='200') -> None:
        super().__init__(pc, master, title, width, height, leftdis, topdis)

        self.create_popup_ui('connection_ui')

        self.create(delete=False)
    
    def element_creator(self):
        return UI_backend.create_connection(self.pc)

class new_door:
    def __init__(self,pc = None, master = None) -> None:
        self.pop_w = tk.Toplevel(master)
        self.pop_w.title("Adicionar Porta")
        self.pop_w.geometry("370x250+550+200")
        self.pc = pc
        self.door = None

        main_frame = tk.Frame(self.pop_w)

        frameL = tk.Frame(main_frame)
        frameE = tk.Frame(main_frame)

        create_double_frame_ui_by_text(frameL,frameE,self=self,txt='UI/POPUP/door_ui')
        
        frameL.grid(row=0,column=0,padx=20,pady=20)
        frameE.grid(row=0,column=1,padx=20,pady=20)

        main_frame.pack(anchor=tk.CENTER,pady=10)

        self.create(delete=False)

        createB = ttk.Button(self.pop_w,text='ADD DOOR',command = self.create)
        createB.pack()

        self.pop_w.bind_all('<Key>',self.update)
        pass

    def create(self, delete = True):
        if delete:
            self.pop_w.destroy()
            self.pop_w.update()

        if self.door: self.door.die()
        self.door = UI_backend.create_door(self.pc.draw_canvas,self.pc, self.cornerDistance.get(), self.width.get(),
        self.side.get(),self.orientation.get(), self.clock.get())
    def update(self, var):
        if self.door: self.door.die()
        
        self.door = UI_backend.create_door(self.pc.draw_canvas, self.pc,  self.cornerDistance.get(), self.width.get(),
        self.side.get(),self.orientation.get(), self.clock.get())
    
class new_window:
    def __init__(self,pc = None, master = None) -> None:
        self.pop_w = tk.Toplevel(master)
        self.pop_w.title("Adicionar Janela")
        self.pop_w.geometry("370x250+550+200")
        self.pc = pc
        self.window = None

        main_frame = tk.Frame(self.pop_w)

        frameL = tk.Frame(main_frame)
        frameE = tk.Frame(main_frame)

        create_double_frame_ui_by_text(frameL,frameE,self=self,txt='UI/POPUP/window_ui')
        
        frameL.grid(row=0,column=0,padx=20,pady=20)
        frameE.grid(row=0,column=1,padx=20,pady=20)

        main_frame.pack(anchor=tk.CENTER,pady=10)

        self.create(delete=False)

        createB = ttk.Button(self.pop_w,text='ADD WINDOW',command = self.create)
        createB.pack()

        self.pop_w.bind_all('<Key>',self.update)
        pass

    def create(self, delete = True):
        if delete:
            self.pop_w.destroy()
            self.pop_w.update()

        if self.window: self.window.die()
        self.window = UI_backend.create_window(self.pc.draw_canvas,self.pc, self.lado.get(), self.dim.get())
    def update(self, var):
        if self.window: self.window.die()
        self.window = UI_backend.create_window(self.pc.draw_canvas,self.pc, self.lado.get(), self.dim.get())

    


