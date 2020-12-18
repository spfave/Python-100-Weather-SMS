import requests
from api_keys import api_key_open_weather

api_open_weather = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": 38.880470,
    "lon": -77.301872,
    "appid": api_key_open_weather}

response = requests.get(url=api_open_weather, params=parameters)
response.raise_for_status()

print(response.json())


# ""
