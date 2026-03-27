
from langchain_community.document_loaders import WebBaseLoader

urls=["https://en.wikipedia.org/wiki/Cricket",
 "https://en.wikipedia.org/wiki/One_Day_International",
 "https://en.wikipedia.org/wiki/Cricket_World_Cup"]

loader=WebBaseLoader(web_path=urls)

docs=loader.load()

print(docs[1].page_content[5500:5800])




