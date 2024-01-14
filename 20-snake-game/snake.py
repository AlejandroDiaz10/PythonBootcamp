from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    # Create the snake body (with 3 squares - 20x20)
    def create_snake(self):
        for position in INITIAL_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.snake.append(new_turtle)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        # for square in snake: # Not working when turning
        #     square.forward(20)
        for square in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[square - 1].xcor()
            new_y = self.snake[square - 1].ycor()
            self.snake[square].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
