# It's recommended to use the latest version of Python
# Tested with Python v3.12.1

# python3 -m venv env
# source env/bin/activate
# pip install colorgram.py

"""
Replicate Hirst Spot Painting with the Turtle Graphics Module
"""

from turtle import Turtle, Screen
from random import choice, randint

# ======================================= EXTRACT COLORS FROM IMAGE
# import colorgram

# # Extract 20 dot colors from the hirst painting image.
# colors = colorgram.extract("spot-painting.jpg", 80)

# # Create a list of tuples with the RGB values of the extracted colors.
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)

# ======================================= CREATE THE PAINTING
colors = [
    (233, 233, 232),
    (231, 233, 237),
    (236, 231, 233),
    (224, 233, 227),
    (207, 160, 82),
    (54, 88, 130),
    (145, 91, 40),
    (140, 26, 49),
    (221, 207, 105),
    (132, 177, 203),
    (158, 46, 83),
    (45, 55, 104),
    (169, 160, 39),
    (129, 189, 143),
    (83, 20, 44),
    (37, 43, 67),
    (186, 94, 107),
    (187, 140, 170),
    (85, 120, 180),
    (59, 39, 31),
    (88, 157, 92),
    (78, 153, 165),
    (194, 79, 73),
    (45, 74, 78),
    (80, 74, 44),
    (161, 201, 218),
    (57, 125, 121),
    (219, 175, 187),
    (169, 206, 172),
    (219, 182, 169),
    (179, 188, 212),
    (48, 74, 73),
    (147, 37, 35),
    (43, 62, 61),
]


def initialize_turtle(turtle):
    turtle.hideturtle()
    turtle.speed("fastest")
    turtle.setheading(225)
    turtle.forward(300)
    turtle.setheading(0)


def draw_dot(turtle):
    turtle.dot(20, choice(colors))
    turtle.forward(50)


def draw_row(turtle):
    for _ in range(10):
        draw_dot(turtle)


def reposition_turtle(turtle):
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)


def draw_painting(turtle):
    initialize_turtle(turtle)
    for _ in range(10):
        draw_row(turtle)
        reposition_turtle(turtle)


my_screen = Screen()
my_screen.colormode(255)

my_turtle = Turtle()
my_turtle.penup()
draw_painting(my_turtle)

my_screen.exitonclick()
