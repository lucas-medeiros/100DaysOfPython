from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", "15", "normal")
FILE_PATH = "Data/high_score.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.color("white")
        self.speed("fastest")
        self.score = 0
        with open(file=FILE_PATH, mode="r") as file:
            self.high_score = int(file.read())
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", move=False, align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file=FILE_PATH, mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.refresh()

    def add_score(self):
        self.score += 1
        self.refresh()
