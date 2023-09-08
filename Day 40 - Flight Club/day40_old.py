# @author   Lucas Cardoso de Medeiros
# @since    17/08/2022
# @version  1.0

# Flight Deal Finder for multiple users

import requests
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from user_manager import UserManager
from notification_manager import NotificationManager


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
user_manager = UserManager()

ORIGIN_CITY_IATA = "CWB"

print("Welcome to the Flight Club.\nWe find the best deals and email you!\n")

if "y" in input("New user? "):
    user_manager.register_user()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city=destination["city"],
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is None:
        continue
    if flight.price < destination["lowestPrice"]:

        users = user_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        msg = f"Subject:Flight Deal!\n\nLow price alert!\nOnly R${flight.price} to fly from " \
              f"{flight.origin_city}-{flight.origin_airport} " \
              f"to {flight.destination_city}-{flight.destination_airport}, " \
              f"from {flight.out_date} to {flight.return_date}.\nDon't miss!"

        if flight.stop_overs > 0:
            msg += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
        msg += f"\nhttps://www.google.com.br/flights?hl=pt#flt={ORIGIN_CITY_IATA}.{destination['iataCode']}." \
               f"{flight.out_date}*{ORIGIN_CITY_IATA}.{destination['iataCode']}.{flight.return_date} "
        print(msg)
        notification_manager.send_emails(
            msg=msg.encode('utf-8'),
            emails=emails
        )
