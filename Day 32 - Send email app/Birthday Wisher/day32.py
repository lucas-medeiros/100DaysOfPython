# @author   Lucas Cardoso de Medeiros
# @since    08/07/2022
# @version  1.0

# Birthday Wisher SMTP


import smtplib
from datetime import datetime
import random
import pandas

FROM_EMAIL = "zedlucastest@gmail.com"
PASSWORD = "osndmxppboqkapvs"


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


def get_letter(name):
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file=file_path, mode="r") as file:
        template = file.read()
        return template.replace("[NAME]", name)


df = pandas.read_csv("birthdays.csv")
for index, row in df.iterrows():
    birthday = datetime(year=row['year'], month=row['month'], day=row['day'])
    today = datetime.today()
    if today.day == birthday.day and today.month == birthday.month:
        print(f"Happy Birthday {row['name']}! Email: {row['email']}")
        sent = send_email(
            from_add=FROM_EMAIL,
            password=PASSWORD,
            to_add=row['email'],
            msg=f"Subject:Happy Birthday!\n\n{get_letter(row['name'])}"
        )
        if sent:
            print("Happy Birthday email sent!")
        else:
            print("Error sending email")
