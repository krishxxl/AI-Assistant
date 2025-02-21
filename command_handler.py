from datetime import datetime
from weather_api import get_weather
from text_to_speech import speak

def handle_command(command):
    if 'hello' or 'hi' or 'hey' in command:
        speak("Hello! How can I assist you today?")
    elif 'time' in command:
        now = datetime.now()
        speak(f"The current time is {now.strftime('%H:%M')}")
    elif 'weather' in command:
        city = command.split('weather in ')[-1].split(' ')[0]
        get_weather(city)
    elif 'remind me to' in command:
        # Extract the task and time from the command
        task = command.split('remind me to ')[-1].split(' at ')[0]
        time_str = command.split(' at ')[-1]
        add_reminder(task, time_str)
    else:
        speak("Sorry, I don't understand that command.")