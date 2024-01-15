from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, initial_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(initial_position)

    def move_up(self):
        x = self.xcor()
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y < 280:
            self.goto(x, new_y)

    def move_down(self):
        x = self.xcor()
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y > -260:
            self.goto(x, new_y)
