from turtle import Turtle
FONT = ("Arial",12,"bold")
ALIGN = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()

        self.goto(0, 280)
        self.write_score(0)


    def write_score(self, score):
        self.clear()
        self.write(f"Score: {score}", align= ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!", align=ALIGN, font=FONT)