import pyttsx3
import datetime
import speech_recognition as sr
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voices', voices[0].id)
#print(voices[1].id)
# text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# to convert voice into text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1,phrase_time_limit=5)
    try:
        print("Recognition....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("Say that again please....")
        return "none"
    return query
# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good AfterNoon!")
    else:
        speak("Good Evening")
    speak("I am Jarvis sir. Please tell me Prasant sir how can I help you")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('prasantaman2022@gmail.com', 'Prasant@#$%2024')
    server.sendmail('prasantaman2022@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    wish()
    while True:
    #if 1:


        query = takeCommand().lower()
        # logic building for tasks
        if "open notepad" in query:
            npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2401.26.0_x64__8wekyb3d8bbwe\\Notepad"
            os.startfile(npath)
        elif"open arduino ide" in query:
            apath = "C:\\Users\\Aman Sahu\\AppData\\Local\\Programs\\Arduino IDE\\Arduino IDE.exe"
            os.startfile(apath)
        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            #print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        elif "open linkedin" in query:
            webbrowser.open("www.linkedin.com")
        elif "open chrom" in query:
            webbrowser.open("www.chrom.com")

        elif "send message" in query:
            kit.sendwhatmsg("+917991302003","hi",11,53)
        elif "play song on youtube" in query:
            kit.playonyt("tu nazm nazm sa mere slowed and reverb")
        elif "email to prashant" in query:
            try:
                speak("what should i say?")
                content = takeCommand().lower()
                to = "prasantaman2022@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to prashant")
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this mail to prashant")
        elif "no thanks" in query:
            speak("thanks for using me sir, have a nice day")
            sys.exit()



        speak("sir, do you have any other work ")












