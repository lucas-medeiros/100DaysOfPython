# @author   Lucas Cardoso de Medeiros
# @since    28/08/2023
# @version  1.0


"""Build the classic arcade game where you shoot down alien ships.

Using Python Turtle, build the classic shoot 'em up game - space invaders game.

Your spaceship can move left and right, and it can hit some alien ships. Every second the aliens will move closer to
your ship. Once the aliens touch your ship, then it's game over. There are usually some barriers between you and the
aliens, which offers you defensive positions.

You can play the game here:
https://elgoog.im/space-invaders/"""


import time
import turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_MOVE = 20
ENEMY_MOVE = 10
ENEMIES_COUNT = 15
ENEMIES_ROWS = 3
ENEMY_M0VE_DELAY = 1
ALIEN_POINTS = 10
BULLET_SPEED = 10
SCORE_FONT = ("Courier", 20, "normal")
END_GAME_FONT = ("Courier", 36, "normal")


class SpaceInvadersGame:
    def __init__(self):
        self.enemies = []
        self.bullets = []
        self.player = None
        self.score_display = None
        self.game_over = False
        self.score = 0

        self.screen = turtle.Screen()
        self.screen_setup()
        self.player_setup()
        self.enemies_setup()
        self.score_display_setup()
        self.keyboard_setup()

    def screen_setup(self):
        """Sets screen parameters"""
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Space Invaders")
        self.screen.tracer(0)

    def player_setup(self):
        """Draw the player's spaceship"""
        self.player = turtle.Turtle()
        self.player.shape("triangle")
        self.player.color("blue")
        self.player.penup()
        self.player.speed(0)
        self.player.setposition(0, -250)
        self.player.setheading(90)
        
    def enemies_setup(self):
        """Draw {ENEMIES_ROWS} rows of {ENEMIES_COUNT} aliens each"""
        y = 300
        for _ in range(ENEMIES_ROWS):
            y -= 50
            for _ in range(ENEMIES_COUNT):
                enemy = turtle.Turtle()
                enemy.shape("circle")
                enemy.color("red")
                enemy.penup()
                enemy.speed(0)
                enemy.setposition(-350 + _ * 50, y)
                self.enemies.append(enemy)

    def score_display_setup(self):
        self.score_display = turtle.Turtle()
        self.score_display.speed(0)
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(0, 260)
        self.score_display.write("Score: {}".format(self.score), align="center", font=SCORE_FONT)

    def keyboard_setup(self):
        self.screen.listen()
        self.screen.onkeypress(self.move_right, "Right")
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.fire_bullet, "space")

    def increase_score(self):
        self.score += ALIEN_POINTS
        self.score_display.clear()
        self.score_display.write("Score: {}".format(self.score), align="center", font=SCORE_FONT)

    def fire_bullet(self):
        bullet = turtle.Turtle()
        bullet.speed(0)
        bullet.color("yellow")
        bullet.shape("square")
        bullet.shapesize(0.75, 0.25)
        bullet.penup()
        bullet.goto(self.player.xcor(), self.player.ycor())
        bullet.showturtle()
        bullet.speed = BULLET_SPEED
        self.bullets.append(bullet)

    def move_left(self):
        self.player.setx(self.player.xcor() - PLAYER_MOVE)

    def move_right(self):
        self.player.setx(self.player.xcor() + PLAYER_MOVE)

    def move_enemies(self):
        """Move enemies down {ENEMY_MOVE} positions every {ENEMY_M0VE_DELAY} seconds"""
        for enemy in self.enemies:
            enemy.sety(enemy.ycor() - ENEMY_MOVE)
        if not self.game_over:
            self.screen.ontimer(self.move_enemies, ENEMY_M0VE_DELAY * 1000)

    def move_bullets(self):
        for bullet in self.bullets:
            if bullet.isvisible():
                bullet.sety(bullet.ycor() + bullet.speed)
                self.check_bullet_collision(bullet)

    def check_bullet_collision(self, bullet):
        for enemy in self.enemies:
            if enemy.isvisible() and bullet.isvisible() and bullet.distance(enemy) < 20:
                bullet.hideturtle()
                enemy.hideturtle()
                self.bullets.remove(bullet)
                self.enemies.remove(enemy)
                self.increase_score()
                self.check_win()

    def check_win(self):
        if len(self.enemies) == 0:
            self.end_game("You win!")

    def check_lose(self):
        for enemy in self.enemies:
            if enemy.isvisible() and self.player.ycor() >= enemy.ycor():
                self.end_game("Game Over!")

    def end_game(self, message):
        self.score_display.goto(0, 0)
        self.score_display.write(message, align="center", font=END_GAME_FONT)
        self.screen.update()
        self.game_over = True
        turtle.done()

    def run(self):
        """Main game logic"""
        time.sleep(0.5)
        self.move_enemies()

        while not self.game_over:
            self.move_bullets()
            self.check_lose()
            self.screen.update()

        turtle.mainloop()


if __name__ == '__main__':
    app = SpaceInvadersGame()
    app.run()
