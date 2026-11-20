import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

FOLLOW_ACCOUNT = "rordongamsay"
USERNAME = "piyushgoel17@gmail.com"
PASSWORD = "Z4EnCmYHiIgvqMG4"
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"
LOGIN_URL = f"{BASE_URL}/welcome"

class InstaFollowerBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True) #keeps browser open
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(LOGIN_URL)
        time.sleep(2)

        email = self.driver.find_element(By.NAME, "username")
        email.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.RETURN)
        time.sleep(2)

        save_info_not_now = self.driver.find_element(By.XPATH, '//*[@id="popup-save-login"]/div/div[2]')
        if save_info_not_now:
            save_info_not_now.click()

        time.sleep(2)

        turn_notifications_not_now = self.driver.find_element(By.XPATH, '//*[@id="popup-notifications"]/div/button[2]')
        if turn_notifications_not_now:
            turn_notifications_not_now.click()

    def find_followers(self):
        self.driver.get(f"{BASE_URL}/u/{FOLLOW_ACCOUNT}")
        time.sleep(2)

        followers = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/header/div[2]/div[2]/span[2]/a')
        no_of_followers = int(followers.text.split()[0])
        followers.click()

        time.sleep(3)

        followers_scroll = self.driver.find_element(By.CSS_SELECTOR, ".followers-scroll")
        data_offset = 7
        for _ in range(no_of_followers//data_offset):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_scroll)
            time.sleep(1)

    def follow(self):
        followers_accts = self.driver.find_elements(By.CSS_SELECTOR, ".followers-scroll button")
        for btn in followers_accts:
            try:
                btn.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel.click()
        close = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/a")
        close.click()


bot = InstaFollowerBot()
bot.login()
bot.find_followers()
bot.follow()





