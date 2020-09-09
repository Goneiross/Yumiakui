import speech_recognition as sr
import pyttsx3
import os
from playsound import playsound
import random
import threading
import time

from utilities import *
from dictionary import *
from tts import *
from google_functions import *

studies_tracker = []

class Assistant_Session:
    """
    Contains all the data of the current session.
    Is used to analyse user speech, and speak.
    """
    def __init__(self):
        self.tts = tts_init()

        # Initialize user's states
        self.user_is_asking_nextEvent = False
        self.user_is_computing = False
        self.user_is_greeting = False
        self.user_is_leaving = False
        self.user_is_opening_ext_app = False
        self.user_is_studying = False
        self.user_is_studying_started = False
        self.user_is_studying_stopped = False
        # Initialize user's personnality
        self.user_polite = 0 

        os.system('clear')
        say("Watson", "Initialized", self.tts)

    def update_user_states(self, text):
        # States
        if is_asking_nextEvent(text):
            self.user_is_asking_nextEvent = True
        if is_computing(text):
            self.user_is_computing = True
        if is_greetings(text):
            self.user_is_greeting = True
        if is_leaving(text):
            self.user_is_leaving = True   
        if is_opening_ext_app(text):
            self.user_is_opening_ext_app = True
        if is_studying(text):
            if user_is_studying_started:
                self.user_is_studying_stopped = True
                self.user_is_studying_started = False
            else:
                self.user_is_studying = True
            
        # Personnality
        if is_polite(text):
            self.user_polite += 1

    def act(self, text):
        """
        Given user_state flags, choose how the AI should react and organize her response.
        """
        speech = ""
        understood = False
        if self.user_is_greeting: 
            self.user_is_greeting = False
            understood = True
            say_greetings(self.tts)
        if self.user_is_studying:
            self.user_is_studying = False
            self.user_is_studying_started = True
            understood = True
            track_studying(self.tts)
        if self.user_is_studying_stopped:
            self.user_is_studying_stopped = False
            understood = True
        if self.user_is_asking_nextEvent:
            self.user_is_asking_nextEvent = False
            understood = True
            say_nextEvent(self.tts)
        if self.user_is_computing:
            self.user_is_computing = False
            understood = True
            compute(text, self.tts)
        if self.user_is_opening_ext_app:
            self.user_is_opening_ext_app = False
            understood = True
            open_app(text, self.tts)
        if (self.user_polite > 5):
            be_humble(self.tts)
        if self.user_is_leaving:
            self.user_is_leaving = False
            understood = True
            say_leaving(self.tts)
            os._exit(0)
        if not understood:
            say_notUnderstood(self.tts)

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

def be_humble(tts):
    r = random.randrange(0, 1)
    if (r == 0):
        r = random.randrange(0, len(credo))
        say(ASSISTANT_NAME, credo[r], tts)

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

def track_studying(tts):
    say(ASSISTANT_NAME, "Starting the tracking of study time. Good luck !", tts)
    studies_tracker.append([])
    studies_tracker[-1].append(time.localtime())

def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    session = Assistant_Session()
    while(1) :
        with mic as source:
            # r.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                sentence = recognizer.recognize_google(audio)
                print(USER_NAME + " : " + sentence)
                try: 
                    session.update_user_states(sentence)
                    try:
                        session.act(sentence)
                        pass
                    except:
                        print(ASSISTANT_NAME + " : ERROR Unable to act")
                        pass
                    pass
                except:
                    print(ASSISTANT_NAME + " : ERROR Unable to analyse your voice")
                pass
            except:
                print(ASSISTANT_NAME + " : ERROR Voice unrecognized")
                pass
            
if __name__ == "__main__":
    main()