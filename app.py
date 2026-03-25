import streamlit as tv
import sqlite3
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import datetime
from dateutil import parser 
import pytz 
from dotenv import load_dotenv #to read env file
from langchain_google_genai import ChatGoogleGenerativeAI  #gemini
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
tv.title("bhagwan bhrose ")
#today date
now_ist = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
today_string = now_ist.strftime("%A, %d %b %Y")
tv.subheader(f"📅 {today_string}")
tv.write("---")

col1,col2=tv.columns(2)
with col1:
    tv.header("college Timetable")
    data=uni_data()
    for row in data:
        tv.info(f"**{row[0]}**| {row[1]}|{row[2]}| {row[3]}")
    

with col2:

    tv.header("events")
    #adding manual button
    if tv.button('sync google calendar'):
     tv.rerun()
    events = google_calend()
    
    if not events:
            tv.warning("kuch nahi hai bhai")
    else:  
        for e in events:
            name = e.get('summary', 'No Title')
        
            #Time showing
            start=e.get('start',{})
            full_time=start.get('dateTime')
            #to change universal timezone to india timezone
            if full_time:
                temp_time=parser.parse(full_time)

                indian_time=pytz.timezone("Asia/Kolkata")
                ist_time=temp_time.astimezone(indian_time)
            #am pm date year
                clean=ist_time.strftime("%d %b %Y | %I:%M %p")
            
            else:
                clean="All Day"
            tv.success(f"**{name}** \n \nTime:{clean}")

tv.write("-----------------")
tv.header("😎 Assistant:")
api_key=tv.secrets["GEMINI_API_KEY"]
llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

user_input=tv.chat_input("kYA BK RHE HO MC?")
if user_input:
       with tv.spinner("rukja"):
            context="you are a chill intelligent freindly assistant for students. Use 'BSDK' and be concise."
            response=llm.invoke(f"context:{context} \n \n user question:{user_input}")
                
            with tv.chat_message("assistant"):
                 tv.write(response.content)

