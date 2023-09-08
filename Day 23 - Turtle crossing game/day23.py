# @author   Lucas Cardoso de Medeiros
# @since    28/06/2022
# @version  1.0

# Turtle Crossing Game

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TOP_LIMIT = 280
SCREEN_SIDE_LIMIT = 320
screen = Screen()


def screen_setup():
    """Sets screen parameters"""
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("white")
    screen.title("Turtle Crossing Game")
    screen.tracer(0)


def keyboard_setup(turtle):
    """Set keyboard listeners to call functions"""
    screen.listen()
    screen.onkey(key="Up", fun=turtle.up)


def screen_refresh():
    """Waits 0.1s and updates the screen"""
    time.sleep(0.1)
    screen.update()


def turtle_race():
    """Main game logic"""
    turtle = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()
    keyboard_setup(turtle)
    game_running = True

    while game_running:
        screen_refresh()

        # Generate new car and move all the cars
        car_manager.generate_car()
        car_manager.move_cars()

        # Detects collision with one of the cars
        if car_manager.is_crashed(turtle):
            scoreboard.game_over()
            game_running = False

        # Turtle made across
        if turtle.finished():
            scoreboard.increase_level()
            turtle.reset_position()


if __name__ == '__main__':
    screen_setup()
    turtle_race()
    screen.exitonclick()
