from turtle import Turtle


STEP = 10
UP = 90
DOWN = 270
STARTING_Y = -270
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(UP)
        self.goto(0, STARTING_Y)

    def up(self):
        """Move up"""
        self.fd(STEP)

    def finished(self):
        """Return True if turtle is at finish line"""
        return self.ycor() > FINISH_LINE_Y

    def reset_position(self):
        """Resets turtle position"""
        self.goto(0, STARTING_Y)
