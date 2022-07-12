from util import get_mid_p
class Fonte:
    def __init__(self,canvas,w =30,h = 10,center = (100,100)) -> None:

        self.id_list = []
        
        self.canvas         = canvas
        self.top_left       = self.tl = center[0] - w/2,center[1] + h/2
        self.botton_right   = self.br = self.tl[0]+w , self.tl[1]+h
        self.top_right      = self.tr = self.br[0],self.tl[1]
        self.botton_left    = self.bl = self.tl[0],self.br[1]

        self.middle_top     = self.mt = get_mid_p(self.tl,self.tr)
        self.middle_botton  = self.mb = get_mid_p(self.br,self.bl)
        self.middle_right   = self.mr = get_mid_p(self.tr,self.br)
        self.middle_left    = self.ml = get_mid_p(self.tl,self.bl)

        self.id_list.append(canvas.create_rectangle(self.tl,self.br,fill = 'white',width = 2))
        self.id_list.append(canvas.create_polygon(self.tl,self.br,self.bl))
        pass

    def deletar(self):
        for id in self.id_list:
            self.canvas.delete(id)