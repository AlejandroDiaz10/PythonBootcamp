from turtle import Turtle

INITIAL_POSITION = (0, -280)
FINISH_LINE = 290
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(INITIAL_POSITION)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.setheading(90)
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y > -260:
            self.setheading(270)
            self.goto(self.xcor(), new_y)

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        if new_x < 280:
            self.setheading(0)
            self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        if new_x > -290:
            self.setheading(180)
            self.goto(new_x, self.ycor())

    def has_arrived(self):
        return self.ycor() >= FINISH_LINE

    def reset_position(self):
        self.goto(INITIAL_POSITION)
