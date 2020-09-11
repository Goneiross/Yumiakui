import json 
from os.path import join, dirname 
from ibm_watson import SpeechToTextV1 
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 

STT_NAME = "GOOGLE"

def stt_init():
    """
    Initialize choosen STT.
    Supports IBM Watson and Google Cloud.

    Returns: stt (SpeechToText)
    """
    if (STT_NAME == "IBM"):
        f = open(join(dirname(__file__), "data/", "credentials/", "IBM_STT_key"), "r")
        IMB_KEY = f.readline()
        f.close()
        f = open(join(dirname(__file__), "data/", "credentials/", "IBM_STT_url"), "r")
        IMB_URL = f.readline()
        f.close()
        authenticator = IAMAuthenticator(IMB_KEY)
        speech_to_text = SpeechToTextV1(authenticator=authenticator)
        speech_to_text.set_service_url(IMB_URL)
        return speech_to_text
    elif (STT_NAME == "GOOGLE_CLOUD"):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=join(dirname(__file__), "data/", "credentials/", "GOOGLE_STT_key.JSON")
    elif (STT_NAME == "GOOGLE"):
        pass
    else: 
        print("ERROR - WRONG STT NAME")

def stt_transcript(stt, audioSource):
    """
    Recognizes the voice to return a text.

    Parameters: audioSource(Audio)

    Returns: text (string)
    """
    if (STT_NAME == "IBM"):
        results = stt.recognize(audio=audioSource.get_wav_data(), content_type='audio/wav').get_result()
        print(results)
        r = ""
        try:
            r = results.get('results').pop().get('alternatives').pop().get('transcript')
            pass
        except:
            print("ERROR")
            pass
        print(r)
        return (r)
    elif (STT_NAME == "GOOGLE_CLOUD"):
        return stt.recognize_google_cloud(audioSource, language = 'en-US')
    else: 
        print("ERROR - WRONG STT NAME")