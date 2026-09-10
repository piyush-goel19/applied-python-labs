import tkinter as tk
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FROM_LANGUAGE = "German"
TO_LANGUAGE = "English"

#----------------------READING CSV---------------------#
words_to_learn = []
current_card = {}
flip_timer = None

def next_card():
    global current_card, flip_timer, words_to_learn
    window.after_cancel(flip_timer)

    try:
        data = pd.read_csv("./data/words_to_learn.csv")
    except FileNotFoundError:
        data = pd.read_csv("./data/german_to_english_words_list.csv")
    finally:
        words_to_learn = data.to_dict(orient="records")

    current_card = choice(words_to_learn)
    canvas.itemconfig(card_img, image=front_image)
    canvas.itemconfig(card_title, text=FROM_LANGUAGE, fill="black")
    canvas.itemconfig(card_word, text=current_card[FROM_LANGUAGE], fill="black")
    flip_timer = window.after(3000, flip_card)

def know_card():
    global words_to_learn
    words_to_learn = [item for item in words_to_learn if item!=current_card]
    df = pd.DataFrame(words_to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_img, image=back_image)
    canvas.itemconfig(card_title, text=TO_LANGUAGE, fill="white")
    canvas.itemconfig(card_word, text=current_card[TO_LANGUAGE], fill="white")
    window.after_cancel(flip_timer)

#-------------------UI Setup---------------------------#

window = tk.Tk()
window.title("Flashy")
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0, borderwidth=0)
front_image = tk.PhotoImage(file="./images/card_front.png")
back_image = tk.PhotoImage(file="./images/card_back.png")
card_img = canvas.create_image(400, 264, image=front_image)

card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"), text="", fill="black")
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"), text="", fill="black")
canvas.grid(row=0, column=0, columnspan=2)

right_button_img = tk.PhotoImage(file="./images/right.png")
wrong_button_img = tk.PhotoImage(file="./images/wrong.png")

r_button = tk.Button(image=right_button_img, highlightthickness=0, borderwidth=0, command=know_card)
w_button = tk.Button(image=wrong_button_img, highlightthickness=0, borderwidth=0, command=next_card)

r_button.grid(row=1, column=1)
w_button.grid(row=1, column=0)

flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()