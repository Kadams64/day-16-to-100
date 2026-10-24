import random
from tkinter import *
from tkinter import messagebox
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT=("Ariel", 40, "italic")
WORD_FONT=("Ariel", 60, "bold")

counts = 0
random_dict = {}

# ---------------------------- DATA METHODS ------------------------------- #

try:
    dataframe = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    dataframe = pandas.read_csv("./data/french_words.csv")
list_words_dict = dataframe.to_dict(orient="records")

def new_card():
    global list_words_dict, random_dict, timer
    window.after_cancel(timer)

    # fails if list_words_dict is empt (len = 0)
    random_dict = random.choice(list_words_dict)
    canvas.itemconfig(language_label, text="French")
    canvas.itemconfig(word_label, text=random_dict["French"])
    flip_card_to_front()
    timer = window.after(3000, flip_card_to_back)

def delete_known_entry(dict):
    global list_words_dict
    print(f"in delete, len(list_words_dict)= {len(list_words_dict)}")
    removal_word = dict["French"]
    # my solution is much more complicated than the course recommended one
    # I am actually using list comprehension to remove the matching entry
    # based on the value of the french word or phrase
    # - at least I didn't use a for loop!
    reduced_list = [d for d in list_words_dict
                    if d.get("French") != removal_word]

    list_words_dict = reduced_list

    #save to a new file; words_to_learn.csv
    words_to_learn_frame = pandas.DataFrame(list_words_dict)
    words_to_learn_frame.to_csv("./data/words_to_learn.csv", index=False)

# ---------------------------- UI METHODS ------------------------------- #
def right():
    delete_known_entry(random_dict)
    new_card()



def wrong():
    new_card()

def flip_card_to_back():
    global random_dict
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=random_dict["English"], fill="white")

def flip_card_to_front():
    global random_dict
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=random_dict["French"], fill="black")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=850, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(440,270,image=front_img)
canvas.grid(row=0, column=0, columnspan=2)
language_label = canvas.create_text(
    430,
    150,
    text="French",
    font=LANGUAGE_FONT,
    fill="black"
)
word_label = canvas.create_text(
    430,
    263,
    text="trouve",
    font=WORD_FONT,
    fill="black"
)



# Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, command=wrong, borderwidth=0, highlightthickness=0)
wrong_button.grid(row=1, column=0, padx=50)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, command=right, borderwidth=0, highlightthickness=0)
right_button.grid(row=1, column=1)

timer = window.after(3000, flip_card_to_back)
new_card()


window.mainloop()