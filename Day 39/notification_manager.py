import smtplib

FROM_EMAIL = "zedlucastest@gmail.com"
TO_EMAIL = "lucascarmed@gmail.com"
PASSWORD = "osndmxppboqkapvs"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_email(self, msg, from_add=FROM_EMAIL, password=PASSWORD, to_add=TO_EMAIL):
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
        except smtplib.SMTPConnectError:
            print("Error: SMTPConnectError")
            return False
