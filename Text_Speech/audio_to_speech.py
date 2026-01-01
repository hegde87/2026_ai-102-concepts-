###### TEXT TO SPEECH #####
# WE NEED TO INSTALL :- pip install azure-cognitiveservices-speech

import azure.cognitiveservices.speech as speechsdk



endpoint="https://speech3300.cognitiveservices.azure.com/"
key="" 


config=speechsdk.SpeechConfig(subscription=key,endpoint=endpoint)

output_file="transcribed.txt"
audio_filename="speech01.wav"
config.speech_recognition_language="en-US"

audio_input= speechsdk.AudioConfig(filename=audio_filename)

text_generator = speechsdk.SpeechRecognizer(speech_config=config,audio_config=audio_input)

result=text_generator.recognize_once_async().get()
if result.reason== speechsdk.ResultReason.RecognizedSpeech:
    print("Successfuly generated Text")
else:
    print("Generating text failed") 


