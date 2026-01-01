# Image Generation 
##### we are using a tool from OpenAI To Generate Image #######

# we had used Dalle Model to generate  Imaage 

# when we chatGPT Model to generate Image --> it will call "Dalle-3" Model in the backend to generate Image
# Thereis a separate model in place for Image Generation

# Now, instead of me specific calling ---> Dalle-3 Model
# we will directly call "gpt-5" Model and tell it to generate Image i.e use ur inbuild tools to generate image 


#### we are using a tool from OpenAI To Generate Image #######



from openai import OpenAI
import base64


api_key = "xxxxxxxxxxxxxxxxxxx"
client = OpenAI(api_key=api_key)


response = client.chat.completions.create(
    
    input= "Generate a high resolution image of a futuristic cityscape during sunset with flying cars and neon lights.",
    tools=[{"type": "image_generation"}],
    model="gpt-image-1",
    prompt=prompt,
)

image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]

if image_data:
    image_base64 = image_data[0]
    with open("futuristic_cityscape.png", "wb") as img_file:
        img_file.write(base64.b64decode(image_base64))


