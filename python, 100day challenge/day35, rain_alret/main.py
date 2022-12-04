import requests

import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
phone_number = os.environ.get("MY_PHONE_NUMBER")
client = Client(account_sid, auth_token)

API_KEY = "9a987bf5d207aff8c1f86915ec7e08d7"
# LAT = 37.456257
# LON = 126.705208

# 임의의 지역의 위, 경도를 사용함
LAT = 66.208504
LON = 177.579182


parameter = {
    "lat": LAT,
    "lon": LON,
    "exclude": "current,minutely,daily,alerts",
    "units": "metric",
    "appid": API_KEY
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameter)
print(response.status_code)
# response.raise_for_status()

weather_data = response.json()
print(weather_data["hourly"][0]["weather"][0]["id"])
twelve_hour_weather = weather_data["hourly"][:12]

will_rain = False

for weather in twelve_hour_weather:
    weather_code = weather["weather"][0]["id"]
    if weather_code < 700:
        will_rain = True

if will_rain:
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+19375078026',
        to=phone_number
    )

    print(message.status)




