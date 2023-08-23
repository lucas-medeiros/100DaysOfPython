# @author   Lucas Cardoso de Medeiros
# @since    22/08/2023
# @version  1.0


"""An online writing app where if you stop typing, your work will disappear.

For most writers, a big problem is writing block. Where you can't think of what to write, and you can't write anything.

One of the most interesting solutions to this is a web app called The Most Dangerous Writing App, an online text
editor where if you stop writing, all your progress will be lost.

A timer will count down and when the website detects the user has not written anything in the last 5/10 seconds,
it will delete all the text they've written so far.

Try it out here:

https://www.squibler.io/dangerous-writing-prompt-app

You are going to build a desktop app that has similar functionality. The design is up to you, but it should allow a
user to type and if they stop for more than 5 seconds, it should delete everything they've written so far."""


import tkinter as tk
import random

SECONDS = 5
FONT = ("Helvetica", 14)
BUTTON_FONT = ("Helvetica", 16)
SENTENCES = [
    "The moonlit night held a secret that only the stars knew",
    "In a forgotten corner of the world, an ancient treasure lay buried",
    "The old oak tree whispered tales of forgotten legends to the wind",
    "Beyond the misty mountains, a hidden valley held mysteries untold",
    "With a single touch, the ordinary pen became a portal to another world",
    "Underneath the cobblestone streets, a labyrinth of tunnels hid ancient secrets",
    "The abandoned mansion on the hill had a history that no one dared to mention",
    "In the heart of the enchanted forest, a magical creature watched over the land",
    "A single feather held the power to grant wishes, but at a great cost",
    "Among the bustling city streets, a street performer held the key to an alternate reality",
    "The forgotten diary in the attic revealed the life of an adventurer from a bygone era",
    "The mysterious door in the library led to a realm where time stood still",
    "On a deserted island, a castaway stumbled upon a map marked with an X",
    "The shattered mirror in the antique shop revealed glimpses of other dimensions",
    "A simple painting had the ability to change the course of history",
    "Hidden in a dusty bookshop, an ancient tome held the secrets of immortality",
    "Through the window, a shooting star granted a single wish to the curious child",
    "Deep within the cave, a shimmering crystal held the power to heal",
    "The whispering winds carried messages from a world beyond our own",
    "In the attic of a quaint cottage, a time-traveling device awaited its next journey",
]


class DangerousWritingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("The Most Dangerous Writing App")
        self.root.geometry("1000x650")

        self.timer_seconds = SECONDS

        self.text = tk.Text(self.root, wrap=tk.WORD, font=FONT, width=500, height=20)
        self.text.pack(padx=50, pady=50)
        self.text.bind("<Key>", self.on_key_press)

        self.start_button = tk.Button(self.root, text="Start Typing", command=self.start_typing, font=BUTTON_FONT)
        self.start_button.pack()

        self.timer_label = tk.Label(self.root, text=f"Time left: {self.timer_seconds}", font=BUTTON_FONT)
        self.timer_label.place(relx=1, rely=1, anchor="se", x=-50, y=-75)

    def generate_sentence(self):
        self.clear_text()
        self.text.insert(tk.END, f"{random.choice(SENTENCES)} ")

    def on_key_press(self):
        self.reset_timer()

    def start_typing(self):
        self.generate_sentence()
        self.text.focus()
        self.timer_seconds = SECONDS
        self.root.after(1000, self.check_typing)

    def check_typing(self):
        self.timer_seconds -= 1
        self.timer_label.config(text=f"Time left: {self.timer_seconds}")
        if self.timer_seconds == 0:
            self.clear_text()
        else:
            self.root.after(1000, self.check_typing)

    def reset_timer(self):
        self.timer_seconds = SECONDS + 1

    def clear_text(self):
        self.text.delete("1.0", tk.END)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = DangerousWritingApp()
    app.run()
