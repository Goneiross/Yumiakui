from __future__ import print_function
import datetime
import pickle
from os.path import join, dirname, exists
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from data.credentials.google_calandar_ids import *

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def google_init():
    """
    Initialize google API.

    Returns: creds (Credentials)
    """
    creds = None
    if exists(join(dirname(__file__), "data/", "credentials/", 'token.pickle')):
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

def google_calandar(range = "day", max_events = 10, calendar = "CALENDAR_EPFL") {
    """
    Gets and returns next user's events, given parameters.
    By default returns the next 10 events from all the calendars of the current day.
 
    Parameters: 
    range(string): can be 'day' or 'week' or 'month', 
    max_events(int): max number of events to return,
    calendar(string): the ID of the calendar to use, from /data/credentials/google_calendar_ids.py

    Returns: events(string)
    """

    creds = google_init() # SHOULD ONLY BE INIT ONCE ## TO DO
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.now().isoformat()
    if (range == "day"):
        end_time = (datetime.datetime.now() + datetime.timedelta(days=1)).isoformat()
    elif (range == "week"):
        end_time = (datetime.datetime.now() + datetime.timedelta(weeks=1)).isoformat()
    elif (range == "month"):
        end_time = (datetime.datetime.now() + datetime.timedelta(days=30)).isoformat() # During current month or 30 days ?
    events_result = service.events().list(calendarId=calendar, timeMin=now, timeMax=end_time
                                        maxResults=max_events, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return " "
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date')) # check this
        # print(start, event['summary'])
    return start + " " + event['summary'] # check this ??

    }