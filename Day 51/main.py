import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = r"C:\Program Files\chromedriver-win64\chromedriver.exe"
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "DarshGupta91355"
TWITTER_PASSWORD = "106639Vansh@"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        self.driver.find_element(By.XPATH,
                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[3]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[4]/span').text
        time.sleep(2)

    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com/login")
        time.sleep(5)
        self.driver.find_element(By.TAG_NAME, 'input').send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]').click()
        time.sleep(5)
        self.driver.find_element(By.NAME, 'password').send_keys(TWITTER_PASSWORD)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/span').send_keys(
            f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button').click()
        time.sleep(7)


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
