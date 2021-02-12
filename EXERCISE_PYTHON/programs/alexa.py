import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listner=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[2].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening Your Voice Command")
            voice=listner.listen(source)
            command=listner.recognize_google(voice)
            command=command.lower()
            if 'sura' in command:
                command=command.replace("sura"," ")
                print(command)           
    except:
        pass
    return command
def run_alexa():
    commmand=take_command()
    if "play" in commmand:
        song=commmand.replace("play"," ")
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif "time" in commmand:
        time=datetime.datetime.now().strftime('%I:%M:%p')
        talk("Current time is "+time+" honourable lister")
        print("Current time is "+time+" honourable lister")
    elif "who" in commmand:
        person=commmand.replace("who"," ")
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif "what" in commmand:
        person=commmand.replace("what"," ")
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif "tell me a joke" in commmand:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif "How are You" in commmand:
        talk("I'm Fine Thankyou!!!")
    elif "WHAT is YOUR NAME" in commmand:
        talk("WHAT YOU CALLED BEFORE WHAT'S YOUR NAME!!!")
    elif "are you single" in commmand:
        talk("No Babes I'M in REALTIONSHIP WITH WIFI!!!")
    elif "do you want to talk with me" in commmand:
        talk("No I'm Busy!!!")
    elif "father" in commmand:
        talk("Prajjal has Created me!!!")
    elif "hii sura" in commmand:
        talk("hello majesty!!!")
    elif "do you want to go for a date" in commmand:
        talk("No Babes I can fix date for you!!!")
    elif "ARE YOU INDIAN" in commmand:
        talk("prajjal has created me If he is Indian then I'M too!!!")
    elif "Fuck" in commmand:
        talk("behave properly IDIOT!!!!")
    elif "bring me a cup of tea" in commmand:
        talk("My lister I'M not your waiter")
    
    else:
        talk("Plzz repeat Your Voice Command")
        print("Plzz repeat Your Voice Command")
if __name__ == "__main__":
    while True:
        engine.say("HEY I'M SURA")
        engine.runAndWait()
        engine.say("How may I CAN HELP YOU my Majesty")
        engine.runAndWait()
        run_alexa()