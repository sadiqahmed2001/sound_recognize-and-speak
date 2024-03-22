# Sadiq-Ahmed
hello,welcome to my mini project "chaliya shuru kartay hay firstly hum iskay feature dekh laytay hay or unboxing kartay hay meray code ko jo bahot hi dimag khaya hay mera:-----"

---------------------------------******* Namaskar may youth ka vafadar pythoncode kumar ************-----------------------------------------------------
---------------------------------******* lets begins with *********************------------------------------------------------------------------------

import face_recognition as sr   #for lisining the user input through the voice
import pyttsx3   # for speaking what user says

step1:-

Creating a Recognizer Object:-
 we need to create a Recognizer object, which will be responsible for recognizing the speech...


recognizer = sr.Recognizer()
Recording Audio
To recognize speech, we first need to record audio. 
We will use the Microphone class from the SpeechRecognition library to do this.
we have  to install the PyAudio library to use the Microphone class. 
 

step2:-

Now, let's create a function to record audio:

def record_audio():
    with sr.Microphone() as source:
        print("Listening...")
        speak("listening...")
        audio = recognizer.listen(source)
    return audio

step3:-

Recognizing Speech:-
Now  we have a function to record audio,
we can use the Recognizer object to recognize the speech. 


def recognize_speech(audio):
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")

step4:-
in this step we have to define the speak function, which is written below.....!!

def speak(text):
    engine=pyttsx3.init()
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 120)  
    engine.setProperty("voice","english_rp")
    engine.say(text)
    engine.runAndWait()

step5:-Put It All Together.......!!!!!!!!!!

lastly,  put the above code which i have just writen and then --"boom"-- that records audio and recognizes speech:



import speech_recognition as sr

recognizer = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        print("Listening...")
        speak("listening...")
        audio = recognizer.listen(source)
    return audio

def recognize_speech(audio):
    try:
        text = recognizer.recognize_google(audio)
        speak(f"You said: {text}")
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
    except sr.RequestError:
        speak("Sorry, there was an error processing your request.")

def speak(text):
    engine=pyttsx3.init()
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 120)  
    engine.setProperty("voice","english_rp")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    audio = record_audio()
    speak(audio)
    recognize_speech(audio)
When you run this code, it will listen to your speech and speak out the recognized text. 



conclusion:-
The above code is written for the puprose of problem solving the labour cost problems like for an instance if the resturant or any small scale 
bussiness have to take a feedback or take any orders from customer they must have to hire the skilled person to handel customer.
but this program which i written it can be modify in such a mannner that can be handle huge customers at a time to solve the problems for online platforms like uber,zommato,myntra,flipkart,amazon many moree...


references:-
Python Notes which i have learned till know, and libraries and google.......
----------------------------------------------------------------------------------------------------**** By Sadiq Ahmed ***------------------
