import math
import tkinter as tk
from tkinter import PhotoImage

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
COUNT_DOWN_SEC = 5
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    if timer is not None:
        window.after_cancel(timer)
        timer = None
        label.configure(text="Timer", fg=GREEN)
        check_mark.configure(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label.configure(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label.configure(text="Break", fg=YELLOW)
    else:
        countdown(work_sec)
        label.configure(text="Work Mode", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global timer, reps
    minutes, seconds = divmod(count, 60)
    formatted_time = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=str(formatted_time))
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        check_mark_str = ""
        for _ in range(math.floor(reps/2)):
            check_mark_str += "✔"
        check_mark.configure(text=check_mark_str)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, bg=PINK)

label = tk.Label(text="Timer", font=(FONT_NAME, 35, "normal"), fg=GREEN, bg=PINK)
label.grid(row=0, column=1)

canvas = tk.Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=img)
timer_text = canvas.create_text(100, 130, text="00.00", font=(FONT_NAME, 35, "bold"), fill=YELLOW)
canvas.grid(row=1, column=1)

start_button = tk.Button(text="Start", highlightthickness=0, borderwidth=0, command=start_timer)
reset_button = tk.Button(text="Reset", highlightthickness=0, borderwidth=0, command=reset_timer)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

check_mark = tk.Label(fg=GREEN, bg=PINK)
check_mark.grid(row=3, column=1)

window.mainloop()