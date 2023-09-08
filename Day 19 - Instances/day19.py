# @author   Lucas Cardoso de Medeiros
# @since    25/06/2022
# @version  1.0

# Turtle GUI - Games

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.hideturtle()
screen = Screen()
colors = ["purple", "blue", "green", "yellow", "orange", "red"]


def move_forward():
    timmy.fd(10)


def move_backwards():
    timmy.bk(10)


def turn_left():
    timmy.left(10)


def turn_right():
    timmy.right(10)


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


def etch_a_sketch():
    """Main etch_a_sketch game logic"""
    screen.listen()
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=turn_right)
    screen.onkey(key="d", fun=turn_left)
    screen.onkey(key="c", fun=clear_screen)
    screen.exitonclick()


def get_turtles():
    """Returns a list of colored and shaped Turtles"""
    turtles = []
    for i in range(len(colors)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        turtles.append(new_turtle)
    return turtles


def get_bet():
    return screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


def turtle_race():
    """Main turtle race game logic"""
    winner = None
    screen.setup(width=500, height=400)
    bet = get_bet()
    turtles = get_turtles()
    x = -230
    y = 130

    # Places turtles in starting positions
    for turtle in turtles:
        turtle.penup()
        turtle.goto(x=x, y=y)
        y -= 50

    while winner is None:
        for turtle in turtles:
            turtle.fd(random.randint(1, 10))
            if turtle.xcor() > 250:
                winner = turtle
                break

    if winner.color()[0] == bet:
        print(f"You won! The {winner.color()[0]} turtle won the race!")
    else:
        print(f"You lost. The {winner.color()[0]} turtle won the race!")


if __name__ == '__main__':
    turtle_race()
