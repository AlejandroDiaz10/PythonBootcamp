import datetime as dt
import smtplib
from dotenv import load_dotenv
import os
import sys
from random import choice

load_dotenv()

gmail_mail = os.getenv("GMAIL_MAIL")
app_pwd_gmail = os.getenv("APP_PWD_GMAIL")
yahoo_mail = os.getenv("YAHOO_MAIL")

# Mails will only be sent on Thursdays (dt.weekday == 3)
if dt.datetime.now().weekday() == 3:
    try:
        with open("quotes.txt") as file:
            quotes = file.readlines()
    except FileNotFoundError as e:
        print("Error: ", e)
        sys.exit(1)
    else:
        selected_quote = choice(quotes)
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=gmail_mail, password=app_pwd_gmail)
                connection.sendmail(
                    from_addr=gmail_mail,
                    to_addrs=yahoo_mail,
                    msg=f"Subject:Motivational Quote\n\n{selected_quote}",
                )
        except smtplib.SMTPConnectError as e:
            print(f"SMTP connection error: {e}")
        except smtplib.SMTPAuthenticationError as e:
            print(f"SMTP authentication error: {e}")
        except smtplib.SMTPException as e:
            print(f"SMTP error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        else:
            print("\nMail was sent succesfully!\n")
            print(f"Subject: Motivational Quote\n{selected_quote}")
