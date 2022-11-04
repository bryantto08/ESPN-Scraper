from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Initiate webdriver
driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get("https://www.espn.com/")
driver.maximize_window()
driver.implicitly_wait(10)  # Waiting for page to load

#  Clicking NFL tab first, then specific team
driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/header/nav[1]/ul/li[1]/a/span/span[1]").click()
driver.find_element(By.XPATH,
                    "/html/body/div[5]/div[2]/header/nav[1]/ul/li[1]/div/ul[2]/li/div/ul[5]/li[2]/a/span/span[1]").click()

r = requests.get(driver.current_url).content
doc = BeautifulSoup(r,  "html.parser")

# Getting Team Leader Stats
tag = doc.find("div", class_="ResponsiveWrapper")
print(tag)

