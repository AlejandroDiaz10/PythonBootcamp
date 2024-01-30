import requests

# api_endpoint = "https://opentdb.com/api.php?amount=10&type=boolean"
# "category": 18 -> Computer Science related
parameters = {"amount": 10, "type": "boolean", "category": 18}
api_endpoint = "https://opentdb.com/api.php"

response = requests.get(url=api_endpoint, params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
