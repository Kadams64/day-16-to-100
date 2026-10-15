import random
from turtle import Turtle, Screen
from tkinter import simpledialog

screen = Screen()
screen.title("Turtle Race!")
screen.setup(width=500,height=400)

# I was able to get this to work by installing Python from the official python
# downloads page => https://www.python.org/downloads/
choice = screen.textinput(title= "Make your bet", prompt="Which turtle do you bet on? Enter a colour: ")
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
    # populate turtles dictionary
    turtles[c]= turtle
    turtles[c].penup()
    turtles[c].goto(x=-180, y=starty)

print(choice)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y = -150
for color in colors:
    create_turtle(color, y)
    y += 30

is_race_on = False

if choice in colors:
    is_race_on = True

while is_race_on:
    for key, value in turtles.items():
        # width of turtle is 40, width of screen is 250, turtle contact is measured from
        # turtle center
        value.forward(random.randint(0,10))
        if value.xcor() > 230:
            winning_color = key # could alternately use turtle (value).pencolor
            if winning_color == choice:
                print(f"You've won!  The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost!  The {winning_color} turtle is the winner!")
            is_race_on = False
            break # exit the for loop early so we don't end up with multiple winners


screen.exitonclick()
