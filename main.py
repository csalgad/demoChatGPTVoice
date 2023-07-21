#IMPORT libraries
import openai
import pyttsx3

#Set API Key
openai.api_key="<INSERT API KEY HERE>"

#Get Audiot File
audio_file=open("C:/Users/chris/Downloads/Recording.mp3", "rb")

#Transcribe
transcript=openai.Audio.translate("whisper-1", audio_file)
print(transcript)

#Completion
response=openai.Completion.create(
    model="text-davinci-003",
    prompt=transcript,
    temperature=0,
)

#Cleanup
final_response = response.choices[0].text
final_response = final_response.replace('\n','')
print(final_response)

#Speak
engine = pyttsx3.init()
engine.say(final_response)
engine.runAndWait()