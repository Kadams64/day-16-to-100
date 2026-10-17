from turtle import Turtle

MOVE = 2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white", "white")
        self.goto(0,0)
        self.x_move = MOVE
        self.y_move = MOVE

    # def ball_move(self, loc: tuple):
    #     self.goto(loc)
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset(self):
        self.clear()
        self.goto(0, 0)
        self.bounce_x()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
