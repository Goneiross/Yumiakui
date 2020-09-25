USER_NAME = "Gon"
ASSISTANT_NAME = "Yumiakui"

greetings = [
    "Aloha",
    "Heyya",
    "Hey",
    "Hello",
    "Yo"
]

leaving = [
    "See you",
    "See ya",
    "See you space-cowboy",
    "Bye",
    "Bye-bye",
    "See you later",
    "Later bro"
]

notUnderstood = [
    "I don't understand",
    "I did not catch what you were saying",
    "Could you repeat please ?",
    "I'm sorry, I don't understand"
]

userName = [
    USER_NAME,
    "Sir",
    "Bro"
]

askingHowAreYou = [
    "How are you ?",
    "How are you doing ?",
    "Watcha doing ?",
    "How is today going on ?"
]

credo = [
    "En todo amar e serveer"
]

def is_asking_nextEvent(text):
    """
    Checks if user is asking for next event.

    Parameters: text (string): user's speech

    Returns: (bool)
    """
    state = False
    keyword = [
        "event",
        "events",
        "timetable",
        "class"
    ]
    for word in keyword:
        if ((text.lower()).find(word.lower()) != -1):
            state = True
    return state

def is_greetings(text):
    """
    Checks if user is saying hi.

    Parameters: text (string): user's speech

    Returns: (bool)
    """
    state = False
    keyword = [
        "hey", 
        "hello", 
        "hi", 
        "good morning", 
        "good afternoon", 
        "greetings"
    ]
    for word in keyword:
        if ((text.lower()).find(word.lower()) != -1):
            state = True
    return state

def is_leaving(text):
    """
    Checks if user is leaving.

    Parameters: text (string): user's speech

    Returns: (bool)
    """
    state = False
    keyword = [
        "exit", 
        "quit", 
        "bye", 
        "see you", 
        "see ya"
    ]
    for word in keyword:
        if ((text.lower()).find(word.lower()) != -1):
            state = True
    return state

def is_opening_ext_app(text):
    """
    Checks if user wants to open an app.

    Parameters: text (string): user's speech

    Returns: (bool)
    """
    state = False
    keyword = [
        "open", 
        "launch",
        "start"
    ]
    for word in keyword:
        if ((text.lower()).find(word.lower()) != -1):
            state = True
    return state

def is_computing(text):
    """
    Checks if user wants to compute something.

    Parameters: text (string): user's speech

    Returns: (bool)
    """
    state = False
    keyword = [
        "compute", 
        "calculate"
    ]
    for word in keyword:
        if ((text.lower()).find(word.lower()) != -1):
            state = True
    return state

def is_studying(text):
    """
    Checks if user starts or stops studying.

    Parameters: text (string): user's speech

    Returns: (bool)
    """
    state = False
    keyword = [
        "study",
        "studies"
    ]
    for word in keyword:
        if ((text.lower()).find(word.lower()) != -1):
            state = True
    return state

def is_polite(text):
    """
    Checks if the user is polite. For AI personality purpose.

    Parameters: text (string): user's speech

    Returns: (bool)
    """
    state = False
    keyword = [
        "please"
    ]
    for word in keyword:
        if ((text.lower()).find(word.lower()) != -1):
            state = True
    return state

def is_waking_up():
    """
    Checks if the user state is waking up. 

    Parameters: text (string): user's speech

    Returns: (bool)
    """
    state = False
    keyword = [
        "waking up",
        "feed",
        "news",
        "today's plan"
    ]
    for word in keyword:
    if ((text.lower()).find(word.lower()) != -1):
        state = True
    return state