from selenium import webdriver
import requests
import helper
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Initiates webdriver
from webdriver_manager.chrome import ChromeDriverManager


def init_driver(type):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    if type == "player_stats":
        driver.get("https://www.espn.com/nfl/stats/player")
    else:
        driver.get("https://www.espn.com/")
    driver.implicitly_wait(10)  # Waiting for page to load
    return driver


def team_leader(team):
    driver = init_driver("team_leader")

    #  Clicking NFL tab first, then specific team, then by stats page
    driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/header/nav[1]/ul/li[1]/a/span/span[1]").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, team.split()[-1]).click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div[2]/div[2]/nav/ul/li[3]/a/span").click()

    # Using BeautifulSoup to Parse HTML
    r = requests.get(driver.current_url).content
    doc = BeautifulSoup(r,  "html.parser")

    # Getting Team Leader Stats via BeautifulSoup
    logo = doc.find("img", class_="Image Logo Logo__xxl")
    logo_tag = driver.find_element(By.XPATH,"//img[@class='Image Logo Logo__xxl']")
    logo = logo_tag.get_attribute("src")
    tag = doc.find("section", class_="StatLeaders flex")
    team_leader = tag.children
    players = []  # Storing Players in List

    for i in team_leader:  # Each Player is a Dictionary
        player = {"stat_name": i.find("h2", class_="h8 mb2 clr-gray-03").text,
                  "name": i.find("span", class_="Athlete__PlayerName").text,
                  "position": i.find("span", class_="Athlete__NameDetails ml2 clr-gray-04 di ns9").text,
                  "stat": i.find("div", class_="clr-gray-01 pr3 hs2").text}
        players.append(player)
        # print(stat_name.text)
        # print(position.text + ": " + name.text + ", " + stat.text)
    return [players, logo]

def player_stats(name, position):
    driver = init_driver("player_stats")
    if position == "RB":
        driver.find_element(By.XPATH,"//a[contains(text(),'Rushing')]").click()
