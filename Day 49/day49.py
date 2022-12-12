# @author   Lucas Cardoso de Medeiros
# @since    12/12/2022
# @version  1.0

# Automating Job Applications on LinkedIn

# NOTE: Do not enable 2-factor authentication/phone number verification while we are using Selenium. If you don't
# want to use your primary account for this project, feel free to set up a new LinkedIn account.

from selenium import webdriver
from selenium.common import NoSuchElementException
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

sleep(3)
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    sleep(2)

    # Try to locate the apply button, if it can't locate then skip the job.
    try:
        apply_button = driver.find_elements(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        sleep(2)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # If the submit_button is a "Next" button, then this is a multistep application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        sleep(1)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

sleep(3)
driver.quit()
