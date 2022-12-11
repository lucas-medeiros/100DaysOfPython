# @author   Lucas Cardoso de Medeiros
# @since    10/12/2022
# @version  1.0

# Selenium Webdriver Browser and Game Playing Bot

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

URL = 'http://orteil.dashnet.org/experiments/cookie/'
chrome_driver_path = "C:\Development\chromedriver.exe"


def refresh_timeout_buy():
    return time.time() + 5


def refresh_timeout_end():
    return time.time() + 60 * 5  # 5 minutes from now


def get_cookie_amount():
    global driver

    money_element = driver.find_element(By.ID, "money").text
    if "," in money_element:
        money_element = money_element.replace(",", "")

    return int(money_element)


def buy_upgrade(upgrades, money):
    global driver

    # Find upgrades that we can currently afford
    affordable_upgrades = {}
    for cost, id in upgrades.items():
        if money > cost:
            affordable_upgrades[cost] = id

    # Purchase the most expensive affordable upgrade
    highest_price_affordable_upgrade = max(affordable_upgrades)
    to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
    driver.find_element(By.ID, to_purchase_id).click()


def get_store():
    global items, item_ids, driver

    # Get all upgrade <b> tags
    all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
    item_prices = []

    # Convert <b> text into an integer price.
    for price in all_prices:
        element_text = price.text
        if element_text != "":
            cost = int(element_text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)

    # Create dictionary of store items and prices
    store = {}
    for n in range(len(item_prices)):
        store[item_prices[n]] = item_ids[n]

    return store


def get_cookies_per_second():
    global driver
    cps = driver.find_element(By.ID, "cps")
    print(cps.text)


service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)
# driver.maximize_window()
driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")

# Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout_end = refresh_timeout_end()
timeout_buy = refresh_timeout_buy()

while True:
    cookie.click()
    if time.time() > timeout_buy:
        cookie_upgrades = get_store()
        cookie_count = get_cookie_amount()
        buy_upgrade(upgrades=cookie_upgrades, money=cookie_count)
        timeout_buy = refresh_timeout_buy()
    if time.time() > timeout_end:
        break

get_cookies_per_second()
print("Game over")
driver.quit()
