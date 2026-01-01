from azure.ai.language.conversations import ConversationAnalysisClient
from azure.core.credentials import AzureKeyCredential

# 1. Use the Language (CLU) endpoint, NOT the Speech endpoint
endpoint="https://speech3300.cognitiveservices.azure.com/"
key=""


client = ConversationAnalysisClient(endpoint=endpoint,
                                    credential=AzureKeyCredential(key))

utterance = "I need a double room for me and my family for the weekend"

# 2. Use the exact CLU project + deployment names
project_name = "TraininProject"          
deployment_name = "TrainingDeplyment"  

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
            # NOTE: camelCase names required by the API
            "projectName": project_name,
            "deploymentName": deployment_name,
            "verbose": True
        }
    }
)

print(response)
