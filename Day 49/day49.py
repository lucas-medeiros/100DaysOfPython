# @author   Lucas Cardoso de Medeiros
# @since    12/12/2022
# @version  1.0

# Automating Job Applications on LinkedIn

# NOTE: Do not enable 2-factor authentication/phone number verification while we are using Selenium. If you don't
# want to use your primary account for this project, feel free to set up a new LinkedIn account.

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

EMAIL = "test@gmail.com"
PASSWORD = "password123"
PHONE = "123456789"
URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3284242595&f_AL=true&f_WT=2&geoId=106057199&keywords=python' \
      '%20developer&location=Brasil&refresh=true&sortBy=R '
chrome_driver_path = "C:\Development\chromedriver.exe"


service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)
driver.maximize_window()
driver.get(URL)

# Go to log in form
signin_button = driver.find_element(By.LINK_TEXT, "Entrar")
signin_button.click()

# Submit form information
sleep(1)
email_input = driver.find_element(By.ID, "username")
email_input.send_keys(EMAIL)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

# Locate the apply button
sleep(1)
apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
apply_button.click()

# If application requires phone number and the field is empty, then fill in the number.
sleep(1)
phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

# Submit the application
submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()

# Quit
sleep(1)
print("Application submitted")
driver.quit()
