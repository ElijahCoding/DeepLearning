import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import yfinance as yf # to fetch financial data
import ssl
import certifi
import time
import os # to remove created audio files

r = sr.Recognizer()

with sr.Microphone() as source:
    print('SAY SOMETHING')
    audio = r.listen(source)
    voice_data = r.recognize_google(audio)
    print(voice_data)