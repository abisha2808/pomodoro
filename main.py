from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
resp = 0
timer_on = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel("timer_on")
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global  resp
    resp = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global resp
    if resp % 2 == 0:
        countdown(WORK_MIN * 60)
        resp += 1
        timer.config(text="Work", fg=GREEN)
    elif resp == 7:
        countdown(LONG_BREAK_MIN * 60)
        resp += 1
        timer.config(text="Break", fg=RED)
    else:
        countdown(SHORT_BREAK_MIN * 60)
        resp += 1
        timer.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_on
        timer_on = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        for _ in range(resp % 2 == 0):
            check_mark.config(text="✔")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=("Ariel", 25, "normal"))
timer.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "normal"))
check_mark.grid(column=1, row=2)

window.mainloop()
