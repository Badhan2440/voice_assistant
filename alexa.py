import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener= sr.Recognizer()
alexa= pyttsx3.init()

alexa.say("Hello Paul. How may I help u?")
alexa.runAndWait()

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    try:
        with  sr.Microphone() as source:
            print("Listening...")
            voice= listener.listen(source)
            command= listener.recognize_google(voice)
            command=command.lower()

            if 'alexa' in command:
                command=command.replace('alexa', '')

    except:
        pass
    return command


def run_alexa():
    command= take_command()
    if 'time' in command:
        time= datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Current time is "+time)


    elif 'play' in command:
        song=command.replace('play', '')
        talk('playing '+song)
        pywhatkit.playonyt(song)


    elif 'tell me about' in command:
        info= command.replace('tell me about ', '')
        info= wikipedia.summary(info, 1)
        print(info)
        talk(info)

    
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'date' in command:
        talk('Sorry, I have a boyfriend')

    else:
        talk('I do not know it but google does. let me search it for you.')
        pywhatkit.search(command)





while True:
    run_alexa()