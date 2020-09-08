from __future__ import print_function
import datetime
import pickle
import os.path
from os.path import join, dirname
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from data.credentials.google_calandar_ids import *

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def google_init():
    creds = None
    if os.path.exists(join(dirname(__file__), "data/", "credentials/", 'token.pickle')):
        with open(join(dirname(__file__), "data/", "credentials/", 'token.pickle'), 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                join(dirname(__file__), "data/", "credentials/", 'google_calandar_api_credentials.json'), SCOPES)
            creds = flow.run_local_server(port=0)
        with open(join(dirname(__file__), "data/", "credentials/", 'token.pickle'), 'wb') as token:
            pickle.dump(creds, token)
    return creds

def google_calandar():
    creds = google_init() # SHOULD ONLY BE INIT ONCE ## TO DO

    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time 
    print('Getting the upcoming 1 events')
    events_result = service.events().list(calendarId=CALANDAR_EPFL, timeMin=now,
                                        maxResults=1, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        # print(start, event['summary'])
    return event['summary']