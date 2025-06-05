from turtle import *

# Start of G
width(5)
color("black")
begin_fill()

penup()
goto(-200,0)
pendown()

forward(100)
right(270)
forward(100)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(120)
right(90)
forward(100)
left(90)
forward(50)
left(90)
forward(150)
left(90)
forward(220)
left(90)
forward(100)

end_fill()
# End of G

# Start of O

width(5)
color("dark green")

begin_fill()

penup()
goto(-50,0)
pendown()

forward(170)
left(90)
forward(220)
left(90)
forward(170)
left(90)
forward(220)

end_fill()

penup()
goto(-10,35)
pendown()

width(5)
color("white")

begin_fill()

left(90)
forward(80)
left(90)
forward(140)
left(90)
forward(90)
left(90)
forward(140)

end_fill()

# End of O

exitonclick()