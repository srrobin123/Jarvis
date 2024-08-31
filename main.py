import speech_recognition as sr
import pyaudio
import webbrowser
import pyttsx3
import musicLibrary


engine = pyttsx3.init()

def speak(text: str):
   engine.say(text)
   engine.runAndWait()

def processCommnad(c: str):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("Open google")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("Open youtube")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("Open facebook")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        speak("Open linkedin")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com/")
        speak("Open whatsapp")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
        speak("Open instagram")
    elif "open threads" in c.lower():
        webbrowser.open("https://www.threads.net/")
        speak("Open threads")
    elif "open fiverr" in c.lower():
        webbrowser.open("https://www.fiverr.com/rs_rashedul")
        speak("Open fiverr")
    elif "open mail" in c.lower():
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        speak("Open google")
    elif "open blc" in c.lower():
        webbrowser.open("https://elearn.daffodilvarsity.edu.bd/my/")
        speak("Open universtiy blc")
    elif "thank you" in c.lower():
        speak("Walcome sir")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1] +" "+ c.lower().split(" ")[2]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        speak("Play song")
    else:
        pass
    
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    
    while(True):
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recongnizing...")
        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if("jarvis" in word.lower()):
                speak("Yes sir")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommnad(command)
                    
        except Exception as e:
            print(f"error; {e}")
