import speech_recognition as sr
import win32com.client as sapi
import os
#import pyttsx3      ##########NOT USING currently
r=sr.Recognizer()
d=sapi.Dispatch("SAPI.SpVoice")
mic=sr.Microphone()




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



d.Speak('What can i do for you')
while(True):
    try:
        print('Listening...')
        with mic as source:
            sound=r.listen(source)
            d.Speak("Ok sir")
            print("\n\n\t\t\t***")
            text=r.recognize_sphinx(sound)
        print("\t\t\t\t{}".format(text))
        if ('shutdown' in text):
            if('in' in text):
                num4str(text)
                if('second' in text):
                    t=num4str(text)
                elif('minute' in text):
                    t=num4str(text)*60
                elif('hour' in text):
                    t=num4str(text)*3600
            comm='shutdown.exe -s -t '+str(t)
            print(comm)
            os.system(comm)
            if('not' in text):
                os.system("shutdown/a")
        if('computer' in text):
            continue
            
    except:
        print('\n\n\t\t\t...........ERROR...........\n\n')
        d.Speak("Please say it again sir")
        print('Command now')



    d.Speak('listening')
  
