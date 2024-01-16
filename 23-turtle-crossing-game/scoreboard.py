from turtle import Turtle

CENTER = "center"
LEFT = "left"
FONT = ("Courier", 20, "normal")
MAX_GOALS = 3


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 260)
        self.write_scoreboard()

    def write_scoreboard(self):
        self.write(f"Level: {self.level}", align=LEFT, font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.write_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=CENTER, font=FONT)
