"""
Created on Fri Nov 20 11:45:08 2020

@author: Noah Hubbard

This stops when the snowflake gets to the ground but the while loop continues to run which
bogs down the script
"""

import turtle, random, time
turtle.colormode(255)
turtle.tracer(0)
turtle.bgcolor(153,208,242)

w=600
h=600
turtle.setup(w,h) # start with calling setup to turn on listeners
# sets the window size up here

# define variables here
panel=turtle.Screen()  # make a window using the setup info
panel.register_shape('snowflake.gif')


# ========== YOU CODE BELOW HERE ===============

numSnow=15


class setUp():
    def __init__(self):
        self.Turts = []
        self.heading=270
        self.size=5
        self.colors=[(2,56,89),(5,74,89),(53,124,140),(137,207,217),(242,242,242),(50,71,89)]
        self.backgroundTurts =[]
    def backGround(self):
        numballs=random.randint(5,15)
        for i in range(numballs):
            self.backgroundTurts.append(turtle.Turtle())
            self.backgroundTurts[i].hideturtle()
            self.backgroundTurts[i].up()
            self.backgroundTurts[i].shape('circle')
            self.backgroundTurts[i].color(random.choice(self.colors))
            self.backgroundTurts[i].turtlesize(random.randint(15,20))
            self.backgroundTurts[i].goto(random.randint(-280,280),random.randint(-200,-150))
            self.backgroundTurts[i].showturtle()
            panel.update()
    def createTurt(self,i):
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
        time.sleep(.005)
        forward=3.2
        self.Turts[selected].forward(forward)
        panel.update()
def isCollision(turt,target,i,buffer=30):
    '''Detects collision with an object or list of objects.
    turt is the main object 
    target = the collision target (can be turtle or list of turtles)
    buffer = area surrounding turt center that counts as a collision. Default value is 30 pixels.
    Returns true or false statement if the two items have collided. This code was taken from Dr.Z's
    helpful code repo'''
    target = target[:]
    x = turt.xcor()
    y = turt.ycor()
    if type(target)==list:
        # If it's a list, step through each value and check
        if turt in target: #is the turtle we're colliding in the list?
            idx = target.index(turt) # find out where it is
            target.pop(idx) # remove it (just for the function)
        for i in range(len(target)):
            targX = target[i].xcor()
            targY = target[i].ycor()
            if round(targX)-buffer<=round(x)<=round(targX)+buffer and round(targY)-buffer<=round(y)<=round(targY)+buffer:
                print("True")
                return True
            else:
                print("False")
                return False
"""
allObj = panel.turtles()
(assumes class makes one object, and self.turt is the turtle object that does all the drawing) allObj.remove(self.turt)
self.isCollision(self.turt,allObj)
each class should make 1 snowflake object,
movement methods move by STEP not by full movement
first create list of all turtles on panel:
allObj = panel.turtles()
allObj.remove(self.turt)
collide = self.isCollision(self.turt,allObj)


put the iscolision into code (cite) remove the drawing turtle from the panel
"""

animation = setUp()
for i in range(numSnow):    
    animation.createTurt(i)
animation.backGround()
panel.update() 
    
for i in range(190):
    for k in range(len(animation.Turts)):
        y = animation.Turts[k].ycor()
        if isCollision(animation.Turts[k],animation.Turts,50) or y <= -265:
            continue
        else:
            animation.falling(k)
        
        





panel.mainloop() #keeps listeners on so we can get interactivity\
turtle.done() # turtle clean up
