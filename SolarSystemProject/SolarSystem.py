

############################
#  PSEUDO CODE FOR PROJECT
############################

#  PURPOSE: To draw the the sun and three planets using
#           Python turtle

#  METHOD:  Four circles of various distances and radii
#           will be drawn using the Python turtle library 


# START


#   set background color to BLACK 
#   set turtle  color to ORANGE

#   FIRST PLANET 

#   begin fil
#   draw circle 60px radius 
#   end fille 

#   pen up
#   move forwards 100px 
#   pen down 

#   SECOND PLANET 

#   set turtle color to GRAY 

#   begin fill
#   draw circle 20px radius
#   end fill

#   pen up
#   move forwards 80px
#   pen down 

#   THIRD PLANET

#   set turtle color to RED 

#   begin fill
#   draw circle 40px radius 
#   end fill

#   pen up 
#   move forwards 90px 
#   pen down 

#   FOURTH PLANET 

#   set turtle color to GREEN

#   begin fill
#   draw circle 30px radius 
#   end fill 


#   END

#######################
#######################

#import turtle library 
from turtle import *

# used to setup the screen for the live coding
Screen().setup(800, 500)

#speed up animation
speed(0)

#background color 
bgcolor("black")

#turtle color 
color("orange")

# filled circle of x radius
begin_fill()
circle(60)
end_fill()

#moving forward no line
penup()
forward(100)
pendown()

#turtle color
color("gray")

# filled circle of x radius
begin_fill()
circle(20)
end_fill()

#moving forward no line
penup()
forward(80)
pendown()

#turtle color 
color("red")

# filled circle of x radius
begin_fill()
circle(40)
end_fill()

#moving forward no line
penup()
forward(90)
pendown()

#turtle color 
color("green")

# filled circle of x radius
begin_fill()
circle(30)
end_fill()

#prevents window from closing 
done()

#CONCLUSION: We draw the sun and three planets using
#           Python turtle. These four objects are represented
#           by four filled circles varying in distance and 
#           radii. 



