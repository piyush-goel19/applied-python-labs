import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://www.amazon.in/dp/B0DJH2J2FC/?coliid=I1EKLFZAZX1DHH&colid=1DST5B5ZT6RIL&ref_=list_c_wl_lv_ov_lig_dp_it&th=1"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"153\", \"Not_A Brand\";v=\"8\", \"Chromium\";v=\"153\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
price_with_currency = soup.select_one("span.a-offscreen").getText().strip()
currency = soup.select_one("span.a-price-symbol").getText().strip()
item_name = soup.select_one("span#productTitle").getText().strip()
item_name_formatted = " ".join(item_name.split())
item_price = float(price_with_currency.split('₹')[1].replace(",",""))

target_price = float(8000.00)

if item_price < target_price:
    message = EmailMessage()
    message["Subject"] = "Amazon Price Alert!"
    message["From"] = os.getenv("USERNAME")
    message["To"] = "piyushgoel94@yahoo.com"

    msg_text = f"{item_name_formatted} is now {price_with_currency}, below your target price of {currency}{target_price}.\nGo ahead and Buy Now at {URL}"

    message.set_content(msg_text)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(str(os.getenv("USERNAME")), str(os.getenv( "PASSWORD")))
            connection.send_message(message)
            print("Email sent!")
    except Exception as e:
        print(f"Error sending email: {e}")

