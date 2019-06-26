import os

from dotenv import load_dotenv

from Instagram import Instagram

load_dotenv(verbose=True)
USERNAME = os.getenv("INSTA_USERNAME")
PASSWORD = os.getenv("INSTA_PASSWORD")

if __name__ == "__main__":
    instagram = Instagram(USERNAME, PASSWORD)
    instagram.signin()
    instagram.like_user_posts("melvinoyx")
