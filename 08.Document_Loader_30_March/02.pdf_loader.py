from langchain_community.document_loaders import PyPDFLoader

file=PyPDFLoader("Python_Training_Slides_With_Images.pdf")

document=file.load()

print(type(document))
print(len(document))
print(document[44].page_content)
print(document[44].metadata)