import tkinter

window = tkinter.Tk()
window.title("My first gui program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text= "I am a label", font=("Ariel",24,"bold"))
my_label.pack()  # pack required to cause label to show; side tells it which side
                            # to align with
my_label["text"] = "New text"

def button_clicked():
    my_label["text"] = input.get()

# button
my_button = tkinter.Button(text= "Click Me", command=button_clicked)
my_button.pack()

# entry component
input = tkinter.Entry()
input.pack()


window.mainloop()
