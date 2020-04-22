# PythonDraw.py
# drawing 1
import turtle
turtle.setup(800, 450, 100, 100)
turtle.penup()
turtle.fd(-200)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
# drawing 2
import turtle as tt
tt.clearscreen()
tt.penup()
tt.goto(0, 0)
tt.pencolor("blue")
tt.pensize(10)
tt.pendown()
tt.goto(100, 100)
tt.goto(100, -100)
tt.goto(-100, -100)
tt.goto(-100, 100)
tt.goto(0, 0)
# drawing 3
from turtle import *
clearscreen()
colormode(255)
color(57, 197, 187)
left(45)
fd(150)
right(135)
fd(300)
left(135)
fd(150)
turtle.done()
