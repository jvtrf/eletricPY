import math

class Square_comodo_in_dim:
    def __init__(self,eL = 0 ,eR = 0,eT = 0,eB = 0,horizotal_dim = 0,vertical_dim = 0 ,s_x = 0 ,s_y = 0 ,canvas = None,e = None) -> None:
        
        if e != None:
            eL = e ; eR = e ; eT = e ; eB = e
        
        s = s_x,s_y
        f = (s[0]+horizotal_dim,s[1]+vertical_dim)
        points = (s[0]-eL,s[1]-eT,f[0]+eR,f[1]+ eB)

        color = 'grey'
        canvas.create_rectangle(points,fill=color,outline = '')
        canvas.create_rectangle(s[0],s[1],f[0],f[1],fill='white',outline = 'black')

        self.bottom_dim = horizotal_dim
        self.top_dim = horizotal_dim
        self.right_dim = vertical_dim
        self.left_dim = vertical_dim

        self.left_m = (s[0]-eL/2),(s[1]+f[1])/2 #Pontos médios
        self.right_m = (f[0]+eR/2),(s[1]+f[1])/2
        self.top_m = (s[0]+f[0])/2, (s[1]-eT/2)
        self.botton_m = (s[0]+f[0])/2, (f[1]+eB/2)
        
        self.eL = eL #Espessura
        self.eR = eR
        self.eT = eT
        self.eB = eB

        self.l_dim = vertical_dim #Tamanho das Paredes
        self.r_dim = vertical_dim
        self.t_dim = horizotal_dim
        self.d_dim = horizotal_dim

        self.tl_inp = s_x,s_y   #Pontos internos
        self.tr_inp = s_x+horizotal_dim,s_y
        self.dl_inp = f[0]-horizotal_dim,f[1]
        self.br_inp = f

        self.tl_outp = s_x - self.eL, s_y - self.eT     #Pontos externos
        self.tr_outp = self.tr_inp[0] +self.eR, self.tr_inp[1] - self.eT
        self.bl_outp = self.dl_inp[0] - self.eL, self.dl_inp[1] + self.eB
        self.br_outp = self.br_inp[0] + self.eR, self.br_inp[1] + self.eB

        self.A = s_x - self.eL,s_y
        self.B = s_x,s_y - self.eT
        self.C = self.tr_inp[0] , self.tr_inp[1] - self.eT
        self.D = self.tr_inp[0] + self.eR , self.tr_inp[1]
        self.E = self.dl_inp[0] - self.eL, self.dl_inp[1]
        self.F = self.dl_inp[0], self.dl_inp[1] + self.eB
        self.G = self.br_inp[0], self.br_inp[1] + self.eB
        self.H = self.br_inp[0] + self.eR , self.br_inp[1]

        self.area = vertical_dim * horizotal_dim
        self.perimetro = vertical_dim*2 + horizotal_dim*2


        self.door_w = 5         #Config

        self.canvas = canvas
        pass
    
    def create_left_window(self,dim):
        first_p = self.left_m[0]-(self.eL/2) , self.left_m[1]-(dim/2) # Primeiro ponto da Janela
        second_p = first_p[0]+self.eL, first_p[1]+(dim)

        first_p_p = first_p[0]+self.eB/3,first_p[1] #Primeiro Ponto do rentangulo interno da Janela
        second_p_p = second_p[0]-self.eB/3,second_p[1]
        
        points = first_p,second_p
        pointss = first_p_p,second_p_p
        self.canvas.create_rectangle(points,fill='white')
        self.canvas.create_rectangle(pointss,fill='white')

        pass
    
    def create_right_window(self,dim):
        first_p = self.right_m[0]-(self.eR/2) , self.right_m[1]-(dim/2) # Primeiro ponto da Janela
        second_p = first_p[0]+self.eR, first_p[1]+(dim)

        first_p_p = first_p[0]+self.eR/3,first_p[1] #Primeiro Ponto do rentangulo interno da Janela
        second_p_p = second_p[0]-self.eR/3,second_p[1]
        
        points = first_p,second_p
        pointss = first_p_p,second_p_p
        self.canvas.create_rectangle(points,fill='white')
        self.canvas.create_rectangle(pointss,fill='white')
    
    def create_top_window(self,dim):
        first_p = self.top_m[0]-(dim/2),self.top_m[1]-(self.eB/2)  # Primeiro ponto da Janela
        second_p = first_p[0]+dim, first_p[1]+(self.eB)

        first_p_p = first_p[0],first_p[1]+self.eB/3 #Primeiro Ponto do rentangulo interno da Janela
        second_p_p = second_p[0],second_p[1]-self.eB/3
        
        points = first_p,second_p
        pointss = first_p_p,second_p_p
        self.canvas.create_rectangle(points,fill='white')
        self.canvas.create_rectangle(pointss,fill='white')
    
    def create_top_window(self,dim):
        first_p = self.top_m[0]-(dim/2),self.top_m[1]-(self.eT/2)  # Primeiro ponto da Janela
        second_p = first_p[0]+dim, first_p[1]+(self.eT)

        first_p_p = first_p[0],first_p[1]+self.eT/3 #Primeiro Ponto do rentangulo interno da Janela
        second_p_p = second_p[0],second_p[1]-self.eT/3
        
        points = first_p,second_p
        pointss = first_p_p,second_p_p
        self.canvas.create_rectangle(points,fill='white')
        self.canvas.create_rectangle(pointss,fill='white')
    
    def create_botton_window(self,dim):
        first_p = self.botton_m[0]-(dim/2),self.botton_m[1]-(self.eB/2)  # Primeiro ponto da Janela
        second_p = first_p[0]+dim, first_p[1]+(self.eB)

        first_p_p = first_p[0],first_p[1]+self.eB/3 #Primeiro Ponto do rentangulo interno da Janela
        second_p_p = second_p[0],second_p[1]-self.eB/3
        
        points = first_p,second_p
        pointss = first_p_p,second_p_p
        self.canvas.create_rectangle(points,fill='white')
        self.canvas.create_rectangle(pointss,fill='white')
    
    # w-> Tamanaho da porta; ld-> distância do lado esquerdo da parede(left distance).
    # clock -> seintdo = 'a' para abrir antihorário e 'h' para abrir horário.
    def create_botton_space(self,ld,w):
        sp_1 = (self.dl_inp[0]+ld,self.dl_inp[1])
        sp_2 = (sp_1[0]+w,sp_1[1]+self.eB+1)

        self.canvas.create_rectangle(sp_1,sp_2,fill='white',width=0)
        self.canvas.create_line(sp_1,(sp_1[0],sp_1[1]+self.eB+1))
        self.canvas.create_line((sp_2[0],sp_2[1]-1),(sp_2[0],sp_2[1]-self.eB-1))

        return sp_1,sp_2
    
    def create_top_space(self,ld,w):
        sp_1 = (self.tl_inp[0]+ld,self.tl_inp[1]+1)
        sp_2 = (sp_1[0]+w,sp_1[1]-self.eT-1)

        self.canvas.create_rectangle(sp_1,sp_2,fill='white',width=0)
        self.canvas.create_line((sp_1[0],sp_1[1]-1),(sp_1[0],sp_1[1]-self.eT-2))
        self.canvas.create_line((sp_2[0],sp_2[1]),(sp_2[0],sp_2[1]+self.eT))

        return sp_1,sp_2
    
    def create_left_space(self,td,w):
        sp_1 = (self.tl_inp[0]+1,self.tl_inp[1]+td)
        sp_2 = (self.tl_inp[0]-self.eL,sp_1[1]+w)

        self.canvas.create_rectangle(sp_1,sp_2,fill='white',width=0)
        self.canvas.create_line((sp_1[0]-1,sp_1[1]),(sp_1[0]-self.eL-1,sp_1[1]))
        self.canvas.create_line((sp_1[0]-1,sp_1[1]+w),(sp_1[0]-self.eL-1,sp_1[1]+w))
        return sp_1,sp_2
    
    def create_right_space(self,td,w):
        sp_1 = (self.tr_inp[0],self.tr_inp[1]+td)
        sp_2 = (self.tr_inp[0]+self.eR+1,sp_1[1]+w)

        self.canvas.create_rectangle(sp_1,sp_2,fill='white',width=0)
        self.canvas.create_line((sp_1[0]+1,sp_1[1]),(sp_1[0]+self.eL+1,sp_1[1]))
        self.canvas.create_line((sp_1[0]+1,sp_1[1]+w),(sp_1[0]+self.eL+1,sp_1[1]+w))
        return sp_1,sp_2

    def create_top_indoor(self,ld,w,clock='a'):
        sp1,sp2 = self.create_top_space(ld,w)
        if clock == 'a':
            points = [(x+sp1[0],(math.sqrt(w**2 - x**2))+sp1[1])  for x in range(int(w),-1,-1)]
            self.canvas.create_line(points,(points[-1][0],points[-1][1]-w-1),smooth = 1)
            self.canvas.create_rectangle(sp1,(sp1[0]+self.door_w,sp1[1]+w))
        if clock == 'b':
            points = [(-x+sp1[0]+w,(math.sqrt(w**2 - x**2))+sp1[1])  for x in range(int(w),-1,-1)]
            self.canvas.create_line(points,sp2,smooth = 1)
            self.canvas.create_rectangle((sp1[0]+w-self.door_w,sp1[1]),points[-1])
    
    def create_top_outdoor(self,ld,w,clock='a'):
        sp1,sp2 = self.create_top_space(ld,w)
        if clock == 'a':
            points = [(x+sp1[0],(-math.sqrt(w**2 - x**2))+sp1[1]-self.eT)  for x in range(int(w),-1,-1)]
            self.canvas.create_line(points,sp1,smooth = 1)
            self.canvas.create_rectangle((sp1[0],sp1[1]-w-self.eT),(sp1[0]+self.door_w,sp1[1]-self.eT))
        if clock == 'b':
            points = [(-x+sp1[0]+w,(-math.sqrt(w**2 - x**2))+sp1[1]-self.eT)  for x in range(int(w),-1,-1)]
            self.canvas.create_line(points,sp2,smooth = 1)
            self.canvas.create_rectangle((sp1[0]+w-self.door_w,sp1[1]-w-self.eT),(sp1[0]+w,sp1[1]-self.eT))
    
    def create_botton_outdoor(self,ld,w,clock='a'):
        sp1,sp2 = self.create_botton_space(ld,w)
        if clock == 'a':
            points = [(x+sp1[0],(math.sqrt(w**2 - x**2))+sp1[1]+self.eB)  for x in range(int(w),-1,-1)]
            self.canvas.create_line(points,(points[-1][0],points[-1][1]-w-1),smooth = 1)
            self.canvas.create_rectangle((sp1[0],sp1[1]+self.eB),(sp1[0]+self.door_w,sp1[1]+w+self.eB))
        if clock == 'b':
            points = [(-x+sp1[0]+w,(math.sqrt(w**2 - x**2))+sp1[1]+self.eB) for x in range(int(w),-1,-1)]
            self.canvas.create_line(points,sp2,smooth = 1)
            self.canvas.create_rectangle((sp1[0]+w-self.door_w,sp1[1]+self.eB),points[-1])
            
    def create_botton_indoor(self,ld,w,clock='b'):
        sp1,sp2 = self.create_botton_space(ld,w)
        if clock == 'a':
            points = [(x+sp1[0],(-math.sqrt(w**2 - x**2))+sp1[1])  for x in range(int(w),-1,-1)]
            self.canvas.create_line(points,sp1,smooth = 1)
            self.canvas.create_rectangle((sp1[0],sp1[1]-w),(sp1[0]+self.door_w,sp1[1]))
        if clock == 'b':
            points = [(-x+sp1[0]+w,(-math.sqrt(w**2 - x**2))+sp1[1])  for x in range(int(w),-1,-1)]
            self.canvas.create_line(points,sp2,smooth = 1)
            self.canvas.create_rectangle((sp1[0]+w-self.door_w,sp1[1]-w),(sp1[0]+w,sp1[1]))

    def create_left_indoor(self,tp,w,clock='a'):
        sp1,sp2 = self.create_left_space(tp,w)
        if clock == 'a':
            points = [(x+sp1[0],(math.sqrt(w**2 - x**2))+sp1[1])  for x in range(int(w),-1,-1)]
            self.canvas.create_line(sp1,points,sp2,smooth = 0)
            self.canvas.create_rectangle((sp1),(sp1[0]+w,sp1[1]+self.door_w))
        if clock == 'b':
            points = [(x+sp1[0],(-math.sqrt(w**2 - x**2))+sp1[1]+w)  for x in range(int(w),-2,-1)]
            self.canvas.create_line(sp2,points,smooth = 0)
            self.canvas.create_rectangle((sp2[0]+self.eL,sp2[1]),(sp2[0]+self.eL+w+1,sp2[1]-self.door_w))
    
    def create_right_indoor(self,tp,w,clock='b'):
        sp1,sp2 = self.create_right_space(tp,w)
        if clock == 'a':
            points = [(x+sp1[0],(math.sqrt(w**2 - x**2))+sp1[1])  for x in range(int(w),-1,-1)]
            self.canvas.create_line(sp1,points,sp2,smooth = 0)
            self.canvas.create_rectangle((sp1[0]+self.eR,sp1[1]),(sp1[0]+w,sp1[1]+self.door_w))
        if clock == 'b':
            points = [(x+sp2[0],(-math.sqrt(w**2 - x**2))+sp2[1])  for x in range(int(w),-2,-1)]
            self.canvas.create_line(sp2,points,smooth = 0)
            self.canvas.create_rectangle((sp2),(sp2[0]+w,sp2[1]-self.door_w))
    
    def join_botton(self,eL = 0,eR = 0,eT = 0,eB = 0 ,horizotal_dim = 0 ,vertical_dim = 0,point = 'F',e = None):
        
        if e != None:
            eL = e ; eR = e ; eT = e ; eB = e

        if point == 'F':
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.F[0],s_y = self.F[1],canvas = self.canvas)
            self.canvas.create_rectangle((comodo.tl_inp[0]+1,comodo.tl_inp[1]+1),comodo.C,fill = 'white',width = 0)

            self.area = self.area + comodo.area + (eT*horizotal_dim)

            return comodo
        elif point == 'G':
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.F[0] + (self.bottom_dim - horizotal_dim),s_y = self.F[1],canvas = self.canvas)
            self.canvas.create_rectangle((comodo.tl_inp[0]+1,comodo.tl_inp[1]+1),(comodo.C),fill = 'white',width = 0)

            self.area = self.area + comodo.area + (eT*horizotal_dim)
            return comodo
    
    def add_botton(self,eL = 0,eR = 0,eT = 0,eB = 0 ,horizotal_dim = 0 ,vertical_dim = 0,point = 'F',e = None):
        
        if e != None:
            eL = e ; eR = e ; eT = e ; eB = e

        if point == 'F':
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.F[0],s_y = self.F[1],canvas = self.canvas)

            return comodo
        elif point == 'G':
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.F[0] + (self.bottom_dim - horizotal_dim),s_y = self.F[1],canvas = self.canvas)
            return comodo
    
    def join_top(self,eL = 0,eR = 0,eT = 0,eB = 0 ,horizotal_dim = 0 ,vertical_dim = 0,point = 'B',e = None):

        if e != None:
            eL = e ; eR = e ; eT = e ; eB = e

        if point == 'B':
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.B[0],s_y = self.B[1]-horizotal_dim,canvas = self.canvas)
            self.canvas.create_rectangle((comodo.F[0]+1,comodo.F[1]+1),comodo.br_inp,fill = 'white',width = 0)

            self.area = self.area + comodo.area + (eB*horizotal_dim)

            return comodo
        elif point == 'C':
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.B[0] + (self.bottom_dim - horizotal_dim),s_y = self.B[1] - vertical_dim,canvas = self.canvas)
            self.canvas.create_rectangle((comodo.F[0]+1,comodo.F[1]+1),comodo.br_inp,fill = 'white',width = 0)

            self.area = self.area + comodo.area + (eB*horizotal_dim)
            return comodo
        
    def add_top(self,eL = 0,eR = 0,eT = 0,eB = 0 ,horizotal_dim = 0 ,vertical_dim = 0,point = 'B',e = None):

        if e != None:
            eL = e ; eR = e ; eT = e ; eB = e

        if point == 'B':
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.B[0],s_y = self.B[1]-horizotal_dim,canvas = self.canvas)

            return comodo
        elif point == 'C':
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.B[0] + (self.bottom_dim - horizotal_dim),s_y = self.B[1] - vertical_dim,canvas = self.canvas)
            self.canvas.create_rectangle((comodo.F[0]+1,comodo.F[1]+1),comodo.br_inp,fill = 'white',width = 0)

            self.area = self.area + comodo.area + (eB*horizotal_dim)
            return comodo

    def join_right(self,eL = 0,eR = 0,eT = 0,eB = 0 ,horizotal_dim = 0 ,vertical_dim = 0,point = 'D',e = None):

        if e != None:
            eL = e ; eR = e ; eT = e ; eB = e

        if point == 'D':
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.D[0],s_y = self.D[1],canvas = self.canvas)
            
            self.canvas.create_rectangle((comodo.tl_inp[0]+1,comodo.tl_inp[1]+1),comodo.E,fill = 'white',width = 0)

            self.area = self.area + comodo.area + (eL*vertical_dim)

            return comodo
        elif point == 'H':
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.D[0] ,s_y = self.D[1]+ (self.left_dim - vertical_dim),canvas = self.canvas)
            self.canvas.create_rectangle((comodo.tl_inp[0]+1,comodo.tl_inp[1]+1),comodo.E,fill = 'white',width = 0)

            self.area = self.area + comodo.area + (eL*vertical_dim)
            
            return comodo
    
    def add_right(self,eL = 0,eR = 0,eT = 0,eB = 0 ,horizotal_dim = 0 ,vertical_dim = 0,point = 'D',e = None):

        if e != None:
            eL = e ; eR = e ; eT = e ; eB = e

        if point == 'D':
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.D[0],s_y = self.D[1],canvas = self.canvas)
            return comodo
        elif point == 'H':
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.D[0] ,s_y = self.D[1]+ (self.left_dim - vertical_dim),canvas = self.canvas)
            return comodo
    
    def join_left(self,eL = 0,eR = 0,eT = 0,eB = 0 ,horizotal_dim = 0 ,vertical_dim = 0,point = 'A', e = None):

        if e != None:
            eL = e ; eR = e ; eT = e ; eB = e

        if point == 'A':
            #Encaixa o ponto tr_inp do novo comodo no ponto A do comodo atual.
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.A[0] - horizotal_dim, s_y = self.A[1],canvas = self.canvas)
            self.canvas.create_rectangle((comodo.tr_inp[0],comodo.tr_inp[1]+1),(comodo.H[0]+1,comodo.H[1]),fill = 'white',width = 0)

            self.area = self.area + comodo.area + (eR*vertical_dim)
            return comodo
        elif point == 'E':
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.A[0] - horizotal_dim ,s_y = self.A[1]+ (self.left_dim - vertical_dim),canvas = self.canvas)
            self.canvas.create_rectangle((comodo.tr_inp[0],comodo.tr_inp[1]+1),(comodo.H[0]+1,comodo.H[1]),fill = 'white',width = 0)

            self.area = self.area + comodo.area + (eR*vertical_dim)
            return comodo
    
    def add_left(self,eL = 0,eR = 0,eT = 0,eB = 0 ,horizotal_dim = 0 ,vertical_dim = 0,point = 'A', e = None):

        if e != None:
            eL = e ; eR = e ; eT = e ; eB = e

        if point == 'A':
            #Encaixa o ponto tr_inp do novo comodo no ponto A do comodo atual.
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.A[0] - horizotal_dim, s_y = self.A[1],canvas = self.canvas)
            return comodo
        elif point == 'E':
            comodo = Square_comodo_in_dim(eL,eR,eT,eB,horizotal_dim,vertical_dim,
                                        s_x = self.A[0] - horizotal_dim ,s_y = self.A[1]+ (self.left_dim - vertical_dim),canvas = self.canvas)
            return comodo
    
    def rect_area(sef,p1,p2):
        return (((p2[0] - p1[0]) * (p1[1] - p2[1]))**2)**(1/2)

    def point_finder(self,p):
        r = 3
        self.canvas.create_line((0,p[1]),(p[0]+5000,p[1]))
        self.canvas.create_line((p[0],0),(p[0],p[1]+5000))
        self.canvas.create_oval(p[0]-r,p[1]-r,p[0]+r,p[1]+r,fill= 'red')
    
