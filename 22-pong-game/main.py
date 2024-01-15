from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong Game")
my_screen.tracer(0)  # Turn off the animation

r_player = Paddle((350, 0))
l_player = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

my_screen.listen()
my_screen.onkey(r_player.move_up, "Up")
my_screen.onkey(r_player.move_down, "Down")
my_screen.onkey(l_player.move_up, "w")
my_screen.onkey(l_player.move_down, "s")

game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move_ball()

    # Detect ball collision with wall and bounce
    if ball.detect_wall_collision():
        ball.wall_bounce()

    if ball.detect_paddle_collision(r_player) or ball.detect_paddle_collision(l_player):
        ball.paddle_bounce()

    if ball.goal_detected() != "":
        scorer = ball.goal_detected()
        game_over = scoreboard.increase_score(scorer)
        ball.reset_position()

scoreboard.winner_detected()

my_screen.exitonclick()
