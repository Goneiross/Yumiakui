import speech_recognition as sr
import pyttsx3
import os
from playsound import playsound
import random
from subprocess import Popen
import threading

USER_NAME = "Gon"
ASSISTANT_NAME = "Yumiakui"

def convertSentenceToWords(text, index): 
    words = text.split()
    for i in range (0, index):
        words.pop(0)
    return  words

def say (name, text, tts):
    print(name + " : " + text)
    # os.system('/opt/mimic/mimic -t ' + text + ' -voice slt' + ' -o tmp.wav')
    # playsound('tmp.wav')
    tts.say(text)
    tts.runAndWait()

def open_code():
    code = '/usr/share/code/bin/code'
    Popen(code)

def open_firefox():
    firefox = '/usr/lib/firefox-trunk/firefox-trunk'
    Popen(firefox)

def open_matlab():
    matlab = '/usr/local/MATLAB/R2020a/bin/matlab'
    Popen(matlab)

def open_Xournal():
    xournal = '/usr/bin/xournalpp'
    Popen(xournal)

def open_spotify():
    spotify = '/snap/bin/spotify'
    Popen(spotify)

def is_greetings(text):
    state = False
    keyword = [
        "hey", 
        "hello", 
        "hi", 
        "good morning", 
        "good afternoon", 
        "greetings"
    ]
    for word in keyword:
        if (text.find(word) != -1):
            state = True
    return state

def is_leaving(text):
    state = False
    keyword = [
        "exit", 
        "quit", 
        "bye", 
        "see you", 
        "see ya"
    ]
    for word in keyword:
        if (text.find(word) != -1):
            state = True
    return state

def is_openning(text):
    state = False
    keyword = [
        "open", 
        "launch",
        "start"
    ]
    for word in keyword:
        if (text.find(word) != -1):
            state = True
    return state

def is_computing(text):
    state = False
    keyword = [
        "compute", 
        "calculate",
        "Calculate"
    ]
    for word in keyword:
        if (text.find(word) != -1):
            state = True
    return state

def say_greetings(tts):
    sentences = [
        "Aloha " + USER_NAME,
        "Heyya",
        "Hey",
        "Hello",
        "Yo"
    ]
    r = random.randrange(0, len(sentences))
    say(ASSISTANT_NAME, sentences[r], tts)

def say_leaving(tts):
    sentences = [
        "See you",
        "See ya",
        "See you space-cowboy",
        "Bye",
        "Byebye",
        "See you later",
        "Later bro"
    ]
    r = random.randrange(0, len(sentences))
    say(ASSISTANT_NAME, sentences[r], tts)

def say_notUnderstood(tts):
    sentences = [
        "I don't understand",
        "I did not catch what you were saying",
        "Could you repeat please ?",
        "I'm sorry, I don't understand"
    ]
    r = random.randrange(0, len(sentences))
    say(ASSISTANT_NAME, sentences[r], tts)

def compute(text, tts):
    operators = {
        '-': lambda a, b: a-b,
        '+': lambda a, b: a+b,
        '/': lambda a, b: a/b,
        '*': lambda a, b: a*b 
    }
    words = convertSentenceToWords(text, 1)
    result = operators[words[1]](int(words[0]),int(words[2]))
    print(result)
    say(ASSISTANT_NAME, "The result is " + str(result), tts)

def open_app(text, tts):
    if (text.find("code") != -1):
        code_thread = threading.Thread(target=open_code)
        code_thread.start()
        say(ASSISTANT_NAME, "Opening Visual Studio Code", tts)
    elif (text.find("Firefox") != -1):
        firefox_thread = threading.Thread(target=open_firefox)
        firefox_thread.start()
        say(ASSISTANT_NAME, "Opening Firefox", tts)
    elif (text.find("Matlab") != -1):
        matlab_thread = threading.Thread(target=open_matlab)
        matlab_thread.start()
        say(ASSISTANT_NAME, "Opening Matlab", tts)
    elif (text.find("xournal") != -1):
        xournal_thread = threading.Thread(target=open_xournal)
        xournal_thread.start()
        say(ASSISTANT_NAME, "Opening Xournal", tts)
    elif (text.find("Spotify") != -1):
        spotify_thread = threading.Thread(target=open_spotify)
        spotify_thread.start()
        say(ASSISTANT_NAME, "Opening Spotify", tts)

def analyse(text, tts):
    if is_leaving(text):
        say_leaving(tts)
        os._exit(0)
    elif is_openning(text):
        open_app(text, tts)
    elif is_computing(text):
        compute(text, tts)
    elif is_greetings(text):
        say_greetings(tts)
    else :
        say_notUnderstood(tts)

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
                print(USER_NAME + " : " + sentence)
                analyse(sentence, tts)
                pass
            except:
                print(USER_NAME + " : ERROR Voice unrecognized")
                pass

if __name__ == "__main__":
    main()