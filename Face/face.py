
# install: pip install azure-ai-vision-face 

# if we want to take the image from local system
import json
from xmlrpc import client
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.face import FaceClient
from azure.ai.vision.face.models import *

endpoint="https://face3300.cognitiveservices.azure.com/"
key=""

clinet=FaceClient(endpoint=endpoint,credential=AzureKeyCredential(key))

features_to_client=[
    FaceAttributeType.AGE,
    FaceAttributeType.SMILE,
    FaceAttributeType.HEAD_POSE
]

with open("face01.png","rb") as img_file:
    response=client.detect(
        image_content=img_file.read(),
        detection_model=FaceDetectionModel.DETECTION01,
        recognition_model=FaceRecognitionModel.RECOGNITION01,
        return_face_attributes=features_to_client,
        return_face_id=False
    )

print(json.dumps(response[0].as_dict(),indent=4))