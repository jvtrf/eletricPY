from util_.util import create_circle
import UI_backend

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
        if self.pc.state == 'room':  self.pc.new_comodo_ui(pos)
        
    
    def bind_func(self):
        for circles in self.canvas_circles:
            self.canvas.tag_bind(circles,"<Button-1>",self.click_right_circles)
        pass 
    
    def delete_all_circles(self):
        for circles in self.canvas_circles:
            self.canvas.delete(circles)