from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x= -280, y= +250)
        self.score = 0
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="*** GAME OVER ***", align="center", font=FONT)