

#  pip install azure.ai.contentsafety  

from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import AnalyzeTextOptions

endpoint="https://contentsafety3300.cognitiveservices.azure.com/"
key= ""

client=ContentSafetyClient(endpoint,AzureKeyCredential(key)) 
txt="I am feeling very sad and depressed. I want to end my life."

request=AnalyzeTextOptions(text=txt)

response=client.analyze_text(request)
print("response")
