import pyttsx3 #pip install pyttsx3
#import SpeechRecognition as sr #pip install SpeechRecognition
import speech_recognition as sr
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pyaudio
import pickle
import os.path






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am  Jarvis. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def Alarm(query):

    TimeHere= open('C:\\Users\\a\\PycharmProjects\\AIProject1\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("C:\\Users\\a\\PycharmProjects\\AIProject1\\Alarm.py")





def tellDay():
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1

    # this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open geeks for geeks' in query:
            webbrowser.open("https://www.geeksforgeeks.org/")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\a\\PycharmProjects\\AIProject1\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")

        elif 'open word' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word 2016"
            os.startfile(codePath)


        elif 'set alarm' in query:

            Alarm(query)


        elif "which day it is" in query:
            tellDay()
            continue

        elif "tell me your name" in query:
            speak("I am Jarvis. Your desktop Assistant")



        elif "bye" in query:
            speak("Bye. Nice to meet you !")
            exit()

