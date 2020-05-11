# DigitTubeDraw.py
import turtle
import time
def drawLine(draw, pen):
    pen.pendown() if draw else pen.penup()
    pen.fd(40)
    pen.right(90)
def drawDigit(digit, pen):
    drawLine(True, pen) if digit in [2,3,4,5,6,8,9] else drawLine(False, pen)
    drawLine(True, pen) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False, pen)
    drawLine(True, pen) if digit in [0,2,3,5,6,8,9] else drawLine(False, pen)
    drawLine(True, pen) if digit in [0,2,6,8] else drawLine(False, pen)
    pen.left(90)
    drawLine(True, pen) if digit in [0,4,5,6,8,9] else drawLine(False, pen)
    drawLine(True, pen) if digit in [0,2,3,5,6,7,8,9] else drawLine(False, pen)
    drawLine(True, pen) if digit in [0,1,2,3,4,7,8,9] else drawLine(False, pen)
    pen.left(180)
    pen.penup()
    pen.fd(20)
def drawDate(date, pen):
    for i in date:
        drawDigit(eval(i), pen)

def main():
    turtle.setup(800, 350, 200, 200)
    penA = turtle.Pen()
    penA.speed(0)
    penA.hideturtle()
    while(True):       
        # penB = turtle.Pen()
        # penC = turtle.Pen()
        
        penA.speed(0)
        penA.penup()
        penA.fd(-300)
        penA.pensize(5)
        now = time.localtime()
        turtle.tracer(0)
        drawDate(time.strftime("%H", now), penA)
        drawDate(time.strftime("%M", now), penA)
        drawDate(time.strftime("%S", now), penA)
        # turtle.hideturtle()
        # turtle.done()
        # time.sleep(2)
        if time.localtime() == now:
            continue
        penA.reset()
        penA.hideturtle()

main()

