from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatOpenAI()

parser=StrOutputParser()

prompt=PromptTemplate(
    template="provide answer of the following query /n {query}",
    input_variables=["query"]
)

loader=TextLoader("/home/prashant/Desktop/komal/Langchain/Document_Loader/query.txt",encoding="utf-8")

doc=loader.load()

print(doc[0].page_content)

chain=prompt|model|parser

result=chain.invoke({"query":doc[0].page_content})

print(result)