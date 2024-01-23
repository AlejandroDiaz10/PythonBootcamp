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
# WORK_MIN = 0.1
# SHORT_BREAK_MIN = 0.1
# LONG_BREAK_MIN = 0.1
SECONDS_IN_A_MINUTE = 60

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Pomodoro Timer", fg=GREEN)
    checkmarks_label.config(text="")
    canvas.itemconfig(canvas_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_time = int(WORK_MIN * SECONDS_IN_A_MINUTE)
    short_break_time = int(SHORT_BREAK_MIN * SECONDS_IN_A_MINUTE)
    long_break_time = int(LONG_BREAK_MIN * SECONDS_IN_A_MINUTE)

    if reps % 8 == 0:
        new_text = "✔" * (reps // 2)
        checkmarks_label.config(text=new_text)
        timer_label.config(text="Long Break", fg=RED)
        countdown_mechanism(long_break_time)
    elif reps % 2 == 0:
        new_text = "✔" * (reps // 2)
        checkmarks_label.config(text=new_text)
        timer_label.config(text="Short Break", fg=PINK)
        countdown_mechanism(short_break_time)
    elif reps % 2 != 0:
        timer_label.config(text="Work Time", fg=GREEN)
        countdown_mechanism(work_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown_mechanism(count):
    minutes = count // SECONDS_IN_A_MINUTE
    seconds = count % SECONDS_IN_A_MINUTE

    if seconds < 10:
        seconds = "0" + str(seconds)

    # The GUI is Event Driven
    canvas.itemconfig(canvas_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown_mechanism, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)

timer_label = Label(text="Pomodoro Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)
timer_label.config(width=15, height=2)

checkmarks_label = Label(bg=YELLOW, fg=GREEN)
checkmarks_label.grid(row=3, column=1)

start_button = Button(
    text="Start",
    bg=YELLOW,
    highlightthickness=0,
    highlightbackground=YELLOW,
    command=start_timer,
)
start_button.grid(row=2, column=0)

reset_button = Button(
    text="Reset",
    bg=YELLOW,
    highlightthickness=0,
    highlightbackground=YELLOW,
    command=reset_timer,
)
reset_button.grid(row=2, column=2)

window.mainloop()
