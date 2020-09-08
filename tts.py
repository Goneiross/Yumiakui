from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import SynthesizeCallback
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from os.path import join, dirname

import os

from subprocess import DEVNULL, STDOUT, check_call

TTS_NAME = "watson"

def watson_initialization():
    f = open("IBM_key", "r")
    IMB_KEY = f.readline()
    f.close()
    f = open("IBM_url", "r")
    IMB_URL = f.readline()
    f.close()
    authenticator = IAMAuthenticator(IMB_KEY)
    watson = TextToSpeechV1(authenticator=authenticator)
    watson.set_service_url(IMB_URL)
    return watson

def pytts_initialization():
    pytts = pyttsx3.init()
    pytts.setProperty("rate", 180)
    return pytts

def tts_init():
    if (TTS_NAME == "watson"):
        return watson_initialization()
    elif (TTS_NAME == "pytts"):
        return pytts_initialization()
    else:
        print("ERROR - WRONG TTS")

def say(name, text, tts):
    print(name + " : " + text)
    if (TTS_NAME == "watson"):   
        try:
            with open(join(dirname(__file__), 'output.wav'),'wb') as audio_file:
                response = tts.synthesize(text, accept='audio/wav', voice="en-US_AllisonVoice").get_result()
                audio_file.write(response.content)
            check_call(['play', 'output.wav'], stdout=DEVNULL, stderr=STDOUT)
            pass
        except:
            print("ERROR - WATSON TTS")
            pass
    elif (TTS_NAME == "pytts"):
        try:
            tts.say(text)
            tts.runAndWait()
            pass
        except:
            print("ERROR - PYTTS")
            pass
    else:
        print("ERROR - WRONG TTS")