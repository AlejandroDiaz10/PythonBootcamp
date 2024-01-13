from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt=f"Which turtle will win the race? Enter a color: \n{colors}",
)


def create_turtles():
    # If width is 500, then the left edge is -250 and the right edge is 250
    # If height is 400, then the top edge is 200 and the bottom edge is -200
    x_position = -230
    y_positions = [-100, -60, -20, 20, 60, 100]

    all_turtles = []
    for i in range(0, 6):
        my_turtle = Turtle("turtle")
        my_turtle.color(colors[i])
        my_turtle.penup()
        my_turtle.goto(x=x_position, y=y_positions[i])
        my_turtle.pendown()
        all_turtles.append(my_turtle)

    return all_turtles


def move_turtle(turtle):
    distance = randint(0, 10)
    turtle.penup()
    turtle.forward(distance)


def check_winner(turtles):
    winner = None
    for turtle in turtles:
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            break
    return winner


def race(turtles):
    winner = None
    while not winner:
        for turtle in turtles:
            move_turtle(turtle)
        winner = check_winner(turtles)
    return winner


if user_bet.lower() in colors:
    racing_turtles = create_turtles()
    winner_tutle = race(racing_turtles)
    if winner_tutle == user_bet.lower():
        print(f"You've won! The {winner_tutle} turtle is the winner!")
    else:
        print(f"You've lost! The {winner_tutle} turtle is the winner!")


screen.exitonclick()
