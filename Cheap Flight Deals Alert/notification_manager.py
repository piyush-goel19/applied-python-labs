import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.username = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.receiver = os.getenv("RECIPIENT_EMAIL")

    def send_email(self, cheapest_flight, users_email_data):
        if cheapest_flight.stopovers == 0:
            msg_body = (f"Low Price Alert!\nOnly INR {cheapest_flight.price} to fly from "
                        f"{cheapest_flight.departure_airport} to {cheapest_flight.arrival_airport}, "
                        f"departing on {cheapest_flight.out_date} and returning on "
                        f"{cheapest_flight.return_date}\n\n"
                        f"From: Cheap Flight Scanner Team")
        else:
            msg_body = (f"Low Price Alert!\nOnly INR {cheapest_flight.price} to fly from "
                        f"{cheapest_flight.departure_airport} to {cheapest_flight.arrival_airport}, "
                        f"with {cheapest_flight.stopovers} stop(s) departing on "
                        f"{cheapest_flight.out_date} and returning on {cheapest_flight.return_date}\n\n"
                        f"From: Cheap Flight Scanner Team")
        if users_email_data is not None:
            for email in users_email_data:
                with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                    connection.starttls()
                    connection.login(str(self.username), str(self.password))
                    connection.sendmail(
                        from_addr=str(self.username),
                        to_addrs=email,
                        msg=f"Subject: Cheap Flight Alert!\n\n{msg_body}"
                    )
                    print("Alert sent successfully!")
        else:
            print("No email to be sent!")