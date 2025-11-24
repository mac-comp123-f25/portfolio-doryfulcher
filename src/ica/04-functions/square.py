import turtle

def turtle_square(sqTurt, side_len):
    for i in range(4):
        sqTurt.forward(side_len)
        sqTurt.right(90)

win = turtle.Screen()
doby = turtle.Turtle()
turtle_square(doby, 100)
win.exitonclick()
