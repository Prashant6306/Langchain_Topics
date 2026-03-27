
from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path="/home/prashant/Desktop/komal/Langchain/Document_Loader/Student_Placement_Skills_2025.csv")

docs=loader.load()

print(len(docs))

print(docs[1])