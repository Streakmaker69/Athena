from ast import main
from twilio.rest import Client
from ecapture import ecapture as ec
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import spotipy
import json
import wolframalpha
import requests
import pyjoke

username = '......................'
clientID = '...........................'
clientSecret = '........................'
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
    elif 'weather' in query:
        speak("The weather is:")
    elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)
    elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headline")
            speak('Here are some headlines from the Times of India, Happy reading!')
            time.sleep(6)
    elif 'ask' in query:
        speak('I can answer to computational and geographical questions  and what question do you want to ask now')
        question=takeCommand()
        app_id="XV4X4P-EVWTXPTH6E"
        client = wolframalpha.Client('XV4X4P-EVWTXPTH6E')
        res = client.query(question)
        answer = next(res.results).text
        print(answer)
        speak(answer)
        elif "weather" in query:
            api_key=".............................................."
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
            else:
                speak(" City Not Found ")
    elif 'good job' in query:
        speak("Thank You for the compliments!" )
    elif "who i am" in query:
            speak("If you talk then definitely your Homo Sapien.")
    elif "why you came to world" in query:
            speak("Thanks to Streakmaker. Further it's a secret.")  
    elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
    elif "camera" in query or "take a photo" in query:
        ec.capture(0, "Athena Camera ", "img.jpg")
    elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
    elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
    elif "send message " in query:
                account_sid = '...............................'
                auth_token = '.................................'
                client = Client(account_sid, auth_token)
 
                message = client.messages \
                                .create(
                                    body = takeCommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )
 
                print(message.sid)
    elif 'joke' in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    elif "who are you" in query:
            speak("I am a virtual assistant created by Streakmaker.")
