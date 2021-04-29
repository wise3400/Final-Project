import turtle, random, time
""""
@author: Jack Pudlo

Description: This is one of three different generative nature settings in the gallery.
This particular setting is a forest that generates two different kinds of trees. The trees were
created from a recursive loop and are made of fractals that make up the branches and leaves.
The random library is used to make slight changes to the size of the branches to give more variety.
The random library is also used to change the color scheme of the forest after each run.

Fractal Tree inspired by: https://www.codheadz.com/2019/06/30/Trees-with-Turtle-in-Python/
"""
# BACKGROUND COLORS
bg_color = [(190,219,167),(149, 166, 136),(102, 105, 70),(145, 135, 108)]

# VARIABLES
numTrees = 6
numBigtrees = 3
length = 35
scale = random.uniform(0.6,0.8)
angle = random.randint(20,28)
size = length/10

#COLOR PALETTES
bigtree_colors = [(59, 57, 57),(28, 26, 26),(61, 58, 58)]
bigtree_leaf_colors = [(191, 146, 86),(184, 131, 61),(207, 163, 83),(237, 201, 102),(189, 163, 102)]
fractal_bark_colors = [(87,73,68),(82,32,13),(36, 15, 7),(84, 26, 4)]
fractal_leaf_colors = [(89, 135, 78),(111, 148, 102),(94, 122, 87)]

# GRASS CLASS

# draws little tufts of grass at random locations throughout the landscape
class Grass():
 
    def __init__(self):
        self.bgcolors = [(190,219,167),(149, 166, 136),(102, 105, 70),(145, 135, 108)]
        self.grass = turtle.Turtle()
        self.rand_value = random.randint(0,1)
        self.rand_pensize = random.randint(1,3)
        self.numGrass = 50
        self.length = 8
        self.grass_colors = [(117, 156, 114),(105, 163, 101),(134, 173, 132),(151, 168, 123),(196, 183, 118),(176, 161, 123),(159, 163, 104)]
    
    def drawGrass(self,numGrass,length):
        
        for i in range(self.numGrass):
            self.grass.hideturtle()
            self.grass.setheading(90)
            self.grass.color(random.choice(self.grass_colors))
            self.grass.penup()
            self.grass.goto((random.randint(-290,290)),(random.randint(-290,290)))
            self.grass.pensize(random.randint(1,3))
            self.grass.pendown()
            self.grass.forward(self.length)
            self.grass.penup()
            
            if self.rand_value == 0:
                self.grass.left(90)
                self.grass.forward(random.randint(5,10))
                self.grass.left(90)
                self.grass.pendown()
                self.grass.forward(self.length/2)
            else:
                self.grass.right(90)
                self.grass.forward(random.randint(5,10))
                self.grass.right(90)
                self.grass.pendown()
                self.grass.forward(self.length/2)
        self.grass.penup()


class Tree():
    def __init__(self):
        self.panel = turtle.Screen()

    # uses recursion to draw a group of trees created from fractals
    # ===== BUG ======
    # branches of fractal tree no longer get smaller

    def drawFractaltree(self,turt,length):
        turtle.pensize(size)
        
        # builds off of branches to make them smaller and smaller to a point 
        if length > 10:
            turtle.forward(length)
            turtle.left(angle)
            self.drawFractaltree(turt,length*scale)
            turtle.right(angle*2)
            self.drawFractaltree(turt,length*scale)
            turtle.left(angle)
            turtle.backward(length)
            
        # stamps leaves at the end of the branches 
        if length < 20:
            turtle.color(random.choice(fractal_leaf_colors))
            turtle.stamp()
            turtle.color(random.choice(fractal_bark_colors))
            
            
    # uses recursion to draw a tree that is slightly leaning to one side (also using fractals)
    def drawBigtree(self,turt,length):
        if length > 2:
            turtle.color(random.choice(bigtree_colors))
            turtle.width(length/10)
            turtle.forward(length)
            turtle.left(60)
            self.drawBigtree(turt,length/2)
            turtle.right(60)
            turtle.width(length/10)
            turtle.forward(length/2)
            turtle.right(60)
            self.drawBigtree(turt,length/2)
            turtle.left(70)
            self.drawBigtree(turt,2 * length/3)
            turtle.right(10)
            turtle.penup()
            turtle.width(length/10)
            turtle.backward(3 * length/2)
            turtle.pendown()
            
        # stamps leaves at the end of the branches 
        if length < 2:
            turtle.color(random.choice(bigtree_leaf_colors))
            turtle.stamp()
            turtle.color(random.choice(bigtree_colors))
        
    
    # CALL FUNCTIONS
    def call(self):
        for i in range(numBigtrees):
            turtle.setheading(90)
            turtle.hideturtle()
            turtle.color(random.choice(bigtree_colors))
            turtle.penup()
            turtle.goto((random.randint(-280,280)),(random.randint(-280,280)))
            turtle.pendown()
            self.drawBigtree(i,140)
            print("big trees")
            self.panel.update()
               
        for i in range(numTrees):
            turtle.setheading(90)
            turtle.color(random.choice(fractal_bark_colors))
            turtle.penup()
            turtle.goto((random.randint(-280,280)),(random.randint(-280,280)))
            turtle.pendown()
            self.drawFractaltree(i,80)
            print("fractal tree")
            self.panel.update()