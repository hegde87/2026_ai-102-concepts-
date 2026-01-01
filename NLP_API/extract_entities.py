# How we can extract name entities by Python Programm





from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


endpoint="https://language3300.cognitiveservices.azure.com/"
key=""

clinet=TextAnalyticsClient(endpoint=endpoint,credential=AzureKeyCredential(key))

documents=[
    "Satya Nadella announced at Microsoft's headquaters in Redmond"
    "that the comapany's revenue for the fourth quarter was 46$ billion"
]

response=clinet.recognize_entities(documents=documents)[0]
for entity in response.entities:
    print(f"Entity Text: {entity.text} - Enity Category: {entity.category}")

