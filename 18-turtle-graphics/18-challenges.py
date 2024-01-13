# It's recommended to use the latest version of Python
# Tested with Python v3.12.1

# python3 -m venv env
# source env/bin/activate

from turtle import Turtle, Screen
from random import choice, randint

colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]

directions = [0, 90, 180, 270]


# Chalenge 1: Function to draw a square
def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)


# Challenge 2: Draw a dashed line
def draw_dashed_line(turtle):
    for _ in range(15):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


# Challenge 3.1: Draw different a shape
def draw_shape(turtle, sides):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)


# Challenge 3.2: Draw multiple shapes in one run
def draw_multiple_shapes(turtle):
    for sides in range(3, 11):
        turtle.color(choice(colours))
        draw_shape(turtle, sides)


# Challenge 4: Random walk
def random_walk(turtle):
    turtle.pensize(10)
    turtle.speed("fastest")
    for _ in range(200):
        # turtle.color(choice(colours))
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        turtle.color(color)
        turtle.forward(30)
        turtle.setheading(choice(directions))


# Challenge 5: Spirograph
def spirograph(turtle, size_of_gap=5):
    turtle.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        # turtle.color(choice(colours))
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        turtle.color(color)
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


my_screen = Screen()
my_screen.colormode(255)

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")

# draw_square(my_turtle)
# draw_dashed_line(my_turtle)
# draw_shape(my_turtle, 3)
# draw_multiple_shapes(my_turtle)
# random_walk(my_turtle)
spirograph(my_turtle, 3)

my_screen.exitonclick()
