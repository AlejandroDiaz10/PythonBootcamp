import datetime as dt
import pandas as pd
from random import choice
import smtplib
import sys
import os
from dotenv import load_dotenv

load_dotenv()

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# ---------------------- Env variables
gmail_mail = os.getenv("GMAIL_MAIL")
app_pwd_gmail = os.getenv("APP_PWD_GMAIL")
yahoo_mail = os.getenv("YAHOO_MAIL")

# ---------------------- Read CSV file
try:
    data = pd.read_csv("birthdays.csv", usecols=["name", "email", "month", "day"])
except FileNotFoundError as e:
    print(e)
    sys.exit(1)

# ---------------------- Check if today is someone's birthday
today = dt.datetime.now()
birthdays_today = data[(data["month"] == today.month) & (data["day"] == today.day)]

if birthdays_today.empty:
    print("No need to send today birthday emails")
else:
    birthday_people = {
        row[1]["email"]: row[1]["name"]
        for row in birthdays_today[["name", "email"]].iterrows()
    }

    # ---------------------- Select letter file
    try:
        with open(f"./letter_templates/{choice(letters)}", mode="r") as file:
            raw_message = file.read()
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    # ---------------------- Create SMTP connection
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=gmail_mail, password=app_pwd_gmail)
            for email, name in birthday_people.items():
                message = raw_message.replace("[NAME]", name)
                connection.sendmail(
                    from_addr=gmail_mail,
                    to_addrs=email,
                    msg=f"Subject:Happy Birthday!\n\n{message}",
                )
    except Exception as e:
        print(e)
    else:
        print("\nMails were sent succesfully!\n")
