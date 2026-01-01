
# Install: pip install azure.ai.textanalytics
# Make use of service -->In Background u have a AI Model in place that has the capability
# Taking the input ---> Performing that functionallity and Giving response back! 

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


endpoint="https://language3300.cognitiveservices.azure.com/"
key=""

clinet=TextAnalyticsClient(endpoint=endpoint,credential=AzureKeyCredential(key))

documents=[
    "Me gusta aprender nuevos idiomas"
    "Comment allez-vous ce martin ?"
]

response=clinet.detect_language(documents=documents)

print(response)