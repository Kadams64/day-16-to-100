import turtle as t
import random

# import colorgram as c
#
# colors = c.extract("image.jpg", 32)
#
# colorlist = []
# for color in colors:
#     rgb = tuple(color.rgb)
#     colorlist.append(rgb)
#
# print(colorlist)

# sampled colors from image.jpg using colorgram
color_list = [
    (244, 230, 203), (215, 242, 229), (217, 156, 103), (234, 208, 101),
    (245, 223, 233), (207, 228, 239), (114, 171, 201), (120, 190, 161),
    (42, 109, 150), (203, 136, 159), (156, 61, 95), (208, 78, 109), (31, 133, 100),
    (223, 81, 61), (193, 168, 28), (173, 72, 45), (141, 219, 193), (236, 164, 183),
    (142, 26, 58), (58, 170, 136), (18, 38, 83), (238, 170, 158), (52, 158, 184),
    (138, 215, 227), (37, 51, 117), (8, 101, 74), (68, 24, 58), (6, 64, 41),
    (103, 117, 179), (176, 20, 10), (176, 184, 224), (7, 91, 108)
]

tim = t.Turtle()
t.colormode(255)

def start_position():
    tim.penup()
    tim.goto(-150, -500)

def draw_circle():
    random_colour = random.choice(color_list)
    tim.color(random_colour, random_colour)
    tim.begin_fill()
    tim.circle(20)
    tim.end_fill()

def draw_row():
    for _ in range(10):
        draw_circle()
        tim.penup()
        tim.forward(50)
        tim.pendown()

def new_row():
    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

start_position()
tim.speed("fastest")
for _ in range(10):
    draw_row()
    new_row()


screen = t.Screen()
screen.exitonclick()