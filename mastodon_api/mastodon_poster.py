from mastodon import Mastodon
import os
from dotenv import load_dotenv

load_dotenv()

client_key = os.getenv("MASTODON_CLIENT_KEY")
client_secret = os.getenv("MASTODON_CLIENT_SECRET")
access_token = os.getenv("MASTODON_ACCESS_TOKEN")
api_base_url = "https://mastodon.social"

email = os.getenv("MASTODON_EMAIL")
password = os.getenv("MASTODON_PW")

account_id = os.getenv("MASTADON_ACCOUNT_ID") 

def post_to_mastodon(content):
    
    mastodon = Mastodon(
    client_id=client_key,
    client_secret=client_secret,
    access_token=access_token,
    api_base_url=api_base_url,
)

    mastodon.status_post(content)