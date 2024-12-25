# import pyttsx3
# import speech_recognition as sr
# import pandas
# import nltk
# nltk.download('punkt_tab')
# nltk.download('punkt')
# nltk.download('wordnet')
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
# engine.setProperty('volume', 10.0)
# engine.setProperty('rate',180)



# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 2
#         audio = r.listen(source,0,3)
#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language= "en-in") 
#         print(f"Boss: {query}\n")      
#     except Exception as e:
#         # print (e)
        
#         print("Say that again please...")
#         return "None"
#     return query

# lemmatizer = WordNetLemmatizer()
# responses = {
#     "hello": "Hello, I am a esha.",
#     "how are you": "I am fine, thank you.",
#     "what is your name": "My name is esha.",
#     "what can you do": "I can chat with you hiand answer some questions.",
#     "bye": "Goodbye, have a nice day, bye sir."
# }

# def preprocess(text):
#     text = text.lower()
#     query = word_tokenize(text)
#     query = [lemmatizer.lemmatize(word) for word in query]
#     return query

# def match(query):
#     scores = []
#     for key in responses.keys():
#         key_query = preprocess(key)
#         similarity = len(set(query).intersection(set(key_query))) / len(set(query).union(set(key_query)))
#         scores.append(similarity)
#     if scores:
#         max_index = scores.index(max(scores))
#         return list(responses.values())[max_index]
#     else:
#         return "I didn't understand that."

# def chat():
#     while True:
#         query = takeCommand().lower()
#         if query == 'quit':
#             break
#         user_query = preprocess(query)
#         bot_output = match(user_query)
#         print("ishe: " + bot_output)
#         speak(bot_output)

# if __name__  ==  "__main__":
#     chat()




import pyttsx3
import speech_recognition as sr
import pandas as pd
import nltk
# nltk.download('punkt_tab')
# nltk.download('punkt')
# nltk.download('wordnet')
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices)
# engine.setProperty('volume', 1.0)  # Set volume to maximum
# engine.setProperty('rate',180)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 2
#         audio = r.listen(source, timeout=3)  # Added timeout for better handling
#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language="en-in") 
#         print(f"Boss: {query}\n")      
#     except Exception as e:
#         # print (e)
        
#         print("Say that again please...")
#         return "None"
#     return query

# lemmatizer = WordNetLemmatizer()
# conversations_df = pd.read_csv('conversations.csv')
# responses = conversations_df.set_index('input')['response'].to_dict()

# def preprocess(text):
#     text = text.lower()
#     query = word_tokenize(text)
#     query = [lemmatizer.lemmatize(word) for word in query]
#     return query

# def match(query):
#     scores = []
#     for key in responses.keys():
#         key_query = preprocess(key)
#         similarity = len(set(query).intersection(set(key_query))) / len(set(query).union(set(key_query)))
#         scores.append(similarity)
#     if scores:
#         max_index = scores.index(max(scores))
#         return list(responses.values())[max_index]
#     else:
#         return "I didn't understand that."

# def chat():
#     while True:
#         query = takeCommand().lower()
#         if query == 'quit':
#             break
#         user_query = preprocess(query)
#         bot_output = match(user_query)
#         print("ishe: " + bot_output)
#         speak(bot_output)

# if __name__  ==  "__main__":
#     chat()