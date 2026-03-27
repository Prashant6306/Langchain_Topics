
from langchain_community.document_loaders import TextLoader

loader=TextLoader("/home/prashant/Desktop/komal/Langchain/Document_Loader/doc1.txt",encoding="utf-8")

doc=loader.load()

#print(doc)

print(type(doc))

#print(doc[0])

print(doc[0].page_content)
print(doc[0].metadata)