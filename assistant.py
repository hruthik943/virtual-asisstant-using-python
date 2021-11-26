import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')   
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        super("Good Evening")
    speak("I am Jarvis Sir.Please tell me how may i help you")

def takecommand():
    #It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")

    except Exception as e:
        print("say that again pleaase") 
        return "None"   
    return query

if __name__=='__main__':
    wishme()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("Acoording to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir='C:\\Users\\hruthik\\Desktop\\music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")
        elif 'open code' in query:
            codepath="C:\\Users\\hruthik\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
            os.startfile(codepath)
        

            
