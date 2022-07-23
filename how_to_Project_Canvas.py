import tkinter as tk
from EletricPyCanvas import ProjectCanvas
from Grid import Grid
from UiComodoInsert import UiComodoInsert
from util import intersec_lines,create_circle
from erase import erase
from Options_bar import option_bar
from Lampada import Lampada
import world


master = tk.Tk()
master.state('zoomed')

u_w, u_h = master.winfo_screenwidth() ,master.winfo_screenheight()

op_bar = option_bar(master)
op_ui = op_bar.get_op_bar()
op_ui.pack(anchor=tk.NW)

pc  = ProjectCanvas(master= master ,
                    user_w = u_w , user_h = u_h ,
                    project_h = 2000 , project_w = 2000)

op_bar.pc = pc


pc.pack()

draw_canvas = pc.draw_canvas

world.grid = Grid(pc,t_w = 2000, t_h = 2000 , shift= 70)

#Test Area

lmp = Lampada(draw_canvas,(200,200),100,'100','a','1',pc)

#


def canvas_loop(event):
    global e,u_w,u_h
    if pc.state == 'erease': 
        pc.e.update_pos(event.x+15,event.y-15)
        pc.unpack()
        pc.pack()

    pass

draw_canvas.bind('<Motion>',canvas_loop)

master.mainloop()