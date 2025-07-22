import requests

def get_weather(city_name, api_key):
    # OpenWeatherMap API URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    # Send request to the API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Extract relevant data
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        city = data['name']
        country = data['sys']['country']
        print(f"\nWeather in {city}, {country}")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {description.capitalize()}")
    else:
        print("\nCity not found or invalid API key!")

# Replace with your actual API key from OpenWeatherMap
api_key = "your_api_key_here"

city = input("Enter city name: ")
get_weather(city, api_key)
