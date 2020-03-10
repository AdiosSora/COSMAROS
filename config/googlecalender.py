from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
class googlecalender_connect():
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    def __init__(self) :
        print("カレンダー挿入開始")

    def insert_event(e_title=None,e_description=None,e_year=2020,e_month=1,e_day=1):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)
        e_datetime = str(e_year) + "-" + str(e_month) +"-" + str(e_day)
        event = {
          'summary': e_title,
          'description': e_description,
          'start': {
            'date': e_datetime,
            'timeZone': 'Japan',
          },
          'end': {
            'date': e_datetime,
            'timeZone': 'Japan',
          },
        }

        event = service.events().insert(calendarId='er4lhgl9de86l7r0gum2abrqh8@group.calendar.google.com',
                                        body=event).execute()
        print (event['id'])
        print(str(e_year) + '/' + str(e_month) + '/' + str(e_day) + '/' + e_title + '/' + e_description)
