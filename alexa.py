import speech_recognition as sr
import pyttsx3

listener= sr.Recognizer()
siri= pyttsx3.init()
siri.say("Hello Joyanti Paul. How can I help you?")
siri.runAndWait()

try:
    with sr.Microphone() as source:
        print('listening')
        voice= listener.listen(source)
        command= listener.recognize_google(voice)
        command= command.lower()

        if 'siri' in command:
            print(command)

except:
    pass