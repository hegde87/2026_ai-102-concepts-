# Extract text from the image using OCR 



from urllib import response
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures
import json


endpoint="https://vision3300.cognitiveservices.azure.com/"
key=""

client=ImageAnalysisClient(endpoint=endpoint,credential=AzureKeyCredential(key))

with open("quote.png","rb") as img_file:
    image_details=img_file.read()

response=client.analyze(
    image_data=image_details,
    visual_features=[VisualFeatures.READ]
)

# print(json.dumps(response.as_dict(),indent=4))

for line in response.read.blocks[0].lines:
    print(f"{line.text}")
    