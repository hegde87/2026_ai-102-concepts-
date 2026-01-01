# this is for Image file 

# we are not dealing with OpenAI 
# WE ARE MAKING USE OF Azure Content Safety Service
# eg: User is inserting a Image or text that is harmful 

# First Step: we need to filter the content what USER is sending to the LLM
# Second Step: we need to filter the content what LLM is sending back to USER

# we are using Azure Content Safety  --> we have a resource deployed in Azure Portal
# we are making use of Endpoint and Key from that resource  -->To authenticate our requests


#  pip install azure.ai.contentsafety  

from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety import AnalyzeImageOptions, ImageData

endpoint="https://contentsafety3300.cognitiveservices.azure.com/"
key= ""

client=ContentSafetyClient(endpoint,AzureKeyCredential(key)) 
with open("img1.jpg","rb") as image_file:
    request=AnalyzeImageOptions(image=ImageData(content=image_file.read()))
                                


response=client.analyze_image(request)
print("response")