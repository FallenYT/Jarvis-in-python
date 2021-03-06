
from typing import Mapping
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)

engine.setProperty('voice',voices[1].id)






def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")

    speak("Hello I am Ishwari the child. Please tell me how may I help you")

def takeCommand():
    #It takes Microphone input fromthe User and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold=300
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
      

    except Exception as e:
        # print(e)
        print("Say tht again plz....")
        return"None"
    return query

def sendEmail(to, content):# less secured apps in gmail have to enable while starting
    server = smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login()
    server.login('shritejlakade02@gmail.com','Password')# Type your password whie running
    server.sendmail('shritejlakade02@gmail.com',to,content)
    server.close()
    
    
if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
        
        # logic on task based on query
        
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            
            
        elif 'play music' in query:
            music_dir = 'D:\\python project JARVIS\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")     
        

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
            
        elif 'email to shri' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "shritejlakade02@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry")    
                
    
    



