import pyttsx3
import datetime
import time
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import pyjokes
import subprocess
import tkinter
from bs4 import BeautifulSoup
import psutil
import pyautogui
from playsound import playsound
import random
import json
import requests
from win10toast import ToastNotifier





engine = pyttsx3.init()
rate = engine.setProperty('rate',175)
engine.say('welcome commander')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def start():
    speak('welcome back commander')
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        speak('Good morning commander')

    elif hour >=12 and hour <18:
        speak('good afternoon commander')

    else:
        speak('good evening commander')


    assname=("Olivegreen")
    speak('i am ur buddy !' + assname)

    
def buddyday():
    day = datetime.datetime.today().weekday() + 1
    day_dict={1:"monday",2:"tuesday",3:"wednesday",
              4:"thursday",5:"friday",6:"saturday",
              7:"sunday"}
    if day in day_dict.keys():
        dayoftheweek=day_dict[day]
        print(dayoftheweek)
        speak("the day is "+ dayoftheweek)
        speak('anything else buddy ?')
        
def buddytime():
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    speak("the time is " + localtime)

def location():
    speak('getting ur location as per ur request ')
    speak('you home is at')
    speak('opening google maps location for your reference')
    webbrowser.open("enter ur google map location")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)


def screenshot():
    speak('taking screenshot')
    img = pyautogui.screenshot()
    img.save(r"F:\screenshots olive\screenshot.png")

def melodies():
    songs_dir = "paste ur song location"
    music = os.listdir(songs_dir)
    speak('playing songs randomly')
    speak('enjoy ur time')
    no = random.randint(1,100)
    os.startfile(os.path.join(songs_dir, music[no]))

def spotify():
    speak('Get relaxation')
    webbrowser.open('www.spotify.com')

def websitealarm():
    speak("setting website alarm")
    Set_Alarm = input("Set the website alarm as H:M:S:")
    speak('alarmset')
    Actual_Time = time.strftime("%H:%M:%S")
    while (Actual_Time != Set_Alarm):
        print("The time is " + Actual_Time)
        speak('the time is' + Actual_Time)
        Actual_Time = time.strftime("%H:%M:%S")
        time.sleep(1)

    if (Actual_Time == Set_Alarm):
        print("You should see your webpage now :-)")
        speak('you should see the webpage now')

        webbrowser.open("www.youtube.com")


def weatherreport():
    speak('opening weather report')
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    speak('enter the city name ?')
    CITY = input('enter the city name ?')
    API_KEY = "enter ur API Key"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        print(f"{CITY:-^30}")
        speak('the city u mentioned is '+ CITY)
        print(f"Temperature: {temperature}")
        speak(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        speak(f"Humidity: {humidity}")
        speak(f"Pressure: {pressure}")
        print(f"Pressure: {pressure}")
        speak(f"Weather Report: {report[0]['description']}")
        print(f"Weather Report: {report[0]['description']}")
    else:
        print("Error in the HTTP request")
        speak('error in the HTTP request')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....buddy....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("unable to hear ur voice buddy ?")
        return "none"
    return search


if __name__=='__main__':
    clear = lambda: os.system('cls')

    clear()
    start()
              
    while True:
        search = takecommand().lower()


        if'wikipedia' in search:
            speak('searching ur results in wiki ,pls wait')
            search = search.replace('wikipedia', '')
            results = wikipedia.summary(search,3)
            print(results)
            speak(results)
            speak('anything else required buddy ?')

        elif 'open youtube' in search:
            speak('opening youtube as per ur request !')
            webbrowser.open("www.youtube.com")

        elif 'open google' in search:
            speak('opening google as per ur request !')
            webbrowser.open("www.google.com")

        elif 'how are you man ?' in search:
            speak('i am fine and how about you buddy ?')

        elif 'fine' or 'good' or 'ok' in search:
            speak('thats good to hear from you ')

        elif 'who are you ?' in search:
            speak('i am commanders virtual assistant, created by him')

        elif 'what can you do ' in search:
            speak('i will try my evel best to satisfy u')
            speak('what do you what me to do ?')

        elif 'jokes' in search:
            speak(pyjokes.get_joke())

        elif 'change name' in search:
            speak('what my new name ?')
            assname = takecommand().lower()
            speak('thank you for giving me anew name')
            speak('i am'+assname+'now')

        elif 'olive' in search:
            speak('yes buddy')
            speak('how can i help u ?')

        elif 'new note' in search:
            speak('on ur way')
            note = takecommand().lower()
            file = open('olive.txt','w')
            file.write(note)

        elif 'time now' in search:
            speak("the time is ")
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")

        elif 'stop listening' in search or 'take rest' in search :
            speak('thank you and how much time do you want me to stop listening')
            a = int(takecommand().lower())
            time.sleep(a)
            print(a)

        elif 'hospitals' in search:
            speak('searching hospitals nearby......')
            speak('opening locations details for hospitals via google maps')
            webbrowser.open("https://www.google.com/maps/search/hospitals+nearby/")

        elif 'tourists' in search:
            speak("enjoy ur day")
            speak('opening google maps')
            webbrowser.open("https://www.google.com/maps/search/tourists+places+nearby/")

        elif 'open meet' in search or 'google meet' in search:
            speak('opening google meet for attending online classes')
            webbrowser.open("https://meet.google.com/")

        elif 'shutdown system' in search:
            speak('system is on its way to shutdown')
            speak('are you sure wanna shutdown ur system ?')
            ans = takecommand().lower()
            if 'yes' in ans or 'sure' in ans:
                 subprocess.call('shutdown / p /f')
            else:
                speak('sorry for the intereption, carry on the work')

        elif 'turn off system' in search:
            speak('thank you, see u later')
            speak('turning off the system')
            subprocess.call('shutdown/p/f')

        elif 'restart' in search:
            speak("restarting system")
            subprocess.call(["shutdown", "/r"])

        elif 'goodnight' in search:
            speak('system moving to sleep')
            subprocess.call(['shutdown', '/h'])

        elif 'search youtube' in search:
            speak('what do you want me to search ? buddy')
            search_Term = takecommand().lower()
            webbrowser.open('https://www.youtube.com/results?search_query=' + search_Term)

        elif 'search in chrome' in search:
            speak('opening google chrome')
            cb = r"paste ur chrome.exe location here"
            speak('what do you want me to search ?')
            search_cb = takecommand().lower()
            webbrowser.get(cb).open_new_tab(search_cb+'.com')

        elif 'cpu usage' in search:
            cpu()
              

        elif 'take notes' in search:
            speak('What contents should i take notes sir?')
            notes = takecommand()
            file = open('notes.txt', 'w')
            speak("sir should i include Date and Time in your notes?")
            ans = takecommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done Taking Notes, SIR!')
            else:
                file.write(notes)

        elif 'keywords' in search:
            speak('opening keywords')
            kw =r"C:\Users\SElangovan\Desktop\keywords of olivegreenVA.txt"
            os.startfile('kw')

        elif 'screenshot' in search:
            screenshot()

        elif 'spotify' in search:
            spotify()

        elif 'melodies' in search:
            melodies()

        elif 'weatherreport' in search:
            weatherreport()

        elif 'quit' in search or 'bye bye' in search:
            speak('bye buddy, have a nice day')
            exit()





















