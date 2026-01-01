
import os
from openai import AzureOpenAI
import base64



# We need to take the image content and pass it to the model
#  Diff ways we can send in our image data 
#   a) Read the contents of the image as binary format Encode it in base64 and send it in the messages

with open("code.py","r",encoding="utf-8") as code_file:
    code_contents = code_file.read()

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://hegde-mjl1rsax-eastus2.cognitiveservices.azure.com/",
    api_key="",
)


response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an assistant who helps teach how to code.",
        },
        {
            "role": "user",
            "content": f"Explain clearly what the following Python code does:\n\n{code_contents}"
        }
    ],
    max_completion_tokens =500,
    temperature=1,
    model="gpt-5.1-chat"
)


print(response.choices[0].message.content)

# dumped_respose=response.model_dump()

# print(json.dumps(dumped_respose, indent=2))
