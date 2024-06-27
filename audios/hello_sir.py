import gtts
import playsound
#yaha pr text dalne jise text to speech convert krna he
#as an input bhi le sakta he
text='please remove the charger, battery is full'
sound=gtts.gTTS(text, lang='hi')

sound.save('splease remove the charger, battery is full.mp3')#kis naam se save krna he
playsound.playsound('splease remove the charger, battery is full.mp3')#ye play krne ke liye, agar iska kaam na ho to hata dena, aur package ko bhi hata dena


































"""
import speech_recognition as s

sr=s.Recognizer()
print('eNTER something : ')
with s.Microphone() as m:
    audio=sr.listen(m)
    jarvis_see=sr.recognize_google(audio, language='eng-in')
    jarvis=str(jarvis_see)
print(jarvis)
"""
