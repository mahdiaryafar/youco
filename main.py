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
engine.setProperty('voice','voices[0].id')

def  speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = r.listen(source)
        print(audio)
    try:
        statement = r.recognize_google(audio,language='fa-IR')
        print(f"user said:{statement}\n")
        return statement

    except Exception as e:
        speak("Pardon me, please say that again")
        return None

    

print("Loading your AI personal assistant G-One")
speak("Loading your AI personal assistant G-One")
wishMe()


if __name__=='__main__':
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand()
        if statement == 0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant G-one is shutting down,Good bye')
            break