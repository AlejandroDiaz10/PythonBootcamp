"""
This program is going to send you a SMS at 6 am if you'll need an umbrella
For that, you can use python anywhere (https://www.pythonanywhere.com/)
This library supports the following Python implementations:
* Python 3.7
* Python 3.8
* Python 3.9
* Python 3.10
* Python 3.11
"""

import requests
from dotenv import load_dotenv
import os
from response import response_example  # Testing
from twilio.rest import Client

load_dotenv()

# =========================================================== Open Weather API
# Geo position for Mexico City
MC_LATITUDE = 19.432608
MC_LONGITUDE = -99.133209

# Geo position for Cuiabá - Testing (raining location)
# MC_LATITUDE = -15.601411
# MC_LONGITUDE = -56.097893

# Personal API Key
API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

# API reference: https://openweathermap.org/forecast5
parameters = {
    "lat": MC_LATITUDE,
    "lon": MC_LONGITUDE,
    "appid": API_KEY,
    "cnt": 4,  # Number of timestamps needed for a 12h window
}
api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(url=api_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# weather_data = response_example # Testing

# We need to verify if it'll rain in our location (list.weather.id < 700)
# API refrence: https://openweathermap.org/weather-conditions
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2

# weather_info_list = [dictionary["weather"] for dictionary in weather_data["list"]]
# weather_ids = [dictionary["id"] for lst in weather_info_list for dictionary in lst]
# for lst in weather_info_list -> Get every list in weather_info_list
# for dictionary in lst -> Iterate every dictionary in the list created
# dictionary["id"] -> Obtain the id of every dictionary iterated
# if any(item < 700 for item in weather_ids):
#     print("Bring an umbrella!")

will_rain = False
for list_item in weather_data["list"]:
    for weather_item in list_item["weather"]:
        if int(weather_item["id"]) < 700:
            will_rain = True


# =========================================================== Twilio API
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
personal_personal_number = os.getenv("PERSONAL_PHONE_NUMBER")

if will_rain:
    print("Bring an umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=personal_personal_number,
        from_=twilio_phone_number,
        body="It's going to rain today. Remember to bring an ☔️!",
    )

    print(message.status)
