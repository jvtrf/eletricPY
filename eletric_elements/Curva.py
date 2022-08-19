from msilib.schema import Class
from operator import index
from util_.util import percent_line,perpendicular_point,angle_sin,get_mid_p,create_circle,get_radius_point
import tkinter as tk
from numpy import linspace
from eletric_elements.Element import Element

#root = tk.Tk()


#canvas = tk.Canvas(root,width=1300,height=700, background='white')
#canvas.pack()

def draw_curve(A,B,curve = 100, smoth = 50,orientation = 0):
    points = []
    for ang in linspace(0,-180,smoth).tolist():
            inter_p , head = perpendicular_point(A,B,d = angle_sin(-ang)*curve,p = ang/-180, dir = orientation)
            points.append(head)
    return points

def get_line_fragments(points):
    lines = []
    for i in range(len(points)):
        try:
            lines.append([points[i],points[i+1]])
        except : return lines
    return lines

    return head2,head1,head3
        
class Condutor(Element):
    def __init__(self, pc=None,A = (0,0),B = (0,0),curve = 100, smoth = 50,orientation = 0) -> None:
        super().__init__(pc)
        
        self.ori = orientation
        self.canvas = pc.canvas
        self.smoth = smoth

        self.points = draw_curve(A,B,curve=curve,smoth=smoth,orientation=orientation)
        self.create_line(self.points)

    def set_arm(self,index = None,arm_size = 30,hand_size = 50,base_angle = None):
        if index == None:
            index = int(self.smoth/2)
        if base_angle == None:
            base_angle = self.ori*(90) - 135
        
        arm = get_radius_point(self.points[index],radius=arm_size,angle=base_angle) 
        self.create_line(self.points[index],arm)

        if int(arm[0]) >= int(self.points[index][0]):
            self.create_line(arm,(arm[0]+hand_size,arm[1]))
        else: self.create_line(arm,(arm[0]-hand_size,arm[1]))

         


#cond = Condutor(canvas=canvas,A = A,B = B,orientation=1)
#cond.set_arm(base_angle=45)

#root.mainloop()