import gtts
import playsound
import speech_recognition as s

def all_speech():
    sr=s.Recognizer()
    print('eNTER something : ')
    with s.Microphone() as m:
        audio=sr.listen(m)
        query=sr.recognize_google(audio, language='eng-in')

#speech.all_speech()
