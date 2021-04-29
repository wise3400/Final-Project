import turtle, random, time


import pygame
pygame.mixer.init()

 
panel=turtle.Screen()
turtle.colormode(255)
turtle.tracer(0)
w=600
h=600
#Bacground Image
image = "Unknown.gif"
turtle.bgpic(image)
turtle.addshape(image)
turtle.setup(w,h)

#Sound of Thunder


pygame.mixer.music.load("thunder_thunder.wav")
pygame.mixer.music.play()
 

#pygame.mixer.music.stop()

#=================================================
class DrawLandscaping():
  def __init__(self):
    self.mountTurt1 = turtle.Turtle()
    self.mountTurt2 = turtle.Turtle()
    self.mountTurt3 = turtle.Turtle()
#Mountain 1
  def draw(self):
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
#Mountain2
  def draw2(self):
    self.mountTurt2.up()
    self.mountTurt2.goto(-310,-100)
    self.mountTurt2.down()
    self.mountTurt2.color("gray")
    self.mountTurt2.begin_fill()
    for i in range(3):
      self.mountTurt2.forward(330)
      self.mountTurt2.left(120)
    self.mountTurt2.end_fill()
#Mountain 3
  def draw3(self):
    self.mountTurt3.up()
    self.mountTurt3.goto(70,-100)
    self.mountTurt3.down()
    self.mountTurt3.color("dark gray")
    self.mountTurt3.begin_fill()
    for i in range(3):
      self.mountTurt3.forward(280)
      self.mountTurt3.left(120)
    self.mountTurt3.end_fill()

#Grass 
class drawGrass():
  def __init__(self):
    self.land_image = "assembled grass.gif"
    self.makegrass = turtle.Turtle()
  def drawTheGrass(self):
    self.makegrass.up()
    panel.addshape(self.land_image)
    self.makegrass.shape(self.land_image)
    self.makegrass.goto(70,-290)

#Rain
#Description:
  def drawRain(self):
    rain = []
    numRain = 50
    y = 300
    for i in range(numRain):
      rain.append(turtle.Turtle())
      rain[i].up()
      rain[i].setheading(270)
      rain[i].color("darkblue")
      rain[i].shape('circle') 
      rain[i].turtlesize(0.3) #Size of rain drops
      rain[i].goto(random.randint(-300,300), random.randint(-300,300))
      rain[i].showturtle()
      

    done = False
    while (done==False):
      for i in range(numRain):
        y = rain[i].ycor()
        if y < -310:
           rain[i].goto(random.randint(-300,300),300)
        down = 50 #Speed of rain drops
        rain[i].forward(down)
        
        panel.update()

#Click Flower!








#Call Mountain
mountain = DrawLandscaping()
mountain.draw()
mountain.draw2()
mountain.draw3()

#Call Grass
land = drawGrass()
land.drawTheGrass()

#Call Rain
land.drawRain()

#Call Flower


panel.listen() #needed for key presses
panel.mainloop() #keep listeners on
turtle.done()