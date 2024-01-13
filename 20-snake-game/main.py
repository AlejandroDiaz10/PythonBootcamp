from turtle import Turtle, Screen
import time
from random import randint
from snake import Snake

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)  # Turn off the animation

snake = Snake()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

while True:
    my_screen.update()  # Update the screen to make the snake move
    time.sleep(0.15)
    snake.move()

my_screen.exitonclick()
