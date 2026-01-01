### Structured Output ####
# ----------------------------
# when u send a Promt to the Model ---> When we get the response back from the Model ==>Output is in Unstructured Format
# ie -->Text 
# ie --> Pragraph
# i.e -->List 
# when we send a prompt to the model we can specify that we want the output in a structured format

# Example:- 
# We have add a Invoice Copy ---> We want the output in a structured format i. json format
# Model will extract the relevant fields from the invoice and give it to us in a structured json format

            ### We want to get a structured output from the model ###
# -------------------------------------------------------------------------------------

import os
from openai import AzureOpenAI
import base64, json 

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://hegde-mjl1rsax-eastus2.cognitiveservices.azure.com/",
    api_key="",
)

with open("Invoice01.jpg", "rb") as image_file:
    document_details = base64.b64encode(image_file.read()).decode("utf-8")

tools = [{
    "type": "function",
    "function": {
        "name": "return_invoice_fields",
        "description": "Return only extracted invoice fields",
        "parameters": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
            "invoice_number": {"type": "string"},
            "invoice_date": {"type": "string", "format": "date"},
            "due_date": {"type": "string", "format": "date"},
            "total_amount": {"type": "number"},
            "company_name": {"type": "string"},
        },
        "required": ["invoice_number", "invoice_date", "due_date", "total_amount", "company_name"],

    },
}
}]

message = [
    {"role": "system", "content": "Extract structured info from invoice accurately and consisely."},
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": (
                    "Extract the following and return them via the functions call:\n"
                    "- invoice_number (string)\n"
                    "- invoice_date (YYYY-MM-DD)\n"
                    "- due_date (YYYY-MM-DD)\n"
                    "- total_amount (number only)\n"
                    "- company_name (string)\n"
                    "If fields are missing, infer carefully from context."
                ),
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{document_details}"
                },
            },
        ],
    },
    
]

resp = client.chat.completions.create(
    model="gpt-5-chat",
    messages=message,
    tools=tools,
    # tool_invocation="auto",
    tool_choice={"type": "function", "function": {"name": "return_invoice_fields"}},
    max_completion_tokens=1000,
    temperature=0
)

choice = resp.choices[0]
tool_call = choice.message.tool_calls[0]
args = json.loads(tool_call.function.arguments)
print(
    args["invoice_number"],
    args["invoice_date"],
    args["due_date"],
    args["total_amount"],
    args["company_name"]
)