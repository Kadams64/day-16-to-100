import os
import smtplib

from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())


# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        self.sender_email = os.environ.get("MY_EMAIL")
        self.sender_email_password = os.environ.get("MY_EMAIL_PASSWORD")

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VERIFIED_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)

    def send_emails(self, member_list, msg_body):
        for email in member_list:
            self.send_email(email, "New lowest flight prices from Kelly's Flight Club!", msg_body)

    def send_email(self, msg_to, msg_subject, msg_body):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.sender_email, password=self.sender_email_password)
            connection.sendmail(from_addr=self.sender_email, to_addrs=msg_to,
                                msg=f"Subject:{msg_subject}\n\n{msg_body}")