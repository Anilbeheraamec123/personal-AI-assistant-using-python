import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import pywhatkit



engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
 engine.say(audio) 
 engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
       speak("Good Morning!")

    elif hour>=12 and hour<18:
       speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am lara sir how may i help you")  
def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
 

if __name__=="__main__" :
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play music' in query:
            music_dir = 'C:\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath ="C:\\Users\\anil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        elif 'date' in query:
            speak('sorry, I have a headache')
        elif 'are you single' in query:
            speak('I am in a relationship with wifi')
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'send message' in query:
            pywhatkit.sendwhatmsg('+91111111111','Hello appa',15,9)
            speak("ok sir sending message as above the mentioned time")