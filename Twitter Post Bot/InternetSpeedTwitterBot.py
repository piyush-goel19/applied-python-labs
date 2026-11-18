import os
import time
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv(override=True)

email = str(os.getenv("TWITTER_EMAIL"))
password = str(os.getenv("TWITTER_PASSWORD"))

promised_download_speed = str(os.getenv("PROMISED_DOWN"))
promised_upload_speed = str(os.getenv("PROMISED_UP"))

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

        self.down_speed = 0
        self.up_speed = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(2)
        go_button = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button")
        go_button.click()
        time.sleep(45)
        self.down_speed = float(self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/h3").text)
        print(self.down_speed)
        self.up_speed = float(self.driver.find_element(By.XPATH, ".//*[@id='root']/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/h3").text)
        print(self.up_speed)

    def tweet_at_provider(self):
        self.driver.get("https://app.100daysofpython.dev/services/y/login")
        time.sleep(5)

        email_input = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        email_input.clear()
        email_input.send_keys(email)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        password_input.clear()
        password_input.send_keys(password)

        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/form/button")
        login_button.click()

        tweet_compose = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Post text"]')))
        tweet = f"Hey Internet Provider, why my speed is {self.down_speed}down/{self.up_speed}up, when I pay for {promised_download_speed}down/{promised_upload_speed}up?"
        tweet_compose.send_keys(tweet)

        time.sleep(5)

        tweet_button = self.driver.find_element(By.CSS_SELECTOR, ".x-compose-form button")
        tweet_button.click()