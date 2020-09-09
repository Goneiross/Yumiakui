from subprocess import Popen

def convertSentenceToWords(text, index): 
    """ 
    Converts a sentence given into a list of words.

    Parameters: text (string): a sentence

    Returns: words (list): list of the sentence's words
    """
    words = text.split()
    for i in range (0, index):
        words.pop(0)
    return  words

def open_code():
    """
    Opens your favorite IDE, VSCode, in a new thread.
    """
    code = '/usr/share/code/bin/code'
    Popen(code)

def open_firefox():
    """
    Opens Firefox, in a new thread.
    """
    firefox = '/usr/lib/firefox-trunk/firefox-trunk'
    Popen(firefox)

def open_matlab():
    """
    Opens Matlab, in a new thread.
    """
    matlab = '/usr/local/MATLAB/R2020a/bin/matlab'
    Popen(matlab)

def open_Xournal():
    """
    Opens Xournalpp, a draw app, in a new thread.
    """
    xournal = '/usr/bin/xournalpp'
    Popen(xournal)

def open_spotify():
    """
    Opens Spotify, in a new thread.
    Don't support choosing a music yet.
    """
    spotify = '/snap/bin/spotify'
    Popen(spotify)

def open_discord():
    """
    Opens Discord, in a new thread.
    """
    spotify = '/usr/bin/discord'
    Popen(spotify)

def open_steam():
    """
    Opens Steam, don't play to much, in a new thread.
    """
    spotify = '~/.steam/ubuntu12_32'
    Popen(spotify)

def open_deluge():
    """
    Opens Deluge to Torrent, in a new thread.
    """
    spotify = '/usr/bin/deluge'
    Popen(spotify)