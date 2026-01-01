from openai import OpenAI
import base64


api_key = ""
client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-5",   # or gpt-4.1 / gpt-4o etc., any model that supports the image tool
    input="Generate a image of a futuristic cityscape during sunset with flying cars and neon lights.",
    tools=[{"type": "image_generation"}],  # enable the built-in image tool
)

# Collect all image-generation tool calls
image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]

if image_data:
    image_base64 = image_data[0]
    with open("futuristic_cityscape.png", "wb") as img_file:
        img_file.write(base64.b64decode(image_base64))




######### NOTE #################
# OpenAI organization is not verified --> so image generation is not working
# Need to verify the org to get this working
# Refer : https://platform.openai.com/docs/guides/images/image-generation

# To let a "model decide and call the image tool itself”, you should use the Responses API with the built‑in 
# image_generation tool, not chat.completions and not a direct image model name. 

# The text model (for example gpt-5 or gpt-4.1) will automatically invoke gpt-image-1 behind the scenes when you enable that too
