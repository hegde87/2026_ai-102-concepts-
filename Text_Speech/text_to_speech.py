###### TEXT TO SPEECH #####
# WE NEED TO INSTALL :- pip install azure-cognitiveservices-speech

import azure.cognitiveservices.speech as speechsdk



endpoint="https://speech3300.cognitiveservices.azure.com/"
key="" 


config=speechsdk.SpeechConfig(subscription=key,endpoint=endpoint)
config.speech_synthesis_voice_name="en-US-steffanMultilingualNeural"

input_txt="Machine learining is a branch of artificial intelligence (AI)" \
"that focuses on building systems that can learn from data and improve over time without being explicitly programmed." \
"Sagar Hegde is learning AI " \
"Very soon he would be an AI Engineer and working in some product based company" \
"Rushika is sagar only daughter" \
"Thank you Usha Hegde & Mohan Hegde, parents of Sagar from Chinchwad Pune" \
"With out you guys this journey was impossible, thank you onces again Sagar Hegde"

output_file="speech01.wav"
audio_output= speechsdk.audio.AudioConfig(filename=output_file)

speech_generator = speechsdk.SpeechSynthesizer(speech_config=config,audio_config=audio_output)

result=speech_generator.speak_text_async(input_txt).get()
if result.reason== speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Successfuly generated speech")
else:
    print("Generating speech failed") 


