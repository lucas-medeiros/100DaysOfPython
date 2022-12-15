# @author   Lucas Cardoso de Medeiros
# @since    15/12/2022
# @version  1.0
import json

# Data entry job automation

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.zillow.com"
SEARCH_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
             "%22mapBounds%22%3A%7B%22north%22%3A37.865613447952974%2C%22east%22%3A-122.2278658128552%2C%22south%22" \
             "%3A37.647921346964594%2C%22west%22%3A-122.62955343492551%7D%2C%22isMapVisible%22%3Atrue%2C" \
             "%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C" \
             "%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22" \
             "%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22" \
             "%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22" \
             "%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C" \
             "%22regionType%22%3A6%7D%5D%2C%22mapZoom%22%3A12%7D "
FORM_URL = "https://forms.gle/2Lhs1QDqGLs3e8SE7"
HEADERS = {
    "User-Agent": "Defined",
    "Accept-Language": "pt-BR,pt;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5",
}
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"


class DataManager:
    def __init__(self):
        self.soup = None
        self.driver = None
        self.properties = {}

    def get_soup(self):
        """Create Soup object"""
        response = requests.get(url=SEARCH_URL, headers=HEADERS)
        web_page = response.text
        self.soup = BeautifulSoup(web_page, "html.parser")

    def get_properties(self):
        """Scrap web for data"""
        # Create list with all addresses, except the ones with blank text
        addresses = [link.getText() for link in self.soup.find_all(name="a", class_="property-card-link") if
                     link.getText() != ""]

        # Create list with all links, except the ones with internal path only
        links = [link['href'] for link in self.soup.find_all(name="a", class_="property-card-link") if
                 'http' in link['href']]
        # Fill the list with the base site URL for the missing links
        for _ in range(len(addresses)):
            links.append(BASE_URL)

        # Create list with all valid prices
        prices = [price.getText() for price in self.soup.select(selector=".property-card-data span") if
                  '$' in price.getText()]
        # Remove duplicates and cast to float
        prices = [float(price[1:6].replace(",", ".")) for price in list(dict.fromkeys(prices))]

        # Create dictionary with all the scrapped data
        for i in range(len(addresses)):
            self.properties[i] = {
                'address': addresses[i],
                'price': prices[i],
                'link': links[i]
            }

    def print_properties(self):
        """Print collected data in json format"""
        print(json.dumps(self.properties, indent=4))

    def get_driver(self, driver_path):
        """Create driver object"""
        service = Service(driver_path)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()

    def send_data(self):
        """Send collected data to Google Forms"""
        self.driver.get(FORM_URL)

        for key in self.properties:
            # Get form elements
            sleep(2)
            address_question = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
            )
            price_question = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
            )
            link_question = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
            )
            send_button = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
            )

            # Input information
            sleep(1)
            address_question.send_keys(self.properties[key]['address'])
            price_question.send_keys(self.properties[key]['price'])
            link_question.send_keys(self.properties[key]['link'])

            # Send information
            send_button.click()
            print(f"Data sent - payload {int(key) + 1}/{len(self.properties)}")

            # Go back to the form to send another answer
            sleep(2)
            self.driver.find_element(By.TAG_NAME, "a").click()

    def quit(self):
        """Quit browser"""
        self.driver.quit()


bot = DataManager()
bot.get_soup()
bot.get_properties()
bot.print_properties()
bot.get_driver(CHROME_DRIVER_PATH)
bot.send_data()
bot.quit()
