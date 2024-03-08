import speech_recognition as sr
import pyttsx3
import colorama
from colorama import Fore

recognizer = sr.Recognizer()
CurrentLanguage = "ja"

"""
english: en
Japanese:ja
Korean:ko
Traditional Chinese:zh-CN
"""

while True:

        with sr.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
        
        try:

            text = recognizer.recognize_google(audio, language=CurrentLanguage)
            text = text.lower()
            #out = translator.translate(text, dest="en")
            print(Fore.BLUE,text)
            #print(out.text)
            
            
        except:
            if CurrentLanguage == "en":
                print(Fore.RED,"can not hear your voice")
            if CurrentLanguage == "ja":
                print(Fore.RED,"あなたの声が聞こえなかった")
            if CurrentLanguage == "zh-CN":
                print(Fore.RED,"我聽不見你的聲音")
            if CurrentLanguage == "ko":
                print(Fore.RED,"나는 당신의 목소리를들을 수 없었습니다")
