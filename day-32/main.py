import random
import smtplib
import datetime as dt

MY_EMAIL = "app_id@gmail.com"
MY_PASSWORD = "app_password"

def email_self(msg_subject, msg_body):
    # Google had no "App Passwords" option and I had to find and use the direct link
    # to get to it=> https://myaccount.google.com/apppasswords


    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="kadams1@telus.net",
                            msg=f"Subject:{msg_subject}\n\n{msg_body}")

def get_random_quote():
    quotes_file = "quotes.txt"

    with open(quotes_file) as file:
        lines = file.readlines()
    quote = random.choice(lines)
    print(quote)
    return quote

now = dt.datetime.now()
if now.weekday() == 6: # sunday: today
    quote = get_random_quote()
    email_self(msg_subject="Inspirational quote for today!", msg_body=quote)

print(now)