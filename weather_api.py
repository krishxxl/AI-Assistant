import requests
from text_to_speech import speak

def get_weather(city):
    api_key = "your_api_key"  #  OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]["description"]
        speak(f"The weather in {city} is {weather} with a temperature of {main['temp']} Kelvin.")
    else:
        speak("City not found.")
