# we have a image --> Hand written image 
# we want to extract the TEXT at the same we want to check if it Hand Written Or Not !!!!


from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult


endpoint="https://document3300.cognitiveservices.azure.com/"
key=""
document_url="https://blobstorage3300.blob.core.windows.net/documents/Document-handwritten.png"

client=DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))

response=client.begin_analyze_document("prebuilt-read",AnalyzeDocumentRequest(url_source=document_url))

result: AnalyzeResult = response.result()

# i want to add a conditional step to understand the style of the Text 
for style in result.styles:
    if style.is_handwritten==True:
        print(f"Handwritten text, Confidence : {style.confidence}")

for index,para in enumerate(result.paragraphs):
    print(f"Paragraph {index+1}: {para.content}")
 

