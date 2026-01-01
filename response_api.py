
# Using New Response API    -->New Set of API 
# Its designed to go beyond chat completions
#Early when it came on to AI Model  Give --> Text Input  & Giving Text Output
# Now we have Multimodal Models  --> Take Image Input , Audio Input , Video Input
# So Response API is designed to handle all these different input and output types in a unified way

# Model can use Tools , OpenAI has developed a new API ==>Response API
# 1 API For chat 
# 1 API for Image
# 1 API for Audio
# 1 API for Tool Calling 




import os
from openai import AzureOpenAI


client = AzureOpenAI(
    api_version="2025-03-01-preview",
    azure_endpoint="https://hegde-mjl1rsax-eastus2.cognitiveservices.azure.com/",
    api_key="",
)


response = client.responses.create(
    input=[
        {"role": "system", "content": "You are an assistant who helps teach how to code."},
        {"role": "user", "content": "How can i write a simple python program that interacts with an OpenAI Model"},
    ],
    max_output_tokens =1000,
    temperature=1,
    model="gpt-5.1-chat"
)


print(response.output_text)

