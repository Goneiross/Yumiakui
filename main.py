import speech_recognition as sr

def main():
    r = sr.Recognizer()
    mic = sr.Microphone()
    while(1) :
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                sentence = r.recognize_google(audio)
                print("Goneiross: " + sentence)
                pass
            except:
                print("Goneiross : ERROR Voice unrecognized")
                pass

if __name__ == "__main__":
    main()