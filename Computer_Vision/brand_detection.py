### Brsnd Detection

## Fruit basket image 


from urllib import response
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures
import json


endpoint="https://vision3300.cognitiveservices.azure.com/"
key=""

client=ImageAnalysisClient(endpoint=endpoint,credential=AzureKeyCredential(key))

with open("microsoft.png","rb") as img_file:
    image_details=img_file.read()

response=client.analyze(
    image_data=image_details,
    visual_features=[VisualFeatures.TAGS.BRANDS]
)

print(json.dumps(response.as_dict(),indent=4))
