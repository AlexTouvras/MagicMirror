import time
import requests

# Replace with your real API key later
API_KEY = "YOUR_API_KEY"
CITY = "Helsinki"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

while True:
    try:
        response = requests.get(BASE_URL, params={"q": CITY, "appid": API_KEY, "units": "metric"})
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]
            print(f"[WEATHER] {CITY}: {temp}°C, {condition}", flush=True)
        else:
            print(f"[WEATHER] API error: {response.status_code}", flush=True)
    except Exception as e:
        print(f"[WEATHER] Exception: {e}", flush=True)
    time.sleep(3600)  # Update every hour
