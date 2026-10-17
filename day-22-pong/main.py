import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

from wcwidth import width

screen = Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
p_right = Paddle(loc=(350,0))
p_left = Paddle(loc=(-350,0))
ball = Ball()

screen.listen()

# beware of calling function immediately i.e.: function() instead of passing a reference
# i.e.: function
screen.onkey(fun= p_right.move_up, key="Up")
screen.onkey(fun= p_right.move_down, key="Down")
screen.onkey(fun= p_left.move_up, key="w")
screen.onkey(fun= p_left.move_down, key="s")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.01)
    # ball.ball_move((ball.xcor() + 1, ball.ycor() + 1))
    ball.move()

    # detect wall collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # detect right paddle collision
    if (ball.distance(p_right) < 50 and ball.xcor() > 340
            or ball.distance(p_left) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    # detect out of bounds ball
    if ball.xcor() > 380:
        ball.reset()

    if ball.xcor() < -380:
        ball.reset()

screen.exitonclick()




