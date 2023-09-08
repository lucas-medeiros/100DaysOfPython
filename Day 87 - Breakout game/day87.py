# @author   Lucas Cardoso de Medeiros
# @since    19/08/2023
# @version  1.0

"""Using Python Turtle, build a clone of the 80s hit game Breakout.

Breakout was a hit game originally coded up by Steve Wozniak before he and Jobs started Apple. It's a simple game
that is similar to Pong where you use a ball and paddle to break down a wall."""

import turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_MOVE = 20
BRICK_POINTS = 10
SCORE_FONT = ("Courier", 24, "normal")


class BreakoutGame:
    def __init__(self):
        self.score_display = None
        self.ball = None
        self.paddle = None
        self.score = 0
        self.bricks = []

        self.screen = turtle.Screen()
        self.screen_setup()
        self.create_paddle()
        self.create_ball()
        self.create_bricks()
        self.create_score_display()
        self.keyboard_setup()

    def screen_setup(self):
        """Sets screen parameters"""
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Breakout")
        self.screen.tracer(0)

    def create_paddle(self):
        """Create the paddle"""
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=1, stretch_len=6)
        self.paddle.penup()
        self.paddle.goto(0, -250)

    def create_ball(self):
        """Create the ball"""
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 2
        self.ball.dy = -2

    def create_bricks(self):
        """Create the bricks"""
        for i in range(5):
            for j in range(10):
                brick = turtle.Turtle()
                brick.speed(0)
                brick.shape("square")
                brick.color("blue")
                brick.shapesize(stretch_wid=1, stretch_len=3)  # Increase width of bricks
                brick.penup()
                brick.goto(-380 + j * 80, 250 - i * 30)
                self.bricks.append(brick)

    def create_score_display(self):
        """Create the score display"""
        self.score_display = turtle.Turtle()
        self.score_display.speed(0)
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(0, 260)
        self.score_display.write("Score: {}".format(self.score), align="center", font=SCORE_FONT)

    def move_right(self):
        x = self.paddle.xcor() + PADDLE_MOVE
        self.paddle.setx(x)

    def move_left(self):
        x = self.paddle.xcor() - PADDLE_MOVE
        self.paddle.setx(x)

    def stop_paddle(self):
        self.paddle.dx = 0  # Stop paddle movement

    def keyboard_setup(self):
        self.screen.listen()
        self.screen.onkeypress(self.move_right, "Right")
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeyrelease(self.stop_paddle, "Right")
        self.screen.onkeyrelease(self.stop_paddle, "Left")

    def increase_score(self):
        """increase player's current score"""
        self.score += BRICK_POINTS
        self.score_display.clear()
        self.score_display.write("Score: {}".format(self.score), align="center", font=SCORE_FONT)

    def run(self):
        """Main game logic"""
        while True:
            self.screen.update()

            # Move the ball
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            # Boundary checking
            screen_x_limit = SCREEN_WIDTH / 2 - 10
            screen_y_limit = SCREEN_HEIGHT / 2 - 10
            if self.ball.xcor() > screen_x_limit or self.ball.xcor() < -screen_x_limit:
                self.ball.dx *= -1

            if self.ball.ycor() > screen_y_limit:
                self.ball.dy *= -1

            if self.ball.ycor() < -screen_y_limit:
                self.ball.goto(0, 0)
                self.ball.dy *= -1

            # Paddle and ball collisions
            if ((self.ball.dy < 0)
                    and (self.ball.ycor() < -240)
                    and (self.paddle.xcor() - 60 < self.ball.xcor() < self.paddle.xcor() + 60)):
                self.ball.dy *= -1

            # Brick collisions
            for brick in self.bricks:
                if ((brick.ycor() + 15 > self.ball.ycor() > brick.ycor() - 15)
                        and (brick.xcor() - 30 < self.ball.xcor() < brick.xcor() + 30)):
                    brick.goto(1000, 1000)  # Move the brick out of sight
                    self.ball.dy *= -1
                    self.increase_score()

                if self.score == len(self.bricks) * BRICK_POINTS:
                    self.ball.goto(0, -50)
                    self.ball.dx = 0
                    self.ball.dy = 0
                    self.score_display.goto(0, 0)
                    self.score_display.color("red")
                    self.score_display.write("Game over!\nScore: {}".format(self.score),
                                             align="center",
                                             font=("Courier", 36, "normal"))
                    self.screen.exitonclick()


if __name__ == '__main__':
    app = BreakoutGame()
    app.run()
