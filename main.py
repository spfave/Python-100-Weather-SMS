import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()


# Functions
def get_weather_data(lat, lng):
    api_open_weather = "https://api.openweathermap.org/data/2.5/onecall"
    parameters = {
        "lat": lat,
        "lon": lng,
        "exclude": "current,minutely,daily",
        "appid": os.getenv("api_key_open_weather"),
    }
    response = requests.get(url=api_open_weather, params=parameters)
    response.raise_for_status()

    return response.json()


def check_hour_rain(weather_data):
    for hour in weather_data:
        hour_weather = hour["weather"]
        for condition in hour_weather:  # if multiple weather conditions in hour
            # weather condition ids; https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
            if condition["id"] < 700:
                return True


def send_rain_message():
    client = Client(os.getenv("twilio_sid"), os.getenv("twilio_token"))
    message = client.messages \
                    .create(
                        body="Looks like rain's in the 12 hour forcast, suggest grabbing an umbrella 🌧",
                        from_=os.getenv("twilio_number"),
                        to=os.getenv("phone_number")
                    )
    print(message.status)


# Main
weather_data = get_weather_data(lat=38.880470, lng=-77.301872)
# weather_data = get_weather_data(
#     lat=40.760780, lng=-111.891045)  # test location with rain
weather_next_12_hours = weather_data["hourly"][:12]

if check_hour_rain(weather_next_12_hours):
    send_rain_message()
    # print("Grab an umbrella")
