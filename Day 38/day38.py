# @author   Lucas Cardoso de Medeiros
# @since    11/08/2022
# @version  1.0

# Workout Tracking with Google Sheets

import datetime
import requests

# NUTRITIONIX PARAMETERS
NUTRITIONIX_USERNAME = "zedlucas"
NUTRITIONIX_APP_ID = "adf561e6"
NUTRITIONIX_APP_KEY = "YOUR_API_KEY_HERE"
NUTRITIONIX_REMOTE_USER_ID = "0"

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
    "x-remote-user-id": NUTRITIONIX_REMOTE_USER_ID,
}

GENDER = "male"
WEIGHT_KG = 70.0
HEIGHT_CM = 174.2
BIRTHDATE = datetime.date(1998, 12, 27)

# SHEETY PARAMETERS
SHEETY_USERNAME = "12d5544606eac08f1c286ae5355daa0b"
PROJECT_NAME = "myWorkouts"
SHEET_NAME = "workouts"

SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
SHEETY_HEADERS = {
    "Authorization": "Basic emVkbHVjYXM6cHVjQDE4MzA="
}


def calculate_age(birthdate):
    today = datetime.datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))


# Example input: """Ran 2 miles and walked for 3km."""
query = input("Tell me which exercises you did: ")

nutritionix_params = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": calculate_age(BIRTHDATE)
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=nutritionix_params, headers=NUTRITIONIX_HEADERS)
# print(response.text)

for exercise in response.json()["exercises"]:
    sheety_params = {
        "workout": {
            "date": datetime.datetime.today().strftime('%d/%m/%Y'),
            "time": datetime.datetime.today().strftime('%H:%M:%S'),
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=SHEETY_HEADERS)
    print(response.text)
