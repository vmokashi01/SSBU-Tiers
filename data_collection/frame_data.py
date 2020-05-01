import pandas as pd
import numpy as np
import requests
from statistics import mean
from bs4 import BeautifulSoup as soup


def get_chars():
    url = "https://ultimateframedata.com/#"
    page = requests.get(url)
    page_soup = soup(page.text, "html.parser")
    charlist = page_soup.find_all(
        "div", {"class": "charactericon"})
    names = []
    for char in charlist:
        try:
            # remove hidden jokes in span tags
            name = char.span.decompose().get_text(strip=True)
        except:
            name = char.get_text(strip=True)
        names.append(name)

    return(names[1:])  # don't include stats box


def get_air_acc():
    url = "https://ultimateframedata.com/stats.php"
    page = requests.get(url)
    page_soup = soup(page.text, "html.parser")
    # , id="airaccelerationtable")
    tables = page_soup.find_all("table")[0]
    rows = tables.find_all("tr")
    air_acc = []
    for tr in rows:
        air_acc.append(tr.text.strip().replace("\n", " ").split())
    # concatenate multiple word names
    for arr in air_acc:
        while len(arr) != 5:
            arr[1] += " " + arr[2]
            arr.remove(arr[2])

    # Nana & Popo values should be averaged + renamed to Ice Climbers
    air_acc.insert(20, ['20', 'Ice Climbers', str(mean([float(air_acc[20][2]), float(air_acc[26][2])])), str(
        mean([float(air_acc[20][3]), float(air_acc[26][3])])), str(mean([float(air_acc[20][4]), float(air_acc[26][4])]))])
    air_acc.remove(air_acc[21])  # remove Nana
    air_acc.remove(air_acc[26])  # remove Popo

    return(air_acc)


def get_air_spd():
    url = "https://ultimateframedata.com/stats.php"
    page = requests.get(url)
    page_soup = soup(page.text, "html.parser")
    tables = page_soup.find_all("table")[1]
    rows = tables.find_all("tr")
    air_spd = []
    for tr in rows:
        air_spd.append(tr.text.strip().replace("\n", " ").split())
    # concatenate multiple word names
    for arr in air_spd[1:]:
        while len(arr) != 3:
            arr[1] += " " + arr[2]
            arr.remove(arr[2])
    # fix title list
    air_spd[0][2] += " " + air_spd[0][3]
    air_spd[0].remove(air_spd[0][3])

    return air_spd


def get_fall_spd():
    url = "https://ultimateframedata.com/stats.php"
    page = requests.get(url)
    page_soup = soup(page.text, "html.parser")
    tables = page_soup.find_all("table")[2]
    rows = tables.find_all("tr")
    fall_spd = []
    for tr in rows:
        fall_spd.append(tr.text.strip().replace("\n", " ").split())
    # concatenate multiple word names
    for arr in fall_spd[1:]:
        while len(arr) != 5:
            arr[1] += " " + arr[2]
            arr.remove(arr[2])
    # fix title list
    fall_spd[0][2] += " " + fall_spd[0][3]
    fall_spd[0].remove(fall_spd[0][3])
    fall_spd[0][3] += " " + fall_spd[0][4]
    fall_spd[0].remove(fall_spd[0][4])
    fall_spd[0][4] += " " + fall_spd[0][5]
    fall_spd[0].remove(fall_spd[0][5])

    return fall_spd


def get_grav():
    url = "https://ultimateframedata.com/stats.php"
    page = requests.get(url)
    page_soup = soup(page.text, "html.parser")
    tables = page_soup.find_all("table")[3]
    rows = tables.find_all("tr")
    grav = []
    for tr in rows:
        grav.append(tr.text.strip().replace("\n", " ").split())
    # concatenate multiple word names
    for arr in grav[1:]:
        while len(arr) != 2:
            arr[0] += " " + arr[1]
            arr.remove(arr[1])

    return grav


def get_jump_height():
    url = "https://ultimateframedata.com/stats.php"
    page = requests.get(url)
    page_soup = soup(page.text, "html.parser")
    tables = page_soup.find_all("table")[4]
    rows = tables.find_all("tr")
    jump_ht = []
    for tr in rows:
        jump_ht.append(tr.text.strip().replace("\n", " ").split())
    # concatenate multiple word names
    for arr in jump_ht[1:]:
        while len(arr) != 4:
            arr[0] += " " + arr[1]
            arr.remove(arr[1])

    # fix title list
    jump_ht[0][1] += " " + jump_ht[0][2]
    jump_ht[0].remove(jump_ht[0][2])
    jump_ht[0][2] += " " + jump_ht[0][3]
    jump_ht[0].remove(jump_ht[0][3])
    jump_ht[0][3] += " " + jump_ht[0][4]
    jump_ht[0].remove(jump_ht[0][4])

    return jump_ht


def get_jump_duration():
    url = "https://ultimateframedata.com/stats.php"
    page = requests.get(url)
    page_soup = soup(page.text, "html.parser")
    tables = page_soup.find_all("table")[5]
    rows = tables.find_all("tr")
    jump_dur = []
    for tr in rows:
        jump_dur.append(tr.text.strip().replace("\n", " ").split())
    # concatenate multiple word names
    for arr in jump_dur[1:]:
        while len(arr) != 5:
            arr[0] += " " + arr[1]
            arr.remove(arr[1])

    # fix title list
    jump_dur[0][1] += " " + jump_dur[0][2]
    jump_dur[0].remove(jump_dur[0][2])
    jump_dur[0][2] += " " + jump_dur[0][3]
    jump_dur[0].remove(jump_dur[0][3])
    jump_dur[0][3] += " " + jump_dur[0][4] + " " + jump_dur[0][5]
    jump_dur[0].remove(jump_dur[0][4])
    jump_dur[0].remove(jump_dur[0][4])
    jump_dur[0][4] += " " + jump_dur[0][5] + " " + jump_dur[0][6]
    jump_dur[0].remove(jump_dur[0][5])
    jump_dur[0].remove(jump_dur[0][5])

    return jump_dur


def get_weight():
    url = "https://ultimateframedata.com/stats.php"
    page = requests.get(url)
    page_soup = soup(page.text, "html.parser")
    tables = page_soup.find_all("table")[6]
    rows = tables.find_all("tr")
    weight = []
    for tr in rows:
        weight.append(tr.text.strip().replace("\n", " ").split())
    # concatenate multiple word names
    for arr in weight[1:]:
        while len(arr) != 3:
            arr[1] += " " + arr[2]
            arr.remove(arr[2])

    return weight


def get_landing():
    url = "https://ultimateframedata.com/stats.php"
    page = requests.get(url)
    page_soup = soup(page.text, "html.parser")
    tables = page_soup.find_all("table")[7]
    rows = tables.find_all("tr")
    landing = []
    for tr in rows:
        landing.append(tr.text.strip().replace("\n", " ").split())
    # concatenate multiple word names
    for arr in landing[1:]:
        while len(arr) != 3:
            arr[0] += " " + arr[1]
            arr.remove(arr[1])

    # fix title list
    landing[0][1] += " " + landing[0][2]
    landing[0].remove(landing[0][2])
    landing[0][2] += " " + landing[0][3]
    landing[0].remove(landing[0][3])
    landing[0].remove(landing[0][3])

    return landing


def get_walk_spd():
    url = "https://ultimateframedata.com/stats.php"
    page = requests.get(url)
    page_soup = soup(page.text, "html.parser")
    tables = page_soup.find_all("table")[8]
    rows = tables.find_all("tr")
    walk_spd = []
    for tr in rows:
        walk_spd.append(tr.text.strip().replace("\n", " ").split())
    # concatenate multiple word names
    for arr in walk_spd[1:]:
        while len(arr) != 3:
            arr[1] += " " + arr[2]
            arr.remove(arr[2])

    # fix title list
    walk_spd[0][2] += " " + walk_spd[0][3]
    walk_spd[0].remove(walk_spd[0][3])

    # Nana & Popo values should be averaged + renamed to Ice Climbers

    walk_spd.insert(53, ['53', 'Ice Climbers', str(
        mean([float(walk_spd[45][2]), float(walk_spd[53][2])]))])
    walk_spd.remove(walk_spd[45])  # remove Nana
    walk_spd.remove(walk_spd[53])  # remove Popo

    return walk_spd


def get_dash_spd():
    url = "https://ultimateframedata.com/stats.php"
    page = requests.get(url)
    page_soup = soup(page.text, "html.parser")
    tables = page_soup.find_all("table")[9]
    rows = tables.find_all("tr")
    dash_spd = []
    for tr in rows:
        dash_spd.append(tr.text.strip().replace("\n", " ").split())
    # concatenate multiple word names
    for arr in dash_spd[1:]:
        while len(arr) != 5:
            arr[0] += " " + arr[1]
            arr.remove(arr[1])

    # fix title list
    dash_spd[0][1] += " " + dash_spd[0][2]
    dash_spd[0].remove(dash_spd[0][2])
    dash_spd[0][2] += " " + dash_spd[0][3]
    dash_spd[0].remove(dash_spd[0][3])
    dash_spd[0][3] += " " + dash_spd[0][4]
    dash_spd[0].remove(dash_spd[0][4])
    dash_spd[0][4] += " " + dash_spd[0][5] + " " + dash_spd[0][6]
    dash_spd[0].remove(dash_spd[0][5])
    dash_spd[0].remove(dash_spd[0][5])

    return(dash_spd)


def get_dash_turn():
    url = "https://ultimateframedata.com/stats.php"
    page = requests.get(url)
    page_soup = soup(page.text, "html.parser")
    tables = page_soup.find_all("table")[10]
    rows = tables.find_all("tr")
    dash_turn = []

    for row in rows:
        dash_turn.append((" ".join(tr.strip()
                                   for tr in row.find_all(text=True)).split()))

    # concatenate multiple word names
    for arr in dash_turn[1:]:
        while len(arr) != 4:
            arr[0] += " " + arr[1]
            arr.remove(arr[1])
        arr[0] = arr[0].replace(" Frames", "")

    # fix title list
    dash_turn[0][1] += " " + dash_turn[0][2] + " " + dash_turn[0][3]
    dash_turn[0].remove(dash_turn[0][2])
    dash_turn[0].remove(dash_turn[0][2])
    dash_turn[0][2] += " " + dash_turn[0][3] + " " + dash_turn[0][4]
    dash_turn[0].remove(dash_turn[0][3])
    dash_turn[0].remove(dash_turn[0][3])
    dash_turn[0][3] += " " + dash_turn[0][4] + " " + dash_turn[0][5]
    dash_turn[0].remove(dash_turn[0][4])
    dash_turn[0].remove(dash_turn[0][4])

    return(dash_turn)


def get_ledge():
    url = "https://ultimateframedata.com/stats.php"
    page = requests.get(url)
    page_soup = soup(page.text, "html.parser")
    tables = page_soup.find_all("table")[11]
    rows = tables.find_all("tr")
    ledge = []
    for td in rows:
        ledge.append(td.text.splitlines())
    for row in ledge:
        if len(row) != 5:
            del row[0]

    return ledge


def get_shield():
    url = "https://ultimateframedata.com/stats.php"
    page = requests.get(url)
    page_soup = soup(page.text, "html.parser")
    tables = page_soup.find_all("table")[12]
    rows = tables.find_all("tr")
    shield = []
    for row in rows:
        shield.append(row.find_all(text=True))

    # fix header line
    for i in shield[0]:
        if i == '\n':
            shield[0].remove(i)

    # remove legend columns from rows
    for row in shield:
        if len(row) == 14:
            row.remove(row[13])

    return shield


# these sorted by rank
# get_air_acc()
# get_air_spd()
# get_fall_spd()
# get_grav()
# get_jump_height()
# get_jump_duration()
# get_weight()
# get_landing() -- MIRRORS ARE MERGED; split into different characters; Terry is duplicated, Byleth is missing
# get_walk_spd()
# get_dash_spd()
# get_dash_turn()
# get_ledge()
# get_shield() -- colours for attacks are not grabbed
