# Language Translator 
import googletrans as gt
import pyttsx3
import speech_recognition as sr
import gtts
import playsound
import os

print(gt.LANGUAGES, "\n")

language = input("Enter your language code: ")

recognizer = sr.Recognizer()
translator = gt.Translator()

x = 0

while(x == 0):
    try:
        with sr.Microphone() as source:
            print('Speak Now...')
            voice = recognizer.listen(source)
            text = recognizer.recognize_google(voice)
            print(text)
            x = 1
    except:
        print("Try Again!")
        pass

output = translator.translate(text, dest=language)
print("Translation: ", output.text)
print("Pronunciation: ", output.pronunciation)

converted_audio = gtts.gTTS(output.text, lang=language)
converted_audio.save('TCET Hackanova\Flask\lang_trans1.mp3')
playsound.playsound('TCET Hackanova\Flask\lang_trans1.mp3')

os.remove('TCET Hackanova\lang_trans1.mp3')