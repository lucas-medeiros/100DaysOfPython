# @author   Lucas Cardoso de Medeiros
# @since    09/07/2022
# @version  1.0

# Using APIs

import smtplib
import time
from datetime import datetime
import requests


FROM_EMAIL = "zedlucastest@gmail.com"
TO_EMAIL = "lucascarmed@gmail.com"
PASSWORD = "osndmxppboqkapvs"
MY_LAT = -25.424809
MY_LONG = -49.245135


def send_email(from_add, password, to_add, msg):
    """Send Email, return True if was successful"""
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=from_add, password=password)
            connection.sendmail(
                from_addr=from_add,
                to_addrs=to_add,
                msg=msg
            )
        return True
    except smtplib.SMTPAuthenticationError:
        print("Error: SMTPAuthenticationError")
        return False


# ISS Location API
def iss_location():
    """Returns a tuple with ISS currents location (lat, lng)"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    return float(data["iss_position"]["longitude"]), float(data["iss_position"]["latitude"])


def is_iss_overhead():
    """Returns True if it's close, otherwise returns False"""
    iss_loc = iss_location()
    print(iss_loc)
    if MY_LAT - 5 <= iss_loc[0] <= MY_LAT + 5 and MY_LONG - 5 <= iss_loc[1] <= MY_LONG + 5:
        return True
    else:
        return False


def is_dark():
    """Returns True if it's dark, returns False if it's day time"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    hour_now = datetime.now().hour
    if hour_now > int(data["results"]["sunset"][11:13]) or hour_now < int(data["results"]["sunrise"][11:13]):
        return True
    else:
        return False


while True:
    if is_dark() and is_iss_overhead():
        send_email(
            from_add=FROM_EMAIL,
            password=PASSWORD,
            to_add=TO_EMAIL,
            msg="Subject:Look Up!\n\nISS is now visible and above your head, look up! =)"
        )
    time.sleep(60)
