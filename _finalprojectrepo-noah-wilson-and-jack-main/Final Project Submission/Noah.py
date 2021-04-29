import turtle, random, time
""""
DESCRIPTION:
This code creates a random winter scene using Turtle.
First a background is drawn using large circles to simulate
rolling hills. These circles are random both in their size, color, and
location. The snowflakes are also randomly generated and placed in random spots around the screen. As the snow comes down they accumulate on the ground. 
"""
#================Class========================
class setUp():
    def __init__(self):
        self.panel = turtle.Screen()
        self.Turts = []
        self.heading=270
        self.size=5
        self.colors=[(2,56,89),(5,74,89),(53,124,140),(137,207,217),(242,242,242),(50,71,89)]
        self.backgroundTurts =[]
        self.yCors = []
        self.xCors = []
        self.letitSnow = True
        self.numSnow = 15
        self.running = True
    def newBack(self):
      """"
      This method randomly draws the background which the scene will take place on top of
      """
      numballs = random.randint(5,15)
      colors=[(2,56,89),(5,74,89),(53,124,140),(137,207,217),(242,242,242),(50,71,89)]
      drawBackground = turtle.Turtle()
      drawBackground.hideturtle()
      drawBackground.up()
      for i in range(numballs):
            randoX = random.randint(-280,280)
            randoY = random.randint(-400,-350)
            drawBackground.goto(randoX,randoY)
            drawBackground.color(random.choice(colors))
            drawBackground.down()
            drawBackground.begin_fill()
            drawBackground.circle(random.randint(150,200))
            drawBackground.end_fill()
            drawBackground.up()
    def createTurt(self,i):
      """"
      This method creates the Turtles that will become snowflakes and slowly fall from the sky.
      """
      self.Turts.append(turtle.Turtle())
      self.Turts[i].hideturtle()
      self.Turts[i].up()
      self.Turts[i].setheading(self.heading)
      self.Turts[i].shape('snowflake.gif')
      self.Turts[i].turtlesize(self.size)
      self.Turts[i].color("lightblue")
      self.Turts[i].goto(random.randint(-280,280),random.randint(-280,280))
      self.Turts[i].showturtle()
    def falling(self,selected):
      """
      this method is called to make the snowflakes 'fall' to the ground
      """
      time.sleep(.0001)
      forward=6
      self.Turts[selected].forward(forward)
      self.panel.update()
      """"
      The next two checkrange methods work as 'checks' to see if a snowflake is colliding into another snowflake by adding the cordinate to a list and seeing if there are any collisions
      """   
    def checkRangeY(self,val1,val2,buffer):
        for v in val2:
            if val1-buffer < v < val1+buffer:
                return True
        else:
            return False
        
    def checkRangeX(self,val1,val2,buffer):
        for v in val2:
            if val1-buffer < v < val1+buffer:
                return True
        else:
            return False
    def makeTurts(self,numSnow=30):
    #This method actually creates the turtles by calling the createTurt method
        for i in range(numSnow):    
            self.createTurt(i)
    def Run(self):
      #This is where all of the methods are called through a large for loop which checks for collisons, makes new turtles, and all that good stuff
        for i in range(1000):
            if not self.running:
              break
            for k in range(len(self.Turts)):
                y = self.Turts[k].ycor()
                """
                If the turtle is the first one to be on the ground in a certain spot
                add that spot to the list
                """
                if  y <= -265:
                    if round(self.Turts[k].ycor()) in self.yCors and round(self.Turts[k].xcor()) in self.xCors:
                        continue
                    else:
                        self.yCors.append(round(self.Turts[k].ycor()))
                        self.xCors.append(round(self.Turts[k].xcor()))
                        continue
                #if the turtle is hitting any of the y-cordinates in the yCors and xCors lists
                #then add those the iterated turtle's cordinates into the list
                elif self.checkRangeY(self.Turts[k].ycor(),self.yCors,10) and self.checkRangeX(self.Turts[k].xcor(),self.xCors,7):
                    self.yCors.append(round(self.Turts[k].ycor()))
                    self.xCors.append(round(self.Turts[k].xcor()))
              
                else:
                    self.falling(k)
            if not self.letitSnow:
                newturt =self.Turts[1].clone()
                self.Turts.append(newturt)
                newturt.goto(random.randint(-280,280),random.randint(265,285))
                self.letitSnow = not self.letitSnow
            else:
                self.letitSnow = not self.letitSnow