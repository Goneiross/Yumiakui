from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import SynthesizeCallback
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from os.path import join, dirname

import os

from subprocess import DEVNULL, STDOUT, check_call

TTS_NAME = "watson"

def watson_initialization():
    """
    Initialize Watson, IBM TTS API.

    Returns: watson (TextToSpeech)
    """
    f = open(join(dirname(__file__), "data/", "credentials/", "IBM_key"), "r")
    IMB_KEY = f.readline()
    f.close()
    f = open(join(dirname(__file__), "data/", "credentials/", "IBM_url"), "r")
    IMB_URL = f.readline()
    f.close()
    authenticator = IAMAuthenticator(IMB_KEY)
    watson = TextToSpeechV1(authenticator=authenticator)
    watson.set_service_url(IMB_URL)
    return watson

def pytts_initialization():
    """
    Initialize pyttsx3, open source, using system TTS.

    Returns: pytts (TextToSpeech)
    """
    pytts = pyttsx3.init()
    pytts.setProperty("rate", 180)
    return pytts

def tts_init():
    """
    Initialize choosen TTS.

    Returns: tts (TextToSpeech)
    """
    if (TTS_NAME == "watson"):
        return watson_initialization()
    elif (TTS_NAME == "pytts"):
        return pytts_initialization()
    else:
        print("ERROR - WRONG TTS")

def say(name, text, tts):
    """
    Makes the TTS say the given sentence.

    Parameters: name (string): name of the AI to print it, text (string): sentence to say, tts (TextToSpeech)
    """
    print(name + " : " + text)
    if os.path.exists(join(dirname(__file__), "data/", "speech/", text + ".wav")):
        check_call(['play', join(dirname(__file__), "data/", "speech/", text + ".wav")], stdout=DEVNULL, stderr=STDOUT)
    else:
        if (TTS_NAME == "watson"):   
            with open(join(dirname(__file__), "data/", "speech/", text + ".wav"),'wb') as audio_file:
                response = tts.synthesize(text, accept='audio/wav', voice="en-US_AllisonVoice").get_result()
                audio_file.write(response.content)
            check_call(['play', join(dirname(__file__), "data/", "speech/", text + ".wav")], stdout=DEVNULL, stderr=STDOUT)
        elif (TTS_NAME == "pytts"):
            tts.say(text)
            tts.runAndWait()
        else:
            print("ERROR - WRONG TTS")