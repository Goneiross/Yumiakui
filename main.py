import speech_recognition as sr
import pyttsx3
import os
from playsound import playsound

def is_greetings(text):
    state = False
    keyword = {"hey", "hello", "hi", "good morning", "good afternoon", "greetings"}
    for word in keyword:
        if (text.find(word) != -1):
            state = True
    return state

def is_leaving(text):
    state = False
    keyword = {"exit", "quit", "bye", "see you", "see ya"}
    for word in keyword:
        if (text.find(word) != -1):
            state = True
    return state

def say (name, text, tts):
    print(name + " : " + text)
    # os.system('/opt/mimic/mimic -t ' + text + ' -voice slt' + ' -o tmp.wav')
    # playsound('tmp.wav')
    tts.say(text)
    tts.runAndWait()


def analyse(text, tts):
    if is_leaving(text):
        say("Yumiakui", "See ya space cow-boy !", tts)
        os._exit(0)
    elif is_greetings(text):
        say("Yumiakui", "Aloha Gon", tts)
    else :
        say("Yumiakui", "I don't understand this ...", tts)

def main():
    r = sr.Recognizer()
    mic = sr.Microphone()
    tts = pyttsx3.init()
    tts.setProperty("rate", 180)
    os.system('clear')
    while(1) :
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                sentence = r.recognize_google(audio)
                print("Goneiross: " + sentence)
                analyse(sentence, tts)
                pass
            except:
                print("Goneiross : ERROR Voice unrecognized")
                pass

if __name__ == "__main__":
    main()