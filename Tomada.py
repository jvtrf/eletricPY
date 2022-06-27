from turtle import width

from numpy import arange
from util import rotate_points,draw_text,get_radius_point,distance,get_widget_box,shift_points

class Tomada_baixa:
    def __init__(self,canvas,angle = 0,tail_pos = (100,100),tail_size = 10,label = '',font_size = 10,amount = 1) -> None:

        self.canvas = canvas
        self.tail = tail_pos
        self.label = label
        self.angle = angle
        
        points = [tail_pos] #0
        points.append((points[-1][0],points[-1][1]-tail_size)) #1
        points.append((points[-1][0]+tail_size,points[-1][1])) #2
        points.append((points[-1][0]-tail_size,points[-1][1]-tail_size*2)) #3 -> head
        points.append((points[-1][0]-tail_size,points[-1][1]+tail_size*2)) #4
        points.append((points[-1][0]+tail_size,points[-1][1])) #5
        points = rotate_points(points=points,pivo = tail_pos,rot_ang = angle)

        #points = shift_points(points=points[1:],y=-40)
        
        self.head = points[3]
        self.canvas.create_line(points,width = 2)

        self.arrow_height = distance(self.head,self.tail)

        if angle == 0 and amount >1:
            self.canvas.create_line(shift_points(points=points[1:], y = - self.arrow_height + tail_size),width = 2)
            self.head = shift_points(points=points[1:], y = - self.arrow_height + tail_size)[2]
            if amount>2:
                self.canvas.create_line(shift_points(points=points[1:], y = - self.arrow_height*2 + tail_size*2),width = 2)
                self.head = shift_points(points=points[1:], y = - self.arrow_height*2 + tail_size*2)[2]
        
        if angle == -90 and amount >1:
            self.canvas.create_line(shift_points(points=points[1:], x = - self.arrow_height + tail_size),width = 2)
            self.head = shift_points(points=points[1:], x = - self.arrow_height + tail_size)[2]
            if amount>2:
                self.canvas.create_line(shift_points(points=points[1:], x = - self.arrow_height*2 + tail_size*2),width = 2)
                self.head = shift_points(points=points[1:], x = - self.arrow_height*2 + tail_size*2)[2]
        
        if angle == 90 and amount >1:
            self.canvas.create_line(shift_points(points=points[1:], x = + self.arrow_height - tail_size),width = 2)
            self.head = shift_points(points=points[1:], x = + self.arrow_height - tail_size)[2]
            if amount>2:
                self.canvas.create_line(shift_points(points=points[1:], x = + self.arrow_height*2 - tail_size*2),width = 2)
                self.head = shift_points(points=points[1:], x = + self.arrow_height*2 - tail_size*2)[2]

        if angle == 180 and amount >1:
            self.canvas.create_line(shift_points(points=points[1:], y =  self.arrow_height - tail_size),width = 2)
            self.head = shift_points(points=points[1:], y = + self.arrow_height - tail_size)[2]
            if amount>2:
                self.canvas.create_line(shift_points(points=points[1:], y = + self.arrow_height*2 - tail_size*2),width = 2)
                self.head = shift_points(points=points[1:], y = + self.arrow_height*2 - tail_size*2)[2]

        text = draw_text(self.canvas,(0,0),self.label,font_size) ; h,w = get_widget_box(self.canvas,text); self.canvas.delete(text)
        
        if angle == 0 or angle == 180:
            pos = get_radius_point(self.tail,self.arrow_height*amount + 5,self.angle-90)
        else: pos = get_radius_point(self.tail,self.arrow_height*amount + w/2 +2,self.angle-90)

        text = draw_text(self.canvas,pos,self.label,font_size)

        pass

class Tomada_media:
    def __init__(self,canvas,angle = 0,tail_pos = (100,100),tail_size = 10,label = '',font_size = 10,amount = 1) -> None:

        self.canvas = canvas
        self.tail = tail_pos
        self.label = label
        self.angle = angle
        
        points = [tail_pos] #0
        points.append((points[-1][0],points[-1][1]-tail_size)) #1
        points.append((points[-1][0]+tail_size,points[-1][1])) #2
        points.append((points[-1][0]-tail_size,points[-1][1]-tail_size*2)) #3 -> head
        points.append((points[-1][0]-tail_size,points[-1][1]+tail_size*2)) #4
        points.append((points[-1][0]+tail_size,points[-1][1])) #5
        points = rotate_points(points=points,pivo = tail_pos,rot_ang = angle)

        self.head = points[3]
        self.canvas.create_line(points,width = 2)
        self.canvas.create_polygon(points[1],points[2],points[3])

        self.arrow_height = distance(self.head,self.tail)

        if angle == 0 and amount >1:

            shifited = shift_points(points=points[1:], y = - self.arrow_height + tail_size)
            self.canvas.create_line(shifited,width = 2)
            self.canvas.create_polygon(shifited[0],shifited[1],shifited[2])
            self.head = shifited[2]

            if amount>2:
                shifited = shift_points(points=points[1:], y = - self.arrow_height*2 + tail_size*2)
                self.canvas.create_line(shifited,width = 2)
                self.canvas.create_polygon(shifited[0],shifited[1],shifited[2])
                self.head = shifited[2]
        
        if angle == -90 and amount >1:
            
            shifited = shift_points(points=points[1:], x = - self.arrow_height + tail_size)
            self.canvas.create_line(shifited,width = 2)
            self.canvas.create_polygon(shifited[0],shifited[1],shifited[2])
            self.head = shifited[2]

            if amount>2:
                shifited = shift_points(points=points[1:], x = - self.arrow_height*2 + tail_size*2)
                self.canvas.create_line(shifited,width = 2)
                self.canvas.create_polygon(shifited[0],shifited[1],shifited[2])
                self.head = shifited[2]
        
        if angle == 90 and amount >1:
            shifited = shift_points(points=points[1:], x = + self.arrow_height - tail_size)
            self.canvas.create_line(shifited,width = 2)
            self.canvas.create_polygon(shifited[0],shifited[1],shifited[2])
            self.head = shifited[2]
            if amount>2:
                shifited = shift_points(points=points[1:], x = + self.arrow_height*2 - tail_size*2)
                self.canvas.create_line(shifited,width = 2)
                self.canvas.create_polygon(shifited[0],shifited[1],shifited[2])
                self.head = shifited[2]

        if angle == 180 and amount >1:
            shifited = shift_points(points=points[1:], y =  self.arrow_height - tail_size)
            self.canvas.create_line(shift_points(points=points[1:], y =  self.arrow_height - tail_size),width = 2)
            self.head = shift_points(points=points[1:], y = + self.arrow_height - tail_size)[2]
            if amount>2:
                shifited = shift_points(points=points[1:], y = + self.arrow_height*2 - tail_size*2)
                self.canvas.create_line(shifited,width = 2)
                self.canvas.create_polygon(shifited[0],shifited[1],shifited[2])
                self.head = shifited[2]

        
        text = draw_text(self.canvas,(0,0),self.label,font_size) ; h,w = get_widget_box(self.canvas,text); self.canvas.delete(text)
        
        if angle == 0 or angle == 180:
            pos = get_radius_point(self.tail,self.arrow_height*amount + 5,self.angle-90)
        else: pos = get_radius_point(self.tail,self.arrow_height*amount + w/2 +2,self.angle-90)
        
        text = draw_text(self.canvas,pos,self.label,font_size)


        pass

class Tomada_alta:
    def __init__(self,canvas,angle = 0,tail_pos = (100,100),tail_size = 10,label = '',font_size = 10,amount = 1) -> None:

        self.canvas = canvas
        self.tail = tail_pos
        self.label = label
        self.angle = angle
        
        points = [tail_pos] #0
        points.append((points[-1][0],points[-1][1]-tail_size)) #1
        points.append((points[-1][0]+tail_size,points[-1][1])) #2
        points.append((points[-1][0]-tail_size,points[-1][1]-tail_size*2)) #3 -> head
        points.append((points[-1][0]-tail_size,points[-1][1]+tail_size*2)) #4
        points.append((points[-1][0]+tail_size,points[-1][1])) #5
        points = rotate_points(points=points,pivo = tail_pos,rot_ang = angle)

        self.head = points[3]
        self.canvas.create_polygon(points,width = 2)
        self.canvas.create_line(points[0],points[1])

        self.arrow_height = distance(self.head,self.tail)

        if angle == 0 and amount >1:
            self.canvas.create_plygon(shift_points(points=points[1:], y = - self.arrow_height + tail_size),width = 2)
            self.head = shift_points(points=points[1:], y = - self.arrow_height + tail_size)[2]
            if amount>2:
                self.canvas.create_plygon(shift_points(points=points[1:], y = - self.arrow_height*2 + tail_size*2),width = 2)
                self.head = shift_points(points=points[1:], y = - self.arrow_height*2 + tail_size*2)[2]
        
        if angle == -90 and amount >1:
            self.canvas.create_line(shift_points(points=points[1:], x = - self.arrow_height + tail_size),width = 2)
            self.head = shift_points(points=points[1:], x = - self.arrow_height + tail_size)[2]
            if amount>2:
                self.canvas.create_plygon(shift_points(points=points[1:], x = - self.arrow_height*2 + tail_size*2),width = 2)
                self.head = shift_points(points=points[1:], x = - self.arrow_height*2 + tail_size*2)[2]
        
        if angle == 90 and amount >1:
            self.canvas.create_plygon(shift_points(points=points[1:], x = + self.arrow_height - tail_size),width = 2)
            self.head = shift_points(points=points[1:], x = + self.arrow_height - tail_size)[2]
            if amount>2:
                self.canvas.create_plygon(shift_points(points=points[1:], x = + self.arrow_height*2 - tail_size*2),width = 2)
                self.head = shift_points(points=points[1:], x = + self.arrow_height*2 - tail_size*2)[2]

        if angle == 180 and amount >1:
            self.canvas.create_plygon(shift_points(points=points[1:], y =  self.arrow_height - tail_size),width = 2)
            self.head = shift_points(points=points[1:], y = + self.arrow_height - tail_size)[2]
            if amount>2:
                self.canvas.create_plygon(shift_points(points=points[1:], y = + self.arrow_height*2 - tail_size*2),width = 2)
                self.head = shift_points(points=points[1:], y = + self.arrow_height*2 - tail_size*2)[2]

        
        text = draw_text(self.canvas,(0,0),self.label,font_size) ; h,w = get_widget_box(self.canvas,text); self.canvas.delete(text)
        
        if angle == 0 or angle == 180:
            pos = get_radius_point(self.tail,self.arrow_height*amount + 5,self.angle-90)
        else: pos = get_radius_point(self.tail,self.arrow_height*amount + w/2 +2,self.angle-90)

        text = draw_text(self.canvas,pos,self.label,font_size)

        pass