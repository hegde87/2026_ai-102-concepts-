# To see and understand videos and images 
# It should be able to detect diff attributes of the image

# 	>Comman Tags 
# 	>caption generation
# 	>Object detection
# 	>OCR --->OPTICAL CHARACTER RECOGNITION
	

# Azure Vision Studio 
# Azure computer vision

# https://portal.vision.cognitive.azure.com 

# First install :- pip install azure-ai-vision-imageanalysis

from urllib import response
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures
import json


endpoint="https://vision3300.cognitiveservices.azure.com/"
key=""

client=ImageAnalysisClient(endpoint=endpoint,credential=AzureKeyCredential(key))

with open("AzureAIVision-ImageTagging.png","rb") as img_file:
    image_details=img_file.read()

response=client.analyze(
    image_data=image_details,
    visual_features=[VisualFeatures.TAGS.CAPTION]
)

print(json.dumps(response.as_dict(),indent=4))

