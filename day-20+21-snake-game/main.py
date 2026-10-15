from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)    # turn off tracer, skip intermediate drawing steps
                    # call update to redraw screen

snake_parts = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

def draw_snake():
    for position in starting_positions:
        new_segment = Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.goto(position)
        snake_parts.append(new_segment)




draw_snake()
screen.update()

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)

    # get the tail to follow the head
    # end segment moves to second from end and so on until the head is reached
    # this is not visible as we are only updating the screen once on each while loop
    for seg_num in range(len(snake_parts) - 1, 0, -1):
        new_x = snake_parts[seg_num - 1].xcor()
        new_y = snake_parts[seg_num - 1].ycor()
        snake_parts[seg_num].goto(new_x, new_y)
    snake_parts[0].forward(20)
    snake_parts[0].left(90)

screen.exitonclick()
