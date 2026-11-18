import os
from instafollower import InstaFollower


from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


SIMILAR_ACCOUNT = "chefsteps"   # the account whose followers you'll follow
USERNAME = os.environ.get("SHARE_NAN_USER")
PASSWORD = os.environ.get("SHARE_NAN_PASSWORD")

follower = InstaFollower(user=USERNAME, password=PASSWORD)
follower.login()

follower.find_followers()

follower.follow()