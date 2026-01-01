import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://sagarfoundry3300ai.cognitiveservices.azure.com/",
    api_key="",
)
rag_params = {
    "data_sources": [
        {
            "type": "azure_search",
            "parameters": {
                "endpoint": "https://search3300.search.windows.net",
                "index_name": "dataindex",
                "authentication": {
                    "type": "api_key",
                    "key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                }
            }
        }
    ]
}

response = client.chat.completions.create(
    model="gpt-4.1",  # Use your actual deployment name
    messages=[
        {"role": "system", "content": "You are an assistant who helps users find information about places to visit in Russia."},
        {"role": "user", "content": "what are the places to visit in moscow?"}
    ],
    extra_body=rag_params
    # NO max_completion_tokens, NO temperature here
)



print(response.choices[0].message.content)
