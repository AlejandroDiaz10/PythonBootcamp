"""
W = Forwards
S = Backwards
A = Counter-Clockwise
D = Clockwise
C = Clear drawing
"""

from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()


def move_forwards():
    my_turtle.forward(10)


def move_backwards():
    my_turtle.backward(10)


def counter_clockwise():
    my_turtle.left(10)


def clockwise():
    my_turtle.right(10)


def clear_drawing():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


my_screen.listen()
my_screen.onkey(key="w", fun=move_forwards)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="a", fun=counter_clockwise)
my_screen.onkey(key="d", fun=clockwise)
my_screen.onkey(key="c", fun=clear_drawing)

my_screen.exitonclick()
