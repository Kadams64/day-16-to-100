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

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(1, num_sides +1):
        timmy.right(angle)
        timmy.forward(100)

for sides in range(3,10 + 1):
    timmy.color(random.choice(color_list))
    draw_shape(sides)


screen = Screen()
screen.exitonclick()
