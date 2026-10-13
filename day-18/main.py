from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "green") # pen and fill colours

# draw a square
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for i in range(15):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

color_list = ["red", "blue", "green", "purple", "orange", "hotpink", "gold"]

def random_angle():
    angle_list = [0, 90, 180, 270]
    return random.choice(angle_list)

timmy.pensize(10)
timmy.speed("fastest")
for _ in range(200 ):
    timmy.color(random.choice(color_list))
    timmy.setheading(random_angle())
    timmy.forward(20)


screen = Screen()
screen.exitonclick()
