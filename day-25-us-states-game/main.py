import turtle
import pandas

IMAGE = "blank_states_img.gif"
FONT =  ("Arial",8,"bold")
screen = turtle.Screen()
screen.title("U.S. States game")

screen.addshape(IMAGE)
turtle.shape(IMAGE)

# set up the text turtle
text_turtle = turtle.Turtle()
text_turtle.penup()
text_turtle.hideturtle()
text_turtle.color("black")

# # Get x and y coordinates of a screen click
# # with turtle graphics.  From Google search AI
# # 2. Define a function that accepts x and y parameters
# def get_click_coordinates(x, y):
#     print(f"Screen clicked at X: {x}, Y: {y}")
#
# # 3. Bind the click event to your function
# screen.onscreenclick(get_click_coordinates)
#
# # 4. Keep the window open and listening for events
# screen.mainloop()
data = pandas.read_csv("50_states.csv")

correct_answers = []
score = 0
game_on = True
while game_on:
    answer_state = screen.textinput(f"Score {score} / 50", "Enter the name of another state")
    # convert the answer to Title case to match the csv
    answer_state = answer_state.title()

    # check if guess is in list of previous correct answers
    if answer_state not in correct_answers:
        # check if the guess is among the 50 states in the csv
        result = data[data["state"] == answer_state]
        if result.empty:
            # no match found; wrong state
            pass
        else:
            # new match found


            # write correct guesses onto the map
            x = result["x"].item()
            y = result["y"].item()
            text_turtle.goto(x,y)
            text_turtle.write(result["state"].item(), align="center", font=FONT)

            # record the correct guesses in a list
            correct_answers.append(result["state"].item())

            # keep track of the score
            score += 1

screen.exitonclick()