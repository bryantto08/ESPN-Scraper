from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Initiate webdriver
driver = webdriver.Chrome(executable_path='chromedriver.exe')


def team_leader(team):
    driver.get("https://www.espn.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)  # Waiting for page to load

    #  Clicking NFL tab first, then specific team, then by stats page
    driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/header/nav[1]/ul/li[1]/a/span/span[1]").click()
    driver.find_element(By.XPATH, f"//span[contains(text(),'{team}')]").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div[2]/div[2]/nav/ul/li[3]/a/span").click()

    r = requests.get(driver.current_url).content
    doc = BeautifulSoup(r,  "html.parser")

    # Getting Team Leader Stats
    tag = doc.find("section", class_="StatLeaders flex")
    team_leader = tag.children
    players = []
    for i in team_leader:
        player = {"stat_name": i.find("h2", class_="h8 mb2 clr-gray-03").text,
                  "name": i.find("span", class_="Athlete__PlayerName").text,
                  "position": i.find("span", class_="Athlete__NameDetails ml2 clr-gray-04 di ns9").text,
                  "stat": i.find("div", class_="clr-gray-01 pr3 hs2").text}
        players.append(player)
        # print(stat_name.text)
        # print(position.text + ": " + name.text + ", " + stat.text)
    return players




