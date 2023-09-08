# @author   Lucas Cardoso de Medeiros
# @since    09/12/2022
# @version  1.0

# Selenium Webdriver Browser - Get list of upcoming events on python.org

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = 'https://www.python.org/'
chrome_driver_path = "C:\Development\chromedriver.exe"
XPATH = '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li'

service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)
driver.maximize_window()
driver.get(URL)

events = {}
for i in range(1, 6):
    event_element = driver.find_element(By.XPATH, f"{XPATH}[{i}]")
    event_info = event_element.text.split("\n")
    events[i-1] = {
        'time': event_info[0],
        'name': event_info[1],
    }

print(events)
driver.quit()
