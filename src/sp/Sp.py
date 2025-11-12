import random
import turtle

window=turtle.Screen()
window.bgcolor("black")
window.setup(width=800, height=900)
window.title("Turtle Nighttime City Scape")
turtle.speed(0)
turtle.color("white")

def draw_stars(size=5):
    """This function will draw tiny stars in the background of the window"""
    turtle.begin_fill()
    turtle.color("yellow")
    for _ in range(4):
        turtle.forward(size)
        turtle.backward(size)
        turtle.right(90)
    turtle.end_fill()

def random_placement_stars():
    """This function will randomly place the tiny stars in the background of the window and draw them"""
    for _ in range(100):
        x = random.randint(-350, 350)
        y = random.randint(160, 430)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        draw_stars(size=4)

def draw_skyscraper(x, y, floors=8, floor_height=20, width=80, color="gray"):
    """Draws a skyscraper"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.fillcolor(color)

    for _ in range(floors):
        turtle.begin_fill()
        # draw one rectangular floor
        for _ in range(2):
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(floor_height)
            turtle.left(90)
        turtle.end_fill()

        turtle.penup()
        turtle.left(90)
        turtle.forward(floor_height)
        turtle.right(90)
        turtle.pendown()

def draw_shaped_skyscraper(x, y, base_width=100, base_height=120,
                           mid_width=70, mid_height=200,
                           top_width=40, top_height=140,
                           color="dim gray"):
    """Draws a tiered skyscraper with three sections."""

    turtle.color(color)
    turtle.fillcolor(color)

    def draw_rect(start_x, start_y, w, h):
        turtle.penup()
        turtle.goto(start_x, start_y)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(h)
            turtle.left(90)
        turtle.end_fill()

    draw_rect(x, y, base_width, base_height)

    mid_x = x + (base_width - mid_width) / 2
    mid_y = y + base_height
    draw_rect(mid_x, mid_y, mid_width, mid_height)

    top_x = x + (base_width - top_width) / 2
    top_y = mid_y + mid_height
    draw_rect(top_x, top_y, top_width, top_height)

def draw_moon(radius=40):
    """Draws a moon"""
    turtle.penup()
    turtle.goto(250, 300)
    turtle.pendown()
    turtle.color("light yellow")
    turtle.fillcolor("light yellow")

    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

"""Call to draw the moon"""
draw_moon(radius=40)

"""Calls to draw the skyscrapers, these can take user inupt, the user can decide how tall they want the buildings or what color they would like. """
draw_shaped_skyscraper(-350, -450)
draw_skyscraper(-250, -450, floors=20, width=80, color="silver")
draw_skyscraper(-200, -450, floors=25, width=60, color="dark slate gray")
draw_skyscraper(-150, -450, floors=30, width=80, color="dark blue")
draw_skyscraper(-60, -450, floors=25, width=80, color="dim gray")
draw_shaped_skyscraper(-30, -450, base_width=90, mid_width=60, top_width=35, color="slate gray")
draw_skyscraper(50, -450, floors=20, width=55, color="silver")
draw_skyscraper(100, -450, floors=25, width=70, color="dark blue")
draw_skyscraper(160, -450, floors=29, width=80, color="dark slate gray")
draw_skyscraper(200, -450, floors=20, width=80, color="silver")
draw_shaped_skyscraper(250, -450, base_width=120, mid_width=80, top_width=50, color="dark slate gray")

"""Call to randomly place the stars"""
random_placement_stars()

turtle.done()
window.mainloop()


