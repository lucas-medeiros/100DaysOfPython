from turtle import Turtle


STEP = 20
UP = 90
DOWN = 270
XCOR = 350


class Player(Turtle):

    def __init__(self, side):
        super().__init__()
        self.side = side
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        xcor = XCOR
        if self.side == "left":
            xcor *= -1
        self.goto(xcor, 0)

    def up(self):
        self.goto(self.xcor(), self.ycor() + STEP)

    def down(self):
        self.goto(self.xcor(), self.ycor() - STEP)
