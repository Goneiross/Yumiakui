import speech_recognition as sr
import sys
import pyttsx3
import os
from playsound import playsound

def say (name, text, tts):
    print(name + " : " + text)
    # os.system('/opt/mimic/mimic -t ' + text + ' -voice slt' + ' -o tmp.wav')
    # playsound('tmp.wav')
    tts.say(text)
    tts.runAndWait()


def analyse(text, tts):
    if (text.find("exit") != -1 or text.find("quit") != -1):
        say("Yumiakui", "See ya space cow-boy !", tts)
        sys.exit()
    elif (text.find("hey") != -1):
        say("Yumiakui", "Aloha Gon", tts)
    else :
        say("Yumiakui", "I don't understand this ...", tts)

def main():
    r = sr.Recognizer()
    mic = sr.Microphone()
    tts = pyttsx3.init()
    tts.setProperty("rate", 180)
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