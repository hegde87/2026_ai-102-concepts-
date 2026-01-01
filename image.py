# Using a Model to generate Image  


import os
from openai import AzureOpenAI
import requests


client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="https://sagarfoundry3300ai.cognitiveservices.azure.com/",
    api_key="",
)


response = client.images.generate(
    model="dall-e-3",
    prompt= "A futuristic cat dwelling in the sunset, highly detailed, digital art",
    n=1,
    size="1024x1024",
    quality="standard"
)

image_url=response.data[0].url


# We want to save the image locally
image_data=requests.get(image_url).content
with open("futuristic_cat.png","wb") as handler:
    handler.write(image_data)

print("Finished generating the iamge")