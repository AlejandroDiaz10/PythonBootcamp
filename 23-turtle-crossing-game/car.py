from turtle import Turtle
from random import choice, randint

COLORS = ["red", "green", "blue", "olive", "orange", "purple"]
MOVE_DISTANCE = 10
STREET_RANGE_Y = (-240, 240)
STREET_RANGE_X = (300, 330)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(
            randint(STREET_RANGE_X[0], STREET_RANGE_X[1]),
            randint(STREET_RANGE_Y[0], STREET_RANGE_Y[1]),
        )

    def drive(self):
        # All cars go from right to left
        new_x = self.xcor() - MOVE_DISTANCE
        if new_x < -300:
            self.reset_car()
        else:
            self.goto(new_x, self.ycor())

    def reset_car(self):
        self.goto(300, self.ycor())

    def has_crashed(self, turtle):
        # return self.distance(turtle) < 20 and self.xcor() == turtle.xcor()
        return self.distance(turtle) < 20

    def clear_car(self):
        self.clear()
        self.hideturtle()
