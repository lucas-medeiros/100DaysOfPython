# @author   Lucas Cardoso de Medeiros
# @since    13/12/2022
# @version  1.0

#  Internet Speed Twitter Complaint Bot

from internet_speed_twitter_bot import InternetSpeedTwitterBot

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

bot.get_internet_speed()
bot.tweet_at_provider()
