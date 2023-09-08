# @author   Lucas Cardoso de Medeiros
# @since    07/07/2022
# @version  1.0

# Birthday Wisher SMTP

import smtplib
import datetime as dt
import random
import time

FROM_EMAIL = "zedlucastest@gmail.com"
PASSWORD = "osndmxppboqkapvs"
TO_EMAIL = "lucascarmed@gmail.com"
EMAIL_DAY = 0  # Monday


def send_email(from_add, password, to_add, msg):
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


def get_quote():
    try:
        with open(file="quotes.txt", mode="r") as file:
            return random.choice(file.readlines())
    except FileNotFoundError:
        return "File Not Found Error"


while True:
    if dt.datetime.now().weekday() == EMAIL_DAY:
        sent = send_email(
            from_add=FROM_EMAIL,
            password=PASSWORD,
            to_add=TO_EMAIL,
            msg=f"Subject:Motivational Monday\n\n{get_quote()}"
        )
        if sent:
            print("Email sent!")
        else:
            print("Error sending email...")
    else:
        print("Not the Email day")
    time.sleep(86400)
