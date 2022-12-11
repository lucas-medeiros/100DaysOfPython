# @author   Lucas Cardoso de Medeiros
# @since    09/12/2022
# @version  1.0

# Selenium Webdriver Browser - Wikipedia's interaction

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'https://en.wikipedia.org/wiki/Main_Page'
chrome_driver_path = "C:\Development\chromedriver.exe"
XPATH = '//*[@id="articlecount"]/a[1]'

service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)
driver.maximize_window()
driver.get(URL)

element = driver.find_element(By.XPATH, XPATH)
# element.click()

portuguese = driver.find_element(By.LINK_TEXT, "Português")
# portuguese.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()
