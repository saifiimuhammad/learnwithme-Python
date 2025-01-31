import requests
import json
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice").Speak

API_KEY = "168546ed37044d18b6863210252101"

try:
    while True:
        print("Welcome to Weather App")
        city = str(input("Enter the city or exit: "))
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
        if city == "":
            print("Please enter a city")
            speak("Please enter a city")
            exit()
        if(city == "exit"):
            print("Thank you for using our app")
            speak("Thank you for using our app")
            exit()

        r = requests.get(url)
        weatherDic = json.loads(r.text)
        weather = weatherDic["current"]["temp_c"]
        print(f"The current weather in {city} is {weather}")
        speak(f"The current weather in {city} is {weather}")
except Exception as e:
    print("An error occured")
    print(e)

# todos

# Speak
# Other things also mention