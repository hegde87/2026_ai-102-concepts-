from openai import AzureOpenAI
from pydantic import BaseModel

# ========= CONFIG – EDIT THESE 3 =========
AZURE_OPENAI_ENDPOINT = "https://hegde-mjl1rsax-eastus2.cognitiveservices.azure.com/"  # from Keys & Endpoint
AZURE_OPENAI_API_KEY = ""                                       # from Keys & Endpoint
AZURE_OPENAI_API_VERSION = "2024-12-01-preview"                                   # use version shown in AI Studio code
DEPLOYMENT_NAME = "gpt-5-chat"                           # from Deployments blade
PDF_PATH = "Invoice01.pdf"
# ========================================


# 1) Define schema via Pydantic
class InvoiceFields(BaseModel):
    invoice_number: str
    invoice_date: str
    due_date: str
    total_amount: float
    company_name: str
    company_address: str


# 2) Create AzureOpenAI client
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)


# 3) Upload PDF once
with open(PDF_PATH, "rb") as fpdf:
    uploaded_file = client.files.create(
        file=fpdf,
        purpose="assistants",
    )

# 4) Call beta.chat.completions.parse with file + schema
completion = client.beta.chat.completions.parse(
    model="gpt-5-chat",      # <- MUST match deployment name in Azure
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Read the invoice and return ONLY these fields: "
                            "invoice_number, invoice_date, due_date, "
                            "total_amount, company_name, company_address.",
                },
                {
                    "type": "file",
                    "file":{ 
                        "file.id": uploaded_file.id
                    },
                },
            ],
        }
    ],
    response_format=InvoiceFields,   # Pydantic model, parsed into .parsed
    max_tokens=1000,
    temperature=0,
)


# 5) Use the parsed result
message = completion.choices[0].message

if message.parsed:
    data: InvoiceFields = message.parsed
    print("Structured output as dict:")
    print(data.model_dump())
else:
    print("Model refused request:")
    print(message.refusal)


# 26Dec2025 #
#--------------
#### we need to work on this !!!!! -->Not able to execute properly!!!!!!! ################ 
