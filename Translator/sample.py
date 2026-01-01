        ######## Python Program making use of Translation Service #######
# ------------------------------------------------------------------------------
# Translate text from source language onto a destination language
# Translate batch of documents or compleX files 

# Install the package : pip install azure-ai-translation-text==1.0.0b1    
# This will allows us to work with this service 

from azure.ai.translation.text import  TextTranslationClient,TranslatorCredential
from azure.ai.translation.text.models import InputTextItem


endpoint="https://api.cognitive.microsofttranslator.com/"
key="" 
region="eastus"

credential=TranslatorCredential(key,region)
client=TextTranslationClient(endpoint=endpoint,credential=credential) 

source_language= "en"
target_language= ["it"]

input_txt= "I like to learn new languages"

documents=[InputTextItem(text=input_txt)]

response=client.translate(content=documents,to=target_language,from_parameter=source_language)

print(f"Translated Text : {response[0].translations}")