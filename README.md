# Yumiakui - assistant for linux

## Disclaimer 

Use this app at your own risk. You will have to change the external application paths.
You can choose to change the Speech Recognization API you use (currently Google) and the TTS (currently IBM + sox).
Google API is also used for Google calendar.

## Requirements

Python packages :

    pip install SpeechRecognition

    pip install pyttsx3 

    pip install pyaudio 
    
    pip install ibm_watson

    pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

For ubuntu :

    apt install sox
   
There might be other missing dependencies.

## Configuraton

If you use the same APIs as me, you need to provide few credentials. All should be put inside /data/credentials/.
You need:

 - google_calandar_api_credentials.json
 
 - google_calandar_ids.py with your calendar IDs (ex: CALANDAR_main = "primary" )
 
To use IBM API (you can decide to use another one):

 - IMB_TTS_key for the IBM TTS API key
 
 - IMB_TTS_url for the IBM TTS API url

 - IMB_STT_key for the IBM TTS API key
 
 - IMB_STT_url for the IBM TTS API url
 
 - ibm-credentials.env

 To use Google Cloud API:

 - GOOGLE_STT_key.JSON for the Google Cloud TTS API file
 
 ## Support
 
 Don't hesitate to contact me !
