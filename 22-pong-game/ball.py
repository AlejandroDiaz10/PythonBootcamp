from turtle import Turtle

MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_direction = 1
        self.y_direction = 1
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + (MOVE_DISTANCE * self.x_direction)
        new_y = self.ycor() + (MOVE_DISTANCE * self.y_direction)
        self.goto(new_x, new_y)

    def detect_wall_collision(self):
        return self.ycor() > 280 or self.ycor() < -270

    def wall_bounce(self):
        self.y_direction *= -1

    def detect_paddle_collision(self, paddle):
        return self.distance(paddle) < 50 and (self.xcor() > 320 or self.xcor() < -320)

    def paddle_bounce(self):
        self.x_direction *= -1
        self.move_speed *= 0.9

    def goal_detected(self):
        if self.xcor() > 390:
            return "left"
        elif self.xcor() < -390:
            return "right"
        else:
            return ""

    def reset_position(self):
        self.goto(0, 0)
        self.x_direction *= -1
        self.move_speed = 0.1
