class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, fly_from_airport, fly_from_city, fly_to_airport, fly_to_city, date_from, date_to, price):
        self.fly_from_airport = fly_from_airport
        self.fly_from_city = fly_from_city
        self.fly_to_airport = fly_to_airport
        self.fly_to_city = fly_to_city
        self.date_from = date_from
        self.date_to = date_to
        self.price = price

    def get_price(self):
        return self.price
