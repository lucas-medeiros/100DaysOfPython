# @author   Lucas Cardoso de Medeiros
# @since    28/08/2023
# @version  1.0


"""Write Python code to play the Google Dinosaur Game.
On Chrome, when you try to access a website and your internet is down, you see a little dinosaur.
Apparently because dinosaurs have short arms and they "can't reach" your website.
On this page, there is a hidden game, if you hit space bar you can play the Dinosaur run game.
Alternatively you can access the game directly here:
https://elgoog.im/t-rex/
Your goal today is to write a Python script to automate the playing of this game. Your program will look at the pixels
on the screen to determine when it needs to hit the space bar and play the game automatically."""


import pyautogui
import time
from PIL import ImageGrab


GAME_START = (925, 550)


class DinosaurGame:
    def __init__(self):
        self.jump_sleep = 0.2  # Adjust this delay based on your system's performance
        self.regular_sleep = 0.1
        self.x, self.y, self.width, self.height = 370, 775, 150, 150  # Define the area to analyze for collision

    def is_colliding(self):
        # Capture the screen in the defined area
        screen = ImageGrab.grab(bbox=(self.x, self.y, self.x + self.width, self.y + self.height))

        # Check for dark pixels indicating obstacles
        for pixel in screen.getdata():
            r, g, b = pixel
            if r < 100 and g < 100 and b < 100:  # Adjust the threshold values as needed
                return True
        return False

    def check_area(self):
        pyautogui.moveTo(self.x, self.y)
        time.sleep(2)

        pyautogui.moveTo(self.x, self.y + self.height)
        time.sleep(2)

        pyautogui.moveTo(self.x + self.width, self.y)
        time.sleep(2)

        pyautogui.moveTo(self.x + self.width, self.y + self.height)
        time.sleep(2)

    @classmethod
    def jump(cls):
        pyautogui.press('space')

    def run(self):
        # self.check_area()

        print("Starting Chrome Dinosaur Game Automation...")
        time.sleep(2)

        pyautogui.click(GAME_START[0], GAME_START[1])
        self.jump()

        while True:
            if self.is_colliding():
                self.jump()
                time.sleep(self.jump_sleep)
            else:
                time.sleep(self.regular_sleep)


if __name__ == "__main__":
    game = DinosaurGame()
    game.run()
