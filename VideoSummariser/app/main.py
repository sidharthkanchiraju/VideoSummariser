import speech_recognition as sr 
import os 
import subprocess
import google.generativeai as genai

# MAIN ERROR IS AUDIO FILE IS TOO LARGE

AUDIO_FILE = input("Path to Audio File: \n")

command = f"ffmpeg -i {AUDIO_FILE} audio.wav"

subprocess.call(command, shell=True)

r = sr.Recognizer()

with sr.AudioFile(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'audio.wav')) as file:
    audio = r.record(file)

print("Hello")

recognized_text = ""
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    recognized_text = r.recognize_google(audio)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

genai.configure(api_key=os.environ["GOOGLEAI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("summarise this text: " + recognized_text)
print(response.text)


