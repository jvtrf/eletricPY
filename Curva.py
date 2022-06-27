from operator import index
from turtle import width
from util import percent_line,perpendicular_point,angle_sin,get_mid_p,create_circle,get_radius_point
import tkinter as tk
from numpy import linspace

#root = tk.Tk()


#canvas = tk.Canvas(root,width=1300,height=700, background='white')
#canvas.pack()


A = (100,200)
B = (800,200)

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

class Condutor:
    def __init__(self,canvas,A,B,curve = 100, smoth = 50,orientation = 0):
        self.ori = orientation
        self.canvas = canvas
        self.smoth = smoth
        
        self.points = draw_curve(A,B,curve=curve,smoth=smoth,orientation=orientation)
        
        self.canvas.create_line(self.points)
    
    def set_arm(self,index = None,arm_size = 30,hand_size = 50,base_angle = None):
        if index == None:
            index = int(self.smoth/2)
        if base_angle == None:
            base_angle = self.ori*(90) - 135
        
        arm = get_radius_point(self.points[index],radius=arm_size,angle=base_angle) 
        self.canvas.create_line(self.points[index],arm)

        if int(arm[0]) >= int(self.points[index][0]):
            self.canvas.create_line(arm,(arm[0]+hand_size,arm[1]))
        else: self.canvas.create_line(arm,(arm[0]-hand_size,arm[1]))
        

         


#cond = Condutor(canvas=canvas,A = A,B = B,orientation=1)
#cond.set_arm(base_angle=45)

#root.mainloop()