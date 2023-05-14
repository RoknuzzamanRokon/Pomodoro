from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#3bdeaa"
YELLOW = "#f7f5bd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown_fun(value):
    print(value)
    if value > 0:
        window.after(1000, countdown_fun, value - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

countdown_fun(5)


# Import image here.
canvas = Canvas(width="200", height="224", bg=YELLOW, highlightthickness=0)
image_canvas = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_canvas)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=2, column=2)

# Create Label.
top_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
top_label.grid(row=1, column=2)

checkmark_label = Label(text="🗸", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
checkmark_label.grid(row=4, column=2)

# Create Button.
start_button = Button(text="Start", bg=GREEN, highlightthickness=0, width=5)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", bg=GREEN, highlightthickness=0, width=5)
reset_button.grid(row=3, column=3)


window.mainloop()
