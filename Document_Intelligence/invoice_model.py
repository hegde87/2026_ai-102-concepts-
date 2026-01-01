
# #It all depends on which model we are using when it comes to Analyzing the Document 
#     >prebuilt-invoice
#     >prebuilt-idDocument
#     >prebuilt-layout
#     >prebuilt-read

# https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/invoice?view=doc-intel-4.0.0
# Install : pip install azure-ai-documentintelligence==1.0.0b4


from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult


endpoint="https://document3300.cognitiveservices.azure.com/"
key=""
document_url="https://blobstorage3300.blob.core.windows.net/documents/sampleinvoice33.png"

client=DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))

response=client.begin_analyze_document("prebuilt-invoice",AnalyzeDocumentRequest(url_source=document_url))

result: AnalyzeResult = response.result()

for index,invoice in enumerate(result.documents):
    print(f"Customer Name {invoice.fields.get("CustomerName").get("valueString")}")
    print(f"Invoice ID {invoice.fields.get("InvoiceId").get("valueString")}")
    print(f"SubTotal {invoice.fields.get("SubTotal").get("content")}")

