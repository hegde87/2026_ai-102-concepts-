# We want to use a Combination of SERVICE 
# Use Document Intelligence Service to Extract TEXT from a File 

# Then use Language Service On Analyzing the Sentiments of each and every sentance that we have in Document  i.e 10 sentences

# we want to submit each and ever line to a resource to Analyze the sentiments.
# I want to language service to analyze the Sentiments and give me the response back.

# we are using 2 Services 

#   Azure language service 
#   Azure document intelligence service   --> Use "prebuilt-read" Model We just want to Extract Text 
#   Azure Blob Service   --> upload the customer review pdf in a container

# Install : pip install azure-ai-documentintelligence==1.0.0b4

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.textanalytics import TextAnalyticsClient

endpoint="https://document3300.cognitiveservices.azure.com/"
key=""


language_endpoint="https://ailanguage3300.cognitiveservices.azure.com/"
language_key=""

document_url="https://blobstorage3300.blob.core.windows.net/documents/Customer Feedback Review.pdf"

client=DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))
language_client=TextAnalyticsClient(endpoint=language_endpoint,credential=AzureKeyCredential(language_key))

response=client.begin_analyze_document("prebuilt-read",AnalyzeDocumentRequest(url_source=document_url))

result: AnalyzeResult = response.result()
documents= []

for each_page in result.pages:
    for index,line in enumerate(each_page.lines):
        documents.append(line.content) 

language_response=language_client.analyze_sentiment(documents=documents)

for result in language_response:
    print(f"Sentiment: {result.sentences[0].sentiment} - Sentence: {result.sentences[0].text}")

# For the result --> we want to have the 
# Sentiments: positive - Sentence: 4. This book inspireed me to change the wat i think about my career highly recommended !
