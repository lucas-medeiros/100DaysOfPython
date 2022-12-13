from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

PROMISED = 600
SPEED_TEST_URL = "https://www.speedtest.net/"

TWITTER_EMAIL = "YOUR_TWITTER_EMAIL"
TWITTER_PASSWORD = "YOUR_TWITTER_PASSWORD"

TWITTER_URL = "https://twitter.com/home"
EMAIL_INPUT_XPATH = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[' \
                    '5]/label/div/div[2]/div/input'
TWEET_XPATH = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[' \
              '1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[' \
              '1]/div/div/div/div/div/div[2]/div'
TWEET_BUTTON_XPATH = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[' \
                     '1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div '


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        service = Service(driver_path)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        print("Get internet speed")
        self.driver.get(SPEED_TEST_URL)

        # Start speed test
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, "start-text").click()

        # Wait for test concluded and collect results
        sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"Test results\nDOWNLOAD: {self.down}\nUPLOAD: {self.up}")

    def tweet_at_provider(self):
        print("Tweet at provider")
        self.driver.get(TWITTER_URL)

        # Load login form and submit email
        sleep(3)
        email_input = self.driver.find_element(By.NAME, "text")
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)

        # Load next form and submit password
        sleep(1)
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        # Load home page and write tweet
        sleep(1)
        tweet_input = self.driver.find_element(By.XPATH, TWEET_XPATH)
        sleep(1)
        tweet = f"Hey Ligga Telecom, why is my internet speed {self.down}MB download e {self.up}MB upload when I pay " \
                f"for {PROMISED}MB on both?"
        tweet_input.send_keys(tweet)

        # Send tweet
        sleep(1)
        tweet_button = self.driver.find_element(By.XPATH, TWEET_BUTTON_XPATH)
        print(f"Tweeting: {tweet}")
        tweet_button.click()

        # Quit browser
        sleep(3)
        self.driver.quit()
