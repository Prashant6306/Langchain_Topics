
from langchain_community.document_loaders import WebBaseLoader

url="https://en.wikipedia.org/wiki/International_cricket_in_2026"
loader=WebBaseLoader(web_path=url)

documents=loader.load()

print(documents)