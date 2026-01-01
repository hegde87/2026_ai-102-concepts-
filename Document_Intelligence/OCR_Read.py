# https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/read?view=doc-intel-4.0.0&tabs=sample-code
# Install : pip install azure-ai-documentintelligence==1.0.0b4


from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult


endpoint="https://document3300.cognitiveservices.azure.com/"
key=""
document_url="https://blobstorage3300.blob.core.windows.net/documents/ML Algorithms Guide Condensed (1).pdf"

client=DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))

response=client.begin_analyze_document("prebuild-read",AnalyzeDocumentRequest(url_source=document_url))

result: AnalyzeResult = response.result()

for index,para in enumerate(result.paragraphs):
    print(f"Paragraph {index+1}: {para.content}")
 


