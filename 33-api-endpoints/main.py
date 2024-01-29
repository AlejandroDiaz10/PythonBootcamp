import requests
import datetime as dt
import smtplib
import os
from dotenv import load_dotenv
import time

load_dotenv()

gmail_mail = os.getenv("GMAIL_MAIL")
app_pwd_gmail = os.getenv("APP_PWD_GMAIL")

# Geo position for Mexico City
MC_LATITUDE = 19.432608
MC_LONGITUDE = -99.133209

# Testing values
# MC_LATITUDE = -20.432608
# MC_LONGITUDE = -80.133209


# ========================================= ISS API
def is_iss_overhead():
    iss_api_endpoint = "http://api.open-notify.org/iss-now.json"

    iss_response = requests.get(url=iss_api_endpoint)
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    # #Your position is within +5 or -5 degrees of the ISS position.
    if (
        abs(MC_LATITUDE - iss_latitude) <= 5  # Option 1
        and MC_LONGITUDE - 5 <= iss_longitude <= MC_LONGITUDE + 5  # Option 2
    ):
        return True
    else:
        return False


# ========================================= Sunrise - Sunset API
def is_night():
    sunset_api_endpoint = "https://api.sunrise-sunset.org/json"

    parameters = {"lat": MC_LATITUDE, "lng": MC_LONGITUDE, "formatted": 0}

    sunset_response = requests.get(url=sunset_api_endpoint, params=parameters)
    sunset_response.raise_for_status()
    sunset_data = sunset_response.json()

    sunrise = sunset_data["results"]["sunrise"]
    sunset = sunset_data["results"]["sunset"]
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])

    time_now_hour = dt.datetime.now().hour

    if time_now_hour >= sunset_hour or time_now_hour <= sunrise_hour:
        return True
    else:
        return False


# ========================================= Send email
def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=gmail_mail, password=app_pwd_gmail)
        connection.sendmail(
            from_addr=gmail_mail,
            to_addrs=gmail_mail,
            msg="Subject:Look up!!\n\nThe ISS is above you in the sky",
        )


# Check if the ISS is close to my current position and it is currently dark
# If True, send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    if is_iss_overhead() and is_night():
        send_email()
    time.sleep(60)
