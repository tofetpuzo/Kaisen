import requests

note1 = "6.5095° N, 3.3711° E"
note2 = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
note3 = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
note4 = "https://api.open-meteo.com/v1/forecast?latitude=6.5095&longitude=3.3711&hourly=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"



latitude = 6.5095  # Yaba, Lagos latitude
longitude = 3.3711  # Yaba, Lagos longitude
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temperature_data = data['hourly']['temperature_2m']
    humidity_data = data['hourly']['relative_humidity_2m']
    wind_data = data['hourly']['wind_speed_10m']
    print(f"Temperature forecast for the next few hours: {temperature_data[:5]}")  # Print first 5 hours
    print(f"Relative humidity forecast for the next few hours: {humidity_data[:5]}")  # Print first 5 hours
    print(f"Wind speed forecast for the next few hours: {wind_data[:5]}")  # Print first 5 hours
else:
    print("Failed to fetch weather data.")
