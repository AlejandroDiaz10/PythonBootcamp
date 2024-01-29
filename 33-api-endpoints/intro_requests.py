import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # If there is any error, show it

data = response.json()
# print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)
