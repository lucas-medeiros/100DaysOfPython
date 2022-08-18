import requests

# SHEETY PARAMETERS
SHEETY_USERNAME = "12d5544606eac08f1c286ae5355daa0b"
PROJECT_NAME = "flightDeals"
SHEET_NAME = "prices"

SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
SHEETY_HEADERS = {
    "Authorization": "Basic emVkbHVjYXM6cHVjQDE4MzA="
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = {}
        self.read_data()

    def get_data(self):
        return self.data

    def read_data(self):
        self.data = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS).json()["prices"]

    def update_row(self, id, params):
        return requests.put(url=f"{SHEETY_ENDPOINT}/{id}", headers=SHEETY_HEADERS, json=params)

