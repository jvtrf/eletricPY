from util import create_circle
from UiComodoInsert import UiComodoInsert
import world

class Grid:
    def __init__(self,project_canvas,t_w,t_h,shift,color = 'grey') -> None:
     
        self.canvas_lines = [ ]
        self.canvas_circles = []
        self.color = color
        self.canvas = project_canvas.draw_canvas
        self.pc = project_canvas
        self.radius = 2
        
        self.horizontal_up       = [(x,0) for x in range(0,t_w,shift)]
        self.horizontal_botton   = [(x,t_h) for x in range(0,t_w,shift)]

        self.vertical_left   = [(0,y) for y in range (0,t_h,shift)]
        self.vertical_right  = [(t_w,y) for y in range (0,t_h,shift)]
        
        self.draw_grid()
        self.bind_func()
       
    def draw_grid(self):
        self.points = []
        
        for i in range(len(self.horizontal_up)):
            self.canvas_lines.append(self.canvas.create_line(self.horizontal_up[i],self.horizontal_botton[i],
                                    fill = self.color))
    
        for i in range(len(self.vertical_left)):
            self.canvas_lines.append(self.canvas.create_line(self.vertical_left[i],self.vertical_right[i],
                                    fill = self.color))
        for y in self.vertical_left:
            for x in self.horizontal_botton:
                self.points.append((x[0],y[1]))
                self.canvas_circles.append(create_circle(self.canvas,c=(x[0],y[1]),r = self.radius,color='grey',tag=(x[0],y[1],'aux_point')))
        pass
    
    def click_right_circles(self,event):
        element = self.canvas.gettags("current")
        pos = float(element[0]),float(element[1])
        world.x = pos[0]
        world.y = pos[1]

        if self.pc.insert_ui:
            self.canvas.coords(self.pc.insert_ui_id,-100,0)
            self.pc.insert_ui.delete()
            self.pc.insert_ui == None 
        self.pc.insert_ui = UiComodoInsert(self.canvas)

        self.pc.insert_ui_id = self.canvas.create_window(pos[0],pos[1],anchor='nw',window = self.pc.insert_ui.frame)
        self.canvas.update()
    
    def bind_func(self):
        for circles in self.canvas_circles:
            self.canvas.tag_bind(circles,"<Button-3>",self.click_right_circles)
        pass 
    
    def delete_all_circles(self):
        for circles in self.canvas_circles:
            self.canvas.delete(circles)