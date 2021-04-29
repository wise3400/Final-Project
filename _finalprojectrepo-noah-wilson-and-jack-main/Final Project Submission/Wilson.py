import turtle, random, time
""""
DESCRIPTION:
This code draws random rain drops, a different altitiude of
the 3 mountains, a stormy sky, a flat land, and finally some stormy skies! A lightning is there just for looks!
"""
#=================================================
"""" 
A class that draws 3 mountains, grass, elephant,
lightning, and rain.
"""
class Everything():
  def __init__(self):
    self.rain = [] 
    self.numRain = 50
    self.yCor = 300 
    self.panel = turtle.Screen()
    self.done = False 
    print("done")
#Mountain 1
  def draw1(self):
    self.mountTurt1 = turtle.Turtle()
    self.mountTurt1.speed(-10)
    self.mountTurt1.hideturtle()
    self.mountTurt1.up()
    self.mountTurt1.goto(-100,-100)
    self.mountTurt1.down()
    self.mountTurt1.color("dimgray")
    self.mountTurt1.begin_fill()
    for i in range(3):
      self.mountTurt1.forward(280)
      self.mountTurt1.left(120)
    self.mountTurt1.end_fill()
    self.panel.update()
#Mountain2
  def draw2(self):
    self.mountTurt2 = turtle.Turtle()
    self.mountTurt2.speed(-10)
    self.mountTurt2.up()
    self.mountTurt2.goto(-310,-100)
    self.mountTurt2.down()
    self.mountTurt2.color("gray")
    self.mountTurt2.begin_fill()
    for i in range(3):
      self.mountTurt2.forward(330)
      self.mountTurt2.left(120)
    self.mountTurt2.end_fill()
    self.panel.update()
#Mountain 3
  def draw3(self):
    self.mountTurt3 = turtle.Turtle()
    self.mountTurt3.speed(-10)
    self.mountTurt3.up()
    self.mountTurt3.goto(70,-100)
    self.mountTurt3.down()
    self.mountTurt3.color("dark gray")
    self.mountTurt3.begin_fill()
    for i in range(3):
      self.mountTurt3.forward(280)
      self.mountTurt3.left(120)
    self.mountTurt3.end_fill()
    self.panel.update()
#Draw Grass
  def drawTheGrass(self):
    self.makegrass = turtle.Turtle()
    self.makegrass.speed(-10)
    self.makegrass.up()
    self.panel.register_shape("assembled grass.gif")
    self.makegrass.shape("assembled grass.gif")
    self.makegrass.goto(70,-290)
    self.panel.update()
#Draw an elephant
  def drawAnimals(self):
    self.makeAnimals = turtle.Turtle()
    self.makeAnimals.speed(-10)
    self.makeAnimals.up()
    self.panel.register_shape("source.gif")
    self.makeAnimals.shape("source.gif")
    self.makeAnimals.goto(10,-130)
    self.panel.update()
#Draw lightning 
  def drawLightning(self):
      self.makeLightning = turtle.Turtle()
      self.makeLightning.speed(-10)
      self.makeLightning.up()
      self.panel.register_shape("lightning.gif")
      self.makeLightning.shape("lightning.gif")
      self.makeLightning.goto(20,240)
      self.panel.update()
#Draws rain drops using a for loop and while loop so it keeps repeating over and over again and go back up to the top again.
  def drawRain(self):
    for i in range(self.numRain):
      self.rain.append(turtle.Turtle())
      self.rain[i].up()
      self.rain[i].speed(-10)
      self.rain[i].setheading(270)
      self.rain[i].color("lightblue")
      self.rain[i].shape('circle') 
      self.rain[i].turtlesize(0.3,1) #Size of rain drops
      self.rain[i].goto(random.randint(-300,300), random.randint(-300,300))
      self.rain[i].showturtle()
      self.panel.update()
    while not self.done:
      print("raining")
      for i in range(self.numRain):
        self.y = self.rain[i].ycor()
        if self.y < -310:
           self.rain[i].goto(random.randint(-300,300),300)
        down = 65 #Speed of rain drops
        self.rain[i].forward(down)
        self.panel.update()