from turtle import *

#set
penup()
right(90)
forward(180)
right(90)
forward(15)
left(180)
pendown()

#circle
color("black", "red")
begin_fill()
circle(90)
end_fill()

#set
penup()
forward(15)
pendown()

#set
right(90)
penup()
forward(20)
pendown()
left(90)

#bottom
color("black", "#BC4A3C")
begin_fill()
forward(300)
right(90)
forward(30)
right(90)
forward(600)
right(90)
forward(30)
right(90)
forward(300)
end_fill()

#middle
color("black", "gray")
begin_fill()
right(180)
forward(80)
right(90)
forward(200)
left(10)
forward(100)
right(100)
forward(160)
right(100)
forward(100)
left(10)
forward(200)
right(90)
forward(15)
right(90)
forward(200)
right(10)
forward(85)
left(100)
forward(55)
left(90)
forward(284)
right(90)
forward(15)
right(90)
forward(284)
left(90)
forward(55)
left(100)
forward(85)
right(10)
forward(200)
end_fill()

#left
color("black", "gray")
begin_fill()
right(90)
forward(15)
forward(150)
right(90)
forward(200)
right(90)
forward(80)
right(90)
forward(200)
right(90)
forward(15)
right(90)
forward(185)
left(90)
forward(50)
left(90)
forward(185)
end_fill()

#right
color("black", "gray")
begin_fill()
left(90)
forward(260)
forward(150)
left(90)
forward(200)
left(90)
forward(80)
left(90)
forward(200)
left(90)
forward(15)
left(90)
forward(185)
right(90)
forward(50)
right(90)
forward(185)
end_fill()

done()