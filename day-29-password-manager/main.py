from tkinter import *
from tkinter import messagebox
import random
import pyperclip


DELIMITER = ","
FONT = ("Ariel",12)
DEFAULT_EMAIL = "some_email@gmail.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # convert these three for statements into list comprehension instead

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list) # join concats the separate list members into the string
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def reset_controls():
    print("In reset_controls")
    website_entry.delete(0,END)
    email_entry.delete(0,END)
    password_entry.delete(0,END)

    email_entry.insert(0, DEFAULT_EMAIL)

def save_data():
    # get values from controls website_entry, email_entry, password_entry
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Ooops","All fields must have data: please fill them out.")
        return
    is_ok = messagebox.askokcancel(title=website,
                           message=f"These are the details entered:\n"
                                   f"Email: {email}\nPassword:{password}\nIs it okay to save?")
    if is_ok:
        # save the data to a file named data.text.  Delimit fields with DELIMITER
        with open("data.txt", "a", encoding="utf-8") as file:
            file.write(f"{website}{DELIMITER}{email}{DELIMITER}{password}\n")

        # reset the controls
        reset_controls()


# ---------------------------- UI SETUP ------------------------------- #

# window with title of password manager with canvas displaying logo 200x200 padding 20 pixels

window = Tk()
window.title("Password Manager") # make sure to call the title method, not assign a value
window.config(padx=20, pady=20)
# highlightthickness=0 gets rid of border around canvas
canvas = Canvas(width= 200, height=200, highlightthickness=0)

window.update() #force an update to correct "missing" image

logo_img = PhotoImage(file="logo.png")

# tuple is the center of the image
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)

# labels
website_label = Label(text= "Website:", font=(FONT))
website_label.grid(column=0, row=1)

email_label = Label(text= "Email/Username:", font=(FONT))
email_label.grid(column=0, row=2)

password_label = Label(text= "Password:", font=(FONT))
password_label.grid(column=0, row=3)

# inputs
website_entry = Entry(justify="left", width= 35, font=FONT)
website_entry.grid(column= 1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(justify="left", width= 35, font=FONT)
email_entry.grid(column= 1, row=2, columnspan=2)
email_entry.insert(0, DEFAULT_EMAIL)

password_entry = Entry(justify="left", width= 21, font=FONT)
password_entry.grid(column= 1, row=3)


# buttons
generate_button = Button(text= "Generate Password", font= (FONT, 10),
                         highlightthickness=0, command=generate_password)
generate_button.grid(column= 2, row=3)

add_button = Button(text= "Add", font= (FONT), highlightthickness=0, width= 36, command=save_data)
add_button.grid(column= 1, row=4, columnspan= 2)

window.mainloop()