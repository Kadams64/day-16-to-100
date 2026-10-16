from turtle import Turtle

MOVE = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.draw_snake()
        self.head = self.snake_parts[0]

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.goto(position)
        self.snake_parts.append(new_segment)

    def draw_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)

    def move(self):
        # get the tail to follow the head
        # end segment moves to second from end and so on until the head is reached
        # this is not visible as we are only updating the screen once on each while loop
        for seg_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[seg_num - 1].xcor()
            new_y = self.snake_parts[seg_num - 1].ycor()
            self.snake_parts[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        # if prevents reversing on itself
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.snake_parts[-1].position())
