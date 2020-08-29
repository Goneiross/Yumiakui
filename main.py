import speech_recognition as sr
import sys

def analyse(text):
    if (text.find("exit") != -1 or text.find("quit") != -1):
        print("Yumiakui: See ya space cow-boy !")
        sys.exit()
    elif (text.find("hey") != -1):
        print("Yumiakui: Aloha Gon")
    else :
        print("Yumiakui: I don't understand this ...")

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
                analyse(sentence)
                pass
            except:
                print("Goneiross : ERROR Voice unrecognized")
                pass

if __name__ == "__main__":
    main()