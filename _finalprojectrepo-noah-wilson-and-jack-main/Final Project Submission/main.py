import turtle, random, time, Noah, Wilson,Jack
turtle.colormode(255)
turtle.tracer(0)
"""
Created on December 6th, 2020
@authors: Noah Hubbard, Wilson Seet, and Jack Pudlo

DESCRIPTION: 
Generative art gallery that draws 3 uniquue pieces of art on key press. The  pieces include a randomly generated forest, a winter/snow scene, and a rainy day in front of some mountains.
"""
# ===========GLOBAL VAR===============
panel=turtle.Screen()
w=600
h=600
turtle.setup(w,h)
# =============CLASSES=============
class Manager:
  def __init__(self):
    global N, W, J, J1
    panel.register_shape('Splash_Screen.gif')
    panel.register_shape('snowflake.gif')
    panel.register_shape('sky.gif')
    panel.register_shape('assembled grass.gif')
    panel.register_shape('source.gif')
    panel.register_shape('lightning.gif')
    
    self.makesplashTurt = turtle.Turtle()
    N = Noah.setUp()
    W = Wilson.Everything()
    J = Jack.Grass()
    J1 = Jack.Tree()
    
#=========key Presses==================
    panel.onkeypress(self.Noah,"1")
    panel.onkeypress(self.Wilson,"2")
    panel.onkeypress(self.Jack,"3")

    self.drawSplash()

  def reSet(self):
    """
    Since all of these settings go away when you call panel.clear() this method reset all of these so that the code can run smoothly
    """
    turtle.colormode(255)
    turtle.tracer(0)
    panel.onkeypress(self.Noah,"1")
    panel.onkeypress(self.Wilson,"2")
    panel.onkeypress(self.Jack,"3")

  def drawSplash(self):
    """
    This method creates the splash screen for the gallery
    """
    self.makesplashTurt.shape('Splash_Screen.gif')
    panel.update()

  def Noah(self): 
    """On key press this method draws Noah's code"""
    panel.clear()
    self.reSet()
    W.done = True
    
    self.makesplashTurt.shape("circle")
    self.makesplashTurt.color(153,208,242)
    self.makesplashTurt.goto(-300,300)
    self.makesplashTurt.turtlesize(1)
    self.makesplashTurt.down()
    self.makesplashTurt.begin_fill()
    
    N.Turts = [] # This line ensures that the list of snowflakes is empty. When going back and forth between pieces it can cause issues if there are residual snowflakes in the list

    for i in range(4):#This draws the backgroundcolor
      self.makesplashTurt.forward(600)
      self.makesplashTurt.right(90)
    self.makesplashTurt.end_fill()    
    self.makesplashTurt.up()

    N.running = True
    N.newBack()
    N.makeTurts()
    N.Run()
    
  def Wilson(self):
    """On key press this draws Noah's code"""
    print("in Wilson")
    panel.clear()
    self.reSet()
    N.running = False
    
    W.done = False
    W.rain = []

    self.makesplashTurt.shape("sky.gif")
    self.makesplashTurt.showturtle()
    self.makesplashTurt.goto(0,0)
    self.makesplashTurt.stamp()
    panel.update()
  

    W.draw1()
    W.draw2()
    W.draw3()
    W.drawTheGrass()
    W.drawAnimals()
    W.drawLightning()
    W.drawRain()
  
  """"
  This method calls the Grass and Tree objects to draw a 
  forest
  """
  def Jack(self):
    panel.clear()
    self.reSet()
    N.running = False
    W.done = True
    
    self.makesplashTurt.shape("circle")
    self.makesplashTurt.color(random.choice(J.bgcolors))
    self.makesplashTurt.goto(-300,300)
    self.makesplashTurt.turtlesize(1)
    self.makesplashTurt.down()
    self.makesplashTurt.begin_fill()
    for i in range(4):#This draws the backgroundcolor
      self.makesplashTurt.forward(600)
      self.makesplashTurt.right(90)
    self.makesplashTurt.end_fill()    
    self.makesplashTurt.up()

    J.drawGrass(90,8)
    panel.update()
    J1.call()
    
    print("jacks done")
    panel.update()


Gallery = Manager()

panel.listen() #needed for key presses
panel.mainloop() #keep listeners on
turtle.done() 