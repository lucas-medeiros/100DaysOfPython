import random
from turtle import Turtle


STEP = 20
UP_RIGHT = 45
UP_LEFT = 135
DOWN_LEFT = 225
DOWN_RIGHT = 315


class Ball(Turtle):

    def __init__(self, speed):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slow")
        self.move_speed = speed
        self.penup()
        self.home()
        self.setheading(UP_RIGHT)

    def move(self):
        if self.heading() == UP_RIGHT:
            self.goto(self.xcor() + STEP, self.ycor() + STEP)
        elif self.heading() == UP_LEFT:
            self.goto(self.xcor() - STEP, self.ycor() + STEP)
        elif self.heading() == DOWN_LEFT:
            self.goto(self.xcor() - STEP, self.ycor() - STEP)
        elif self.heading() == DOWN_RIGHT:
            self.goto(self.xcor() + STEP, self.ycor() - STEP)

    def bounce(self):
        if self.heading() == UP_RIGHT:
            self.setheading(DOWN_RIGHT)
        elif self.heading() == UP_LEFT:
            self.setheading(DOWN_LEFT)
        elif self.heading() == DOWN_LEFT:
            self.setheading(UP_LEFT)
        elif self.heading() == DOWN_RIGHT:
            self.setheading(UP_RIGHT)

    def player_bounce(self):
        if self.heading() == UP_RIGHT:
            self.setheading(UP_LEFT)
        elif self.heading() == UP_LEFT:
            self.setheading(UP_RIGHT)
        elif self.heading() == DOWN_LEFT:
            self.setheading(DOWN_RIGHT)
        elif self.heading() == DOWN_RIGHT:
            self.setheading(DOWN_LEFT)
        self.move_speed *= 0.9

    def restart(self):
        current_heading = self.heading()
        self.home()
        if current_heading == UP_RIGHT or current_heading == DOWN_RIGHT:
            self.setheading(DOWN_LEFT)
        else:
            self.setheading(UP_RIGHT)
        self.move_speed = 0.1
