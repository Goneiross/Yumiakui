import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

while(1) :
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            print("Goneiross: " + r.recognize_google(audio))
            pass
        except:
            print("Goneiross : ERROR Voice unrecognized")
            pass