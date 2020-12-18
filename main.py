import requests
from api_keys import api_key_open_weather


# Functions
def get_weather_data(lat, lng):
    api_open_weather = "https://api.openweathermap.org/data/2.5/onecall"
    parameters = {
        "lat": lat,
        "lon": lng,
        "exclude": "current,minutely,daily",
        "appid": api_key_open_weather,
    }
    response = requests.get(url=api_open_weather, params=parameters)
    response.raise_for_status()

    return response.json()


def check_hour_rain(weather_data):
    for hour in weather_data:
        hour_weather = hour["weather"]
        for condition in hour_weather:  # if multiple weather conditions in hour
            # weather id; https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
            if condition["id"] < 700:
                return True


# Main
weather_data = get_weather_data(lat=38.880470, lng=-77.301872)
weather_next_12_hours = weather_data["hourly"][:12]

if check_hour_rain(weather_next_12_hours):
    print("Grab an umbrella")
