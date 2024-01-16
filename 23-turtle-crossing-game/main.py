from turtle import Screen
import time
from player import Player
from traffic_manager import TrafficManager
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.tracer(0)

my_turtle = Player()
my_traffic_manager = TrafficManager()
my_scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(my_turtle.move_up, "Up")
my_screen.onkey(my_turtle.move_down, "Down")
my_screen.onkey(my_turtle.move_right, "Right")
my_screen.onkey(my_turtle.move_left, "Left")


game_over = False
i = 0
while not game_over:
    time.sleep(my_traffic_manager.cars_speed)
    my_screen.update()

    if i % 8 == 0:
        my_traffic_manager.create_car()

    # The speed of the traffic is related to the level
    my_traffic_manager.move_traffic()

    # Turtle reached the other side of the map
    if my_turtle.has_arrived():
        my_scoreboard.update_level()
        my_turtle.reset_position()
        my_traffic_manager.clear_traffic()
        my_traffic_manager.cars_speed *= 0.9

    # A car crashed into the turtle
    if my_traffic_manager.accident_detected(my_turtle):
        my_scoreboard.game_over()
        game_over = True
    i += 1


my_screen.exitonclick()
