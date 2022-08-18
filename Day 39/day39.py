# @author   Lucas Cardoso de Medeiros
# @since    13/08/2022
# @version  1.0

# Flight Deal Finder

import datetime
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Update data
for city in data_manager.get_data():
    if city['iataCode'] == "":
        params = {
            "price": {
                "city": city['city'],
                "iataCode": flight_search.getIATACode(query=city['city']),
                "lowestPrice": city['lowestPrice'],
            }
        }
        data_manager.update_row(city['id'], params)

data_manager.read_data()
pprint(data_manager.get_data())

FLY_FROM = "CWB"
NIGHTS_IN_DST_FROM = 3
NIGHTS_IN_DST_TO = 7

for city in data_manager.get_data():
    print(city['lowestPrice'])
    flight_data = flight_search.search_flight(
        fly_from=FLY_FROM,
        fly_to=city['iataCode'],
        date_from=datetime.datetime.today().strftime('%d/%m/%Y'),
        date_to=(datetime.datetime.now() + datetime.timedelta(days=(6 * 30))).strftime('%d/%m/%Y'),
        nights_in_dst_from=NIGHTS_IN_DST_FROM,
        nights_in_dst_to=NIGHTS_IN_DST_TO
    )
    print(flight_data.get_price())
    if city['lowestPrice'] > flight_data.price:
        print("send notification")
        msg = f"Subject:Flight Deal!\n\n" \
              f"Low price alert!\n" \
              f"Only R${flight_data.price} to fly from " \
              f"{flight_data.fly_from_city}-{flight_data.fly_from_airport} to " \
              f"{flight_data.fly_to_city}-{flight_data.fly_to_airport}, " \
              f"from {flight_data.date_from} to {flight_data.date_to}.\nDon't miss!"
        if notification_manager.send_email(msg=msg):
            print("Notification sent")
