from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
run = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_time():
    screen.after_cancel(run)
    tick.config(text='')
    timer.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    count_down(WORK_MIN * 60, 0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count, temp):
    count_min = floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global run
        run = screen.after(1000, count_down, count - 1, temp)
    else:
        temp += 1
        if temp == 1 or temp == 3 or temp == 5:
            count_down(SHORT_BREAK_MIN * 60, temp)
            timer.config(text='Break', fg=PINK)
            if temp == 1:
                tick.config(text='✅')
            elif temp == 3:
                tick.config(text='✅ ✅')
            elif temp == 5:
                tick.config(text='✅ ✅ ✅')
        elif temp == 2 or temp == 4 or temp == 6:
            count_down(WORK_MIN * 60, temp)
            timer.config(text='Work', fg=GREEN)
        elif temp == 7:
            count_down(LONG_BREAK_MIN * 60, temp)
            timer.config(text='Break', fg=RED)
        else:
            tick.config(text='')
            timer.config(text='Timer', fg=GREEN)
            canvas.itemconfig(timer_text, text=f"00:00")


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title('Pomodoro Alarm')
screen.config(padx=100, pady=100, bg=YELLOW)
canvas = Canvas(width=205, height=223, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=image)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

timer = Label(text='Timer', bg=YELLOW, font=(FONT_NAME, 50), fg=GREEN)
start = Button(text='Start', font=(FONT_NAME, 10, 'bold'), fg='black', command=start_timer)
reset = Button(text='Reset', font=(FONT_NAME, 10, 'bold'), fg='black', command=reset_time)
tick = Label(fg=GREEN, bg=YELLOW)

timer.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start.grid(row=2, column=0)
reset.grid(row=2, column=2)
tick.grid(row=3, column=1)
screen.mainloop()
