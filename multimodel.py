# This is for Multi Model 
# we can give Text/ files/ images as input 
# it will be able to understand the contents of the image and give description

# WE ARE DOING THIS USING A PYTHON PROGRAM NOW !!!!
import os
from openai import AzureOpenAI
# import json
import base64



# We need to take the image content and pass it to the model
#  Diff ways we can send in our image data 
#   a) Read the contents of the image as binary format Encode it in base64 and send it in the messages

with open("pvc.pdf", "rb") as image_file:
    image_details = base64.b64encode(image_file.read()).decode("utf-8") 
# Here above we are -->Opening the image in binary mode ==>("rb")
# Read the raw bytes of the image 
# base64.b64encode(....) -->converst those bytes into a base64-encode string 
# .decode("utf-8") --> turns the encoded bytes into a normal Python string
client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://hegde-mjl1rsax-eastus2.cognitiveservices.azure.com/",
    api_key="",
)


response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an assistant who helps to describe images.",
        },
        {
            "role": "user",
            "content": 
            [
                {
            "type": "text",
            "text":"Give me a discription of what the image is trying to explain.",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "data:image/pdf;base64,{image_details}"
                    }
                }
            ]
        }
    ],
    max_completion_tokens =500,
    temperature=1,
    model="gpt-5.1-chat"
)


print(response.choices[0].message.content)

# dumped_respose=response.model_dump()

# print(json.dumps(dumped_respose, indent=2))
