import speech_recognition as sr
import pyttsx3
import datetime


listener= sr.Recognizer()
alexa= pyttsx3.init()

#alexa.say("Hello Paul. How may I help u?")
#alexa.runAndWait()

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    try:
        with  sr.Microphone() as source:
            print("Ami shuntesi, bolen...")
            voice= listener.listen(source)
            command= listener.recognize_google(voice)
            command=command.lower()

            if 'alexa' in command:
                print(command)

    except:
        pass
    return command


def run_alexa():
    command= take_command()
    if 'time' in command:
        time= datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Current time is "+time)

run_alexa()