import streamlit as tv
import sqlite3
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import datetime


#getting university data
def uni_data():
    conn=sqlite3.connect('timetable.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM classes")
    rows=cursor.fetchall()
    conn.close()
    return rows

def google_calend():
      #check key 
      if os.path.exists('token.json'):
            creds=Credentials.from_authorized_user_file('token.json')
            work=build('calendar','v3',credentials=creds)
            now = datetime.datetime.utcnow().isoformat() + 'Z'
            events_info= work.events().list(
                  calendarId='primary',
                  timeMin=now,
                  maxResults=10,
                  singleEvents=True,
                  orderBy='startTime'
                 ).execute()
            return events_info.get('items',[])
      return []
 
       
#*title
tv.title("abhi socha ni")

col1,col2=tv.columns(2)
with col1:
    tv.header("college Timetable")
    data=uni_data()
    for row in data:
        tv.info(f"**{row[0]}**| {row[1]}|{row[2]}| {row[3]}")
    

with col2:

    tv.header("events")

    events = google_calend()
    
    if not events:
            tv.warning("kuch nahi hai bhai")
    else:  
        for e in events:
            name = e.get('summary', 'No Title')
            tv.success(f"**{name}**")
