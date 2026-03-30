from langchain_community.document_loaders import TextLoader

file=TextLoader("/home/prashant/Desktop/Langchain_Topics/01.Langchain_Intro_and_models_13_March/doc1.txt",encoding="utf-8")

document=file.load()

print(len(document))
print(document[0].page_content)

print(document[0].metadata)
