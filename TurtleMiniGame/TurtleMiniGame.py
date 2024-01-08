############################
#  PSEUDO CODE FOR PROJECT
############################

#  PURPOSE: To create a mini game with the object of moving a turtle 
#           from the beach to the ocean

#  METHOD: Using Python Turtle create a "beach" (orange background),
#          an ocean (blue background), and a turtle that can be moved
#          using the arrow keys. Once the turtle reaches the ocean the 
#          the figure will disappear and a message will appear on the 
#          screen saying "YOU WIN!"
#          
# START

# set background to ORANGE

# draw the ocean
# move the turtle to starting position 

# if MOVE key is pressed
#   move the turtle in that direction

# if the goal is reached
#    hide the turtle 
#    disable the controls 
#    Write "YOU WIN!" on screen

# END 

#######################
#######################

# import turtle library
from turtle import *

# speeding up animation
# speed(0)

# setting move distance for turtle
move_distance = 20

# setting background to beach color (dark orange)
bgcolor("#D2691E")

penup()
goto(100, 200)
pendown()

# setting ocean color
color("blue")

# drawing ocean borders
begin_fill()
goto(300, 200)
goto(300, -200)
goto(100, -200)
goto(100, 200)
end_fill()

# setting character in position
penup()
goto(-200, 0)

# creating turtle character
shape("turtle")
color("green")

# function rotate turtle and move up 20 pixels 
def move_up():
    # used to rotate to account for not knowing orientation
    setheading(90) 

    # move forward
    forward(move_distance)

    #checking if game is won
    check_goal() 


# function to rotate turtle and move down 20 pixels 
def move_down():
    # used to rotate to account for not knowing orientation
    setheading(270) 
    
    # move forward  
    forward(move_distance)
 
    #checking if game is won
    check_goal() 

#  function to rotate turtle and move left 20 pixels    
def move_left():
     # used to rotate to account for not knowing orientation
    setheading(180)

    #  move forward 
    forward(move_distance)

    #checking if game is won
    check_goal() 
    

# function to rotate turtle and move down 20 pixels 
def move_right():
    # used to rotate to account for not knowing orientation
    setheading(0)

    # move forward 
    forward(move_distance)

    #checking if game is won
    check_goal() 

# checking if goal is acheived based on x coordinate
def check_goal():
    #if x coordinate greater than 100
    if xcor() > 100: 
        hideturtle()
        color("white")
        write("YOU WIN!")

        # disable key binds
        onkey(None, "Up")
        onkey(None, "Down")
        onkey(None, "Left")
        onkey(None, "Right")

onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")

listen()

# keeping graphic window open 
done()