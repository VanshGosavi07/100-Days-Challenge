from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

driver_location = 'chrome driver full path'
chrome_driver_path = Service(driver_location)
chromeops = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=chromeops)

driver.get('https://tinder.com/')
time.sleep(5)

# accept cookies
driver.find_element(By.XPATH, '//*[@id="u131058078"]/div/div[2]/div/div/div[1]/div[1]/button').click()
time.sleep(2)

# click log in
driver.find_element(By.XPATH, "//*[text()='Log in']").click()
time.sleep(2)

# fb log in
driver.find_element(By.XPATH, '//*[@id="u-1597322998"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]').click()
time.sleep(2)

base_window = driver.window_handles[0]
time.sleep(1)

fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
time.sleep(2)

email = 'your FB email'
driver.find_element(By.ID, 'email').send_keys(email)

password = 'your FB password'
driver.find_element(By.ID, 'pass').send_keys(password, Keys.ENTER)
time.sleep(5)

driver.switch_to.window(base_window)
time.sleep(2)

# location pop up - allow
driver.find_element(By.XPATH, '//*[@id="u-1597322998"]/div/div/div/div/div[3]/button[1]').click()
time.sleep(2)

# notification pop - not allow
driver.find_element(By.XPATH, '//*[@id="u-1597322998"]/div/div/div/div/div[3]/button[2]/span').click()
time.sleep(15)

while True:
    try:
        # auto-like profile
        ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    except NoSuchElementException:
        # homescreen
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="u-1597322998"]/div/div/div[2]/button[2]/span').click()
    except ElementClickInterceptedException:
        # match found
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".itsAMatch a").click()
    else:
        # if already max likes
        driver.quit()
        break

    time.sleep(2)
