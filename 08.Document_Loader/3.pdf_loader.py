
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("/home/prashant/Desktop/komal/Langchain/Document_Loader/Python_Training_Slides_With_Images.pdf")

docs=loader.load()

print(docs[3].page_content)
print(docs[3].metadata)
# for i in docs:
#     print(i.page_content)