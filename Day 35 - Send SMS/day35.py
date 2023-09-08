# @author   Lucas Cardoso de Medeiros
# @since    12/07/2022
# @version  1.0

# Weather daily forecast

import requests
import smtplib
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

FROM_EMAIL = "zedlucastest@gmail.com"
PASSWORD = "osndmxppboqkapvs"
TO_EMAIL = "lucascarmed@gmail.com"

api_key = os.environ.get("OWM_API_KEY")
account_sid = "YOUR ACCOUNT SID"
auth_token = os.environ.get("AUTH_TOKEN")

URL = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "OWM_API_KEY"
MY_LAT = -25.424809
MY_LONG = -49.245135
PARAMS = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
    "units": "metric",
}

MODE = "email"


def send_email(from_add, password, to_add, msg):
    """Send email based on parameters, returns True if successful"""
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
    except smtplib.SMTPConnectError:
        print("Error: SMTPConnectError")
        return False


def will_rain():
    response = requests.get(url=URL, params=PARAMS)
    response.raise_for_status()
    data = response.json()
    for hour in data["hourly"][:12]:
        weather_id = hour["weather"][0]["id"]
        if int(weather_id) < 700:
            return True
    return False


if MODE == "email":
    # Send email
    if will_rain():
        msg = "Subject:Will rain\n\nIt's going to rain today.\nRemember to bring an ☔️"
        send_email(
            from_add=FROM_EMAIL,
            password=PASSWORD,
            to_add=TO_EMAIL,
            msg=msg
        )
    else:
        print("Won't rain!")
else:
    # Send sms text
    if will_rain():
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}

        client = Client(account_sid, auth_token, http_client=proxy_client)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_="YOUR TWILIO VIRTUAL NUMBER",
            to="YOUR TWILIO VERIFIED REAL NUMBER"
        )
        print(message.status)
    else:
        print("Won't rain!")
