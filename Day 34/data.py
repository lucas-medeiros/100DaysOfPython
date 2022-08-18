import requests

URL = "https://opentdb.com/api.php"
PARAMS = {
    "amount": 10,
    "difficulty": "easy",
    "type": "boolean",
}


class Data:

    def __init__(self):
        self.question_data = []
        self.update_data()

    def update_data(self):
        response = requests.get(url=URL, params=PARAMS)
        response.raise_for_status()
        self.question_data = response.json()["results"]
