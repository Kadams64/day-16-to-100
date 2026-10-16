from turtle import Screen, Turtle
from paddle import Paddle

from wcwidth import width

screen = Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
p_right = Paddle(screen, loc=(350,0))
p_left = Paddle(screen, loc=(-350,0))

screen.listen()

# beware of calling function immediately i.e.: function() instead of passing a reference
# i.e.: function
screen.onkey(fun= p_right.move_up, key="Up")
screen.onkey(fun= p_right.move_down, key="Down")
screen.onkey(fun= p_left.move_up, key="w")
screen.onkey(fun= p_left.move_down, key="s")

screen.exitonclick()




