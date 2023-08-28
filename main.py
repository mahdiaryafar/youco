import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

lang = input('fa OR en? ')
if lang == 'fa':
    lang = 'fa-IR'
else:
    lang = 'en-US'


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening...")
        audio = r.listen(source)
        print(audio)
    try:
        statement = r.recognize_google(audio, language=lang)
        print(f"user said:{statement}\n")
        return statement

    except Exception as e:
        speak("Pardon me, please say that again")
        return 0

speak("Loading yooucoo")
wishMe()
if __name__ == '__main__':
    speak("Tell me how can I help you now?")
    while True:
        statement = takeCommand()
        if statement == 0:
            continue
        if "خداحافظ" in statement or "خدانگهدار" in statement or "تمام" in statement or "پایان" in statement or "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('yooucoo is shutting down,Good bye')
            break
        elif 'open google' in statement or "گوگل" in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)	
        elif 'open gmail' in statement or "جیمیل" in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        elif 'time' in statement or "زمان" in statement or "ساعت چنده" in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")