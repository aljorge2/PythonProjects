

############################
#  PSEUDO CODE FOR PROJECT
############################

#  PURPOSE: To draw a balloon (red dot) that will increase in size every time the 
#           up arrow key is pressed. Once it reaches a certain size, it’ll pop 
#           (disappear) leaving behind a message (POP!)

#  METHOD:  Draw one circle (using Python turtle library) that increase is 
#           circumference when prompted by the up arrow key until a certain 
#           size when it will disappear and a message "POP!" will appear


# START

# Draw the balloon

# Has the key been pressed?
  
#   Has the balloon reached max size?
#       Clear the balloon
#       Write "POP!"
#   If not
#       Increase balloon size
#       Draw the balloon


# END

#######################
#######################

# import turtle library 
from turtle import *

#hiding turtle
hideturtle()

#set variables 
diameter = 40 #of balloon
pop_diameter = 100 #popping threshold

#function to draw balloon (red circle)
def draw_balloon():
    color("red") #color of balloon
    dot(diameter) #drawing filled circle (takes diameter instead of radius)

#function inflating balloon
def inflate_balloon():
    global diameter #allowing diameter to be modified
    diameter = diameter + 10 #increasing diameter
    draw_balloon()

#if diameter is greater than popDiameter
    if diameter >= pop_diameter:
        clear() #clears everything on screen
        diameter = 40 #resets diameter 
        write("POP!") #writes x on screen

#calling function to draw balloon
draw_balloon() 

#inflating balloon by pressing up key
onkey(inflate_balloon, "Up")
listen()

#prevent graphic window from closing
done()

# CONCLUSION: We drew a balloon represented as a red filled circle with
#              a starting diameter of 40 pixels that "inflated" 
#              (increased) in diameter by 10 pixels when the up arrow 
#              key was pressed. When the diameter reached 100 pixels
#              the balloon "popped" (disappeared) and a message appeared
#              saying "POP!". 

#              The baloon was drawn and inflated using functions and 
#              the balloon popped with an "if statement" 