from ast import main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import spotipy
import json

username = '4je7eypho1a3jfi5m90sejo5p'
clientID = 'd81243f80c10454aacccad9bcd867a7c'
clientSecret = '8b3b7ff25ebd4b8f85329e46f4de4ec8'
redirect_uri = 'http://google.com/callback/'

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()

print(json.dumps(user_name, sort_keys=True, indent=4))


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
        
    elif hour >= 12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
        
    else:
        print("Good Evening!") 
        speak("Good Evening!")  

    print("I am Athena.")
    speak("I am Athena.")
    print("Your Virtual Assistant.")
    speak("Your Virtual Assistant.")
    print("How may I be of service?")
    speak("How may I be of service?")     
     
        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You : {query}\n")
    except Exception as e:
        # print(e)

        print("Say that again please....")
        return "None"
    return query




main
wishMe()
while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        qeury = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        url = 'https://www.python.org'
        path = 'D:\opera.exe'
        webbrowser.register('mybrowser', None, webbrowser.BackgroundBrowser(path))
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        url = 'https://www.python.org'
        path = 'D:\opera.exe'
        webbrowser.register('mybrowser', None, webbrowser.BackgroundBrowser(path))
        webbrowser.open("google.co.in")

    elif 'on spotify' in query:       
        query = query.replace("in spotify","")
        search_song = query
        results = spotifyObject.search(search_song, 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        webbrowser.open(song)
        print('Song has opened in your browser.')
    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(f"The time is : {strTime}")
            speak(f"The time is {strTime}")
    elif 'open discord' in query:
            dis = "C:\\Users\\prana\\AppData\\Local\\Discord\\Update.exe"
            os.startfile(dis)