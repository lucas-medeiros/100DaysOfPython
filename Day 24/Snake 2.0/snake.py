from turtle import Turtle


STEP = 20
BODY_SIZE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake(3)
        self.head = self.body[0]

    def create_snake(self, size):
        for i in range(size):
            self.add_body((-BODY_SIZE * i, 0))

    def add_body(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.body.append(new_snake)

    def reset_snake(self):
        for body_part in self.body:
            body_part.hideturtle()
        self.body.clear()
        self.create_snake(3)
        self.head = self.body[0]

    def move(self):
        """Moves the snake forward"""
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i - 1].pos())
        self.head.fd(STEP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def extend(self):
        self.add_body(self.body[-1].position())

    def is_over(self):
        for body_part in self.body[1:]:
            if self.head.distance(body_part) < 10:
                return True
        return False
