# @author   Lucas Cardoso de Medeiros
# @since    14/12/2022
# @version  1.0

# Instagram Follower Bot

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

URL = 'https://www.instagram.com'
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
INSTAGRAM_EMAIL = "YOUR FACEBOOK LOGIN EMAI"
INSTAGRAM_PASSWORD = "YOUR FACEBOOK PASSWORD"
SIMILAR_ACCOUNT = "chefsteps"


class InstaFollower:
    def __init__(self, driver_path):
        service = Service(driver_path)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()

    def login(self):
        print("Login")
        self.driver.get(f"{URL}/accounts/login/")

        sleep(5)
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(INSTAGRAM_EMAIL)
        password.send_keys(INSTAGRAM_PASSWORD)

        sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        print("Find followers")
        sleep(2)
        self.driver.get(f"{URL}/{SIMILAR_ACCOUNT}/")

        sleep(5)
        followers = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        )
        followers.click()

        sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal element by the height of the modal"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(1)

    def follow(self):
        print("Follow accounts")
        sleep(1)

        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

    def quit(self):
        print("Exit browser")
        self.driver.quit()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
bot.quit()
