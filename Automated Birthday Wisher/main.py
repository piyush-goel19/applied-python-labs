##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import random
import pandas as pd
import smtplib

login_user = "<EMAIL>"
login_pass = "<PASSWORD>"

data = pd.read_csv('birthdays.csv')
birthday_dict = {(row.month, row.day):row.to_dict() for (index, row) in data.iterrows()}

now = dt.datetime.now()
today = (now.month,now.day)

for key in birthday_dict:
    if today == key:
        recipient = birthday_dict[key]
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path, "r") as f:
            content = f.read()
            content = content.replace("[NAME]", recipient["name"])

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=login_user, password=login_pass)
            connection.sendmail(
                from_addr=login_user,
                to_addrs=recipient["email"],
                msg=f"Subject: Happy Birthday!\n\n{content}"
            )
            print("Email sent!")