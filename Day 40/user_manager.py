import requests

# SHEETY PARAMETERS
SHEETY_USERNAME = "12d5544606eac08f1c286ae5355daa0b"
PROJECT_NAME = "flightDeals"
SHEET_NAME = "users"

SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
SHEETY_HEADERS = {
    "Authorization": "Basic emVkbHVjYXM6cHVjQDE4MzA="
}


class UserManager:
    # This class is responsible for talking to the Users Sheet.
    def __init__(self):
        self.data = {}
        self.read_data()

    def register_user(self):
        """Get information and register new user"""
        first_name = input("What's your first name? ")
        last_name = input("What's your last name? ")
        email = input("What's your email? ")
        confirm_email = input("Type your email again? ")
        if email != confirm_email:
            print("Emails don't match")
        else:
            print("You're in the club!")
            params = {
                "user": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email,
                }
            }
            return requests.post(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS, json=params)

    def get_data(self):
        return self.data

    def read_data(self):
        self.data = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS).json()["users"]

    def update_row(self, id, params):
        return requests.put(url=f"{SHEETY_ENDPOINT}/{id}", headers=SHEETY_HEADERS, json=params)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_ENDPOINT
        try:
            response = requests.get(customers_endpoint, headers=SHEETY_HEADERS)
            data = response.json()
            self.data = data["users"]
        except KeyError:
            print(f"KeyError:\n {response.text}")
        return self.data
