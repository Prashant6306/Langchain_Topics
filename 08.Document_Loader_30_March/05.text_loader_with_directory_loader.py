from langchain_community.document_loaders import TextLoader, DirectoryLoader

file=DirectoryLoader(
    path="/home/prashant/Desktop/Langchain_Topics/08.Document_Loader/folder2",
    glob="*.txt",
    loader_cls=TextLoader
)

document=file.load()

print(len(document))