import os
from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
OAUTH_TOKEN, OAUTH_TOKEN_SECRET = read_token_file(os.getenv("TWITTER_OAUTH_PATH")
