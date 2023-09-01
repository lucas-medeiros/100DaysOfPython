# @author   Lucas Cardoso de Medeiros
# @since    31/08/2023
# @version  1.0


# Strava data compiler App


"""Automate some aspect of your life using Python.

You've learnt about automation with Python and Selenium. It's your turn to get creative and automate some aspect of
your life using what you have learnt. This could be an aspect of your job, your schoolwork, your home, your chores.
Think about your week and everything that you do on a regular basis, when do you feel like a robot? Which jobs do you
find tedious and boring? Can it be automated?

Here are some stories for inspiration:
Automate an email to your boss to ask for a raise every 3 months.
Automate your lights, so they switch on when your phone is within the radius of your house.
Automatically organize the files in your downloads folder based on a file type.
Automate your gym class bookings.
Automate your library book renewals.
Automate your job.
Automate your home chores.

Personally, I had a job in a hospital where I had to arrange all the doctors' shifts in my department (normal day,
long day, night shift). It would depend on when they wanted to take annual leave/vacation and the staffing
requirements. It started out in an Excel spreadsheet, by the time I was done with it, it was fully automated with
Python, and doctors were able to view a live version of the rota to see when they can take time off. The code took an
evening to write, and it saves me 3 hours per week. (More time to watch Netflix and eat ice cream). Once you're done
with the assignment, let us know what you automated in your life, and maybe it will inspire another student!"""


from datetime import timedelta
import pandas as pd
import requests
import csv

BASE_URL = "https://www.strava.com"

CLIENT_ID = "YOUR_CLIENT_ID_HERE"
CLIENT_SECRET = "YOUR_CLIENT_SECRET_HERE"
CODE = "YOUR_CLIENT_CODE_HERE"
ACCESS_TOKEN = "YOUR_CLIENT_ACCESS_TOKEN_HERE"

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "*/*",
}

FILE_NAME = "running_activities"


def handle_api_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(err)
            return None

    return wrapper


@handle_api_exceptions
def login():
    headers = {"Content-Type": "application/json", "Accept": "*/*"}
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": CODE,
        "grant_type": "authorization_code"
    }
    return requests.post(url=f"{BASE_URL}/oauth/token", params=params, headers=headers)


@handle_api_exceptions
def get_athlete():
    return requests.get(url=f"{BASE_URL}/api/v3/athlete", headers=HEADERS)


@handle_api_exceptions
def get_athlete_activities():
    return requests.get(url=f"{BASE_URL}/api/v3/athlete/activities", headers=HEADERS)


def get_activities_data():
    data = []
    activities = get_athlete_activities()
    try:
        for activity in activities:
            if activity['sport_type'] == "Run":
                average_heartrate = 0.0
                max_heartrate = 0.0
                minutes, seconds = divmod(((activity['moving_time'] / 60) / (activity['distance'] / 1000) * 60), 60)
                if activity['has_heartrate']:
                    average_heartrate = activity['average_heartrate']
                    max_heartrate = activity['max_heartrate']
                data.append(
                    {
                        "id": activity['id'],
                        "name": activity['name'],
                        "type": activity['sport_type'],
                        "distance": activity['distance'],
                        "moving_time": activity['moving_time'],
                        "total_time": str(timedelta(seconds=activity['elapsed_time'])),
                        "total_elevation_gain": int(activity['total_elevation_gain']),
                        "start_date": activity['start_date_local'],
                        "average_speed": round((activity['average_speed'] * 3.6), 2),
                        "max_speed": round((activity['max_speed'] * 3.6), 2),
                        "average_heartrate": average_heartrate,
                        "max_heartrate": max_heartrate,
                        "pace": f"{int(minutes):02d}:{int(seconds):02d}/km",
                        "upload_id": activity['upload_id'],
                    }
                )
    except KeyError as ex:
        print(f"KeyError on data key: {ex}")
        return None
    except TypeError as ex:
        print(f"TypeError on data: {ex}\nCheck the http get request status code on /athlete/activities")
        return None
    return data


def export_activities_data_to_csv(activities):
    csv_header = ["id", "name", "type", "distance", "moving_time", "total_time", "total_elevation_gain", "start_date",
                  "average_speed", "max_speed", "average_heartrate", "max_heartrate", "pace", "upload_id"]

    with open(file=f"{FILE_NAME}.csv", mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_header)
        writer.writeheader()
        writer.writerows(activities)


def export_activities_data_to_excel(activities, export=True):
    data_frame = pd.DataFrame(activities)
    if export:
        data_frame.to_excel(f"{FILE_NAME}.xlsx", index=False)
    return data_frame


if __name__ == "__main__":
    data = get_activities_data()
    export_activities_data_to_csv(activities=data)
    df = export_activities_data_to_excel(activities=data)

    # Can use df to get some data analysis on activities performance and plot some sick graphs...
