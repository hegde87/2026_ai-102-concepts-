



###### TEXT TO SPEECH #####Here we are controlling the way the model is going to speek!!!!!
# WE NEED TO INSTALL :- pip install azure-cognitiveservices-speech
# Speech Synthesis Markup Language (SSML) overview
# ----------------------------------
# https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup

# Customize voice and sound with SSML
# https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice


import os
import azure.cognitiveservices.speech as speechsdk

endpoint="https://speech3300.cognitiveservices.azure.com/"
key="" 


config=speechsdk.SpeechConfig(subscription=key,endpoint=endpoint)

output_file="speech03.wav"
audio_output= speechsdk.audio.AudioConfig(filename=output_file)
speech_generator = speechsdk.SpeechSynthesizer(speech_config=config,audio_config=audio_output)

with open("config.xml", "r", encoding="utf-8") as file:
    ssml_string = file.read()

result = speech_generator.speak_ssml_async(ssml_string).get()
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Successfuly generated speech")
else:
    print("Generating speech failed", result.reason) 



