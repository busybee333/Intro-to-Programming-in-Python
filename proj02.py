# -*- coding: utf-8 -*-
 
    ###############################################################
    #  CSE 231 Project #2
    #
    #  Algorithm
    #    prompt for an integer
    #    input an integer
    #    draw and fill number of squares input inside of each other
    #    close turtle window
    ###############################################################

import turtle
import random

numsquares = int(input("How many squares? "))                                   #prompts user for number of squares
if numsquares <= 0:
    print("User Error: You must enter a positive non-zero number.")

squarewidth = 200/numsquares  

side=400                                                                        #sets max side length
turtle.penup()
turtle.goto(-200,-200)                                                          #Goes to/starts at bottom left corner of the square
turtle.pendown()

for i in range (1,(numsquares + 1)):                                            #Draws & fills the number of squares input by user
   turtle.color(random.random(),random.random(), random.random())               #Chooses random colors
   turtle.begin_fill() 
   turtle.forward(side)
   turtle.left(90)
   turtle.forward(side)
   turtle.left(90)
   turtle.forward(side)
   turtle.left(90)
   turtle.forward(side)
   turtle.left(90)
   turtle.end_fill()
   turtle.penup()
   turtle.forward(squarewidth)
   turtle.left(90)
   turtle.forward(squarewidth)
   turtle.right(90)
   turtle.pendown()
   side=side-(2*squarewidth)

turtle.bye()                                                                    #Closes turtle screen