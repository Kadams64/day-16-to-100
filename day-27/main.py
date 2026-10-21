import tkinter

window = tkinter.Tk()
window.title("My first gui program")
window.minsize(width=500, height=300)
window.config(padx= 20, pady=100)

# label
my_label = tkinter.Label(text= "I am a label", font=("Ariel",24,"bold"))
# my_label.pack()     # pack layout manager- required to cause label to show; side tells it which side
#                     # to align with.  Defaults to center
my_label["text"] = "New text"
my_label.grid(column=0, row=0)

def button_clicked():
    my_label["text"] = input.get()

# button
my_button = tkinter.Button(text= "Click Me", command=button_clicked)
my_button.grid(column= 1, row=1)

# button
my_button = tkinter.Button(text= "Click Me", command=button_clicked)
my_button.grid(column= 2, row=0)

# entry component
input = tkinter.Entry()
input.grid(column= 3, row=2)


window.mainloop()
