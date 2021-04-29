#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:54:58 2020

@author: Jack Pudlo
"""

# LIBRARIES
import turtle, random, time
turtle.colormode(255)
turtle.bgcolor(190,219,167)
turtle.tracer(10)

# PANEL
w=600
h=600
turtle.setup(w,h)
panel=turtle.Screen()
turtle.setheading(90)

# GLOBAL VARIABLES


# CLASSES

class Forest():
        
    def __init__(self):
        
        self.grass = turtle.Turtle()
        self.blade = turtle.Turtle()
        self.tree = turtle.Turtle()
        self.fern = turtle.Turtle()
        
        self.trees = range(5)
        self.minsize = 5
        self.rand_pensize = random.randint(1,3)
        self.grass_colors = [(117, 156, 114),(105, 163, 101),(134, 173, 132),(151, 168, 123)]
        self.randvalue = random.randint(0,1)
        
    # draws little tufts of grass at random locations throughout the landscape
        def drawGrass(self,turtle,numGrass,length):
            turtle.hideturtle()
            for i in range(numGrass):
                self.turtle.setheading(90)
                self.turtle.color(random.choice(self.grass_colors))
                self.turtle.penup()
                self.turtle.goto((random.randint(-290,290)),(random.randint(-290,290)))
                self.turtle.pensize(random.randint(1,3))
                self.turtle.pendown()
                self.turtle.forward(length)
                self.turtle.penup()
                
                if self.randvalue == 0:
                    self.turtle.left(90)
                    self.turtle.forward(random.randint(5,10))
                    self.turtle.left(90)
                    self.turtle.pendown()
                    self.turtle.forward(length/2)
                else:
                    self.turtle.right(90)
                    self.turtle.forward(random.randint(5,10))
                    self.turtle.right(90)
                    self.turtle.pendown()
                    self.turtle.forward(length/2)
            self.turtle.penup()
            
        # draws a tree that is slightly leaning to one side (----- NOT WORKING -----)
        def drawTree(self,turtle,length):
            self.turtle.color(99,96,86)
            if length > 2:
                self.turtle.width(length/10)
                self.turtle.forward(length)
                self.turtle.right(60)
                self.drawTree(turtle,length/2)
                self.turtle.left(60)
                self.turtle.width(length/10)
                self.turtle.forward(length/2)
                self.turtle.left(60)
                self.drawTree(turtle, 2 * length / 3)
                self.turtle.left(10)
                self.turtle.penup()
                self.turtle.width(length/10)
                self.turtle.backward(3 * length / 2)
                self.turtle.pendown()
        
        
        # draws a tree with random sized branches and no leaves 
        # some code used from https://www.codheadz.com/2019/06/30/Trees-with-Turtle-in-Python/
        def drawNoleaves(self,turtle,length):
            self.turtle.hideturtle()
            self.turtle.pensize(self.rand_pensize)
            if (length > self.minsize):
                self.turtle.color(92,67,58)
                self.turtle.forward(length)
                self.turtle.right(25)
                self.drawNoleaves(self.tree, length - random.randint(1,15))
                self.turtle.left(50)
                self.drawNoleaves(self.tree, length - random.randint(1,15))
                self.turtle.right(25)
                self.turtle.backward(length)
                
        # draws a randomly sized bush
        def drawBush(self,turtle, size):
            self.turtle.hideturtle()
            
            
             
                
        # draws multiple trees across the landscape 
        # def drawMultitree(turtle):
        #     for i in trees:
        #         turtle.goto((random.randint(-250,250),(random.randint(-250,250)))
        #         drawNoleaves(tree, random.randint(30,35))
                
        


# CALL FUNCTIONS

forest = Forest()
forest.drawGrass()
forest.drawNoleaves()

panel.listen()
panel.mainloop()

turtle.done()