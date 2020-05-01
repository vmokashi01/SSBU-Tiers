import requests
from bs4 import BeautifulSoup as soup


def get_atk_frames(character):
    base_url = "https://ultimateframedata.com/" + \
        character.lower().replace(" ", "_") + ".php"  # route url to each character
    page = requests.get(base_url)
    page_soup = soup(page.text, "html.parser")
