from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
MAX_GOALS = 3


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write_scoreboard("left")
        self.goto(100, 200)
        self.write_scoreboard("right")

    def write_scoreboard(self, player):
        self.write(f"{self.l_score if player == "left" else self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, player):
        if player == "left":
            self.l_score += 1
        else:
            self.r_score += 1
        self.clear()
        self.update_scoreboard()
        if self.l_score == MAX_GOALS or self.r_score == MAX_GOALS:
            return True
        else:
            return False

    def winner_detected(self):
        self.goto(0, 0)
        self.write(f"Player in the {'left' if self.l_score > self.r_score else 'right'} wins!", align=ALIGNMENT, font=("Courier", 20, "normal"))
