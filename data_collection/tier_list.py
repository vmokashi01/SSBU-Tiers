import pandas as pd
import numpy as np
import requests
import time
from frame_data import get_chars
from selenium import webdriver
# from bs4 import BeautifulSoup as soup

characters = get_chars()
tier_list = [['Character', 'Difficulty', 'Archetype', 'Tier']]


def get_tier_list(character):
    url = "https://www.proguides.com/super-smash-bros-ultimate/characters/" + character
    driver = webdriver.Chrome()
    driver.get(url)
    char_tier = []

    if __name__ == '__main__':
        time.sleep(5)
        name = driver.find_element_by_class_name("header__character-name").text
        difficulty = driver.find_element_by_class_name(
            "header__difficulty").text
        playstyle = driver.find_element_by_class_name("blue").text
        tier = driver.find_element_by_class_name("header__tier").text
        char_tier.append(name)
        char_tier.append(difficulty)
        char_tier.append(playstyle)
        char_tier.append(tier)

        driver.close()

        return char_tier


# get_tier_list("fox")

for character in characters:
    character = character.lower()
    character = character.replace('.', '')
    character = character.replace('& ', '')
    character = character.replace('and ', '')
    character = character.replace(' ', '-')
    if character == 'charizard':
        character = 'pokemon-trainer-charizard'
    elif character == 'ivysaur':
        character = 'pokemon-trainer-ivysaur'
    elif character == 'squirtle':
        character = 'pokemon-trainer-squirtle'
    elif character == 'rob':
        character = 'r-o-b'
    tier_list.append(get_tier_list(character))

f = open("tier_data.csv", "x")
for line in tier_list:
    for item in line:
        f.write(item + ';')
    f.write("\n")
