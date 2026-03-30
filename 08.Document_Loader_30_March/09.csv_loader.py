
from langchain_community.document_loaders import CSVLoader

file=CSVLoader(file_path="/home/prashant/Desktop/Langchain_Topics/08.Document_Loader/Student_Placement_Skills_2025.csv")

document=file.load()

print(len(document))

print(document[1].page_content)

print(document[1].metadata)
