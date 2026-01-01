
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


endpoint="https://language3300.cognitiveservices.azure.com/"
key=""

clinet=TextAnalyticsClient(endpoint=endpoint,credential=AzureKeyCredential(key))

documents=[
    "The restarurant had amazing food and the staff were incredibly friendly. I cant wait to go back!",
    "The product arrived broken and customer service was unhelpful when i tried to get a replacement.",
    "The report produced around 1000 data points"
]

response = clinet.analyze_sentiment(documents=documents)

for result in response:
    for sentence in result.sentences:
        print(f"Sentiment: {sentence.sentiment} - Sentence: {sentence.text}")



# response=clinet.analyze_sentiment(documents=documents)
# # response=clinet.extract_key_phrases(documents=documents)[0]
# # response=clinet.detect_language(documents=documents)
# # in order to get the response back 
# for result in response:
#     print(f"Sentiment: {result.sentences[0].sentimet} -Sentence: {result.sentences[0].text}")