import turtle
import math

def drawFiveCircles(turt,radius,centerX,centerY):
    """this function draws five circles, it starts each turtle at a spot centerX, centerY, and gives it a certain radius."""
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

def drawCenterCircles(turt,centerX, centerY):
    """This function draws the smaller cicles on each flower"""
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()

def drawBee(turt, centerX, centerY):
    """This function places the stamp in the middle of each flower"""
    turt.up()
    turt.goto(centerX, centerY)
    stampTurtle.down()
    stampTurtle.stamp()

def drawflower(sepalTurtle,petalTurtle,centerTurtle,stampTurtle, centerX, centerY):
    drawFiveCircles(sepalTurtle, 50, centerX, centerY)
    drawFiveCircles(petalTurtle, 25, centerX, centerY)
    drawCenterCircles(centerTurtle, centerX, centerY-15)
    drawBee(stampTurtle, centerX-2, centerY)


win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

drawflower(sepalTurtle,petalTurtle,centerTurtle,stampTurtle, 0, 0)

drawflower(sepalTurtle,petalTurtle,centerTurtle,stampTurtle,0,220)

drawflower(sepalTurtle,petalTurtle,centerTurtle,stampTurtle,220,0)

drawflower(sepalTurtle,petalTurtle,centerTurtle, stampTurtle,0,-220)

drawflower(sepalTurtle,petalTurtle,centerTurtle,stampTurtle,-220,0)

win.exitonclick()