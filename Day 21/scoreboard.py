from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", "15", "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.home()
        self.write(arg=f"Game over!", move=False, align=ALIGN, font=FONT)
