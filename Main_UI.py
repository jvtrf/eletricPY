import tkinter as tk
from turtle import bgcolor
from EletricPyCanvas import ProjectCanvas
from Grid import Grid
from util import intersec_lines,create_circle
from Options_bar import option_bar
from Lampada import Lampada
import UI_backend


master = tk.Tk()
master.state('zoomed')

u_w, u_h = master.winfo_screenwidth() ,master.winfo_screenheight()

op_bar = option_bar(master)
op_ui = op_bar.get_op_bar()
op_ui.pack(anchor=tk.NW,padx=10,pady=5)

pc  = ProjectCanvas(master= master ,
                    user_w = u_w , user_h = u_h ,
                    project_h = 2000 , project_w = 2000)

#config
op_bar.pc = pc
op_bar.bind()
#
pc.pack()

draw_canvas = pc.draw_canvas

UI_backend.grid = Grid(pc,t_w = 2000, t_h = 2000 , shift= 70)


master.mainloop()