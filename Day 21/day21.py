# @author   Lucas Cardoso de Medeiros
# @since    27/06/2022
# @version  1.0

# Snake Game

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()


def screen_setup():
    """Returns screen after setup is complete"""
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)


def keyboard_setup(snake):
    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)


def screen_refresh():
    """Waits 0.1s and updates the screen"""
    time.sleep(0.1)
    screen.update()


def snake_game():
    """Main game logic"""
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    keyboard_setup(snake)
    game_running = True

    while game_running:
        screen_refresh()

        # Snake movement
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.add_score()
            snake.extend()

        # Detect collision with walls
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_running = False
            scoreboard.game_over()

        # Detect collision with tail
        if snake.is_over():
            game_running = False
            scoreboard.game_over()


if __name__ == '__main__':
    screen_setup()
    snake_game()
    screen.exitonclick()
