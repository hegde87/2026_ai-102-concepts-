# Azure Custom Vison 
# We train Model to classify images   --->Training Model 
# predicting the image ---> Prediction Model 


# First Install :- pip install azure-cognitiveservices-vision-customvision

from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

endpoint="https://customvision3300-prediction.cognitiveservices.azure.com/"
prediction_key=""

credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
prediction_client = CustomVisionPredictionClient(endpoint, credentials)

image_data = open("img1.jpg", mode="rb").read()
project_id = "3b3a51c1-3083-4cf0-a987-35beed271475"
model_name = "PetModel"

response = prediction_client.classify_image(project_id, model_name, image_data)

for prediction in response.predictions:
    print(prediction.tag_name, prediction.probability)