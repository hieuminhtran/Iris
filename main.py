# Import Libraries
import os
import speech_recognition as sr
from datetime import datetime
from gtts import gTTS
import playsound
import wolframalpha

# Functions
def talk(text):
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    tts = gTTS(text=text,lang="en-GB")
    filename = 'voice'+date_string+'.mp3'
    tts.save(filename)
    print("Iris: "+text)
    playsound.playsound(filename)
    os.remove(filename)
    

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.record(source,duration=4)
        cmd = ""

        try:
            cmd = r.recognize_google(audio)
            print("You said: "+cmd)
        except Exception as e:
            print("Exception: "+str(e))

    return cmd

def solveProblem(problem):
    app_id = "QW6H33-E5W9WHH7J8"
    client = wolframalpha.Client(app_id)
    my_input = problem
    response = client.query(my_input)
    answer = next(response.results).text
    talk(answer)

# Main program
if __name__ == '__main__':
    talk("Hi, I'm Iris. What can I help you ?")
    command = get_audio()
    if "question" in command:
        talk("What is your question")
        question = get_audio()
        solveProblem(question)
    else:
        talk("I cannot hear you, please try again later !")

