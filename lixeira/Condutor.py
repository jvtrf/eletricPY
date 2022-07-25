from util import draw_curve,get_vec_A_B,get_vec_module,draw_radio_line,get_quadrant,perpendicular_point

class Condutor:
    # Classe Condutor.
    # - Gera um fio entre dois pontos.
    # - Recebe um canvas (onde será feito o desenho).
    # - Recebe uma coordenada A e B.
    # - Recebe um valor "d" com o tamanho da curvatura (quanto maior)
    #   menos curvado vai ficar o condutor.
    #  -Recebe um valor "dir" que decide se a curva é pra dentro ou pra fora.

    def __init__(self,canvas,A,B,d = 100,dir = 0) -> None:
        self.points ,self.head, self.angles = draw_curve(A,B,d,dir)
        self.raio = get_vec_module(get_vec_A_B(self.head,self.points[0]))
        self.quad = get_quadrant(get_vec_A_B(A,B))
        self.canvas = canvas

        canvas.create_line(self.points)
        pass

    def add_circuito(self,circ = "NFTR",angle_index = 10,dim=10,shift = 3):
        # Método que gera o circuito
        # - Recebe uma string "circ" que vai definir a ordem dos desenhos.
        # - "N" para neutro ; "F" para fase; "T" para terra e "R" para retorno.
        # - Recebe um valor de 0 a 19 para o "angle_index" que vai definir onde
        #   vai ser desenhado o circuito.
        # - Recebe um valor "dim", que vai definir o tamanho do desenho.
        # - Recebe um valor de "shift" que vai definir o espaço entre cada desenho.

        angle_shift = 0
        dim = dim
        d1 = self.raio - dim
        print(self.quad) #debug
        for c in circ:
            if c == 'N':
                A,B = draw_radio_line(self.head,d1,d1+2*dim,self.angles[angle_index]+angle_shift)
                inter,head = perpendicular_point(A,B,10,p=0)
                self.canvas.create_line(A,B,head)
                angle_shift += shift

            if c == 'F':
                A,B = draw_radio_line(self.head,d1,d1+2*dim,self.angles[angle_index]+angle_shift)
                self.canvas.create_line(A,B)
                angle_shift += shift
            
            if c == 'T':
                A,B = draw_radio_line(self.head,d1,d1+2*dim,self.angles[angle_index]+angle_shift)
                inter,head = perpendicular_point(A,B,10,p=0)
                inter2,head2 = perpendicular_point(A,B,10,p=0,dir=1)
                self.canvas.create_line(A,B,head,head2)
                angle_shift += shift
            
            if c == 'R':
                A,B = draw_radio_line(self.head,self.raio,self.raio+dim,self.angles[angle_index]+angle_shift)
                self.canvas.create_line(A,B)
                angle_shift += shift
                
                
        pass


