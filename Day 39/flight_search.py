import requests
from flight_data import FlightData
import datetime


# TEQUILA PARAMETERS
TEQUILA_KEY = "3k6jytLk7_sPKmXAk_StY3bdW1xcqLQk"
LOCATIONS_ENDPOINT = f"https://tequila-api.kiwi.com/locations/query"
SEARCH_ENDPOINT = f"https://tequila-api.kiwi.com/v2/search"
TEQUILA_HEADER = {
    "apiKey": TEQUILA_KEY,
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def getIATACode(self, query, locale="en-US", location_types="city", limit=1, active_only="True", sort="name"):
        params = {
            "term": query,
            "locale": locale,
            "location_types": location_types,
            "limit": limit,
            "active_only": active_only,
            "sort": sort
        }
        response = requests.get(url=LOCATIONS_ENDPOINT, headers=TEQUILA_HEADER, params=params)
        return response.json()["locations"][0]["code"]

    def search_flight(self, fly_from, fly_to, date_from, date_to, nights_in_dst_from, nights_in_dst_to,
                      flight_type="round", one_per_date=1, adults=2, curr="BRL", vehicle_type="aircraft"):
        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": nights_in_dst_from,
            "nights_in_dst_to": nights_in_dst_to,
            "flight_type": flight_type,
            "one_per_date": one_per_date,
            "adults": adults,
            "curr": curr,
            "vehicle_type": vehicle_type,
        }
        response_data = requests.get(url=SEARCH_ENDPOINT, headers=TEQUILA_HEADER, params=params).json()["data"][0]
        return FlightData(
            fly_from_airport=response_data["flyFrom"],
            fly_from_city=response_data["cityFrom"],
            fly_to_airport=response_data["cityCodeTo"],
            fly_to_city=response_data["cityTo"],
            date_from=datetime.datetime.today().strftime('%d/%m/%Y'),
            date_to=(datetime.datetime.now() + datetime.timedelta(days=(6 * 30))).strftime('%d/%m/%Y'),
            price=response_data["price"]
        )
