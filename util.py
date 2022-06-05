from math import sin, radians,cos,atan2,degrees,acos
from numpy import linspace

def angle_sin(ang):
    #Calcula o seno de um angulo
    return sin(radians(ang))

def angle_cos(ang):
    #Calcula o cos de um angulo
    return cos(radians(ang))

def angle_vector(vec):
    #Calcula o angulo de um vetor que inicia na origem.
    return degrees(atan2(vec[1],vec[0]))

def distance(A,B):
    #Calcula a distância entre dois pontos
    return ((A[0]-B[0])**2 + (A[1] - B[1])**2)**(1/2)

def percent_line(A,B,p):
    #Encontra um ponto intermediário entre A e B baseado em uma procentagem.
    #Exemplo: se p = 0.5 a funcao vai retornar o ponto médio entre A e B.
    #Exemplo: se p = 0 a funcao vai retornar o ponto B.
    #Exemplo: se p = 1 a funcao vai retornar o ponto A.

    vec = B[0] - A[0] , B[1] - A[1]
    ang = angle_vector(vec)
    d = distance(A,B)
    
    if ang <=0:
        point = B[0] - p*d*angle_cos(ang), B[1] - p*d*angle_sin(ang)
    else:
        point = B[0] - p*d*angle_cos(ang), B[1] - p*d*angle_sin(ang)
    return point

def create_circle(canvas,c,r):
    # Cria uma cricunferencia vermelha, com centro "c" e rairo "r".
    # Utilizado pra debugar.

    p1 = c[0]-r,c[1]-r
    p2 = c[0]+r,c[1]+r
    canvas.create_oval(p1,p2,fill='red')

def get_mid_p(A,B):
    # Obtem o midpoint da reta.
    return (A[0]+B[0])/2 , (A[1]+B[1])/2

def perpendicular_point(A,B,d,p = 0.5, dir = 0):
    # Cria um vetor perpendicular ao vetor ab.
    # O parâmetro "p" deve estrar entre 0 e 1 (float), é ele que decide quão posição começa o vetor perpendicular.
    # O parâmetro dir, decide qual lado em relação ao vetor AB a reta perpendicular vai estar.
    # Retorna (inter_point, head)

    vec = get_vec_A_B(A,B)

    inter_point = percent_line(A,B,p)

    ang_vec = angle_vector(vec) #Angulo da reta

    if (ang_vec >=0 and ang_vec<= 90) or (ang_vec>=-180 and ang_vec<=-90):
        if ang_vec>=-180 and ang_vec<=-90: ang_vec +=180
        #Cabeça do vetor no quarto quadrante ou no segundo.
        per_ang = -(90 - ang_vec)  +dir*(180) #Angulo perpendicular
        head = (inter_point[0] + d*angle_cos(per_ang), inter_point[1] + d*angle_sin(per_ang)) #Cabeça do vetor
    else:
        #Cabeça do vetor no primeiro ou no terceiro quadrante.
        if ang_vec <= -180 and ang_vec >= -270: ang_vec += 180
        per_ang = -(90 - ang_vec)  + dir*(180)
        head = (inter_point[0] + d*angle_cos(per_ang), inter_point[1] + d*angle_sin(per_ang)) #Cabeça do vetor
    
    return (inter_point,head)
    pass

def draw_curve(A,B,d,dir = 0):
    inter_point,head = perpendicular_point(A,B,d,p = 0.5,dir = dir)
    
    vec_1 = get_vec_A_B(head,A)
    vec_2 = get_vec_A_B(head,B)

    line = get_vec_A_B(A,B)

    raio = get_vec_module(vec_1) #Tamanho do raio 

    
    ang1 = angle_vector(vec_1)
    ang2 = angle_vector(vec_2) + dir*360

    angles = linspace(ang1,ang2,20).tolist()
    angles = [round(a,2) for a in angles]

    print(ang1,ang2)
    points =  [(head[0]+raio*angle_cos(a),head[1]+raio*angle_sin(a)) for a in angles]
    
    points = [(round(p[0],2),round(p[1],2)) for p in points]

    

    return points,head

def get_vec_A_B(A,B):
    #Retorna o vetor AB (indo de A para B).
    return (B[0] - A[0], B[1] - A[1])
    pass

def get_vec_module(vec):
    # Retorna o módulo de um vetor
    return (vec[0]**2 + vec[1]**2)**(0.5)

def produto_escalar(A,B):
    # Retorna o produto escalar entre AB.
    return A[0]*B[0] + A[1]*B[1]

def get_angle_between(vec1,vec2):
    #Retorna o ângulo entre dois vetores.
    cos_ang = (produto_escalar(vec1,vec2))/(get_vec_module(vec1)*get_vec_module(vec2))
    return acos(cos_ang)
    pass

