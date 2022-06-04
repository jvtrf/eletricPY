from math import sin, radians,cos,atan2,degrees

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
    #Cria uma cricunferencia vermelha, com centro "c" e rairo "r".
    #Utilizado pra debugar.

    p1 = c[0]-r,c[1]-r
    p2 = c[0]+r,c[1]+r
    canvas.create_oval(p1,p2,fill='red')

def get_mid_p(A,B):
    #Obtem o midpoint da reta.
    return (A[0]+B[0])/2 , (A[1]+B[1])/2

def perpendicular_point(A,B,d,p = 0.5, dir = 0):
    
    vec = get_vec_A_B(A,B)

    inter_point = percent_line(A,B,p)

    ang_vec = angle_vector(vec) #Angulo da reta

    if (ang_vec >=0 and ang_vec<= 90) or (ang_vec>=-180 and ang_vec<=-90):
        if ang_vec>=-180 and ang_vec<=-90: ang_vec +=180
        #Cabeça do vetor na direção pra baixo a direita (quarto quadrante).
        per_ang = -(90 - ang_vec)  +dir*(180)#angulo perpendicular
        head = (inter_point[0] + d*angle_cos(per_ang), inter_point[1] + d*angle_sin(per_ang)) #Cabeça do vetor
    else:
        per_ang = (90 - ang_vec)  + dir*(180)
        head = (inter_point[0] + d*angle_cos(per_ang), inter_point[1] + d*angle_sin(per_ang)) #Cabeça do vetor
    
    print(ang_vec)
    return (inter_point,head)
    pass

def get_vec_A_B(A,B):
    return (B[0] - A[0], B[1] - A[1])
    pass
