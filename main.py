import os
import time
import playsound
import speech_recognition as sr 
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said=""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


audio=get_audio()

if "hello" in audio:
    speak("Hello, How are you?")
if "what is your name" in audio:
    speak("My name is Christopher")