# @author   Lucas Cardoso de Medeiros
# @since    27/06/2022
# @version  1.0

# Pong Game

import time
from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TOP_LIMIT = 280
SCREEN_SIDE_LIMIT = 320
screen = Screen()


def screen_setup():
    """Sets screen parameters"""
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("My Pong Game")
    screen.tracer(0)


def keyboard_setup(l_player, r_player):
    screen.listen()
    screen.onkey(key="q", fun=l_player.up)
    screen.onkey(key="a", fun=l_player.down)

    screen.onkey(key="o", fun=r_player.up)
    screen.onkey(key="l", fun=r_player.down)


def screen_refresh(sleep):
    """Waits 0.1s and updates the screen"""
    time.sleep(sleep)
    screen.update()


def pong_game():
    """Main game logic"""
    l_player = Player(side="left")
    r_player = Player(side="right")
    ball = Ball(speed=0.1)
    scoreboard = Scoreboard()
    keyboard_setup(l_player, r_player)
    game_running = True

    while game_running:
        screen_refresh(ball.move_speed)

        # Ball movement
        ball.move()

        # Ball collision with up and down walls
        if ball.ycor() > SCREEN_TOP_LIMIT or ball.ycor() < -SCREEN_TOP_LIMIT:
            ball.bounce()

        # Ball collision with player
        if (ball.xcor() > SCREEN_SIDE_LIMIT and r_player.distance(ball) < 50) \
                or (ball.xcor() < -SCREEN_SIDE_LIMIT and l_player.distance(ball) < 50):
            ball.player_bounce()

        # Right player misses and Left player scores
        if ball.xcor() > (SCREEN_WIDTH / 2):
            scoreboard.add_l_score()
            ball.restart()

        # Left player misses and Right player scores
        if ball.xcor() < -(SCREEN_WIDTH / 2):
            scoreboard.add_r_score()
            ball.restart()


if __name__ == '__main__':
    screen_setup()
    pong_game()
    screen.exitonclick()
