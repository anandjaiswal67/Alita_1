import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import keyboard
import pyjokes
import pyautogui
import os
import pywhatkit
from pywikihow import search_wikihow
from bs4 import BeautifulSoup

import nltk
from news  import get_news
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('volume', 1.5)
engine.setProperty('rate',225)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishME():
    hour = int(datetime.datetime.now().hour)
    if  hour>=0 and hour<12:
        speak("Good morning Boss")
        speak("")
    elif hour>=12 and hour<18:
        speak("good Afternoon Boss")
        speak("")
    else:
        speak("good Evening Boss")
        speak("")

listening = False

def start_listening():
    global listening
    listening = True
    print("started listening")

# def pause_listening():
#     global listening
#     listening = False
#     print("stoped_listening")

# keyboard.add_hotkey('ctrl+alt+s',start_listening)
# keyboard.add_hotkey('ctrl+alt+p',pause_listening)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language= "en-in") 
        print(f"Sir: {query}\n")      
    except Exception as e:
        
        print("Say that again please...")
        return "None"
    return query

if __name__  ==  "__main__":
    while True:
        if listening:
            query = takeCommand().lower()

            if 'who are you' in query:
                speak('i am  ,Alita  a Supercomputer ')

            elif 'Alita' in query or 'hello Alita' in query or 'hello' in query:
                wishME()
            else :
                ""
            if 'joke' in query or 'once more joke' in query:
                speak('ok Boss')
                my_jokes = pyjokes.get_joke('en', category='neutral')
                print(my_jokes)
                speak(my_jokes)

            elif 'Alita search' in query or 'Alita what is' in query or 'Alita who is' in query:
                speak('ok Boss searching')
                speak('')
                query = query.replace("search", "")
                query = query.replace("what is", "")
                query = query.replace("who is", "")
                query = query.replace("Alita ", "")
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(results) 
            elif 'Alita how to' in query:
                speak('ok Boss, searching')
                speak ('wait few seconds Boss')
                query = query.replace("Alita ", "")
                max_results = 1
                how_to = search_wikihow(query, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary) 

            elif 'Alita time' in query or 'time' in query:
                strTime = datetime.datetime.now().strftime("%I %M %p")
                print(strTime)
                speak(f"{strTime}") 

            if 'Alita play' in query or 'song' in query or 'Alita can you play Music' in query or 'Music' in query:
                speak("ok Boss playing")
                query = query.replace("Alita", "")
                query = query.replace("Alita can you", "")
                query = query.replace("play", "")
                query = query.replace(" ", "")
                wab= f"https://www.youtube.com/results?search_query"+ query
                webbrowser.open(wab)
                pywhatkit.playonyt(query)
            elif 'Alita pause' in query or 'stop' in query or 'pause the video' in query or 'stop the video' in query:
                pyautogui.press("k")
            elif 'start' in query or 'play the video' in query:
                pyautogui.press("k")
            elif 'mute' in query or 'mute the video'in query or 'mute' in query:
                pyautogui.press("m")
            elif 'backward' in query:
                pyautogui.press("j")
            elif 'forward' in query:
                pyautogui.press("l")
            elif 'speed up' in query:
                pyautogui.press(">")
            elif 'slow down' in query:
                pyautogui.press("<")
            elif 'full screen' in query:
                pyautogui.press("f")
            elif 'minimise' in query:
                pyautogui.press("f")
            elif 'Next' in query:
                pyautogui.press("SHIFT+N")
            elif 'replay' in query:
                pyautogui.press("shift+P")
            elif "volume up" in query:
                from keyboard import volumeup
                volumeup()
            elif "volume down" in query:
                from keyboard import volumedown
                volumedown()
            else:
                (" ")

            if 'Alita .com' in query or 'Alita .co.in' in query or 'Alita .org' in query or 'open .com' in query:
                speak("ok Boss")
                query = query.replace("Alita", "")
                query = query.replace("open","")
                query = query.replace(" ","")
                webbrowser.open(f'https://www.{query}')

            if 'Alita what the weather' in query or 'temperature' in query:
                weather = f"https://www.google.com/search?q="+ query
                r = requests.get(weather)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div",class_ = "BNeawe").text
                speak(f'current{query} is {temp}')
            
            # elif "news" in query:
            #     speak("Here are the latest news")
            #     speak(get_news())
            #     print(*get_news(),sep='\n')

            elif "traet numders" in query:
                query = query.replace("traet", "")
                from loctionTrack import getResult
                getResult()
                
            
            elif 'Alita sleep' in query or "by" in query:
                speak("ok Boss i can go to sleep ")
                break