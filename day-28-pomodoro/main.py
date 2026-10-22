import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"

timer = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    # reset the timer
    if timer is not None:
        window.after_cancel(timer)

    global reps
    reps = 0
    # reset the clock to 0:00
    canvas.itemconfig(timer_text, text="00:00")

    # reset the checkmarks to empty string
    checkmarks_label.config(text="")

    # reset the title to timer
    top_label.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global timer, reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # use the timer variable to cancel after if it already exists
    # to prevent multiple timers from being started
    if timer is not None:
        window.after_cancel(timer)
    reps += 1
    if reps % 8 == 0:
        #long break
        top_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 1:
        # work
        top_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 2 == 0:
        #short break
        top_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps

    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    # add a leading zero when seconds becomes a single digit
    if count_seconds < 10:
        count_seconds = "0" + str(count_seconds) # could have used an f-string here

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}" )


    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            current_checks = checkmarks_label.cget("text")
            current_checks = current_checks + CHECKMARK
            checkmarks_label.config(text=current_checks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro") # make sure to call the title method, not assign a value
window.config(padx=50, pady=50, bg=YELLOW)
# highlightthickness=0 gets rid of border around canvas
canvas = Canvas(width= 200, height=224, bg= YELLOW, highlightthickness=0)

window.update() #force an update to correct "missing" image

tomato_img = PhotoImage(file="/Users/kellyadams/PycharmProjects/day-16-to-100/day-28-pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold"))
# canvas.pack()
canvas.grid(column=1,row=1)


# top label
top_label = Label(text= "Timer", font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW, width=15)
top_label.grid(column=1, row=0)

# buttons
start_button = Button(text= "Start", font= (FONT_NAME, 12), highlightthickness=0, command=start_timer)
start_button.grid(column= 0, row=2)

reset_button = Button(text= "Reset", font= (FONT_NAME, 12), highlightthickness=0, command=reset)
reset_button.grid(column= 2, row=2)

# checkmarks label
checkmarks_label = Label(font=(FONT_NAME, 24), fg=GREEN, bg=YELLOW)
checkmarks_label.grid(column=1, row=3)

window.mainloop()