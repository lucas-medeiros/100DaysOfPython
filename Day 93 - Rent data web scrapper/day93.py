# @author   Lucas Cardoso de Medeiros
# @since    25/08/2023
# @version  1.0


"""Build a custom web scraper to collect data on things that you are interested in.
Using what you have learnt about web scraping, scrape a website for data that you are interested in. Try to build a
CSV with the scraped data. What you scrape is up to you.

Data subject: Rent data from ZapImoveis website on Curitiba, PR, Brazil"""

from bs4 import BeautifulSoup
import requests
import csv
import json


""" ---- FILTERS ---- """
TYPES = ("apartamento_residencial,"
         "studio_residencial,"
         "casa_residencial,"
         "sobrado_residencial,"
         "condominio_residencial,"
         "cobertura_residencial")
AMENITIES = "Aceita%20pets"
NUM_ROOMS = "3"
NUM_BATHROOMS = "1,2,3"
PARKING_SPOTS = "1,2"
MAX_PRICE = "2500"
MIN_AREA = "50"
""" ----------------- """

FILE_NAME = "rent_data"
SEARCH_URL = (
    f"https://www.zapimoveis.com.br/aluguel/apartamentos/pr+curitiba/"
    f"{NUM_ROOMS}-quartos/"
    f"?transacao=aluguel"
    f"&onde=,Paran%C3%A1,Curitiba,,,,,city,BR%3EParana%3ENULL%3ECuritiba,-25.437238,-49.269973,"
    f"&tipos={TYPES}"
    f"&pagina=1"
    f"&amenities={AMENITIES}"
    f"&banheiros={NUM_BATHROOMS}"
    f"&quartos={NUM_ROOMS}"
    f"&vagas={PARKING_SPOTS}"
    f"&precoMaximo={MAX_PRICE}"
    f"&areaTotalMinima={MIN_AREA}"
)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 "
                  "Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-CA,en;q=0.9,de-DE;q=0.8,de;q=0.7,en-GB;q=0.6,en-US;q=0.5,fr;q=0.4",
    "Accept-Encoding": "utf-8"
}


class DataScraper:
    def __init__(self):
        self.soup = None
        self.data = {}

    def get_soup(self):
        """Create Soup object"""
        response = requests.get(url=SEARCH_URL, headers=HEADERS)
        web_page = response.text
        self.soup = BeautifulSoup(web_page, "html.parser")

    def get_properties(self):
        """Scrap web for data"""
        floor_sizes = []
        room_counts = []
        bathroom_counts = []
        parking_counts = []

        locations = [card.getText() for card in self.soup.find_all(name="h2", class_="card__address")
                     if card.getText() != ""]

        addresses = [card.getText() for card in self.soup.find_all(name="p", class_="card__street")
                     if card.getText() != ""]

        descriptions = [card.getText().replace("\n\n", " ").replace("\n", " ") for card in
                        self.soup.find_all(name="p", class_="card__description") if card.getText() != ""]

        amenities = [card.getText().replace(" m²", "") for card in
                     self.soup.find_all(name="section", class_="card__amenities") if card.getText() != ""]

        for amenity in amenities:
            floor_sizes.append(int(amenity[:-3]))
            room_counts.append(int(amenity[-3]))
            bathroom_counts.append(int(amenity[-2]))
            parking_counts.append(int(amenity[-1]))

        total_prices = [int(card.getText().split('A')[0].replace("Total R$ ", "").replace(".", "")) for card in
                        self.soup.find_all(name="div", class_="listing-price") if card.getText() != ""]

        rent_prices = [int(card.getText().split("R$ ")[-1].replace(".", "")) for card in
                       self.soup.find_all(name="div", class_="listing-price") if card.getText() != ""]

        condo_prices = [total - rent for total, rent in zip(total_prices, rent_prices)]

        links = [card['href'] for card in self.soup.find_all(name="a", class_="result-card") if 'http' in card['href']]

        try:
            for i in range(len(links)):
                self.data[i] = {
                    'url': links[i],
                    'location': locations[i],
                    'address': addresses[i],
                    'total_price': total_prices[i],
                    'rent_price': rent_prices[i],
                    'condo_price': condo_prices[i],
                    'floor_size': floor_sizes[i],
                    'rooms': room_counts[i],
                    'bathrooms': bathroom_counts[i],
                    'parking': parking_counts[i],
                    'description': descriptions[i]
                }

        except IndexError as e:
            print(f"Inconsistent data\nIndex Error: {e}")
            exit(-1)

    def print_data(self):
        """Print collected data in json format"""
        print(json.dumps(self.data, indent=4, ensure_ascii=False))

    def export_data_to_csv(self, filename):
        """Create a csv file and export data"""
        filename += ".csv"
        fieldnames = ["url", "location", "address", "total_price", "rent_price", "condo_price",
                      "floor_size", "rooms", "bathrooms", "parking", "description"]

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in self.data.values():
                writer.writerow(item)

        print(f"\nData exported to file: {filename}")

    def run(self):
        self.get_soup()
        self.get_properties()
        self.print_data()
        self.export_data_to_csv(FILE_NAME)


if __name__ == "__main__":
    bot = DataScraper()
    bot.run()
