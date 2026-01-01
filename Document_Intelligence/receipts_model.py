from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult


endpoint="https://document3300.cognitiveservices.azure.com/"
key=""
document_url="https://blobstorage3300.blob.core.windows.net/documents/samplereceipt.png"

client=DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))

response=client.begin_analyze_document("prebuilt-receipt",AnalyzeDocumentRequest(url_source=document_url))

result: AnalyzeResult = response.result()

for index,receipt in enumerate(result.documents):
    print(f"Merchant Name {receipt.fields.get("MerchantName").get("valueString")}")
    print(f"Transaction Date {receipt.fields.get("TransactionDate").get("content")}")
    print(f"Total {receipt.fields.get("Total").get("content")}")
