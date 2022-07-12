import tkinter as tk
from EletricPyCanvas import ProjectCanvas
from Grid import Grid
from UiComodoInsert import UiComodoInsert
from util import intersec_lines,create_circle
import world


master = tk.Tk()
master.state('zoomed')

u_w, u_h = master.winfo_screenwidth() ,master.winfo_screenheight()

pc  = ProjectCanvas(master= master ,
                    user_w = u_w , user_h = u_h ,
                    project_h = 2000 , project_w = 2000)

pc.pack()

draw_canvas = pc.draw_canvas

world.grid = Grid(pc,t_w = 2000, t_h = 2000 , shift= 70)

master.mainloop()