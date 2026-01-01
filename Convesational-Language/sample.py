# A Python programm that can make a call to our deployment 
#  using -->Language Studio 
# reference link: https://language.cognitive.azure.com/clu/projects/TraininProject/test
# https://docs.azure.cn/en-us/ai-services/language-service/conversational-language-understanding/concepts/best-practices

# Back up and recover your conversational language understanding models
# https://docs.azure.cn/en-us/ai-services/language-service/conversational-language-understanding/how-to/fail-over
# Prerequisites
# Two Language resources in different Azure regions, each of them in a different region.

# Our Model that is deployed as part of Language Resource when it comes onto Conversational Language Understanding

# We will have a model inplace that will take a Input 
# It will understand the Intent & Entities of the input
# We will have a application developed in a progaming language 
# The application takes the query from the User
# Forwad that query on to the Model 
# Model will give the response back in terms of the Intents and Entities
# what response we give to the USER is something we need to do within the Application 
# eg: we might have a knowledge bank of answers -->based on Intent and based on the Entities ==>CAN GIVE RESPONSE TO THE USER!!!

# Frist installl: pip installl azure-ai-language-conversations

from azure.ai.language.conversations import ConversationAnalysisClient
from azure.core.credentials import AzureKeyCredential

endpoint="https://speech3300.cognitiveservices.azure.com/"
key=""

client=ConversationAnalysisClient(endpoint=endpoint,credential=AzureKeyCredential(key))

utterance = "I need a double room for me and my family for the weekend"
project_name = "TrainingProject"
deployment_name = "TrainingDeployment"

response = client.analyze_conversation(
    task={
        "kind": "Conversation",
        "analysisInput": {
            "conversationItem": {
                "participantId": "1",
                "id": "1",
                "modality": "text",
                "language": "en",
                "text": utterance
            },
            "isLoggingEnabled": False
        },
        "parameters": {
            "project_name": project_name,
            "deployment_name": deployment_name
        }
    }
)

print(response)
