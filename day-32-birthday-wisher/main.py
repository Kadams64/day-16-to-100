import random
import smtplib
import pandas
import datetime as dt

my_email = "someemail@gmail.com"
password = "somecode"

##################### Normal Starting Project ######################

def today_tuple():
    today = dt.datetime.now()
    return today.month, today.day

def email(msg_subject, msg_body, msg_to):
    # Google had no "App Passwords" option and I had to find and use the direct link
    # to get to it=> https://myaccount.google.com/apppasswords

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=msg_to,
                            msg=f"Subject:{msg_subject}\n\n{msg_body}")

now_tuple = today_tuple()
dataframe = pandas.read_csv("birthdays.csv")

birthdays_dict = {(row.month,row.day):row.to_dict() for (index, row) in dataframe.iterrows()}
result = birthdays_dict.get(now_tuple)
if result is None:
    print("No birthdays for today.")
else:
    template_number = random.randint(1,3)
    letter_name = f"./letter_templates/letter_{template_number}.txt"
    with open(letter_name, "r") as form:
        form_letter = form.read()

    personal_letter = form_letter.replace("[NAME]", result["name"])

    email(msg_subject="Happy Birthday!", msg_body=personal_letter, msg_to=result["email"])



