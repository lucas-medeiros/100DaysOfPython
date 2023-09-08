import requests

# SHEETY PARAMETERS
SHEETY_USERNAME = "12d5544606eac08f1c286ae5355daa0b"
PROJECT_NAME = "flightDeals"
PRICES_SHEET_NAME = "prices"
USERS_SHEET_NAME = "users"

SHEETY_HEADERS = {
    "Authorization": "Basic emVkbHVjYXM6cHVjQDE4MzA="
}

SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{PROJECT_NAME}/{PRICES_SHEET_NAME}"
SHEETY_USERS_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{PROJECT_NAME}/{USERS_SHEET_NAME}"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        try:
            response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=SHEETY_HEADERS)
            data = response.json()
            self.destination_data = data["prices"]
        except KeyError:
            print(f"Sheety API error:\n{response.text}")
            exit(-1)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
