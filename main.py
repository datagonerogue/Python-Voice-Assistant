import os
import time
import datetime
import glob
import playsound
import speech_recognition as sr 
from gtts import gTTS

SPEECH_DIR = "Generated Speech"

if not os.path.exists(SPEECH_DIR):
    os.makedirs(SPEECH_DIR)

for file in glob.glob(os.path.join(SPEECH_DIR, "*.mp3")):
    os.remove(file)
    
def speak(text):
    now = datetime.datetime.now()
    formatted_time = now.strftime("%H-%M-%S")
    
    filename = os.path.join(SPEECH_DIR, f"Speech_{formatted_time}.mp3")
    tts = gTTS(text=text, tld='us', lang="en", slow=False)
    tts.save(filename)
    print("rA9: " + text)
    playsound.playsound(filename)

    
def get_audio():
    print("Listening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said=""

        try:
            said = r.recognize_google(audio)
            print("You: " + said)
        except sr.UnknownValueError:
            speak("Sorry, I am not able to hear you.")
        except Exception as e:
            speak("An Exception has occured")
            print("Exception: " + str(e))
            

    return said

speak("Hello, I am your virtual assistant. How can I help you?")

while True:
    
    audio=get_audio()
    if "hello" in audio:
        speak("Hello, is there anything i can help you with?")
    elif "your name" in audio:
        speak("My name is r A 9")
    elif audio=="":
        continue
    elif audio=="that's it":
        break
    else:
        speak("Sorry, I can't help you with that.")
