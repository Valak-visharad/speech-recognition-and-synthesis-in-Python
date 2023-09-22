import speech_recognition as sr
#from gtts import gTTS
import os
import win32com.client
import time
#from http.cookies import Morsel
def num4str(text):
    nums=str()
    for an in text:
        try:
            if(int(an)==int(an)):
                nums+=an
        except ValueError: continue
    finalnum=str()
    for mn in nums:
        finalnum+=mn
    return(int(finalnum))

s= win32com.client.Dispatch("SAPI.SpVoice") 
mic=sr.Microphone()
r=sr.Recognizer()
f=1
f2=1
try:
    print("\n\n\t\t\t\twelcome Mr. vilakshan\n")
    s.Speak("Welcome Mr vilukshan")
    time.sleep(2)
    print("\n\n\t...This is a software of Artificial Intelligence,where I would try to add two numbers given by you...")
    s.speak("This is a software of Artificial Intelligence,where I would try to add two numbers given by you")
    while(f!=0):
        print("\n\nTell me your first number:")
        s.Speak("Tell me your first number")
        with mic as source: voice=r.listen(source)
        print("\n\t\t...recognizing...")
        s.Speak("ok sir")
        try:
            value1=r.recognize_google(voice)
            print("your first no.:{}".format(value1))
            s.Speak("you told me:{}".format(value1))
        except sr.UnkownValueError:
            print("Sorry! Can't Recognize that!")
            s.Speak("Sorry! Can't Recognize that!")
        except AttributeError: continue
        try:
            print("\n\tARE YOU SURE?")
            s.Speak("Are you sure sir?")
            with mic as source:
                inp=r.recognize_google(r.listen(source))
            if ('yes' in inp):
                s.Speak("ok sir")
                f=0
                break
            else:
                s.Speak("Sorry sir, tell me your number again")
        except KeyboardInterrupt:
            pass
        except sr.UnkownValueError:
            print("Sorry! Can't Recognize that!")
            s.Speak("Sorry! Can't Recognize that!")
except KeyboardInterrupt:
    pass

        
while(f2!=0):
    try:
        print("Tell me the second no.")
        s.Speak("\n\nnow tell me the second number")
        with mic as source: voice=r.listen(source)
        print("\n\t\t...recognizing...")
        s.Speak("ok sir")
        try:
            value2=r.recognize_google(voice)
            print("your second no.:{}".format(value2))
            s.Speak("your second number is:{}".format(value2))
        except sr.UnkownValueError:
            print("Sorry! Can't Recognize that!")
            s.Speak("Sorry! Can't Recognize that!")
        try:
            print("\n\tARE YOU SURE?")
            s.Speak("Are you sure sir?")
            with mic as source:
                inp=r.recognize_google(r.listen(source))
            if ('yes' in inp):
                s.Speak("ok sir")
                f2=0
            else:
                s.Speak("Sorry sir, tell me your number again")
                f2=1
        except KeyboardInterrupt:
            pass
        except sr.UnkownValueError:
            print("Sorry! Can't Recognize that!")
            s.Speak("Sorry! Can't Recognize that!")
    except KeyboardInterrupt:
        pass
sum1=num4str(value1)+num4str(value2)
print("\n\n\tThe sum of the numbers you told me =",sum1)
s.Speak("The sum of the numbers you told me is"+str(sum1))
#mytext='Thank you to use this software'
#language='en'
#myobj=gTTS(text=mytext, lang=language, slow=False)
#myobj.save('default.mp3')
os.system("default.mp3")
