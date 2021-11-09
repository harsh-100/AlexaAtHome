import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)  #process to change voice in female version
#engine.say('My name is alexa ,how can i help you sir ?')


def talk(text) :
    engine.runAndWait()
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa'in command:
                command = command.replace('alexa',"")
                print(command)
    except:
        pass
    return command
def run_alexa ():
    command = take_command()
    if 'play'in command:
        song=command.replace('play','')
        talk('playing'+song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H %M %p')
        print(time)
        talk("At this moment time is "+time)
    elif 'search for ' in command:
        search = command.replace('search for','')
        info=wikipedia.summary(search,1)
        print(info)
        talk(info)
    elif 'love' in command:
        talk('I am already in a relationship , sorry for it')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    else:
        talk("hey , I can't understand what you said , please repeat again ")


while True:
    run_alexa()
