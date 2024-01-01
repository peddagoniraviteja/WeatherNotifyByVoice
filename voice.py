import requests
from plyer import notification
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime 
import pyjokes
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            return("not understand")
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',130)
    engine.say(x)
    engine.runAndWait()
def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # You can change this to 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        return weather_data['main']['temp'], weather_data['weather'][0]['description']
    else:
        return None

def show_notification(city, temperature, description):
    title = f"Weather in {city}"
    message = f"Temperature: {temperature}°C\nDescription: {description}"

    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # e.g., 'path/to/icon.png'
        timeout=50,  # seconds
    )    
if __name__ == "__main__":
    prasad = True
    if "siri" in sptext().lower() :
        speechtx("AT your service please command....")
        while(prasad):
            speechtx("what service do you need..")
            x = sptext().lower()
            city = "not understand"
            if "weather" in  x or "climate" in x :
                api_key = 'fe2be4e720ba3db464ded44b7bf7de51'
                while(city=="not understand"):
                    speechtx("which city are you looking for")
                    city = sptext().lower()
                    speechtx(city)
                    print(city)
                    weather_info = get_weather(api_key, city)
                    if weather_info:
                        temperature, description = weather_info
                        show_notification(city, temperature, description)
                        speechtx(temperature)
                    else:
                        speechtx("Failed to fetch weather information. Check your API key and city.")
            elif "stop" in x or "exit" in x:
                prasad = False
            # else:
            #     f = sptext().lower()
            #     u = f"https://www.google.com/search?q={f}"
            #     r = requests.get(u)
            #     speechtx(r)
         

    else:
        speechtx("wrong coded your are not my owner....")