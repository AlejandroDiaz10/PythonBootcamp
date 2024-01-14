from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

LIMIT = 285

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)  # Turn off the animation

my_snake = Snake()
my_food = Food()
my_scoreboard = ScoreBoard()

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")


game_over = False
while not game_over:
    my_screen.update()  # Update the screen to make the snake move
    time.sleep(0.10)
    my_snake.move()

    # Detect collision (food - snake)
    if my_snake.head.distance(my_food) < 15:
        my_food.refresh()
        my_snake.extend()
        my_scoreboard.increase_score()

    # Detect collision (wall - snake)
    if (
        my_snake.head.xcor() > LIMIT
        or my_snake.head.xcor() < -LIMIT
        or my_snake.head.ycor() > LIMIT
        or my_snake.head.ycor() < -LIMIT
    ):
        my_scoreboard.game_over()
        game_over = True

    # Detect collision (snake - snake)
    # for square in my_snake.snake:
    #     if square == my_snake.head:
    #         pass
    #     elif my_snake.head.distance(square) < 5:
    #         my_scoreboard.game_over()
    #         game_over = True

    # Using slicing
    for square in my_snake.snake[1:]:
        if my_snake.head.distance(square) < 5:
            my_scoreboard.game_over()
            game_over = True


my_screen.exitonclick()
