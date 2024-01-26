# Initial Problem: https://support.google.com/mail/?p=BadCredentials
# First: Enable 2-step verification
# Finally: Create an app pwd

import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

# ------------------------------------ Retrieve Environment Variables
gmail_mail = os.getenv("GMAIL_MAIL")
# gmail_pwd = os.getenv("GMAIL_PWD")
app_pwd_gmail = os.getenv("APP_PWD_GMAIL")
yahoo_mail = os.getenv("YAHOO_MAIL")

# ------------------------------------ Create Simple Mail Transfer Protocol (SMTP) connection
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # TLS - Transport Layer Security
    connection.login(user=gmail_mail, password=app_pwd_gmail)
    connection.sendmail(
        from_addr=gmail_mail,
        to_addrs=yahoo_mail,
        msg="Subject:Hello\n\nThis is the body of my email",
    )
