from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def read_highscore(self):
        with open(file="data.txt", mode="r") as file:
            self.high_score = int(file.read())

    def write_highscore(self):
        with open(file="data.txt", mode="w") as file:
            file.write(str(self.high_score))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_highscore()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
