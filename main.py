import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #Microsoft developed speech API. Helps in synthesis and recognition of voice.

voices = engine.getProperty('voices')

# print(voices[0].id)

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Goodmorning!")
    elif hour>=12 and hour<18:
        speak("Goodafternoon!")   
    else:
        speak("Goodevening!") 
    speak("I am your virtual Assistant, Please tell me how may I assist you!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    
    try:
        print("Processing...")
        query = r.recognize_google(audio, language='en-in') #using the Google Speech Recognition API
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("\nPlease repeat your query")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail','password')
    server.sendmail('youremail',to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        
        elif 'play music' in query:
            music_dir = 'D:\\Python AI project\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        
        elif 'open code' in query:
            codePath = '"C:\\Users\\JEEVESH JOSHI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codePath)
        
        elif 'email to user' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sender_email"
                sendEmail(to,content)
                speak("Email has been sent successfully!")
            except Exception as e:
                speak("Error occurred Email was not sent!")
        
        elif 'quit' in query:
            exit()
