import speech_recognition as sr
import os

#ffmpeg -i audio1.amr -ar 22050 audio1.mp3
os.system('ffmpeg -i /home/jessica/Music/amy_rehab.mp3 temp.wav')

r = sr.Recognizer()
audioFile = sr.AudioFile('temp.wav')
with audioFile as source:
    audio = r.record(source)

print(r.recognize_sphinx(audio))

