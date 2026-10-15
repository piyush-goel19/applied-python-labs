import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time

load_dotenv()
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
URL = str(os.getenv("WEBSITE_URL"))
email = str(os.getenv("ACCOUNT_EMAIL"))
password = str(os.getenv("ACCOUNT_PASSWORD"))

def retry(func, retries=5, description=None, delay=1):
    for i in range(retries):
        print(f"Trying {description}..., Attempt {i+1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(delay)

def login():
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#email-input")))
    email_input.clear()
    email_input.send_keys(email)

    password_input = driver.find_element(By.CSS_SELECTOR, "input#password-input")
    password_input.clear()
    password_input.send_keys(password)

    submit_button = driver.find_element(By.ID, "submit-button")
    submit_button.click()

    element = wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))
    if element is not None:
        print("Logged in successfully....")

def get_booking_date_time():
    global booking_times
    today = datetime.now()
    days_to_thurs = (3 - today.weekday()) % 7
    if days_to_thurs == 0:
        days_to_thurs = 7

    thursday = today + timedelta(days=days_to_thurs)
    thursday_6pm = thursday.replace(hour=18, minute=0, second=0, microsecond=0)
    thursday_str = thursday_6pm.strftime("%Y-%m-%d-%H%M")

    days_to_tuesday = (1 - today.weekday()) % 7
    if days_to_tuesday == 0:
        days_to_tuesday = 7

    tuesday = today + timedelta(days=days_to_tuesday)
    tuesday_6pm = tuesday.replace(hour=18, minute=0, second=0, microsecond=0)
    tuesday_str = tuesday_6pm.strftime("%Y-%m-%d-%H%M")

    booking_times.append(thursday_str)
    booking_times.append(tuesday_str)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 2)
driver.get(URL)
retry(login, description="login")

booking_times = []
get_booking_date_time()

classes_booked = 0
waitlists_joined = 0
already_booked_waitlisted = 0
bookings = []

def book_class():
    global classes_booked, waitlists_joined, already_booked_waitlisted
    for booking_date_time in booking_times:
        try:
            class_card = driver.find_element(By.CSS_SELECTOR, f"div[id$='{booking_date_time}']")

            class_name = class_card.find_element(By.TAG_NAME, "h3").text
            print(class_name)

            date_text = class_card.find_element(By.XPATH, "./ancestor::div/h2").text
            print(date_text)

            book_button = class_card.find_element(By.TAG_NAME, "button")

            if book_button.text == "Booked":
                print(f"Already Booked: {class_name} on {date_text}")
                already_booked_waitlisted += 1
            elif book_button.text == "Waitlisted":
                print(f"Already on Waitlist: {class_name} on {date_text}")
                already_booked_waitlisted += 1
            elif book_button.text == "Join Waitlist":
                book_button.click()
                print(f"Joined waitlist for: {class_name} on {date_text}")
                waitlists_joined += 1
                bookings.append(f"[New waitlist] {class_name} on {date_text}")
            else:
                book_button.click()
                print(f"Booked: {class_name} on {date_text}")
                classes_booked += 1
                bookings.append(f"[New booking] {class_name} on {date_text}")

        except NoSuchElementException:
            print(f"No classes found on {booking_date_time}")
            continue

retry(book_class, description="bookClass")

print("-----BOOKING SUMMARY-------")
print(f"Classes booked: {classes_booked}")
print(f"Waitlists joined: {waitlists_joined}")
print(f"Already booked/waitlisted: {already_booked_waitlisted}")
total_bookings = classes_booked + waitlists_joined + already_booked_waitlisted
print(f"Total Tuesday & Thursday 6pm classes: {total_bookings}")

# print("----DETAILED CLASS LIST-------")
# for booking in bookings:
#     print(f"‣ {booking}")

print("-----VERIFYING ON MY BOOKINGS PAGE-------")
all_booked_classes = []
all_waitlisted_classes = []

my_bookings_page = driver.find_element(By.CSS_SELECTOR, "a#my-bookings-link")
my_bookings_page.click()

def get_my_bookings():
    global all_booked_classes, all_waitlisted_classes
    element = wait.until(EC.presence_of_element_located((By.ID, "my-bookings-page")))
    if element is not None:
        print("Navigated successfully!")

    try:
        confirmed_bookings = wait.until(EC.presence_of_element_located((By.ID, "confirmed-bookings-section")))
        all_booked_classes = confirmed_bookings.find_elements(By.TAG_NAME, "h3")
    except NoSuchElementException:
        print("No confirmed bookings found")

    try:
        waitlisted_bookings = driver.find_element(By.ID, "waitlist-section")
        all_waitlisted_classes = waitlisted_bookings.find_elements(By.TAG_NAME, "h3")
    except NoSuchElementException:
        print("No waitlisted bookings found")

retry(get_my_bookings, description="get_my_bookings")

if len(all_booked_classes) > 0:
    for booking_element in all_booked_classes:
        class_txt = booking_element.text
        print(f"✔ Verified: {class_txt}")

if len(all_waitlisted_classes) > 0:
    for waitlist_element in all_waitlisted_classes:
        waitlist_class_txt = waitlist_element.text
        print(f"✔ Verified: {waitlist_class_txt}")

total_bookings_found = len(all_booked_classes) + len(all_waitlisted_classes)
print("-----VERIFICATION RESULT-------")
print(f"Expected: {total_bookings}")
print(f"Found: {total_bookings_found}")

if total_bookings_found != total_bookings:
    print(f"❌ Mismatch: Missing {total_bookings - total_bookings_found} bookings")
else:
    print(f"✅ SUCCESS: All bookings were verified!")

