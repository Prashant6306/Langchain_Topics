from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(model="gpt-4o")

parser=StrOutputParser()

prompt=PromptTemplate(
    template="Provide the answer for following query /n {query}"
)

file=TextLoader("query.txt",encoding="utf-8")

doc_query=file.load()

print(doc_query[0].page_content)
query=doc_query[0].page_content

chain= prompt| llm | parser

result= chain.invoke({
    "query":query
})

print(result)