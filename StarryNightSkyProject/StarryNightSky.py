

############################
#  PSEUDO CODE FOR PROJECT
############################

#  PURPOSE: To create a a starry night sky background which is represented
#           as a black background with white dots.

#  METHOD: Using Python Turtle we will use a for loop to iteratively 
#          generate a 100 filled circles (dots) of random size and 
#          position against a black background


# START

# set background to BLACK

# repeat the following sequence 100 times

#   Generate random star position
#   Generate random star size
#   Draw the star

# END

#######################
#######################

# import turtle library 
from turtle import *

#import random library
from random import *

#set background color to black
bgcolor("black")

#hiding turtle
hideturtle()

#increase speed
speed(0)

#setting variables to the height and width of graphic window
width = window_width()
height = window_height()

# function to draw "star" (white filled circle) given an x,y position
def draw_star(x_pos, y_pos):
    #generate random number 2-20
    size= randrange(2,20) 
    
    #lift pen
    penup() 
    
    #takes turtle to specific x,y position
    goto(x_pos, y_pos) 
    
    #place pen
    pendown() 
    
    #drawing filled circle diameter "size" px color white
    dot(size,"white") 

#randomly positioning 100 stars
for x in range(100):
    #random x position (rounding to integer value)
    x_pos = randrange(round(-width/2), round(width/2)) # dividing by 2 to cover negative values
    
    #random x position (rounding to integer value)
    y_pos = randrange(round(-height/2), round(height/2)) # dividing by 2 to cover negative values
    
    #drawing star
    draw_star(x_pos, y_pos)

#keep graphic window open
done()