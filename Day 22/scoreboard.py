from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", "60", "normal")
LEFT_SCORE_POS = (-100, 200)
RIGHT_SCORE_POS = (100, 200)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-100, 200)
        self.color("white")
        self.speed("fastest")
        self.l_score = 0
        self.r_score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(LEFT_SCORE_POS)
        self.write(arg=f"{self.l_score}", move=False, align=ALIGN, font=FONT)
        self.goto(RIGHT_SCORE_POS)
        self.write(arg=f"{self.r_score}", move=False, align=ALIGN, font=FONT)

    def add_l_score(self):
        self.l_score += 1
        self.refresh()

    def add_r_score(self):
        self.r_score += 1
        self.refresh()
