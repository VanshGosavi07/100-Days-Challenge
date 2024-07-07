import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Program Files\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service)

# driver.get(r"https://www.python.org/")
#
# event_date = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# event_name = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
#
# events = {}
#
# for i in range(len(event_name)):
#     events[i] = {
#         "time": event_date[i].text,
#         "name": event_name[i].text,
#     }
#
# print(events)
# driver.quit()

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# # value = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# # print(value.text)
#
# search = driver.find_element(By.NAME, 'search')
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# driver.get(r"http://secure-retreat-92358.herokuapp.com/")
# first_name = driver.find_element(By.NAME, 'fName')
# first_name.send_keys('Vansh')
#
# last_name = driver.find_element(By.NAME, 'lName')
# last_name.send_keys('Gosavi')
#
# email = driver.find_element(By.NAME, 'email')
# email.send_keys('vanshgosavi7@gmail.com')
#
# send = driver.find_element(By.CSS_SELECTOR, 'button')
# send.send_keys(Keys.ENTER)

driver.get(r"https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element(By.CSS_SELECTOR, '#bigCookie')
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

while True:
    cookie.click()

    if time.time() > timeout:
        store_elements = driver.find_elements(By.CSS_SELECTOR, "#store b")[:-1]
        costs = [int(store_elements[i].text.split("-")[1].replace(",", "")) for i in range(len(store_elements))]
        store = [{items[i]: costs[i]} for i in range(len(store_elements))]

        money = driver.find_element(By.ID, "money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        for i in range(len(store)):
            if cookie_count >= store[i][items[i]]:
                item_to_buy = driver.find_element(By.ID, f"buy{items[i]}")
                item_to_buy.click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
