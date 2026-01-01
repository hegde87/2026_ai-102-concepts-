


from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


endpoint="https://language3300.cognitiveservices.azure.com/"
key=""

clinet=TextAnalyticsClient(endpoint=endpoint,credential=AzureKeyCredential(key))

documents=[
    "Machine learning and artificial intelligence are transforming industries such as healthcare, "
    "finance and education by automating task and providing insights."
]

response=clinet.extract_key_phrases(documents=documents)[0]
# response=clinet.detect_language(documents=documents)
# in order to get the response back 
for key_phrase in response.key_phrases:
    print(key_phrase)