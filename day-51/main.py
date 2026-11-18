import os
from internet_speed_bot import InternetSpeedTwitterBot


from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())



Y_EMAIL = os.environ.get("Y_EMAIL")
Y_PASSWORD = os.environ.get("Y_PASSWORD")


speed_bot = InternetSpeedTwitterBot(Y_EMAIL, Y_PASSWORD)
speed_bot.get_internet_speed()
print(f"Upload speed= {speed_bot.up}; Download speed= {speed_bot.down}")
speed_bot.tweet_at_provider()