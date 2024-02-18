import requests
from datetime import datetime

MY_LAT = 37.208958
MY_LONG = -93.292297

# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
#
# response.raise_for_status()
#
# data = response.json()
#
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {"lat": MY_LAT,
              "lng": MY_LONG,
              "formatted": 0,
}

response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])

time_now = datetime.now()

print(time_now)
