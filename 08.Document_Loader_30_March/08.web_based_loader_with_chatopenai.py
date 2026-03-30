from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
load_dotenv()
# provide me information about iran-us war of 2026
llm=ChatOpenAI(model="gpt-4o")

parser=StrOutputParser()

prompt=PromptTemplate(
    template="Provide the answer for following query /n {query} from the following {text}"
)

url="https://en.wikipedia.org/wiki/2026_Iran_war"
file=WebBaseLoader(web_path=url)

document=file.load()


doc=document[0].page_content


final_context=doc[5000:10000]

print("-----> this is extrated text from web",final_context)


chain= prompt| llm | parser

result= chain.invoke({
    "query":"provide me information about iran-us war of 2026",
    "text":final_context
})

print("----->This is the result from llm",result)