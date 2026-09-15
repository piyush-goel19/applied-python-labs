import requests
import requests_cache
import smtplib
from email.message import EmailMessage

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
username = "<USERNAME>"
password = "<PASSWORD>"

#----------Alpha Advantage------------#
STOCK_API_KEY = "<API_KEY>"
STOCK_DATA_URL = "https://www.alphavantage.co/query"

params = {
    "function": "GLOBAL_QUOTE",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
#--------------------------------------#

#-------------News API-----------------#
NEWS_API_KEY = "<API_KEY>"
NEWS_API_URL = "https://newsapi.org/v2/everything"

parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "pageSize": 3,
}
#---------------------------------------#
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

requests_cache.install_cache(cache_name="stock_news_cache", expire_after=3600)

response = requests.get(STOCK_DATA_URL, params=params)
response.raise_for_status()
change_percent = float(response.json()["Global Quote"]["10. change percent"].replace("%", ""))
change = (abs(change_percent), "🔺" if float(change_percent) > 0 else "🔻")
print(change)

list_of_news = []

msg = EmailMessage()
msg["Subject"] = "Stock News Alert"
msg["From"] = username
msg["To"] = "<RECEIVER>"

def create_mssg_text(list_of_news: list) -> str:
    text_body: str = f"{STOCK}: {change[1]}{change[0]}%\n"
    for news in list_of_news:
        text_body += f"Headline: {news['title']}\n"
        text_body += f"Brief: {news['description']}\n"
    return f"{text_body}"

if abs(change_percent) >= 1:
    response = requests.get(NEWS_API_URL, params=parameters)
    response.raise_for_status()
    for item in response.json()["articles"]:
        news_dict: dict = {}
        for key, value in item.items():
            if key == "title" or key == "description":
                news_dict[key] = value
        list_of_news.append(news_dict)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=username, password=password)
            mail_body = create_mssg_text(list_of_news)
            msg.set_content(mail_body)
            connection.send_message(msg)
            # connection.sendmail(
            #     from_addr=username,
            #     to_addrs="piyushgoel94@yahoo.com",
            #     msg=f"Subject: Stock News Alert\n\n{mail_body}"
            # )
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email {e}")