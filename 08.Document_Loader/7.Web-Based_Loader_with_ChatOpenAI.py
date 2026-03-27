from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model=ChatOpenAI()
url="https://inshorts.com/en/news/hardik-pandya-s-world-record-winning-streak-in-icc-tournaments-ends-1771817930087"
prompt=PromptTemplate(
    template="Answer the following queation /n {question} from the following text /n {text}",
    input_variables=["question","text"]
)

parser=StrOutputParser()
loader=WebBaseLoader(web_path=url)
documents=loader.load()
#print(documents)
result=documents
chain=prompt|model|parser

result=chain.invoke({
    "question":"Who holds the second-longest ICC winning streak after Hardik Pandya?",
    "text":result
})

print(result)