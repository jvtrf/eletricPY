from util import create_circle,draw_text,get_radius_point,draw_curve

class Interruptor_s1:
    def __init__(self,canvas,center,raio = 5,label = 'a') -> None:
        # Desenha um interruptor simples no canvas
        # Recebe um canvas.
        # Recebe o centro do interruptor: "center".
        # Recebe o raio da circunferência do interruptor.
        # Recebe uma string pra identificar o interruptor: "label".

        self.center = center
        self.raio = raio
        self.label = label
        self.canvas = canvas

        create_circle(self.canvas,self.center,self.raio,color='')
        
        self.bottom = center[0], center[1] + raio
        self.celling = center[0], center[1] - raio
        self.right = center[0] + raio, center[1]
        self.left = center[0] - raio, center[1]
        pass

    def set_labe(self,angle = 45,shift = 4):
        # Coloca label em algum lugar próximo ao interruptor.
        # Recebe um angulo que decide onde fica a label: "angle".
        # Recebe um valor "shift" que decide a distância da label para o interruptor.

        pos = get_radius_point(self.center,self.raio+shift,angle)
        draw_text(self.canvas,pos,self.label,self.raio)
    
class Interruptor_s2:
    def __init__(self,canvas,center,raio = 5,label1 = 'a',label2='b') -> None:
        # Desenha um interruptor simples no canvas
        # Recebe um canvas.
        # Recebe o centro do interruptor: "center".
        # Recebe o raio da circunferência do interruptor.
        # Recebe uma string pra identificar o interruptor: "label".

        self.center = center
        self.raio = raio
        self.label1 = label1
        self.label2 = label2
        self.canvas = canvas

        create_circle(self.canvas,self.center,self.raio,color='')
        
        self.bottom = center[0], center[1] + raio
        self.celling = center[0], center[1] - raio
        self.right = center[0] + raio, center[1]
        self.left = center[0] - raio, center[1]

        self.canvas.create_line(self.bottom,self.celling)

        pass

    def set_labe(self,angle = 45,shift = 4):
        # Coloca label em algum lugar próximo ao interruptor.
        # Recebe um angulo que decide onde fica a label: "angle".
        # Recebe um valor "shift" que decide a distância da label para o interruptor.

        pos = get_radius_point(self.center,self.raio+shift,angle)
        draw_text(self.canvas,pos,self.label1,self.raio)

        pos = get_radius_point(self.center,self.raio+shift,angle+90)
        draw_text(self.canvas,pos,self.label2,self.raio)

class Interruptor_s3:
    def __init__(self,canvas,center,raio = 5,label1 = 'a',label2='b',label3 ='c') -> None:
        # Desenha um interruptor simples no canvas
        # Recebe um canvas.
        # Recebe o centro do interruptor: "center".
        # Recebe o raio da circunferência do interruptor.
        # Recebe uma string pra identificar o interruptor: "label".

        self.center = center
        self.raio = raio
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.canvas = canvas

        create_circle(self.canvas,self.center,self.raio,color='')
        
        self.bottom = center[0], center[1] + raio
        self.celling = center[0], center[1] - raio
        self.right = center[0] + raio, center[1]
        self.left = center[0] - raio, center[1]

        self.canvas.create_line(self.celling,self.center)

        pos = get_radius_point(self.center,self.raio,45)
        self.canvas.create_line(self.center,pos)

        pos = get_radius_point(self.center,self.raio,45+90)
        self.canvas.create_line(self.center,pos)


        pass

    def set_labe(self,shift = 4):
        # Coloca label em algum lugar próximo ao interruptor.
        # Recebe um angulo que decide onde fica a label: "angle".
        # Recebe um valor "shift" que decide a distância da label para o interruptor.

        pos = get_radius_point(self.center,self.raio+shift,90)
        draw_text(self.canvas,pos,self.label1,self.raio)

        pos = get_radius_point(self.center,self.raio+shift,-135)
        draw_text(self.canvas,pos,self.label2,self.raio)

        pos = get_radius_point(self.center,self.raio+shift,-45)
        draw_text(self.canvas,pos,self.label3,self.raio)

class Interruptor_3way:
    def __init__(self,canvas,center,raio = 5,label = 'a') -> None:
        # Desenha um interruptor simples no canvas
        # Recebe um canvas.
        # Recebe o centro do interruptor: "center".
        # Recebe o raio da circunferência do interruptor.
        # Recebe uma string pra identificar o interruptor: "label".

        self.center = center
        self.raio = raio
        self.label = label
        self.canvas = canvas

        create_circle(self.canvas,self.center,self.raio,color='black')
        
        self.bottom = center[0], center[1] + raio
        self.celling = center[0], center[1] - raio
        self.right = center[0] + raio, center[1]
        self.left = center[0] - raio, center[1]
        pass

    def set_labe(self,angle = 45,shift = 4):
        # Coloca label em algum lugar próximo ao interruptor.
        # Recebe um angulo que decide onde fica a label: "angle".
        # Recebe um valor "shift" que decide a distância da label para o interruptor.

        pos = get_radius_point(self.center,self.raio+shift,angle)
        draw_text(self.canvas,pos,self.label,self.raio)

class Interruptor_4way:
    def __init__(self,canvas,center,raio = 5,label = 'a') -> None:
        # Desenha um interruptor simples no canvas
        # Recebe um canvas.
        # Recebe o centro do interruptor: "center".
        # Recebe o raio da circunferência do interruptor.
        # Recebe uma string pra identificar o interruptor: "label".

        self.center = center
        self.raio = raio
        self.label = label
        self.canvas = canvas

        create_circle(self.canvas,self.center,self.raio,color='')
        
        self.bottom = center[0], center[1] + raio
        self.celling = center[0], center[1] - raio
        self.right = center[0] + raio, center[1]
        self.left = center[0] - raio, center[1]

        points,head,angles = draw_curve(self.bottom,self.celling,0,dir=1)

        self.canvas.create_polygon(points)

        pass

    def set_labe(self,angle = 45,shift = 4):
        # Coloca label em algum lugar próximo ao interruptor.
        # Recebe um angulo que decide onde fica a label: "angle".
        # Recebe um valor "shift" que decide a distância da label para o interruptor.

        pos = get_radius_point(self.center,self.raio+shift,angle)
        draw_text(self.canvas,pos,self.label,self.raio)