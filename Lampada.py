from turtle import width


class Lampada:
    def __init__(self,canvas,centro,raio,pot,id,circ) -> None:
        self.canvas = canvas
        self.centro = centro
        self.raio = raio
        self.pot = pot
        self.circ = circ
        self.id = id
        self.create()
        pass
    
    def create(self):
        p1x = self.centro[0] - self.raio
        p1y = self.centro[1] - self.raio
        p2x = p1x + 2*self.raio
        p2y = p1y + 2*self.raio

        self.canvas.create_oval(p1x,p1y,p2x,p2y,width=2)

        self.left = (p1x,p1y+self.raio)                   #Pontos Tangentes Da circunferência
        self.right = (p1x + 2*self.raio,p1y+self.raio)
        self.botton = (p1x + self.raio,p2y)
        self.top = (p1x + self.raio,p1y)

        self.canvas.create_line(self.left,self.right)
        self.canvas.create_line(self.centro,self.botton)

        #ID
        idpos = (self.centro[0]+self.raio/2.5,self.centro[1]+self.raio/2.5)
        self.canvas.create_text(idpos,fill="black",font="Arial "+str(int(self.raio/2)),
                        text=self.id.upper())
        #Circuito
        circpos = (self.centro[0]-self.raio/2.5,self.centro[1]+self.raio/2.5)
        self.canvas.create_text(circpos,fill="black",font="Arial "+str(int(self.raio/2)),
                        text=self.circ.upper())
        #Pot
        potpos = (self.centro[0],self.centro[1]-self.raio/2.5)
        self.canvas.create_text(potpos,fill="black",font="Arial "+str(int(self.raio/2)),
                        text=str(self.pot))