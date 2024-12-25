import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_news():
    news_headline=[]
    resuilt=requests.get = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=00794e3ab62c47df80cd78b51e5284d1",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=00794e3ab62c47df80cd78b51e5284d1",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=00794e3ab62c47df80cd78b51e5284d1",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=00794e3ab62c47df80cd78b51e5284d1",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=00794e3ab62c47df80cd78b51e5284d1",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=00794e3ab62c47df80cd78b51e5284d"}.json()
    articles = resuilt["articles"]
    for i in articles:
        news_headline.append(i["title"])
        return news_headline[:6]
    