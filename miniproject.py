import speech_recognition as s
import pyttsx3

recognizer = s.Recognizer()

def record_audio():
    with s.Microphone() as source:
        speak("Listening...")
        print("listening....")
        audio = recognizer.listen(source)
    return audio

def recognize_speech(audio):
    try:
        text = recognizer.recognize_google(audio)
        speak(f"You said: {text}")
    except s.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
    except s.RequestError:
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