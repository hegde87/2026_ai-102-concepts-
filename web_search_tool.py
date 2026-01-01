
# OpenAI Docementation Reference : https://platform.openai.com/docs/guides/images/image-generation
# How to call this various tool 

# line 20 --> image_generation ==> tool for image generation
 
# line 22 --> web_search_preview ==> tool for web search   [If we want to go to google and search for something latest]




from openai import OpenAI
import base64
import time


api_key = "xxxxxxxxxxx_xxxxxxxxxxxA"
client = OpenAI(api_key=api_key)

start = time.time()
response = client.responses.create(
    model="gpt-5",   # or gpt-4.1 / gpt-4o etc., any model that supports the image tool
    input="Whats the latest news today in the world  about AI Technology?",
    # tools=[{"type": "image_generation"}],  # enable the built-in image tool
    tools=[{"type": "web_search_preview"}],  # enable the built-in web search tool

)
end = time.time()
elapsed = end - start

print("response time: %.2f seconds"% elapsed)

print(response.output_text)

######Note#####
#e are waiting for the model to go to the Web and search for the latest information about AI Technology

