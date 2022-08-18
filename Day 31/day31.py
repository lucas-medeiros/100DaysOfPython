# @author   Lucas Cardoso de Medeiros
# @since    06/07/2022
# @version  1.0

# Flashy game > Flip cards to learn French!

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

current_card = None
try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("./data/french_words.csv")
finally:
    to_learn = df.to_dict(orient="records")


# ------------------------- GENERATE NEW CARD ---------------------------- #
def next_card():
    global current_card, timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(text_language, text="French", fill="black")
    canvas.itemconfig(text_word, text=current_card["French"], fill="black")
    window.after_cancel(timer)
    timer = window.after(3000, func=card_flip)


# ---------------------------- CARD FLIP ------------------------------- #
def card_flip():
    global current_card
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(text_language, text="English", fill="white")
    canvas.itemconfig(text_word, text=current_card["English"], fill="white")


# ---------------------------- CARD FLIP ------------------------------- #
def save_progress():
    global current_card
    to_learn.remove(current_card)
    new_df = pandas.DataFrame(to_learn)
    new_df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=card_flip)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
text_language = canvas.create_text(400, 150, text="Title", font=LANGUAGE_FONT)
text_word = canvas.create_text(400, 263, text="word", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_img, command=next_card, highlightthickness=0)
button_wrong.grid(column=0, row=1)

right_img = PhotoImage(file="./images/right.png")
button_right = Button(image=right_img, command=save_progress, highlightthickness=0)
button_right.grid(column=1, row=1)

next_card()
window.mainloop()
