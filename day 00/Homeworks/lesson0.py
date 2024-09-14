from turtle import *

#we want to paint a house

#step 1:  draw a square

width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("green")
begin_fill()
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(120)
forward(115)
left(60)
forward(115)
end_fill()


#we want drawing window

color("blue")
left(60)
forward(20)
color("yellow")
begin_fill()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

color("blue")
forward(20)
right(90)
color("red")
forward(200)
right(90)
color("blue")
forward(20)
color("yellow")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
exitonclick()