import requests

city = input("Enter city name: ")

api_key = "weather_app"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print("\n--- WEATHER REPORT ---")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Weather:", description)
else:
    print("Unable to fetch weather data.")
    print("Error:", data.get("message", "Unknown error"))