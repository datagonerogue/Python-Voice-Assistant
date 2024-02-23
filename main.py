import os
import time
import datetime
import glob
import playsound
import speech_recognition as sr 
from gtts import gTTS

# Generating Directory
SPEECH_DIR = "Generated Speech"
if not os.path.exists(SPEECH_DIR):
    os.makedirs(SPEECH_DIR)

for file in glob.glob(os.path.join(SPEECH_DIR, "*.mp3")):
    os.remove(file)

# Speak Function
def speak(text):
    now = datetime.datetime.now()
    formatted_time = now.strftime("%H-%M-%S")
    filename = os.path.join(SPEECH_DIR, f"Speech_{formatted_time}.mp3")
    tts = gTTS(text=text, tld='us', lang="en", slow=False)
    tts.save(filename)
    print("Sara: " + text)
    playsound.playsound(filename)

# Listener
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said=""
        try:
            said = r.recognize_google(audio)
            print("You: " + said)
        except sr.UnknownValueError:
            return ""
        except Exception as e:
            speak("An Exception has occurred")
            print("Exception: " + str(e))  
    return said

# Main Logic
def action():
    while True:
        print("[Listening]")
        audio=get_audio()
        if "hello" in audio:
            speak("Hello, is there anything i can help you with?")
        elif "your name" in audio:
            speak("My name is Sara")
        elif "that's it" in audio:
            break
        elif audio=="":
            speak("Sorry, I am not able to hear you.")
        else:
            speak("Sorry, I can't help you with that.")

while True:
    try:
        print("[Listening in Background]")
        init=get_audio()
        if "Sara" in init:
            print("Processing")
            action()
    except KeyboardInterrupt:
        break
