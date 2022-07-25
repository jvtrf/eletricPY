from random import random
##TODO: VERIFY IF ITS POSSIBLE TO CREATE WINDOW --- IDKH
class Janela:
  def __init__(self, comodo, canvas, dim, side = "L"):
    ##SIDE -> L = Left; R = Right; T = Top; B = Bottom.
    self.comodo = comodo
    self.side = side
    self.dim = dim
    self.canvas = canvas
    if (side == "L"):
      self.create_left_window()
    elif (side == "R"):
      self.create_right_window()
    elif (side == "T"):
      self.create_top_window()
    elif (side == "B"):
      self.create_botton_window()


  def create_left_window(self):
        first_p = self.comodo.left_m[0]-(self.comodo.eL/2) , self.comodo.left_m[1]-(self.dim/2) # Primeiro ponto da Janela
        second_p = first_p[0]+self.comodo.eL, first_p[1]+(self.dim)

        first_p_p = first_p[0]+self.comodo.eB/3,first_p[1] #Primeiro Ponto do rentangulo interno da Janela
        second_p_p = second_p[0]-self.comodo.eB/3,second_p[1]
        
        points = first_p,second_p
        pointss = first_p_p,second_p_p
        
        self.canvas.create_rectangle(points,fill='white',tag = self.generate_random())
        self.canvas.create_rectangle(pointss,fill='white',tag = self.generate_random())

        pass
    
  def create_right_window(self):
      first_p = self.comodo.right_m[0]-(self.comodo.eR/2) , self.comodo.right_m[1]-(self.dim/2) # Primeiro ponto da Janela
      second_p = first_p[0]+self.comodo.eR, first_p[1]+(self.dim)
      first_p_p = first_p[0]+self.comodo.eR/3,first_p[1] #Primeiro Ponto do rentangulo interno da Janela
      second_p_p = second_p[0]-self.comodo.eR/3,second_p[1]
      
      points = first_p,second_p
      pointss = first_p_p,second_p_p
      self.canvas.create_rectangle(points,fill='white',tag = self.generate_random())
      self.canvas.create_rectangle(pointss,fill='white',tag = self.generate_random())
  
  def create_top_window(self):
      first_p = self.comodo.top_m[0]-(self.dim/2),self.comodo.top_m[1]-(self.comodo.eT/2)  # Primeiro ponto da Janela
      second_p = first_p[0]+self.dim, first_p[1]+(self.comodo.eT)
      first_p_p = first_p[0],first_p[1]+self.comodo.eT/3 #Primeiro Ponto do rentangulo interno da Janela
      second_p_p = second_p[0],second_p[1]-self.comodo.eT/3
      
      points = first_p,second_p
      pointss = first_p_p,second_p_p
      self.canvas.create_rectangle(points,fill='white',tag = self.generate_random())
      self.canvas.create_rectangle(pointss,fill='white',tag = self.generate_random())
  
  def create_bottom_window(self):
      first_p = self.comodo.botton_m[0]-(self.dim/2),self.comodo.botton_m[1]-(self.comodo.eB/2)  # Primeiro ponto da Janela
      second_p = first_p[0]+self.dim, first_p[1]+(self.comodo.eB)
      first_p_p = first_p[0],first_p[1]+self.comodo.eB/3 #Primeiro Ponto do rentangulo interno da Janela
      second_p_p = second_p[0],second_p[1]-self.comodo.eB/3
      
      points = first_p,second_p
      pointss = first_p_p,second_p_p
      self.canvas.create_rectangle(points,fill='white',tag = self.generate_random())
      self.canvas.create_rectangle(pointss,fill='white',tag = self.generate_random())

  def generate_random(self):
    ##TODO: GENERATE WINDOW ID
      rd = str(random())
      return rd
  