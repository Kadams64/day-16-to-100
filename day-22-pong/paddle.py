from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, loc: tuple):
        """
        a class for managing a pong paddle.  screen_object is a screen to update
        (should be the same screen with the paddle) and loc is a tuple containing (x,y) coordinates to
        start the paddle at

        :type paddle loc is the location of type: tuple
        """
        super().__init__()
        self.location = loc
        self.draw_paddle()
        # self.screen.listen()
        # self.screen.onkey(fun=self.up(), key=upkey)

    def draw_paddle(self):
        # draw paddle

        self.penup()
        self.color("white", "white")
        self.shape("square")
        self.goto(self.location)
        self.left(90)
        self.shapesize(stretch_len=5)

    def move_up(self):
        x_loc = self.xcor()
        y_loc = self.ycor()
        self.goto(x= x_loc, y= y_loc + 20)

    def move_down(self):
        x_loc = self.xcor()
        y_loc = self.ycor()
        self.goto(x= x_loc, y= y_loc - 20)
