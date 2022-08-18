# @author   Lucas Cardoso de Medeiros
# @since    14/07/2022
# @version  1.0

# Stocks News

import time
import requests
import smtplib
from datetime import datetime, timedelta


FROM_EMAIL = "zedlucastest@gmail.com"
PASSWORD = "osndmxppboqkapvs"
TO_EMAIL = "lucascarmed@gmail.com"
PORT = 587

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PRICE_FLOAT = 5

STOCK_API_KEY = "IRZ95GSC1M57JF5I"
STOCK_URL = "https://www.alphavantage.co/query"
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "apikey": STOCK_API_KEY,
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json"
}

ARTICLES_COUNT = 3

NEWS_API_KEY = "1e18b2ac48e34aa285b4d823bcf01b8a"
NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_PARAMS = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "from": "2022-07-12",
    "to": "2022-07-13",
    "sortBy": "relevancy",
}

BEFORE_YESTERDAY = (datetime.now() - timedelta(2)).strftime("%Y-%m-%d")
YESTERDAY = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")


def send_email(from_add, password, to_add, msg):
    """Send email based on parameters, returns True if successful"""
    try:
        with smtplib.SMTP("smtp.gmail.com", PORT) as connection:
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
    except UnicodeEncodeError:
        print("Error: UnicodeEncodeError")
        return False


def price_diff():
    response = requests.get(url=STOCK_URL, params=STOCK_PARAMS)
    response.raise_for_status()
    time_series = response.json()["Time Series (Daily)"]
    price_yesterday = float(time_series[YESTERDAY]["4. close"])
    price_before_yesterday = float(time_series[BEFORE_YESTERDAY]["4. close"])
    return ((price_yesterday / price_before_yesterday) - 1) * 100  # e.g. -1.6748228147148159%


def get_news():
    global NEWS_PARAMS
    NEWS_PARAMS["from"] = BEFORE_YESTERDAY
    NEWS_PARAMS["to"] = YESTERDAY
    response = requests.get(url=NEWS_URL, params=NEWS_PARAMS)
    response.raise_for_status()
    return response.json()["articles"][:ARTICLES_COUNT]


delta = round(price_diff(), 2)

if delta > 0:
    symbol = "🔺"
else:
    symbol = "🔻"

if delta > PRICE_FLOAT or delta < -PRICE_FLOAT:
    # Trigger news search
    print("Get News")
    news = get_news()
    for new in news:
        msg = f"Subject:{STOCK}: {delta}%\n\n{STOCK}: {symbol}{delta}%\n" \
              f"Headline: {new['title']}\nBrief: {new['description']}\n"
        sent = send_email(
            from_add=FROM_EMAIL,
            password=PASSWORD,
            to_add=TO_EMAIL,
            msg=msg
        )
        if sent:
            print("News email sent!")
            time.sleep(5)
else:
    print("Sideways market... =(")
