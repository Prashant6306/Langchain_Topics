from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

file=DirectoryLoader(
    path="/home/prashant/Desktop/Langchain_Topics/08.Document_Loader/folder1",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

document=file.load()

print(len(document))

print(document[134].page_content)