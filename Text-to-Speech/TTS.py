from playsound import playsound
from datetime import datetime
from gtts import gTTS
/
now = datetime.now()
dt_string = str(now.strftime("-%d-%m-%Y %H:%M:%S"))

mytext = "The destroyer has arrived"

audio = gTTS(mytext, lang='en', tld='co.uk')
FileInfo = str("Speech-file"+dt_string+".mp4")
print(type(FileInfo))
FilePath = str("./Audio/"+FileInfo)
audio.save(FilePath)

playsound(FilePath)
