from turtle import Turtle


ALIGN = "center"
FONT = ("Courier", "15", "normal")
POS = (-230, 250)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(POS)
        self.color("black")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Refresh scoreboard"""
        self.clear()
        self.goto(POS)
        self.write(arg=f"Level: {self.level}", move=False, align=ALIGN, font=FONT)

    def increase_level(self):
        """Increment level"""
        self.level += 1
        self.refresh()

    def game_over(self):
        """Prints game over message"""
        self.home()
        self.write(arg=f"GAME OVER", move=False, align=ALIGN, font=FONT)
