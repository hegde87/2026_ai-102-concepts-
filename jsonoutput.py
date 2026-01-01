import os
from openai import AzureOpenAI
import json

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://hegde-mjl1rsax-eastus2.cognitiveservices.azure.com/",
    api_key="",
)


response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful students learning about Large Language Models.",
        },
        {
            "role": "user",
            "content": "what is the temperature setting",
        }
    ],
    max_completion_tokens =500,
    temperature=1,
    model="gpt-5.1-chat"
)


# print(response.choices[0].message.content)

dumped_respose=response.model_dump()

print(json.dumps(dumped_respose, indent=2))