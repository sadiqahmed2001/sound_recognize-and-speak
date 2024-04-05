# mini-project:-python
hello, welcome to my mini project:-----"

---------------------------------*******************-----------------------------------------------------
---------------------------------******* lets begins with *********************------------------------------------------------------------------------

import face_recognition as sr   #for listening to the user input through the voice
import pyttsx3   # for speaking what the user says 

step1:-

Creating a Recognizer Object:-
 we need to create a Recognizer object, which will recognize the speech...


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
in this step, we must define the speak function, which is written below.....!!

def speak(text):
    engine=pyttsx3.init()
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 120)  
    engine.setProperty("voice","english_rp")
    engine.say(text)
    engine.runAndWait()

step5:-Put It All Together.......!!!!!!!!!!

lastly,  put the above code which I have just written, and then --"boom"-- that records audio and recognizes speech:



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
The above code is written for problem-solving labor cost problems for instance if the restaurant or any small-scale 
business has to take feedback or take any orders from customers they must have to hire a skilled person to handle customers.
but this program which I wrote can be modified in such a manner that it can handle huge customers at a time to solve the problems for online platforms like Uber,zommato,myntra, Flipkart, amazon many more...


references:-
Python Notes which I have learned till now, and libraries and Google.......
----------------------------------------------------------------------------------------------------**** By Sadiq Ahmed ***------------------
