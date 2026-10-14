from google.api_core.client_options import ClientOptions
from google.cloud import documentai_v1
from decouple import config

project_id = config("PROJECT_ID")
location = config("PROCESSOR_LOCATION")
processor_id = config("PROCESSOR_ID")


opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")

client = documentai_v1.DocumentProcessorServiceClient(client_options=opts)

full_processor_name = client.processor_path(project_id, location, processor_id)

request = documentai_v1.GetProcessorRequest(name=full_processor_name)
processor = client.get_processor(request=request)

print(f"Processor Name: {processor.name}")

with open(file_path, "rb") as image:
    image_content = image.read()

raw_document = documentai_v1.RawDocument(
    content=image_content,
    mime_type="application/pdf",
)

request = documentai_v1.ProcessRequest(name=processor.name, raw_document=raw_document)
result = client.process_document(request=request)
document = result.document

print("The document contains the following text:")
print(document.text)