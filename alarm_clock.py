import os
import datetime
import time
import pyttsx3
from mutagen.mp3 import MP3

# this line is to initiate pyttsx3 module and change the speed of the voice
engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# making speak function
def speak(audio,rate=150):
    engine.setProperty('rate',rate)
    engine.say(audio)
    engine.runAndWait()

#defining variables
ddn=datetime.datetime.now()
audio_file_path= "twirling-intime-lenovo-k8-note-alarm-tone-41440.mp3"
n = 1

#Programm starts from here
print("This is a Alarm clock where you can set alarm accordingly a song will start.\nTo use a default value don't type anything just click enter")
print(f"Date and time Now is ==>{datetime.datetime.now()}")


ndate=input(f"Enter the Date or default {ddn.strftime('%d')} =") or ddn.strftime('%d')
month=input(f"Enter the Month or default {ddn.strftime('%m')} =") or ddn.strftime('%m')
year=input(f"Enter the Year or default {ddn.strftime('%Y')} =") or ddn.strftime('%Y')
hr=input(f"Enter the Hour or default {ddn.strftime('%H')} =") or ddn.strftime('%H')
min=input(f"Enter the Minute or default {ddn.strftime('%M')} =") or ddn.strftime('%M')
sec =input(f"Enter the Second or default 00 =") or "00"
reminder=input("Sir is there something you want to add as reminder:\nLeave blank if nothing:") or ""

schedule_date = datetime.date(int(year), int(month), int(ndate))

while n > 0:
    if time.localtime().tm_hour == int(hr) and time.localtime().tm_min == int(min) and time.localtime().tm_sec == int(
            sec) and datetime.date.today() == schedule_date:
        try:
            os.startfile(audio_file_path)
            time.sleep(MP3(audio_file_path).info.length)
        finally:
            speak(f"Wake up sir",200)
            time.sleep(0.1)
            speak("Your scheduled time has come",200)
            time.sleep(0.1)
            speak(f"You told me to remind you about {reminder}",200)
            speak(f"Its {datetime.datetime.now().strftime('%A %I %M %p')}",200)
        break
    else:
        n += 1
