from util import rotate_points,draw_text,get_radius_point,distance,get_widget_box

class Tomada_baixa:
    def __init__(self,canvas,angle = 0,tail_pos = (100,100),tail_size = 10,label = '',font_size = 10) -> None:

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
        self.canvas.create_line(points)

        self.arrow_height = distance(self.head,self.tail)

        
        text = draw_text(self.canvas,(0,0),self.label,font_size) ; h,w = get_widget_box(self.canvas,text); self.canvas.delete(text)
        
        pos = get_radius_point(self.tail,self.arrow_height + w/2 +2,self.angle-90)
        text = draw_text(self.canvas,pos,self.label,font_size)

        pass

class Tomada_media:
    def __init__(self,canvas,angle = 0,tail_pos = (100,100),tail_size = 10,label = '',font_size = 10) -> None:

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
        self.canvas.create_line(points)
        self.canvas.create_polygon(points[1],points[2],points[3])

        self.arrow_height = distance(self.head,self.tail)

        
        text = draw_text(self.canvas,(0,0),self.label,font_size) ; h,w = get_widget_box(self.canvas,text); self.canvas.delete(text)
        
        pos = get_radius_point(self.tail,self.arrow_height + w/2 +2,self.angle-90)
        text = draw_text(self.canvas,pos,self.label,font_size)


        pass

class Tomada_alta:
    def __init__(self,canvas,angle = 0,tail_pos = (100,100),tail_size = 10,label = '',font_size = 10) -> None:

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
        self.canvas.create_polygon(points)
        self.canvas.create_line(points[0],points[1])

        self.arrow_height = distance(self.head,self.tail)

        
        text = draw_text(self.canvas,(0,0),self.label,font_size) ; h,w = get_widget_box(self.canvas,text); self.canvas.delete(text)
        
        pos = get_radius_point(self.tail,self.arrow_height + w/2 +2,self.angle-90)
        text = draw_text(self.canvas,pos,self.label,font_size)

        pass