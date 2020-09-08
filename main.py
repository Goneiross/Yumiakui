import speech_recognition as sr
import pyttsx3
import os
from playsound import playsound
import random
from subprocess import Popen
import threading

from dictionary import *
from tts import *
from google_functions import *

def convertSentenceToWords(text, index): 
    words = text.split()
    for i in range (0, index):
        words.pop(0)
    return  words

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

def open_discord():
    spotify = '/usr/bin/discord'
    Popen(spotify)

def open_steam():
    spotify = '~/.steam/ubuntu12_32'
    Popen(spotify)

def open_deluge():
    spotify = '/usr/bin/deluge'
    Popen(spotify)

def is_asking_nextEvent(text):
    state = False
    keyword = [
        "event",
        "events",
        "timetable",
        "class"
    ]
    for word in keyword:
        if ((text.lower()).find(word.lower()) != -1):
            state = True
    return state

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
        if ((text.lower()).find(word.lower()) != -1):
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
        if ((text.lower()).find(word.lower()) != -1):
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
        if ((text.lower()).find(word.lower()) != -1):
            state = True
    return state

def is_computing(text):
    state = False
    keyword = [
        "compute", 
        "calculate"
    ]
    for word in keyword:
        if ((text.lower()).find(word.lower()) != -1):
            state = True
    return state

def say_greetings(tts):
    post = ""
    r = random.randrange(0, len(greetings))
    r2 = random.randrange(0, 2)
    r3 = random.randrange(0, 4)
    if (r2 == 0):
        r2r = random.randrange(0, len(userName))
        post = ", " + userName[r2r]
    response = greetings[r] + post
    say(ASSISTANT_NAME, response, tts)
    if (r3  == 0):
        say_askingHowAreYou()

def say_askingHowAreYou(tts):
    r = random.randrange(0, len(askingHowAreYou))
    say(ASSISTANT_NAME, askingHowAreYou[r], tts)

def say_leaving(tts):
    r = random.randrange(0, len(leaving))
    say(ASSISTANT_NAME, leaving[r], tts)

def say_notUnderstood(tts):
    r = random.randrange(0, len(notUnderstood))
    say(ASSISTANT_NAME, notUnderstood[r], tts)

def say_nextEvent(tts):
    nextEvent = google_calandar()
    say(ASSISTANT_NAME, nextEvent, tts)

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
    if ((text.lower()).find("code") != -1):
        code_thread = threading.Thread(target=open_code)
        code_thread.start()
        say(ASSISTANT_NAME, "Opening Visual Studio Code", tts)
    elif ((text.lower()).find("firefox") != -1):
        firefox_thread = threading.Thread(target=open_firefox)
        firefox_thread.start()
        say(ASSISTANT_NAME, "Opening Firefox", tts)
    elif ((text.lower()).find("matlab") != -1):
        matlab_thread = threading.Thread(target=open_matlab)
        matlab_thread.start()
        say(ASSISTANT_NAME, "Opening Matlab", tts)
    elif ((text.lower()).find("xournal") != -1):
        xournal_thread = threading.Thread(target=open_xournal)
        xournal_thread.start()
        say(ASSISTANT_NAME, "Opening Xournal", tts)
    elif ((text.lower()).find("spotify") != -1):
        spotify_thread = threading.Thread(target=open_spotify)
        spotify_thread.start()
        say(ASSISTANT_NAME, "Opening Spotify", tts)
    elif ((text.lower()).find("discord") != -1):
        spotify_thread = threading.Thread(target=open_discord)
        spotify_thread.start()
        say(ASSISTANT_NAME, "Opening Discord", tts)
    elif ((text.lower()).find("steam") != -1):
        spotify_thread = threading.Thread(target=open_steam)
        spotify_thread.start()
        say(ASSISTANT_NAME, "Opening Steam", tts)
    elif ((text.lower()).find("Deluge") != -1):
        spotify_thread = threading.Thread(target=open_deluge)
        spotify_thread.start()
        say(ASSISTANT_NAME, "Opening deluge", tts)

def analyse(text, tts):
    if is_leaving(text):
        say_leaving(tts)
        os._exit(0)
    elif is_openning(text):
        open_app(text, tts)
    elif is_computing(text):
        compute(text, tts)
    elif is_asking_nextEvent(text):
        say_nextEvent(tts)
    elif is_greetings(text):
        say_greetings(tts)
    else :
        say_notUnderstood(tts)

def main():
    r = sr.Recognizer()
    mic = sr.Microphone()
    tts = tts_init()
    os.system('clear')
    say("Watson", "Initialized", tts)
    while(1) :
        with mic as source:
            # r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                sentence = r.recognize_google(audio)
                print(USER_NAME + " : " + sentence)
                try: 
                    analyse(sentence, tts)
                    pass
                except:
                    print(USER_NAME + " : ERROR Unable to analyse")
                pass
            except:
                print(USER_NAME + " : ERROR Voice unrecognized")
                pass
if __name__ == "__main__":
    main()