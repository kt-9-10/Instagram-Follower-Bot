from insta_follower import InstaFollower
import os


SIMILAR_ACCOUNT = os.environ["SIMILAR_ACCOUNT"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

insta_follower = InstaFollower()
insta_follower.login(USERNAME, PASSWORD)
insta_follower.find_followers(SIMILAR_ACCOUNT)
insta_follower.follow()