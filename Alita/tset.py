# from datetime import datetime, timedelta

# # Get the current time
# now = datetime.now()

# # Format the current time in 12-hour format with AM/PM
# strTime = now.strftime("%I:%M %p")
# speak(f"The current time is {strTime}")
# print(strTime)

# # Calculate the time 12 hours from now
# time_after_12_hours = now + timedelta(hours=12)

# # Format the time 12 hours after in 12-hour format with AM/PM
# strTime_after_12_hours = time_after_12_hours.strftime("%I:%M %p")
# speak(f"The time 12 hours from now will be {strTime_after_12_hours}")
# print(strTime_after_12_hours)





# lif 'esha time' in query or 'time' in query:
#             strTime = datetime.datetime.now().strftime("%H %M")
#             speak(f"{strTime}") 
#             print(strTime)

###########################################################################################3

import cv2

# Load the pre-trained Haar-Cascade model for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw bounding boxes around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the result
    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

########################################################3
def wiki_search():
    """[Speak out the summary in wikipedia and going to the website according to user's choice.]
    """    
    wiki_search = "What do you want me to search on Wikipedia? Please tell me the exact sentence or word to Search."
    wiki_search_link = "https://en.wikipedia.org/wiki/"
    
    print(wiki_search)
    speak(wiki_search)

    query = hear()
    try:

        if query != "None":
            results = wikipedia.summary(query, sentences = 2)
            print(results)
            speak(results)

            print("Do you want me to open the Wikipedia page?")
            speak("Do you want me to open the Wikipedia page?")
            q = hear().lower()

            if "yes" in q or "okay" in q or "ok" in q or "opun" in q or "opan" in q or "vopen" in q or "es" in q or "s" in q:
                print(wiki_search_link + query)
                webbrowser.open(wiki_search_link + query)

            elif query == "None":
                print("I could'nt understand what you just said!")
                speak("I could'nt understand what you just said!")

    except Exception as e:
        print("Couldn't find")