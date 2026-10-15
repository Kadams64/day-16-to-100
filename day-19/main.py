from turtle import Turtle, Screen
from tkinter import simpledialog

screen = Screen()
screen.setup(width=500,height=400)
#choice = screen.textinput(title= "Make your bet", prompt="Which turtle do you bet on? Enter a colour: ")
#choice = simpledialog.askstring(title= "Make your bet", prompt="Which turtle do you bet on? Enter a colour: ")
# above TK related calls fail with an error of the form:
#     w.tk.call("::tk::unsupported::MacWindowStyle", "style",
#     ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#               w, "moveableModal", "")
#               ^^^^^^^^^^^^^^^^^^^^^^^
# _tkinter.TclError: invalid command name "::tk::unsupported::MacWindowStyle"
# this is apparently a known issue with python-tk and version 9 of the TK libraries
turtles = {}

def create_turtle(c, starty):
    turtle = Turtle(shape="turtle")
    turtle.color(c)
    turtles[c]= turtle
    turtles[c].penup()
    turtles[c].goto(x=-180, y=starty)



choice = input("Which turtle do you bet on? Enter a colour: ").lower()
print(choice)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y = -150
for color in colors:
    create_turtle(color, y)
    y += 30

print(turtles)
turtles["red"].forward(30)

screen.exitonclick()
