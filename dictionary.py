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
    state = False
    keyword = [
        "please"
    ]
    for word in keyword:
        if ((text.lower()).find(word.lower()) != -1):
            state = True
    return state