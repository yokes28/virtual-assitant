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
engine.say('thankyou for turning in back me')


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
    speak('your home is at chinniyampalayam')
    speak('opening google maps location for your reference')
    webbrowser.open("https://www.google.com/maps/place/Chinniyampalayam,+Coimbatore,+Tamil+Nadu/@11.0623152,77.040331,14.5z/data=!4m5!3m4!1s0x3ba85624d5f9b0cf:0x8c0a9bfa4b8ebb40!8m2!3d11.0553431!4d77.0655238")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def keywords():
    speak('opening keywords for ur help')
    speak('go through it and take me on board')
    kw = r"C:\Users\SElangovan\Desktop\keywords of olivegreenVA.txt"
    os.startfile(kw)

def screenshot():
    speak('taking screenshot')
    img = pyautogui.screenshot()
    img.save(r"F:\screenshots olive\screenshot.png")

def melodies():
    songs_dir = "E:\yokes\songs\Melodies"
    music = os.listdir(songs_dir)
    speak('playing songs randomly')
    speak('enjoy ur time')
    no = random.randint(1,100)
    os.startfile(os.path.join(songs_dir, music[no]))

def spotify():
    speak('vela pathathu pothum da poi relax pannu')
    webbrowser.open('https://open.spotify.com/playlist/3DG4JuxAKRLg6zna6Pe04C')

def alarmclock():
    speak('setting alarm')
    Set_Alarm = input("enter the time in HH:MM:SS ?")
    speak('alarmset')
    Actual_Time = time.strftime("%H:%M:%S")
    while (Actual_Time == Set_Alarm):
        speak('wake up buddy , lets move on')
        playsound("E:\yokes\songs\Melodies\Ethir_Neechal_-_Un_Paarvayil_Video___Sivakarthikeyan%2C_Priya(256k).mp3")





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
    API_KEY = "fc59cba909a330b7af27602db31a491a"
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

def calculator():
    speak('opening self build calculator using python ')
    os.startfile(r"C:\Users\SElangovan\Desktop\notes\main.exe")




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
    speak('i am opening keywords for ur refernce and we shall proceed')
    keywords()
    buddyday()
    buddytime()
    speak('anything else sir ?')
    speak('please know the CPU usage for ur better performance ')
    cpu()
    speak('do you wanna know the weather conditions today')
    weatherreport()
    speak('i wish to dedicate a song for you today')
    melodies()













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

        elif 'task of the day' in search:
            speak('just  minute it on the way to you ...')
            note = r'C:\Users\SElangovan\Desktop\shutdown.txt'
            os.startfile(note)
            speak('here it is')

        elif 'open arduino' in search:
            speak("opening arduino IDE")
            ard = r"C:\Program Files (x86)\Arduino\arduino.exe"
            os.startfile(ard)
            speak('her you go ')

        elif 'home location' in search :
            speak('ur home is at')
            speak('chinniyampalayam')
            webbrowser.open("https://www.google.com/maps/place/Chinniyampalayam,+Coimbatore,+Tamil+Nadu/@11.0623152,77.040331,14.5z/data=!4m5!3m4!1s0x3ba85624d5f9b0cf:0x8c0a9bfa4b8ebb40!8m2!3d11.0553431!4d77.0655238")

        elif 'army' in search:
            speak('opening ur passion of life')
            webbrowser.open(r"www.joinindianarmy.nic.in")

        elif 'navy' in search:
            speak('guardians of indianocean')
            webbrowser.open('www.joinindiannavy.nic.in')

        elif 'airforce' in search:
            speak('we rule the sky')
            webbrowser.open("www.joinindianairforce.nic.in")

        elif 'why olivegreen' in search:
            speak('the reason behind my name is')
            speak('he is passionate in joining indian armed forces as a resembelence of remembering everytime he used to call me olivegreen ')

        elif 'who are you ?' in search:
            speak('i am commanders virtual assistant, created by him')

        elif 'what can you do ' in search:
            speak('i will try my evel best to satisfy u')
            speak('what do you what me to do ?')

        elif 'open movies' in search:
            speak('opening downloaded movies')
            movie = r"F:\all movies"
            os.startfile(movie)

        elif 'open video songs' in search:
            speak('opening songs')
            song=r"F:\video songs"
            os.startfile(song)

        elif 'jokes' in search:
            speak(pyjokes.get_joke())

        elif 'emergency' in search:
            speak('displaying ur emergency contacts ?')
            call=r"C:\Users\SElangovan\Desktop\emergencycontacts.txt"
            os.startfile(call)
            speak('be safe')

        elif 'simple calulator' in search:
            speak('opening simple caculator')
            cal=r"C:\Users\SElangovan\PycharmProjects\pythoncalculator\dist\main.exe"
            os.startfile(cal)

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

        elif 'open mail' in search or 'college mail' in search:
            speak("opening skcet mail")
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

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
            cb = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            speak('what do you want me to search ?')
            search_cb = takecommand().lower()
            webbrowser.get(cb).open_new_tab(search_cb+'.com')

        elif 'cpu usage' in search:
            cpu()

        elif 'VM Ware' in search:
            speak('opening vmware workstation')
            vm = r"C:\Program Files (x86)\VMware\VMware Workstation\vmware.exe"
            os.startfile(vm)

        elif 'telegram' in search:
            speak('opening telegram buddy')
            tg=r"C:\Windows.old\Users\SElangovan\AppData\Roaming\Telegram Desktop\Telegram.exe"
            os.startfile(tg)

        elif 'whatsapp' in search:
            speak('opening whatsapp web')
            ww = r"C:\Windows.old\Users\SElangovan\AppData\Roaming\Telegram Desktop\Telegram.exe"
            os.startfile(ww)

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

        elif 'memories' in search:
            speak('opening tenth memories for you buddy')
            tenth = r"F:\yokes\coco"
            os.startfile('tenth')

        elif 'pycharm' in search:
            speak('opening pycharm')
            pc = r"C:\Users\SElangovan\Downloads\pycharm-community-2020.3.exe"
            os.startfile('pc')

        elif 'spotify' in search:
            spotify()

        elif 'melodies' in search:
            melodies()

        elif 'weatherreport' in search:
            weatherreport()

        elif 'quit' in search or 'bye bye' in search:
            speak('bye buddy, have a nice day')
            exit()

        elif 'simple calculator' in search or 'calculator' in search:
            calculator()




















