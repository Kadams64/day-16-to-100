import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()
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

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)

    return r, g, b # separate values with commas to return a tuple

def random_angle():
    angle_list = [0, 90, 180, 270]
    return random.choice(angle_list)

timmy.pensize(10)
timmy.speed("fastest")
for _ in range(200 ):
    timmy.color(random_color())
    timmy.setheading(random_angle())
    timmy.forward(20)


screen = t.Screen()
screen.exitonclick()
