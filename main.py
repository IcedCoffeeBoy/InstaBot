import os

from dotenv import load_dotenv

from Instagram import Instagram

load_dotenv(verbose=True)
## Manually insert username & password here if necessary
USERNAME = os.getenv("INSTA_USERNAME")
PASSWORD = os.getenv("INSTA_PASSWORD")

if __name__ == "__main__":
    instagram = Instagram(USERNAME, PASSWORD, headless=True)
    try:
        instagram.signin()
        instagram.like_tag_posts("gg")
    except:
        instagram.close_driver()
