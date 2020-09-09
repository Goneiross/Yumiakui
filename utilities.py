from subprocess import Popen

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