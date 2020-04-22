# PythonDraw.py
import turtle
turtle.setup(1050, 350, 200, 200)
turtle.penup()
turtle.fd(-450)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
# turtle.penup()
turtle.fd(40)
# turtle.pendown()
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()
