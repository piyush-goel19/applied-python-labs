from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/-P6yHmU3AcCMwjvqGHnACbjcFzCabHpg"
EMAIl = "xx@gmail.com"
PASSWORD = "uuW6qH3JSz@SrCs"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(TINDOG_URL)

login_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-tindog-login.tindog-login-pill')
login_button.click()

main_window = driver.current_window_handle
print(main_window)

WebDriverWait(driver, 2).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="login-modal"]/div/div/div/button[1]'))).click()

WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) == 2)

for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        break

print(f"Current window: {driver.title}")

#<button type="submit" class="btn-primary">Allow</button>
#<button type="submit" class="btn-secondary">Not interested</button>
#<button type="submit" class="btn-primary">I Accept</button>
#<button class="btn-like" aria-label="Like" type="submit">♥</button>
#/html/body/main/div[3]/a <a href="/services/tindog/dismiss-match" class="match-popup-link">Back to Tindog</a>

email_input = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
email_input.clear()
email_input.send_keys(EMAIl)

password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.clear()
password.send_keys(PASSWORD)

driver.find_element(By.XPATH, '/html/body/div[2]/div/form/button').click()

driver.switch_to.window(main_window)

print(f"Current window: {driver.title}")

WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'button.btn-primary'))).click()

WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, '/html/body/main/div/div/form/button[2]'))).click()

for _ in range(3):
    try:
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-primary'))).click()
        break
    except StaleElementReferenceException:
        continue

likes = 0

for _ in range(20):
    if likes == 20:
        break
    time.sleep(2)
    try:
        like_button = driver.find_element(By.CLASS_NAME, 'btn-like')
        ActionChains(driver).move_to_element(like_button).perform()
        like_button.click()
        likes += 1
        print(f"Like {likes} successful....")
    except NoSuchElementException:
        time.sleep(2)
    except ElementClickInterceptedException:
        time.sleep(2)
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, 'a.match-popup-link')
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)
