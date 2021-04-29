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
# turtle.setheading(90)

# TURTLES
grass = turtle.Turtle()
grass.hideturtle()
blade = turtle.Turtle()
blade.hideturtle()
tree = turtle.Turtle()
tree.hideturtle()
fern = turtle.Turtle()
fern.hideturtle()

# GLOBAL VARIABLES
trees = range(5)
minsize = 5
rand_value = random.randint(0,1)
rand_pensize = random.randint(1,3)
grass_colors = [(117, 156, 114),(105, 163, 101),(134, 173, 132),(151, 168, 123)]

# CLASSES

# class Forest():
        
# FUNCTIONS 

# draws little tufts of grass at random locations throughout the landscape
def drawGrass(turtle,numGrass,length):
    turtle.hideturtle()
    for i in range(numGrass):
        turtle.setheading(90)
        turtle.color(random.choice(grass_colors))
        turtle.penup()
        turtle.goto((random.randint(-290,290)),(random.randint(-290,290)))
        turtle.pensize(random.randint(1,3))
        turtle.pendown()
        turtle.forward(length)
        turtle.penup()
        
        if rand_value == 0:
            turtle.left(90)
            turtle.forward(random.randint(5,10))
            turtle.left(90)
            turtle.pendown()
            turtle.forward(length/2)
        else:
            turtle.right(90)
            turtle.forward(random.randint(5,10))
            turtle.right(90)
            turtle.pendown()
            turtle.forward(length/2)
    turtle.penup()
    
# draws a tree that is slightly leaning to one side (----- NOT WORKING -----)
def drawTree(turtle,length):
    turtle.color(99,96,86)
    if length > 2:
        turtle.width(length/10)
        turtle.forward(length)
        turtle.right(60)
        drawTree(turtle,length/2)
        turtle.left(60)
        turtle.width(length/10)
        turtle.forward(length/2)
        turtle.left(60)
        drawTree(turtle, 2 * length / 3)
        turtle.left(10)
        turtle.penup()
        turtle.width(length/10)
        turtle.backward(3 * length / 2)
        turtle.pendown()


# draws a tree with random sized branches and no leaves 
# some code used from https://www.codheadz.com/2019/06/30/Trees-with-Turtle-in-Python/
def drawNoleaves(turtle, length):
    turtle.hideturtle()
    turtle.pensize(rand_pensize)
    if (length > minsize):
        turtle.color(92,67,58)
        turtle.forward(length)
        turtle.right(25)
        drawNoleaves(tree, length - random.randint(1,15))
        turtle.left(50)
        drawNoleaves(tree, length - random.randint(1,15))
        turtle.right(25)
        turtle.backward(length)
        
# draws a randomly sized bush
def drawBush(turtle, size):
    turtle.hideturtle()
    
    
     
        
# draws multiple trees across the landscape (----- NOT WORKING ----)
# def drawMultitree(turtle):
#     for i in trees:
#         turtle.goto((random.randint(-250,250),(random.randint(-250,250)))
#         drawNoleaves(tree, random.randint(30,35))
        
    


# CALL FUNCTIONS

drawGrass(grass,random.randint(70,100),random.randint(8,12))

tree.left(90)
drawNoleaves(tree,random.randint(30,35))

panel.listen()
panel.mainloop()

turtle.done()