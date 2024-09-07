from datetime import datetime, timedelta
import requests
from datetime import datetime
import smtplib

"""
TASK: Print "Bring an Umbrella" if either weather id < 700 in next 12 hours. 
Best way to test this code, pick 2 locations one that's sunny, and that's raining. 

Coordinates for London (Summer time currently), received no print statement = success!
Coordinates for a rainy city (currently, Zilina - Slovakian Area), receive a print statement = success! 
"""

# Coordinates for Zilina (Slovakian Area) (current)
# Coordinates for London
MY_LAT = 0              # TYPE YOUR LAT IN
MY_LONG = 0             # TYPE YOUR LONG IN

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": "c52f9034b7d11d21a46af64f16a1aedb",
    "cnt": 4    # forecast for 4 days, day 0 via JSON viewer is today.
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_ids = []
day_1_id = weather_ids.append(response.json()["list"][0]["weather"][0]["id"])
day_2_id = weather_ids.append(response.json()["list"][1]["weather"][0]["id"])
day_3_id = weather_ids.append(response.json()["list"][2]["weather"][0]["id"])
day_4_id = weather_ids.append(response.json()["list"][3]["weather"][0]["id"])

time_now = datetime.now()
time_later = (time_now + timedelta(hours=12)).strftime('%H:%M:%S')  # 12 hours later

if weather_ids[1] < 700 and time_later:   # If it's the next day, ID < 700 and 12 hours later
    """ I used email for this, however using Twilio was an option."""
    sender_email = " "      # Enter your email
    sender_password = " "   # Passkey found with your email provider
    recipient_email = " "   # recipient email

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure Connection
        connection.login(user=sender_email, password=sender_password)  # Login
        connection.sendmail(from_addr=sender_email,
                            to_addrs=recipient_email,
                            msg="Subject:The Weather\n\n"f"Hey, You need bring an Umbrella")
        connection.close()  # Closes Connection
