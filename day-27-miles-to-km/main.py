import tkinter as tk

FONT = ("Ariel",18,"bold")

window = tk.Tk()
window.title("Miles to kilometres")
window.minsize(width=300, height=200)
window.config(padx= 20, pady=20)

# create input control
input = tk.Entry(justify="center", width= 10, font=FONT)
input.grid(column= 1, row=0)

# create miles label
miles_label = tk.Label(text= "Miles", font=FONT)
miles_label.grid(column=2, row=0)


# create is equal to label

equals_label = tk.Label(text= "is equal to", font=FONT)
equals_label.grid(column=0, row=1)

# create calculated kilometres label
calc_label = tk.Label(text= "0", font=FONT)
calc_label.grid(column=1, row=1)


# create Km label
km_label = tk.Label(text= "Km", font=FONT)
km_label.grid(column=2, row=1)

def calculate_clicked():
    try:
        miles = int(input.get())
    except ValueError:
        print("Invalid value entered- try an integer")
        miles = 0
    kilometres = miles * 1.609344
    calc_label["text"] = round(kilometres, 1)

# create Calculate button
calc_button = tk.Button(text= "Calculate", font= FONT, command=calculate_clicked)
calc_button.grid(column= 1, row=2)


window.mainloop()