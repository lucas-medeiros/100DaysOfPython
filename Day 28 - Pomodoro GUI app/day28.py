# @author   Lucas Cardoso de Medeiros
# @since    04/07/2022
# @version  1.0

# Pomodoro with Tkinter GUI
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
CHECK_MARK = "✔"


# ---------------------------- GLOBAL VARIABLES ------------------------------- #
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    reps = 0
    label_check.config(text="")
    label_timer.config(text="Timer")
    canvas.itemconfig(text_timer, text="00:00")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps > 7:
        label_timer.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        label_timer.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += CHECK_MARK
        label_check.config(text=marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_timer = Label(text="Timer", justify="center", pady=10, font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

label_check = Label(text="", justify="center", pady=10, font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
label_check.grid(column=1, row=3)

button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
button_reset.grid(column=2, row=2)

window.mainloop()
