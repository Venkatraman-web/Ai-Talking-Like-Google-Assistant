import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import pyjokes
import pywhatkit
import datetime
import os


listener = sr.Recognizer()
engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)
voice = engine.getProperty('voices')
person = ''
engine.setProperty('voice', voice[1].id)
engine.say('Hello, Venkatraman, I am TalkMore, What can i do for you ? \n')
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

try:
 while True:
    with sr.Microphone() as source:
        print('Listening....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
    if 'talkmore' in command:
        if 'open google' in command:
            speak('Opening Google....')
            webbrowser.open('www.google.com')
        elif 'open youtube' in command:
            speak('Opening Youtube....')
            webbrowser.open_new_tab('www.youtube.com')
        elif 'what is ' in command:
            person = command.replace('what is ', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'what is the time' in command:
            date = datetime.datetime.now()
            currentTime = date.strftime('%H:%Mpm')
            print('The time is : {}'.format(currentTime))
            speak('The time is : {}'.format(currentTime))
        elif 'open vs code' in command:
            file = 'C:\\Users\\LENOVO\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk'
            print('Opening Visual Studio Code......')
            speak('Opening Visual Studio Code......')
            os.startfile(file)
        elif 'Done Talking' in command:
            speak('Thanks for talking to me, TalkMore')
            print('Thanks for talking to me, TalkMore')
            break

except:
        speak("Can't Recognise your voice ")
        print("Can't recognise your voice ")