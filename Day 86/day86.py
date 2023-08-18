# @author   Lucas Cardoso de Medeiros
# @since    18/08/2023
# @version  1.0

"""Using Tkinter and what you have learnt about building GUI applications with Python, build a desktop app that
assesses your typing speed. Give the user some sample text and detect how many words they can type per minute.
You can build your typing speed test into a typing trainer, with high scores and more text
samples. You can design your program any way you want."""

import tkinter as tk
import time
import random

FONT = ("Helvetica", 14)
SAMPLE_TEXT = [
    "The quick brown fox jumps over the lazy dog",
    "She sells seashells by the seashore",
    "How much wood would a woodchuck chuck",
    "Peter Piper picked a peck of pickled peppers",
    "I scream, you scream, we all scream for ice cream",
    "An apple a day keeps the doctor away",
    "A stitch in time saves nine",
    "Two wrongs don't make a right",
    "Don't cry over spilled milk",
    "Actions speak louder than words",
    "All that glitters is not gold",
    "Honesty is the best policy",
    "The early bird catches the worm",
    "When in Rome, do as the Romans do",
    "Better late than never",
    "Every cloud has a silver lining",
    "You can't judge a book by its cover",
    "Barking up the wrong tree",
    "A penny for your thoughts",
    "Don't put all your eggs in one basket"
]


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.sample_text = random.choice(SAMPLE_TEXT)
        self.current_index = 0
        self.high_score = 0
        self.start_time = None

        self.text_label = tk.Label(root, text=self.sample_text, font=FONT)
        self.text_label.pack(padx=50, pady=50)

        self.input_entry = tk.Entry(root, font=FONT, width=50)
        self.input_entry.pack(padx=50, pady=10)

        self.start_button = tk.Button(root, text="Start Typing", command=self.start_typing)
        self.start_button.pack()

        self.reset_text_button = tk.Button(root, text="Reset sample text", command=self.reset_sample_text)
        self.reset_text_button.pack()

        self.result_label = tk.Label(root, text="", font=FONT)
        self.result_label.pack(padx=50, pady=50)

        self.highscore_label = tk.Label(root, text="", font=FONT)
        self.highscore_label.pack(padx=50, pady=50)

    def reset_sample_text(self):
        self.sample_text = random.choice(SAMPLE_TEXT)
        self.text_label.config(text=self.sample_text)
        self.result_label.config(text="")

    def start_typing(self):
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()
        self.current_index = 0
        self.start_time = time.time()

        self.input_entry.bind("<Key>", self.check_typing)

    def check_typing(self, event):
        if self.input_entry.get() == self.sample_text:
            elapsed_time = time.time() - self.start_time
            words_per_minute = int(len(self.sample_text.split()) / (elapsed_time / 60))
            self.result_label.config(text=f"Typing Speed: {words_per_minute} words per minute")

            if words_per_minute > self.high_score:
                self.high_score = words_per_minute
                self.highscore_label.config(text=f"Highest Speed: {self.high_score} wpm")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    app.run()
