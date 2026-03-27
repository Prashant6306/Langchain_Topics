
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

loader=DirectoryLoader(
    path="/home/prashant/Desktop/komal/Langchain/Document_Loader/PDF_Folder",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs=loader.lazy_loadload()

for doc in docs:
    print(doc)