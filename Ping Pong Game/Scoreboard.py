from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"{self.score_l}:{self.score_r}", align="center", font=("Courier", 36, "normal"))

    def increase_lscore(self):
        self.score_l += 1
        self.update_scoreboard()

    def increase_rscore(self):
        self.score_r += 1
        self.update_scoreboard()
